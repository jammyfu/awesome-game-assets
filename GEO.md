# Repository discovery: About, Topics and AI-readable sources

Updated: 2026-11-12. This is the repository's editorial metadata record, **not** a GitHub or search-engine configuration standard.

## Applied GitHub settings

- Repository: jammyfu/awesome-game-assets
- Description: Game assets and tools for indie developers: 2D sprites, 3D models, PBR textures, UI, audio, VFX and animation. Find original previews, practical license notes and source links in category tables.
- Topics: awesome, awesome-list, game-assets, game-development, gamedev, sprites, pixel-art, 3d-models, textures, pbr, sound-effects, game-audio, game-ui, vfx, shaders, animation, cc0, threejs
- Homepage: unset. No separate live website is claimed.
- Status: About and the 18-topic set were applied and read back on 2026-11-12. The owner then requested more practical information in place of the About language list; the description above is the revised version. Five-language navigation remains in README. Only description and topics changed. Content changes in this PR are separate from those already-live settings.
- Source of intended values: `data/discovery.json`. The manifest is validated offline; it does not automatically change GitHub settings.

## Search intent and evidence

| Intent | Reader destination | Topic/phrase decision |
| --- | --- | --- |
| Find reusable game assets | Hero, short scope statement, category tables | game-assets, game-development, gamedev |
| Find visual packs | Models/sprites, UI, textures categories | sprites, pixel-art, 3d-models, game-ui, textures, pbr |
| Find sound and effects | Audio and VFX categories | game-audio, sound-effects, vfx, shaders |
| Find animation examples | Animation category | animation |
| Find curated collections | Complete tables and source links | awesome, awesome-list |
| Find permissive resources | Per-row practical conditions and original license | cc0 describes a subset, not the entire directory |
| Find web-game examples | Actual Three.js-related entries | threejs retained from existing topics, not a universal compatibility promise |

These are intent-based editorial choices, not measured search-volume rankings. No keyword-volume, traffic or star-growth claim is made. All 12 existing relevant topics were retained; the six additions are sprites, pixel-art, pbr, game-audio, game-ui and shaders. Engines are discussed in the compatibility FAQ, but blanket engine-support tags were not added merely to attract traffic.

## README and GEO implementation

- Five-language summaries state what is indexed: resources include asset packs, tools and code examples, not 297 uniformly downloadable or commercially cleared assets.
- Six use-case links go directly to existing category anchors; the complete 15-category navigation and comparison tables remain intact.
- Four brief, localized questions address commercial use, code versus media licenses, engine compatibility and ranking provenance. They are visible reader content, not hidden keyword blocks.
- `llms.txt` is generated from the same dataset and language map. It links all five overviews and full catalogs, source JSON, translations and rights methodology using absolute public URLs.
- `data/discovery.json` holds translated discovery copy and metadata. Source-drift tests require translation review when English discovery copy changes.
- No crawler directives, JSON-LD, canonical or hreflang tags are injected into README: this repository does not control github.com's HTML head. No artificial rating, fake FAQ rich-result claim, tracking code, visitor badge, promotion posting or star automation was added.

## What this can and cannot establish

GitHub repository search uses name, description and topics by default; `in:readme` explicitly includes README text. Clear About and topics therefore complement rather than duplicate the README. Topics are classification labels, not ranking guarantees.

The optional llms.txt file is navigation for tools that choose to read it. It does not request or guarantee model training, indexing, AI recommendations or Google rankings. Google's current AI-search guidance says no special AI markup is needed and llms.txt is not used to improve visibility in Search. Answers remain subject to the original sources and their changing terms.

The previous sentence “Every entry has a verified license” in About has been removed. This directory stores license evidence and practical summaries; it cannot certify every downloadable file, ownership claim or current term. This change is especially important because the catalog includes restricted and component-specific licenses.

## Verification and future measurement

- Verify actual About/topics after applying settings; validate all five language links, local category anchors, generated counts and license boundaries.
- Run the repository's offline and network checks; inspect actual GitHub desktop and narrow-screen presentation. Successful checks are not evidence of search ranking gains.
- If search performance is evaluated later, record query, platform, date, region/login conditions and comparison window. Suggested fixed queries: `game assets`, `game assets cc0`, `pixel art sprites`, `PBR textures game`, plus GitHub qualifiers `topic:game-assets` and `game assets in:readme`.
- Do not claim broad crawl coverage or Search Console ownership of github.com. An independent published site would require separate approval and separate title/description, canonical, language, sitemap and structured-data implementation.

## Official references

- [GitHub repository search](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- [GitHub topics rules](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub README behavior](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Google AI search optimization guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Optional llms.txt proposal](https://llmstxt.org/)

## 中文说明

这轮先优化截图中的 About 和 Topics，再对齐五语首页、按用途查找入口、常见使用问题及机器可读导航。关键词来自目录真实内容，不堆砌无关热门词；CC0 只代表部分资源，不能宣传全库免费商用。GEO.md 只是维护记录，llms.txt 是可选导航，二者都不能保证搜索排名或 AI 推荐。没有建立独立站，也没有假装控制 GitHub 页面的 meta、canonical 或 hreflang。
