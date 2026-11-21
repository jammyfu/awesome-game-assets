# WORKLOG.md

## 2026-11-21（PLAN-008 README 同步）

- 基线：main `2b08ede`（已合 PR #8），无开放 PR。不复用已合分支，新开 `cursor/readme-sync-counts-3603`。
- 实核：`data/entries.json` 320 条、15 类。分类条数：models 35、ui 23、textures 9、audio 22、fonts 15、vfx 21、abilities 15、animation 27、physics 21、ai 13、procgen 21、engines 29、tools 29、aigen 23、lists 17。GitHub 251 / 网站 69。2026-11-21 新增 23 条。
- 已正确未改：首页总述已是 320·15·5；15 类表格与 hero；精选 ID 仍为 kenney-pixel-platformer / quaternius-base-characters / kenney-ui-pack。
- 缺口：目录无分类计数；特色入口无条数；收录规则仍写许可证于 2026-11-12 核实；排序注记只提 2026-11-12 星标快照；CONTRIBUTING 仍写只做中英。
- 修正：渲染器从条目计算分类计数与最早/最晚核验日（2026-11-12–2026-11-21）；目录与六条特色入口加条数；标题不加数字以免锚点变化；五语 sort_note / 许可规则改占位符；CONTRIBUTING、discovery、llms.txt、GEO 入口同步。不搜集新素材。
- 验证：`python3 tools/verify.py` 绿（42 tests）；`GITHUB_TOKEN` 下 `python3 tools/check_links.py` 0 错误 / 10 警告，警告均为既有 pixabay/blender 403 与 GitHub 未识别许可证条目。无 token 时 GitHub API 会 403 限流，不代表新增链接失效。

## 2026-11-21（PLAN-007 素材扩充）

- 基线：main `b99daf5`，无开放 PR。遵循仓内 AGENTS 与 CoderSkills `continuous-project-loop` / `git-project-harness`（不改造项目骨架）。
- 缺口：贴图仅 5 条且多为工具；音频多为库/生成器；2D/3D 偏 Kenney。本轮只收许可证在官方页写明、链接可达、可公开推荐的素材。
- 新增 23 条（核验日 2026-11-21）：贴图 4（cgbookcase、TextureCan、3DTextures.me、Kenney Prototype Textures）；2D/3D 8（Pixel Adventure、Treasure Hunters、Sunny Land、Medieval King Pack 2、16x16 Industrial Tileset、KayKit Dungeon、KayKit Adventurers、Kenney Nature Kit）；音频 4（Kenney Interface/Impact、5 Chiptunes、512 8-bit SFX）；字体 1（Silkscreen OFL）；UI 3（Kenney Board Game Icons、Golden UI、Ravenmore Fantasy UI）；特效 2（Kenney Smoke Particles、Sinestesia 2D explosions）；动画 1（KayKit Character Animations，区别于已收旧版）。
- 许可证：GitHub 条目核 API `license`（Silkscreen = OFL-1.1，27★，2026-11-21）；网站读官方条款页或素材页的 CC0 / CC-BY-3.0 原文。Kenney 条目以 kenney.nl/support 为许可证据，并在各素材页看到 Creative Commons CC0。
- 配图：全部热链官方预览（Kenney media、itch.zone、OGA files、cgbookcase CDN、TextureCan、3dtextures、GitHub documentation specimen）。核验 HTTP 与魔数；不复制进仓、不生成图。展示不等于再分发授权。
- 未收：ShareTextures（自定义 CC0 + 禁再分发/热链条款）、m6x11（页上写需署名但无标准许可证字段）、Zpix（商业收费）、NASA 3D Resources（GitHub `license` 为空且 NASA 媒体使用限制）、GameArt2D（许可页 404）、Patrick de Arteaga / soundimage（条款不够具体）、Mixamo（专有）、Tiny Swords（禁止再打包）、KayKit furniture-bits 404。
- 五语描述写入 `data/locales/` 后按 `tools/check_locales.py` 刷新 `source_sha256`。生成 README/catalog，不手改。
- 验证：`python3 tools/verify.py` 绿（41 tests）；`python3 tools/check_links.py` 0 错误 / 10 警告，警告均为既有 pixabay/blender 403 与 GitHub 未识别许可证条目，本轮新增链接无 404。

## 2026-11-12

- 按 CoderSkills `multi-project-program-management`（`bootstrap_project.py`）生成骨架，接 `continuous-project-loop` 循环。
- main 只有最小初始提交（占位 README + CC0 LICENSE）；清单内容在 `feat/initial-list` 分支走 PR。
- 首批 25 条：GitHub 仓用 API `license` 字段核实，网站用官方许可页核实；全部链接与图片可达性已检查。
- 配图：18 条用项目原图（引用原地址并注明出处），7 张分类封面 + 7 张无原图条目示意图由 Codex CLI 0.162.1 原创生成。
- 验证：`python3 tools/verify.py` 绿，`python3 tools/check_links.py` 0 错误（blender.org 对机器人 403 记警告；glTF-Sample-Assets 无仓库级许可证，按模型授权，记警告）。

## 2026-11-12（第二轮）

- 新增 14 条，共 39 条：Polyfork（许可页核实：免费模型文件 CC-BY-4.0 或 Polyfork 许可二选一，ES 模块与 HD 版仅 Polyfork 许可）、The Base Mesh、Game-icons.net、Controller & Keyboard Prompts、LPC 角色生成器、AwesomeBump、rFXGen、Bosca Ceoil Blue、JangaFX VDB、GASDocumentation、EX-GAS for Unity、Synfig、Piskel、Krita。
- 参考清单：Calinou/awesome-gamedev（CC-BY-SA-4.0）、madjin/awesome-cc0（CC0-1.0）；只借线索，每个来源重新核实、描述重写；README 加 Credits 节。
- 未收：Poly Pizza、Texture Ninja（页面上查不到许可证文字）、madjin/100Avatars（仓库无许可证）、Incompetech（许可页未能核实）、CMU mocap（官网 500）。
- 联网校验加重试，超时与 403 记警告保留；离线校验加 README 重复链接检查与 Credits 检查。

## 2026-11-12（第三轮：扩充 PR）

- 从最新 main（52e1ac3）开 `feat/round-2-expand`；共 297 条，15 个分类：3D 模型与 2D 素材 27、UI、图标与 HUD 20、贴图与材质 5、音效与音频 18、字体 14、特效、粒子与着色器 19、技能 / 施法 / 战斗演示 15、动画与动捕 26、物理 21、游戏 AI 与寻路 13、程序化生成 21、引擎与框架 29、工具与管线 29、AI 素材生成与 Agent Skill 23、其他清单与设计参考 17。
- 并行搜索：Mac mini 上 agy CLI 1.5.5，模型 `gemini-3.8-flash-medium`（Gemini 3.8 Flash，medium 档），17 条线路（2D/3D、像素、角色、UI、动画/动捕、特效/着色器、音频、字体、技能/战斗、物理、AI/寻路、程序化、引擎、工具链、设计参考、AI 工具/Skill、其他清单）；pixel / abilities / ai-pathfinding 首跑 15 分钟超时，放宽到 20 分钟重跑。再用 gh API 和 WebSearch 自己补搜。
- agy 结果只当线索：每条重新核实可达性（GitHub API / HTTP）、许可证（API `license` 字段；NOASSERTION/NONE 读 LICENSE 或 README 原文；网站读许可页），描述中英自写。agy 给的 found_via 大多对不上（在对应清单 README 里找不到该链接），只有核实到的 6 条写了「参考清单」，Credits 增 ellisonleao/magictools（MIT）、simoninithomas/awesome-ai-tools-for-game-dev（CC0-1.0）、Calinou/awesome-godot（CC-BY-4.0）。
- 配图：原图优先（README 首张非徽章图或官网 og:image，直接引用原地址）；无原图的由 Codex CLI 0.162.1 生成，本轮新生成 80 张（8 张分类封面 + 72 张条目图），统一风格、无真人脸、无商标/IP，单张 < 300KB，提示词见 `docs/image-prompts.md`。
- 警示清单：新建 `data/warnings.json` → `WARNING.md` / `WARNING.zh-CN.md`，23 条（破解 12、疑似恶意软件 9、付费素材二次分发 2、盗版 0、刷星 0）；只链仓库首页，配图只引用 GitHub 上的原图地址，不存进仓库。
- 未收（主清单）：FreePD（站点已关闭）、Smithsonian 3D（Cloudflare 403，许可无法核实）、Game UI Database（无开放许可）、Lospec 调色板（许可不清）、Texture Ninja / Poly Pizza（查不到许可文字）、M3-org/retro3d-assets、DruidMech/GameplayAbilitySystem_Aura、yulrun/godot-gas、StableDelight、blender-animation-retargeting、Expy-Kit、GDQuest/game-sprites、LPC spritesheet 仓、jfxr、vrm-specification、evenfurther/pathfinding、MicroPather、FEMFX、FidelityFX-SDK、3d-game-shaders-for-beginners、KinoGlitch、cocos2d-x（仓库无许可证文件，未能核实）、sjai013/unity-gameplay-ability-system、rhasspy/piper、MB-Lab、liquidfun、qu3e、resonance-audio、0ad、promptfont、godot-mcp、glitch 素材仓、sledge、crunch（已归档）、Aseprite（专有 EULA）、Kenney Input Prompts（与已收 controller-prompts 重复且含主机商标图形）、6 个单函数旧 glsl 小库（glsl-noise 等，与 webgl-noise/glslify 重复）、若干 404/500 链接（CMU mocap、Incompetech、jsfxr、FamiStudio、bosca-ceoil 旧址、raygui 旧址等）、低星模板仓（GDD 模板、CC0Tree 等）。
- 验证：`python3 tools/verify.py` 绿（21 个测试）；`python3 tools/check_links.py` 0 错误，⚠ 警告为 403（pixabay、blender.org）与「GitHub 未识别许可证、已人工核实」类。

## Homepage discovery revision

Baseline: main `5de6564`, clean isolated checkout, no open PRs observed. Reused the current CoderSkills Git Project Harness contract. Generated compact English/Chinese homepages and complete catalogs, preserved all 297 entry records, retained existing category order with explicit unknown recent-heat evidence, and gated third-party media on reuse-license records. Added GEO proposal (not applied) and llms.txt. Offline verification: 23 tests pass. Harness static checks cover both homepages and both catalogs. CLI exposure audit blocked by absent gh authentication; connector remains available. Network and actual GitHub render checks are tracked separately and must not be inferred from the static pass.

GitHub review of commit 083d810: English and Chinese README renders inspected at the available desktop viewport; all three featured images loaded. Both catalog links, 15 category headings per catalog, 297 entry rows plus 5 credit rows, and the contribution path were checked in actual GitHub DOM. Narrow 390px and dark-mode checks remain not checked; no supported viewport control was exposed. Remote offline CI passed; full network/license CI remains pending and is not represented as green. These checks do not establish recent popularity or blanket license clearance.


## Restore the requested table format

The prior responsive revision incorrectly replaced the owner's comparison tables with vertical lists. The owner explicitly requires tables for a large asset directory. Starting from main a44c1e8 with no open PRs observed, this revision restores every entry to both README languages and both catalogs as 15 genuine three-column tables. Preview and project share a cell; license evidence and use descriptions remain separate. Narrow screens may scroll inside tables, never silently receive cards. AGENTS.md and regression tests now preserve this requirement. Original data and permissions remain unchanged. A newly generated game-specific hero is being prepared; actual rendering and final CI evidence will be recorded in the PR.

## 2026-11-12: About, topics and five-language discovery

Inspected the owner's screenshot and live About/topics. Updated only repository description and six additional relevant topics through the owner's existing GitHub session, then read back the exact 18-topic set. No homepage/site, permissions or visibility were changed. Content work uses a separate branch: five-language reader routes and practical FAQ, a generated five-language llms.txt, metadata manifest, official-source rationale and regression tests. Source entries, licenses, previews and popularity values are unchanged. Independent review and public render/CI checks are recorded in the PR before delivery; no ranking or citation improvement is claimed.
