# Selection, licenses and previews / 选材、许可与预览

## Reader path / 阅读路径

The homepage shows three concrete asset packs, then links into the complete bilingual catalog. All 297 original entries and their descriptions, source URLs and license notes remain in `data/entries.json`. Catalog order and counts are generated, not maintained separately. Translations are not counted as extra resources.

首页先展示三组具体素材，再进入完整双语目录。原有 297 条资源及其说明、来源和许可均保留；两种语言不重复计数。

## Ordering evidence / 排序依据

- Source: `data/entries.json`, including the `discovery` record. Observed at the UTC timestamp stored there.
- Comparable recent popularity: **unknown**. No recent-star time series or cross-platform traffic series was available for these asset packs; lifetime stars and release recency are not substitutes.
- Window, metric and value: null (not measured). No claim of a trending leaderboard.
- Priority basis: `editorial_priority`. 2D scene tiles, rigged 3D characters and UI components serve three distinct prototype needs. They are not ranked by quality or popularity.
- Group order: directly usable asset packs first; engines, production tools and references remain available by category. Existing category and within-category order is retained as the stable tie break. Unknown popularity is not treated as zero.
- Confidence: high for catalog membership and license-page links; unknown for current popularity. Both languages consume the same featured ID list.
- Candidates not featured: restricted model weights and code-only tools are useful in the catalog, but less representative of ready-to-use asset packs. No entries are removed.

近期热度缺少同窗口可比数据，明确记为未知。精选以实际搭建游戏的用途作编辑判断，不将累计星数冒充近期热度；中英共用同一排序数据。

## Preview rights / 预览权利

The featured Kenney Pixel Platformer, Kenney UI Pack and Quaternius Universal Base Characters packs declare CC0 on their official pack pages. Those pages were reachable and their CC0 declarations rechecked for this revision. The images depict those packs and link back to the original creator; no third-party files are copied into this repository.

Each embedded third-party entry preview now needs `image.reuse_license` and `image.license_source`. Existing media without this evidence stays accessible through a source-page link instead of being hotlinked. Existing generated illustrations remain explicitly labeled in the full catalog; they are not product screenshots or evidence of the listed tool's output.

精选素材的官方页面标明 CC0，页面可达性与声明已重新检查。未记录媒体再使用依据的旧预览改为来源页链接。目录中的原创示意图仍清楚标注，不冒充实际效果。

## License boundaries / 许可边界

This directory includes permissively licensed assets, per-asset libraries, open-source tools and explicitly restricted resources. Inclusion is not blanket commercial-use permission. Code, weights, outputs, sample content and preview media can have different terms. Read the canonical license before shipping, retain required credits and verify the specific downloaded files.

清单包含宽松许可素材、逐条许可的素材库、开源工具和明确限制用途的资源。收录不等于可无条件商用；代码、权重、输出、示例和媒体可能适用不同许可。

## Maintenance / 维护

Edit the dataset or renderer, then run `python3 tools/render_readme.py`, `python3 tools/verify.py` and `python3 tools/check_links.py`. Link-check warnings are not a clean reachability pass. Homepage renders and all local catalog links need independent GitHub review. No telemetry or automatic growth monitoring is added.
