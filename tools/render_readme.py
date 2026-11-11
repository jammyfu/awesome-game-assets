#!/usr/bin/env python3
"""Render README.md, README.zh-CN.md and docs/image-prompts.md from data/*.json.

Usage:
  python3 tools/render_readme.py          # write files
  python3 tools/render_readme.py --check  # fail if files are out of date
"""
from __future__ import annotations

import sys

from common import ROOT, load_entries, load_prompts, load_warnings

TEXT = {
    "en": {
        "title": "# Awesome Game Assets",
        "switch": "**English** · [简体中文](README.zh-CN.md)",
        "intro": "A curated list of openly licensed game assets and tools: 3D models, sprites, textures, sound effects, VFX, ability / casting demos, animation and editors. Every entry lists its URL, a license we checked on the source page, and what it is good for.",
        "contents": "## Contents",
        "warn_line": "> ⚠️ Repositories we found that look like piracy, cracks, paid-asset redistribution, star farming or malware are listed separately in [WARNING.md](WARNING.md) so you can avoid them. Do not use them.",
        "rules_h": "## Inclusion rules",
        "rules": [
            "Only sources whose license is stated clearly on the project or its official site. Per-asset licenses are marked as such; check each asset before use.",
            "No pirated, cracked or star-farmed repositories (stars, forks and activity are checked), and no archived or unusable ones.",
            "Every link is checked: 404s are removed; sites that answer automated checks with 403 or time out are kept and marked ⚠.",
            "Licenses were checked on {date} via the GitHub API `license` field or the official license page linked in each row.",
            "Preview images are the project's own images, linked from the original address (credited in each row). Category covers and rows marked *illustration* are original images generated for this list; prompts are in [docs/image-prompts.md](docs/image-prompts.md).",
        ],
        "cols": "| Preview | Project | License | Good for |",
        "cover_alt": "Category cover (original illustration)",
        "illustration": "illustration",
        "img_from": "image: project",
        "via": "listed in",
        "credits_h": "## Credits",
        "credits": "Some entries were found through these lists. We only took the pointers: every source was re-checked (license, reachability) and every description was rewritten for this list, nothing was copied wholesale. Entries found this way say *listed in* with a link to the list.",
        "credits_cols": "| List | License |",
        "contrib": "## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md). Edit `data/entries.json`, then run `python3 tools/render_readme.py` and `python3 tools/verify.py`.",
        "license": "## License\n\nThe list text is [CC0 1.0](LICENSE). Linked assets and tools keep their own licenses. Preview images belong to their projects and are linked, not copied.",
        "lang": "en",
    },
    "zh": {
        "title": "# Awesome Game Assets（开源游戏素材清单）",
        "switch": "[English](README.md) · **简体中文**",
        "intro": "精选许可证清楚的游戏素材和工具：3D 模型、2D 精灵、贴图材质、音效、特效、技能 / 施法演示、动画和编辑器。每条写明地址、在来源页核实过的许可证，以及适合做什么。",
        "contents": "## 目录",
        "warn_line": "> ⚠️ 搜到的疑似盗版、破解、付费素材二次分发、刷星或恶意软件仓库单独列在 [WARNING.zh-CN.md](WARNING.zh-CN.md)，用于避坑，请勿使用。",
        "rules_h": "## 收录规则",
        "rules": [
            "只收在项目或官网上写清许可证的来源。按素材单独授权的会标明，使用前请逐个确认。",
            "不收盗版、破解或刷星的仓库（看过 star、fork 和活跃度），不收已归档且不可用的仓库。",
            "每条链接都检查过：404 剔除；对自动检查返回 403 或超时的保留并标 ⚠。",
            "许可证于 {date} 核实：GitHub 仓库看 API 的 `license` 字段，网站看每行链接的官方许可页。",
            "预览图用项目自己的图，直接引用原地址（每行注明出处）。分类封面和标注 *示意图* 的条目是为本清单原创生成的，提示词见 [docs/image-prompts.md](docs/image-prompts.md)。",
        ],
        "cols": "| 预览 | 项目 | 许可证 | 适合做什么 |",
        "cover_alt": "分类封面（原创示意图）",
        "illustration": "示意图",
        "img_from": "图片来源：项目",
        "via": "参考清单",
        "credits_h": "## 致谢 / 参考清单",
        "credits": "部分条目是从下面这些清单里发现的。我们只借了线索：每个来源都重新核实了许可证和可达性，描述全部为本清单重写，没有整份照搬。通过它们找到的条目会写「参考清单」并链接原清单。",
        "credits_cols": "| 清单 | 许可证 |",
        "contrib": "## 参与贡献\n\n见 [CONTRIBUTING.md](CONTRIBUTING.md)。改 `data/entries.json`，再跑 `python3 tools/render_readme.py` 和 `python3 tools/verify.py`。",
        "license": "## 许可证\n\n清单文字采用 [CC0 1.0](LICENSE)。链接的素材和工具各自沿用原许可证。预览图归原项目所有，只引用不复制。",
        "lang": "zh",
    },
}


def anchor(title: str) -> str:
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -":
            out.append("-")
    return "".join(out)


def render(lang: str) -> str:
    t = TEXT[lang]
    data = load_entries()
    lines = [t["title"], "", t["switch"], "", t["intro"], "", t["warn_line"], "", t["contents"], ""]
    for c in data["categories"]:
        lines.append(f"- [{c[lang]}](#{anchor(c[lang])})")
    lines += ["", t["rules_h"], ""]
    lines += [f"- {r.format(date=data['verified_on'])}" for r in t["rules"]]
    for c in data["categories"]:
        lines += ["", f"## {c[lang]}", "", f'<img src="{c["cover"]}" alt="{t["cover_alt"]}: {c[lang]}" width="640">', "", t["cols"], "| --- | --- | --- | --- |"]
        for e in [e for e in data["entries"] if e["category"] == c["id"]]:
            img = e["image"]
            if img["type"] == "original":
                pic = f'<img src="{img["src"]}" alt="{e["name"]}" width="160">'
                credit = f'<br><sub>{t["img_from"]} [{e["name"]}]({img["source"]})</sub>'
            else:
                pic = f'<img src="{img["file"]}" alt="{e["name"]} ({t["illustration"]})" width="160">'
                credit = f'<br><sub>*{t["illustration"]}*</sub>'
            for v in e.get("via", []):
                credit += f'<br><sub>{t["via"]} [{v}](https://github.com/{v})</sub>'
            if e.get("link_note"):
                credit += f'<br><sub>⚠ {e["link_note"][lang]}</sub>'
            lic_text = e["license_zh"] if lang == "zh" else e["license"]
            lic = f"[{lic_text}]({e['license_source']})"
            desc = e[lang].replace("|", "\\|")
            lines.append(f'| {pic} | [{e["name"]}]({e["url"]}){credit} | {lic} | {desc} |')
    lines += ["", t["credits_h"], "", t["credits"], "", t["credits_cols"], "| --- | --- |"]
    for c in data.get("credits", []):
        lines.append(f'| [{c["repo"]}]({c["url"]}) | {c["license"]} |')
    lines += ["", t["contrib"], "", t["license"], ""]
    return "\n".join(lines)


def render_prompts() -> str:
    p = load_prompts()
    lines = [
        "# Image prompts / 配图提示词",
        "",
        "Original images in `docs/images/` were generated for this list. No third-party images are stored in this repo; project previews are linked from their original addresses.",
        "",
        "`docs/images/` 里的图都是为本清单原创生成的。仓库里不存第三方图片，项目预览图直接引用原地址。",
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
        lines.append(f"| `{f}` | {prompt} | Codex CLI 0.162.1 | {p['date']} |")
    lines.append("")
    return "\n".join(lines)


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
}


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
