# WORKLOG.md

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
