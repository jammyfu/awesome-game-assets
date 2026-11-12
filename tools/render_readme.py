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
        "intro": "A curated directory of game assets and tools with license notes, including restricted licenses: 3D models, sprites, textures, sound effects, VFX, ability / casting demos, animation and editors. Every entry lists its URL, a license we checked on the source page, and what it is good for.",
        "contents": "## Contents",
        "warn_line": "> ⚠️ Repositories we found that look like piracy, cracks, paid-asset redistribution, star farming or malware are listed separately in [WARNING.md](WARNING.md) so you can avoid them. Do not use them.",
        "rules_h": "## Inclusion rules",
        "rules": [
            "Only sources whose license is stated clearly on the project or its official site. Per-asset licenses are marked as such; check each asset before use.",
            "No pirated, cracked or star-farmed repositories (stars, forks and activity are checked), and no archived or unusable ones.",
            "Automated checks report broken links and bot-blocked or timed-out sources; a warning is not proof that a source is reachable.",
            "Licenses were checked on {date} via the GitHub API `license` field or the official license page linked in each row.",
            "Preview images are linked from the original project and credited. Display here does not grant reuse rights: check the linked asset terms. The hero/category art is generated; missing original previews are labelled, never replaced with invented results.",
        ],
        "cols": "| Project / Preview | License | Good for |",
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
        "title": "# Awesome Game Assets（游戏素材导航）",
        "switch": "[English](README.md) · **简体中文**",
        "intro": "精选许可证清楚的游戏素材和工具：3D 模型、2D 精灵、贴图材质、音效、特效、技能 / 施法演示、动画和编辑器。每条写明地址、在来源页核实过的许可证，以及适合做什么。",
        "contents": "## 目录",
        "warn_line": "> ⚠️ 搜到的疑似盗版、破解、付费素材二次分发、刷星或恶意软件仓库单独列在 [WARNING.zh-CN.md](WARNING.zh-CN.md)，用于避坑，请勿使用。",
        "rules_h": "## 收录规则",
        "rules": [
            "只收在项目或官网上写清许可证的来源。按素材单独授权的会标明，使用前请逐个确认。",
            "不收盗版、破解或刷星的仓库（看过 star、fork 和活跃度），不收已归档且不可用的仓库。",
            "自动检查报告失效、被拦截或超时的来源；警告不等于已验证可达。",
            "许可证于 {date} 核实：GitHub 仓库看 API 的 `license` 字段，网站看每行链接的官方许可页。",
            "预览优先引用原项目图片并署名。这里展示不等于授予再使用权，请按原始素材条款使用。头图和分类插画为生成图；缺少真实预览会明确说明，不用虚构效果替代。",
        ],
        "cols": "| 项目 / 预览 | 许可证 | 适合做什么 |",
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


def license_summary(license_name: str, lang: str) -> str:
    """Plain-language guidance, not a replacement for the linked terms."""
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
    t = TEXT[lang]
    data = load_entries()
    switch = "**English** · [简体中文](catalog.zh-CN.md)" if lang == "en" else "[English](catalog.md) · **简体中文**"
    lines = [t["title"], "", switch, "", "[Back to overview](README.md)" if lang == "en" else "[返回首页](README.zh-CN.md)", "", t["intro"], "", t["warn_line"], "", t["contents"], ""]
    if homepage:
        lines = [t["title"], "", t["switch"], "", f'<img src="{data["discovery"]["hero"]}" alt="Original game-dev loot drop: a starter hero unlocks an overflowing chest of game assets" width="1200">', "", "原创头图：开局一把木剑，素材全靠捡。" if lang == "zh" else "Original illustration: starter sword equipped. Asset loot unlocked.", "", t["intro"], "", t["warn_line"], "", t["contents"], ""]
    lines += ["**[开始浏览素材](#" + anchor(data["categories"][0][lang]) + ")** · [参与贡献](CONTRIBUTING.md)" if lang == "zh" else "**[Browse the asset tables](#" + anchor(data["categories"][0][lang]) + ")** · [Contribute](CONTRIBUTING.md)", "", "每类默认显示前 15 项，其他可展开。GitHub 项目按累计星标排序（2026-11-12 快照）；无可比数据的网站随后展示，不代表近期趋势。[排序说明](docs/discovery.md)。" if lang == "zh" else "First 15 resources per category; expand for the rest. GitHub repos sort by total stars (2026-11-12 snapshot); sites without comparable data follow. This is not recent growth. [Ordering notes](docs/discovery.md).", ""]
    lines += ["手机浏览：表格可左右滑动，保留项目、许可与用途对照。" if lang == "zh" else "On phones, swipe tables sideways to compare projects, licenses and uses.", ""]
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
                summary = f"展开其余 {len(entries) - 15} 项" if lang == "zh" else f"Show remaining {len(entries) - 15} resources"
                lines += ["", "<details>", f"<summary>{summary}</summary>", "", t["cols"], "| --- | --- | --- |"]
            img = e["image"]
            if img["type"] == "original" and img.get("display_status") == "verified":
                pic = f'<img src="{img["src"]}" alt="{e["name"]}" width="160">'
                credit = f'<br><sub>{t["img_from"]} [{e["name"]}]({img["source"]})</sub>'
                if img.get("kind") == "identity":
                    credit += "<br><sub>项目标识，非素材效果</sub>" if lang == "zh" else "<br><sub>Project identity, not an asset preview</sub>"
            elif img["type"] == "original":
                pic = f'[View at source]({img["source"]})' if lang == "en" else f'[查看原始来源]({img["source"]})'
                credit = ""
            else:
                pic = f'[未找到可用原图 · 查看项目]({e["url"]})' if lang == "zh" else f'[No usable original preview found · open project]({e["url"]})'
                credit = ""
            for v in e.get("via", []):
                credit += f'<br><sub>{t["via"]} [{v}](https://github.com/{v})</sub>'
            if e.get("link_note"):
                credit += f'<br><sub>⚠ {e["link_note"][lang]}</sub>'
            lic_text = e["license_zh"] if lang == "zh" else e["license"]
            scope = ("清单文字：" if lang == "zh" else "List text: ") if e["category"] == "lists" else ""
            lic = f"{scope}{license_summary(e['license'], lang)}<br><sub>([{lic_text}]({e['license_source']}))</sub>"
            desc = e[lang]
            name = e["name"].replace("|", "\\|")
            heat = e.get("popularity", {}).get("value")
            credit += f"<br><sub>GitHub ★ {heat:,}</sub>" if heat is not None else ("<br><sub>热度暂无可比数据</sub>" if lang == "zh" else "<br><sub>No comparable popularity data</sub>")
            lines.append(f'| [{name}]({e["url"]})<br>{pic}{credit} | {lic} | {desc} |')

        if len(entries) > 15:
            lines += ["", "</details>", ""]

    lines += ["", t["credits_h"], "", t["credits"], ""]
    for c in data.get("credits", []):
        lines.append(f'- [{c["repo"]}]({c["url"]}) · {c["license"]}')
    lines += ["", t["contrib"], "", t["license"], ""]
    if homepage:
        return "\n".join(lines)
    text = "\n".join(lines)
    for name in ("README.md", "README.zh-CN.md", "WARNING.md", "WARNING.zh-CN.md", "CONTRIBUTING.md", "LICENSE"):
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
