#!/usr/bin/env python3
"""Offline checks for the list. Standard library only, no network, no telemetry.

Checks: entry format (URL / license / use in EN+ZH), unique ids and links,
EN/ZH README parity, language (English + Chinese only), image provenance
(original images credited, generated images have prompts and stay under the
size limit), banned keywords, and a zero-telemetry scan.
"""
from __future__ import annotations

import re
import sys

from common import MAX_IMAGE_BYTES, ROOT, load_entries, load_prompts, load_warnings

REQUIRED = ["id", "category", "name", "url", "license", "license_zh", "license_source", "en", "zh", "image"]
CJK = re.compile(r"[\u4e00-\u9fff]")
OTHER_SCRIPTS = re.compile(r"[\u3040-\u30ff\uac00-\ud7af\u0400-\u04ff\u0600-\u06ff]")  # kana, hangul, cyrillic, arabic
BANNED = re.compile(r"crack|keygen|activator|warez|nulled|pirat", re.I)
TELEMETRY = re.compile(
    r"google-analytics|googletagmanager|gtag\(|plausible\.io|umami\.|mixpanel|posthog|sentry\.io|"
    r"hotjar|matomo|clarity\.ms|segment\.(com|io)|amplitude\.com|stats\.wp\.com|counter\.dev|visitor-badge|komarev",
    re.I,
)
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".txt", ".html", ".js", ".toml"}
SKIP_TELEMETRY_SCAN = {"tools/check_list.py", "tests/test_check_list.py"}
# The warning list is exempt from the banned-keyword checks by design.
WARNING_FILES = {"WARNING.md", "WARNING.zh-CN.md", "data/warnings.json"}
WARN_TYPES = {"piracy", "crack", "paid-redistribution", "star-farming", "malware"}
INSTALL_WORDS = re.compile(r"\b(download|install|setup\.exe|unzip|extract|password)\b|下载步骤|安装步骤|安装方法|下载方法|解压|密码|/releases|\.(exe|zip|rar|7z|msi|dmg)\b", re.I)


def norm(url: str) -> str:
    u = url.lower().split("#")[0].rstrip("/")
    return u.replace("://www.", "://")


def check_entries(data: dict, errors: list[str]) -> None:
    cats = {c["id"] for c in data["categories"]}
    seen_ids, seen_urls = set(), set()
    for c in data["categories"]:
        for k in ("id", "en", "zh", "cover"):
            if not c.get(k):
                errors.append(f"category missing {k}: {c}")
        if not any(e.get("category") == c["id"] for e in data["entries"]):
            errors.append(f"category {c['id']} has no entries")
    for e in data["entries"]:
        eid = e.get("id", "?")
        for k in REQUIRED:
            if not e.get(k):
                errors.append(f"{eid}: missing {k}")
        if e.get("category") not in cats:
            errors.append(f"{eid}: unknown category {e.get('category')}")
        for k in ("url", "license_source"):
            if e.get(k) and not e[k].startswith("https://"):
                errors.append(f"{eid}: {k} must be https")
        if eid in seen_ids:
            errors.append(f"duplicate id {eid}")
        seen_ids.add(eid)
        u = norm(e.get("url", ""))
        if u in seen_urls:
            errors.append(f"duplicate link {e['url']}")
        seen_urls.add(u)
        if CJK.search(e.get("en", "")) or CJK.search(e.get("license", "")):
            errors.append(f"{eid}: English text contains Chinese")
        if not CJK.search(e.get("zh", "")):
            errors.append(f"{eid}: zh text has no Chinese")
        for k in ("name", "url", "en", "zh"):
            if BANNED.search(e.get(k, "")):
                errors.append(f"{eid}: banned keyword in {k}")
            if OTHER_SCRIPTS.search(e.get(k, "")):
                errors.append(f"{eid}: only English and Chinese allowed in {k}")


def check_credits(data: dict, errors: list[str]) -> None:
    credited = {c["repo"] for c in data.get("credits", [])}
    for c in data.get("credits", []):
        if not (c.get("repo") and c.get("url", "").startswith("https://") and c.get("license")):
            errors.append(f"credit needs repo, https url and license: {c}")
    for e in data["entries"]:
        for v in e.get("via", []):
            if v not in credited:
                errors.append(f"{e['id']}: via {v} is not in credits")


def check_images(data: dict, prompts: dict, errors: list[str]) -> None:
    prompt_files = set(prompts["images"])
    used = set()
    for c in data["categories"]:
        used.add(c["cover"])
    for e in data["entries"]:
        img = e.get("image") or {}
        if img.get("type") == "original":
            if not img.get("src", "").startswith("https://") or not img.get("source", "").startswith("https://"):
                errors.append(f"{e['id']}: original image needs https src and source credit")
        elif img.get("type") == "generated":
            used.add(img.get("file", ""))
        else:
            errors.append(f"{e['id']}: image type must be original or generated")
    for f in sorted(used):
        p = ROOT / f
        if f not in prompt_files:
            errors.append(f"{f}: generated image has no prompt in data/image-prompts.json")
        if not p.exists():
            errors.append(f"{f}: image file missing")
        elif p.stat().st_size > MAX_IMAGE_BYTES:
            errors.append(f"{f}: {p.stat().st_size} bytes > {MAX_IMAGE_BYTES}")
    img_dir = ROOT / "docs" / "images"
    if img_dir.exists():
        for p in sorted(img_dir.iterdir()):
            rel = p.relative_to(ROOT).as_posix()
            if p.is_file() and rel not in prompt_files:
                errors.append(f"{rel}: stored image without prompt/provenance")
    for f in prompt_files - used:
        errors.append(f"{f}: prompt listed but image not used")


def readme_urls(text: str) -> list[str]:
    rows = [l for l in text.splitlines() if l.startswith("| <img")]
    out = []
    for r in rows:
        m = re.search(r"\| \[[^\]]+\]\((https://[^)]+)\)", r)
        out.append(m.group(1) if m else "")
    return out


def check_readmes(data: dict, errors: list[str]) -> None:
    en = (ROOT / "README.md").read_text(encoding="utf-8")
    zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "WARNING.md" not in en or "WARNING.zh-CN.md" not in zh:
        errors.append("READMEs must link to the warning list")
    if "README.zh-CN.md" not in en or "README.md" not in zh:
        errors.append("READMEs must link to each other")
    en_urls, zh_urls = readme_urls(en), readme_urls(zh)
    want = [e["url"] for e in data["entries"]]
    for name, urls in (("README.md", en_urls), ("README.zh-CN.md", zh_urls)):
        normed = [norm(u) for u in urls]
        dups = sorted({u for u in normed if normed.count(u) > 1})
        if dups:
            errors.append(f"{name}: duplicate links {dups}")
    if len(en_urls) != len(zh_urls):
        errors.append(f"EN/ZH entry count differs: {len(en_urls)} vs {len(zh_urls)}")
    if sorted(en_urls) != sorted(want) or sorted(zh_urls) != sorted(want):
        errors.append("README rows do not match data/entries.json (run tools/render_readme.py)")
    en_body = en.replace("简体中文", "")
    if CJK.search(en_body):
        errors.append("README.md contains Chinese outside the language switch")
    for name, text in (("README.md", en), ("README.zh-CN.md", zh)):
        if OTHER_SCRIPTS.search(text):
            errors.append(f"{name}: only English and Chinese allowed")


def check_telemetry(errors: list[str]) -> None:
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if not p.is_file() or rel.startswith(".git/") or rel in SKIP_TELEMETRY_SCAN:
            continue
        if p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        m = TELEMETRY.search(p.read_text(encoding="utf-8", errors="ignore"))
        if m:
            errors.append(f"{rel}: telemetry/tracker pattern '{m.group(0)}'")


def check_warnings(errors: list[str]) -> None:
    w = load_warnings()
    if set(w["types"]) != WARN_TYPES:
        errors.append("warnings.json types must be exactly " + ", ".join(sorted(WARN_TYPES)))
    main_urls = {norm(e["url"]) for e in load_entries()["entries"]}
    seen = set()
    for e in w["entries"]:
        rid = e.get("repo", "?")
        for k in ("repo", "url", "type", "en", "zh"):
            if not e.get(k):
                errors.append(f"warning {rid}: missing {k}")
        if e.get("type") not in WARN_TYPES:
            errors.append(f"warning {rid}: bad type {e.get('type')}")
        u = e.get("url", "")
        if not re.fullmatch(r"https://github\.com/[^/]+/[^/]+", u) and not re.fullmatch(r"https://[^/]+/?", u):
            errors.append(f"warning {rid}: link must be a repo or site home page only")
        if norm(u) in seen:
            errors.append(f"warning {rid}: duplicate")
        seen.add(norm(u))
        if norm(u) in main_urls:
            errors.append(f"warning {rid}: also in the main list")
        for k in ("en", "zh"):
            m = INSTALL_WORDS.search(e.get(k, ""))
            if m:
                errors.append(f"warning {rid}: download/install wording '{m.group(0)}' in {k}")
        img = e.get("image")
        if img and not img.get("src", "").startswith("https://"):
            errors.append(f"warning {rid}: image must be a hotlinked https URL")
    for name in ("WARNING.md", "WARNING.zh-CN.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        if "> [!CAUTION]" not in text:
            errors.append(f"{name}: missing caution box")
        items = [l for l in text.splitlines() if l.startswith("- ") and "](https://github.com/" in l]
        if len(items) != len(w["entries"]):
            errors.append(f"{name}: item count differs from data/warnings.json")
        if any(not l.startswith("- ⚠️ ") for l in items):
            errors.append(f"{name}: every item must start with ⚠️")
    # never store warning images in the repo
    img_dir = ROOT / "docs" / "images"
    if img_dir.exists():
        for p in img_dir.iterdir():
            if p.name.startswith("warning"):
                errors.append(f"{p.name}: warning images must not be stored in the repo")
    for e in w["entries"]:
        img = (e.get("image") or {}).get("src", "")
        if img and not img.startswith("https://"):
            errors.append(f"warning {e['repo']}: local image path not allowed")


def run() -> list[str]:
    errors: list[str] = []
    data = load_entries()
    check_entries(data, errors)
    check_credits(data, errors)
    check_images(data, load_prompts(), errors)
    check_readmes(data, errors)
    check_telemetry(errors)
    check_warnings(errors)
    return errors


def main() -> int:
    errors = run()
    for e in errors:
        print("ERROR:", e)
    if errors:
        return 1
    d = load_entries()
    print(f"List checks passed: {len(d['entries'])} entries in {len(d['categories'])} categories.")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    raise SystemExit(main())
