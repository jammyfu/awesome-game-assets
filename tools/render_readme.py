#!/usr/bin/env python3
"""Render five-language README/catalog files and project documentation from data/*.json.

Usage:
  python3 tools/render_readme.py          # write files
  python3 tools/render_readme.py --check  # fail if files are out of date
"""
from __future__ import annotations

import sys
import json
from functools import lru_cache

from common import ROOT, load_entries, load_prompts, load_warnings

LOCALES = {"en": ("English", ""), "zh": ("简体中文", ".zh-CN"), "zh-TW": ("繁體中文", ".zh-TW"), "ja": ("日本語", ".ja"), "ko": ("한국어", ".ko")}

@lru_cache(maxsize=None)
def locale_data(lang):
    result = json.loads((ROOT / "data" / "locales" / f"{lang}.json").read_text(encoding="utf-8"))
    if lang in ("en", "zh"):
        data = load_entries()
        result.update(categories={c["id"]: c[lang] for c in data["categories"]}, entries={e["id"]: e[lang] for e in data["entries"]}, link_notes={e["id"]: e["link_note"][lang] for e in data["entries"] if e.get("link_note")})
    return result

@lru_cache(maxsize=None)
def discovery_data():
    return json.loads((ROOT / "data/discovery.json").read_text(encoding="utf-8"))

def render_reader_routes(lang):
    data, spec = load_entries(), discovery_data()
    loc = spec["locales"][lang]
    cats = locale_data(lang)["categories"]
    links = [f"[{label}](#{anchor(cats[key])})" for key, label in zip(spec["routes"], loc["route_labels"])]
    return [loc["summary"].format(entries=len(data["entries"]), categories=len(data["categories"])), "", loc["heading"], "", " · ".join(links), ""]

def render_reader_faq(lang):
    loc = discovery_data()["locales"][lang]
    lines = ["", loc["faq_heading"], ""]
    for question, answer in loc["faq"]:
        lines.extend([f"### {question}", "", answer, ""])
    return lines

def render_llms():
    data = load_entries()
    repo = "https://github.com/" + discovery_data()["repository"]
    lines = ["# Awesome Game Assets", "", f"> A curated directory of {len(data['entries'])} game-development resources in {len(data['categories'])} categories, with complete English, Simplified Chinese, Traditional Chinese (Taiwan), Japanese and Korean catalogs. Includes asset packs, tools and code examples, not {len(data['entries'])} interchangeable downloads.", "", "## Scope and use rights", "", "Resources include 2D sprites, pixel art, 3D models, PBR textures, UI, audio, VFX, animation and production tools. Linked assets have different licenses; some are non-commercial or have component-specific terms. The list's CC0 license does not relicense assets, code or preview images. Always follow the original source and license for the selected download.", "", "## Language entry points", ""]
    for lang, (label, suffix) in LOCALES.items():
        lines.append(f"- [{label} overview]({repo}/blob/main/README{suffix}.md): full catalog with original-source previews, practical license summaries and expandable category tables.")
        lines.append(f"- [{label} catalog]({repo}/blob/main/docs/catalog{suffix}.md): the same complete entries in a separate document.")
    lines += ["", "## Data and provenance", "", f"- [Source dataset]({repo}/blob/main/data/entries.json): stable IDs, categories, source URLs, license labels and evidence URLs, previews and dated popularity snapshots. `verified_on` is a recorded source-check date, not a guarantee that today's terms are unchanged.", f"- [Localization files]({repo}/tree/main/data/locales): translated descriptions and use notes keyed by the same entry IDs. Do not count translations as additional assets.", f"- [Discovery and use-rights methodology]({repo}/blob/main/docs/discovery.md): ordering, image provenance and permission boundaries.", f"- [Contributing]({repo}/blob/main/CONTRIBUTING.md): source and review workflow (English/Chinese).", f"- [List license]({repo}/blob/main/LICENSE): CC0 applies to the list text only.", f"- [Risk warnings]({repo}/blob/main/WARNING.md): excluded sources to avoid, not recommended resources (English/Chinese).", "", "## Interpretation limits", "", "Categories show at most 15 entries initially; remaining rows are inside expandable tables. GitHub stars are a dated cumulative snapshot, not recent growth, quality or cross-platform popularity. Non-GitHub sources have no comparable star metric. A project logo is not an asset screenshot; missing previews are labelled. No universal engine compatibility or commercial-use clearance is claimed.", "", "This file is optional navigation for tools that choose to read it. It does not guarantee indexing, search ranking or AI citations.", ""]
    return "\n".join(lines)

def language_nav(lang, stem):
    return " · ".join(f"**{name}**" if code == lang else f"[{name}]({stem}{suffix}.md)" for code, (name, suffix) in LOCALES.items())


def anchor(title: str) -> str:
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -":
            out.append("-")
    return "".join(out)


def license_summary(license_name: str, lang: str) -> str:
    """Plain-language guidance, not a replacement for the linked terms."""
    if lang not in ("en", "zh"):
        return locale_data(lang)["license_summaries"][license_name]
    zh = lang == "zh"
    def pick(en, cn): return cn if zh else en
    l = license_name.lower()
    if "not valid in eu" in l:
        return pick("Commercial use has regional/scale limits; check terms", "有地区及规模限制，商用前查条款")
    if "per " in l or "own licenses" in l or "bundled parts" in l or "except extras" in l:
        return pick("Check the selected asset/component before use", "逐项查素材或组件条件后使用")
    if "cc-by-nc" in l:
        subject = "所列内容/权重" if "code" in l or "scripts" in l else ""
        en_subject = "Listed content/weights: " if subject else ""
        suffix_en = "; no adaptations" if "-nd" in l else ("; adaptations use same terms" if "-sa" in l else "")
        suffix_zh = "，不可改编" if "-nd" in l else ("；改编沿用同许可" if "-sa" in l else "")
        return pick(en_subject + "non-commercial only; credit required" + suffix_en, subject + "仅限非商用，须署名" + suffix_zh)
    if "polyfork" in l:
        return pick("Low-poly: credit or choose Polyfork terms; HD/modules have separate terms", "低模署名或选专有条款；高清与模块另查")
    if "pixabay" in l:
        return pick("Commercial use; no standalone resale", "可商用，不可原样单独转售")
    if "sonniss" in l:
        return pick("Commercial use; no credit required; no standalone redistribution", "可商用免署名，不可单独转分发")
    if "ofl" in l:
        return pick("Commercial use/embedding; keep font license, no font-only resale", "可商用嵌入；保留字体许可，不单卖字体")
    if "cc0" in l:
        if "mit" in l:
            return pick("Assets: commercial, no credit; code: keep MIT notices", "素材可商用免署名；代码保留 MIT 声明")
        if "agpl" in l:
            return pick("Assets: commercial, no credit; code: AGPL obligations", "素材可商用免署名；代码遵守 AGPL")
        return pick("Commercial use and modification; no credit required", "可商用、可修改，免署名")
    if "cc-by-sa" in l:
        return pick("Commercial use; credit and share adaptations under same terms", "可商用，须署名；改编沿用同许可")
    if "cc-by" in l:
        return pick("Commercial use; credit required", "可商用，须署名")
    if "lgpl" in l:
        return pick("Commercial use; distribute library changes/source as required", "可商用；分发时履行库源码及替换义务")
    if "agpl" in l:
        return pick("Commercial use; source-sharing applies to distribution/network service", "可商用；分发或网络服务须履行源码义务")
    if "gpl" in l:
        return pick("Commercial use; distributed covered code must remain open", "可商用；分发受许可代码须按要求开源")
    if "mpl" in l:
        return pick("Commercial use; distribute changes to covered files as source", "可商用；分发时公开受许可文件的修改")
    if "defold" in l:
        return pick("Commercial games; engine redistribution has additional limits", "可做商业游戏；引擎再分发有额外限制")
    if "ms-pl" in l:
        return pick("Commercial use; keep notices and source-license obligations", "可商用；保留声明并遵守源码分发条件")
    if any(k in l for k in ("mit", "apache", "bsd", "zlib")):
        return pick("Commercial use and modification; keep required notices", "可商用、可修改；保留必要版权与许可声明")
    if "unlicense" in l:
        return pick("Commercial use and modification; no credit required", "可商用、可修改，免署名")
    return pick("Check linked terms before use", "使用前查看原始条款")


def render_catalog(lang: str, homepage: bool = False) -> str:
    data = load_entries()
    loc = locale_data(lang)
    t = loc["ui"]
    for c in data["categories"]:
        c[lang] = loc["categories"][c["id"]]
    for e in data["entries"]:
        e[lang] = loc["entries"][e["id"]]
        if e.get("link_note"):
            e["link_note"][lang] = loc["link_notes"][e["id"]]
    suffix = LOCALES[lang][1]
    switch = language_nav(lang, "catalog")
    lines = [t["title"], "", switch, "", f'[{t["back"]}](README{suffix}.md)', "", t["intro"], "", t["warn_line"], "", t["contents"], ""]
    if homepage:
        lines = [t["title"], "", language_nav(lang, "README"), "", f'<img src="{data["discovery"]["hero"]}" alt="{t["hero_alt"]}" width="1200">', "", t["hero_caption"], ""] + render_reader_routes(lang) + [t["warn_line"], "", t["contents"], ""]
    lines += [f'**[{t["browse"]}](#{anchor(data["categories"][0][lang])})** · [{t["contribute_label"]}](CONTRIBUTING.md)', "", t["sort_note"], "", t["mobile"], ""]
    for c in data["categories"]:
        lines.append(f"- [{c[lang]}](#{anchor(c[lang])})")
    lines += ["", t["rules_h"], ""]
    lines += [f"- {r.format(date=data['verified_on'])}" for r in t["rules"]]
    for c in data["categories"]:
        lines += ["", f"## {c[lang]}", ""]
        lines += ["", t["cols"], "| --- | --- | --- |"]
        entries = sorted([e for e in data["entries"] if e["category"] == c["id"]], key=lambda e: (e.get("popularity", {}).get("value") is None, -(e.get("popularity", {}).get("value") or 0)))
        for index, e in enumerate(entries):
            if index == 15:
                summary = t["expand"].format(count=len(entries) - 15)
                lines += ["", "<details>", f"<summary>{summary}</summary>", "", t["cols"], "| --- | --- | --- |"]
            img = e["image"]
            if img["type"] == "original" and img.get("display_status") == "verified":
                pic = f'<img src="{img["src"]}" alt="{e["name"]}" width="160">'
                credit = f'<br><sub>{t["img_from"]} [{e["name"]}]({img["source"]})</sub>'
                if img.get("kind") == "identity":
                    credit += f'<br><sub>{t["identity"]}</sub>'
            elif img["type"] == "original":
                pic = f'[{t["source"]}]({img["source"]})'
                credit = ""
            else:
                pic = f'[{t["missing"]}]({e["url"]})'
                credit = ""
            for v in e.get("via", []):
                credit += f'<br><sub>{t["via"]} [{v}](https://github.com/{v})</sub>'
            if e.get("link_note"):
                credit += f'<br><sub>⚠ {e["link_note"][lang]}</sub>'
            lic_text = e["license_zh"] if lang == "zh" else e["license"]
            scope = t["list_scope"] if e["category"] == "lists" else ""
            lic = f"{scope}{license_summary(e['license'], lang)}<br><sub>([{lic_text}]({e['license_source']}))</sub>"
            desc = e[lang]
            name = e["name"].replace("|", "\\|")
            heat = e.get("popularity", {}).get("value")
            credit += f"<br><sub>GitHub ★ {heat:,}</sub>" if heat is not None else f'<br><sub>{t["unknown_heat"]}</sub>'
            lines.append(f'| [{name}]({e["url"]})<br>{pic}{credit} | {lic} | {desc} |')

        if len(entries) > 15:
            lines += ["", "</details>", ""]

    lines += render_reader_faq(lang)
    lines += ["", t["credits_h"], "", t["credits"], ""]
    for c in data.get("credits", []):
        lines.append(f'- [{c["repo"]}]({c["url"]}) · {c["license"]}')
    lines += ["", t["contrib"], "", t["license"], ""]
    if homepage:
        return "\n".join(lines)
    text = "\n".join(lines)
    for name in tuple("README" + suffix + ".md" for _, suffix in LOCALES.values()) + ("WARNING.md", "WARNING.zh-CN.md", "CONTRIBUTING.md", "LICENSE"):
        text = text.replace("](" + name + ")", "](../" + name + ")")
    text = text.replace('src="docs/images/', 'src="images/')
    for name in ("image-prompts.md", "discovery.md"):
        text = text.replace("](docs/" + name + ")", "](" + name + ")")
    return text



def render(lang: str) -> str:
    return render_catalog(lang, homepage=True)

def render_prompts() -> str:
    p = load_prompts()
    lines = [
        "# Image prompts / 配图提示词",
        "",
        "Original images in `docs/images/` were generated for this list. No third-party images are stored in this repo; official project previews are hotlinked with attribution; this is not a redistribution license.",
        "",
        "`docs/images/` 里的图都是为本清单原创生成的。仓库里不存第三方图片，优先引用并署名官方项目预览，不授予原图再分发许可。",
        "",
        f"- Tool / 工具: {p['tool']}",
        f"- Date / 日期: {p['date']}",
        "- Post-processing / 后处理: resized to 1024 px wide and converted to WebP (Pillow).",
        f"- Shared style suffix / 统一风格后缀: {p['style']}",
        "",
        "| File | Prompt (style suffix appended) | Tool | Date |",
        "| --- | --- | --- | --- |",
    ]
    for f, prompt in p["images"].items():
        meta = p.get("overrides", {}).get(f)
        if meta:
            lines.append(f"| `{f}` | {prompt} (standalone prompt; no shared suffix) | {meta['tool']} | {meta['date']} |")
            lines.append("")
            lines.append(f"Hero post-processing: {meta['post_processing']}")
            lines.append("")
        else:
            lines.append(f"| `{f}` | {prompt} | Codex CLI 0.162.1 | {p['date']} |")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


WARN_TEXT = {
    "en": {
        "title": "# ⚠️ WARNING: repositories to avoid",
        "switch": "**English** · [简体中文](WARNING.zh-CN.md) · [Back to the list](README.md)",
        "caution": [
            "> [!CAUTION]",
            "> **These repositories may infringe copyright or contain malware.** This page exists only to help you avoid them. We do not recommend downloading, running or using anything from them.",
            "> Links point to repository pages only, never to releases or files. Checked on {date}; report them to GitHub if you agree.",
        ],
        "types_h": "## Count by type",
        "list_h": "## List",
        "type": "Type",
        "risk": "Risk",
    },
    "zh": {
        "title": "# ⚠️ 警示清单：请避开这些仓库",
        "switch": "[English](WARNING.md) · **简体中文** · [返回清单](README.zh-CN.md)",
        "caution": [
            "> [!CAUTION]",
            "> **这些仓库可能侵权或含恶意软件。** 本页仅用于避坑，不建议下载、运行或使用其中任何内容。",
            "> 链接只指向仓库首页，不指向 release 或文件。核查日期 {date}；如认同可向 GitHub 举报。",
        ],
        "types_h": "## 各类型条数",
        "list_h": "## 清单",
        "type": "类型",
        "risk": "风险",
    },
}


def render_warning(lang: str) -> str:
    t = WARN_TEXT[lang]
    w = load_warnings()
    lines = [t["title"], "", t["switch"], ""]
    lines += [c.format(date=w["checked_on"]) for c in t["caution"]]
    lines += ["", t["types_h"], ""]
    for key, names in w["types"].items():
        n = sum(1 for e in w["entries"] if e["type"] == key)
        lines.append(f"- {names[lang]}: {n}")
    lines += ["", t["list_h"], ""]
    for e in w["entries"]:
        if lang == "zh":
            body = f'**{t["type"]}：**{w["types"][e["type"]][lang]}。**{t["risk"]}：**{e[lang]}'
        else:
            body = f'**{t["type"]}:** {w["types"][e["type"]][lang]}. **{t["risk"]}:** {e[lang]}'
        lines.append(f'- ⚠️ [{e["repo"]}]({e["url"]}) — {body}')
        if e.get("image"):
            lines.append(f'  <br><img src="{e["image"]["src"]}" alt="{e["repo"]}" width="200">')
    lines.append("")
    return "\n".join(lines)


OUTPUTS = {
    "WARNING.md": lambda: render_warning("en"),
    "WARNING.zh-CN.md": lambda: render_warning("zh"),
    "README.md": lambda: render("en"),
    "README.zh-CN.md": lambda: render("zh"),
    "docs/image-prompts.md": render_prompts,
    "docs/catalog.md": lambda: render_catalog("en"),
    "docs/catalog.zh-CN.md": lambda: render_catalog("zh"),
}

OUTPUTS["llms.txt"] = render_llms

for code, (_, suffix) in LOCALES.items():
    OUTPUTS["README" + suffix + ".md"] = lambda code=code: render(code)
    OUTPUTS["docs/catalog" + suffix + ".md"] = lambda code=code: render_catalog(code)


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for name, fn in OUTPUTS.items():
        path = ROOT / name
        content = fn()
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"wrote {name}")
    if stale:
        print("Out of date (run python3 tools/render_readme.py): " + ", ".join(stale))
        return 1
    if check:
        print("Generated files are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
