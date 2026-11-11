# Awesome Game Assets（开源游戏素材清单）

[English](README.md) · **简体中文**

精选许可证清楚的游戏素材和工具：3D 模型、2D 精灵、贴图材质、音效、特效、技能 / 施法演示、动画和编辑器。每条写明地址、在来源页核实过的许可证，以及适合做什么。

> ⚠️ 搜到的疑似盗版、破解、付费素材二次分发、刷星或恶意软件仓库单独列在 [WARNING.zh-CN.md](WARNING.zh-CN.md)，用于避坑，请勿使用。

## 目录

- [3D 模型与 2D 素材](#3d-模型与-2d-素材)
- [UI、图标与 HUD](#ui图标与-hud)
- [贴图与材质](#贴图与材质)
- [音效与音频](#音效与音频)
- [字体](#字体)
- [特效、粒子与着色器](#特效粒子与着色器)
- [技能 / 施法 / 战斗演示](#技能--施法--战斗演示)
- [动画与动捕](#动画与动捕)
- [物理](#物理)
- [游戏 AI 与寻路](#游戏-ai-与寻路)
- [程序化生成](#程序化生成)
- [引擎与框架](#引擎与框架)
- [工具与管线](#工具与管线)
- [AI 素材生成与 Agent Skill](#ai-素材生成与-agent-skill)
- [其他清单与设计参考](#其他清单与设计参考)

## 收录规则

- 只收在项目或官网上写清许可证的来源。按素材单独授权的会标明，使用前请逐个确认。
- 不收盗版、破解或刷星的仓库（看过 star、fork 和活跃度），不收已归档且不可用的仓库。
- 每条链接都检查过：404 剔除；对自动检查返回 403 或超时的保留并标 ⚠。
- 许可证于 2026-11-12 核实：GitHub 仓库看 API 的 `license` 字段，网站看每行链接的官方许可页。
- 预览图用项目自己的图，直接引用原地址（每行注明出处）。分类封面和标注 *示意图* 的条目是为本清单原创生成的，提示词见 [docs/image-prompts.md](docs/image-prompts.md)。

## 3D 模型与 2D 素材

<img src="docs/images/cover-models.webp" alt="分类封面（原创示意图）: 3D 模型与 2D 素材" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="docs/images/entry-kenney.webp" alt="Kenney Game Assets (示意图)" width="160"> | [Kenney Game Assets](https://kenney.nl/assets)<br><sub>*示意图*</sub> | [CC0-1.0](https://kenney.nl/support) | 上千套风格统一的 2D 精灵、UI、3D 模型和音效包，适合做原型和 Game Jam。 |
| <img src="https://quaternius.com/assets/images/fullres/metadata.jpg" alt="Quaternius" width="160"> | [Quaternius](https://quaternius.com/)<br><sub>图片来源：项目 [Quaternius](https://quaternius.com/)</sub> | [CC0-1.0](https://quaternius.com/faq.html) | 低多边形 3D 素材包（角色、自然、建筑、武器），FBX/OBJ/glTF 格式，免费包为 CC0。 |
| <img src="docs/images/entry-opengameart.webp" alt="OpenGameArt.org (示意图)" width="160"> | [OpenGameArt.org](https://opengameart.org/)<br><sub>*示意图*</sub> | [按素材单独授权（CC0 / CC-BY / CC-BY-SA / GPL / OGA-BY）](https://opengameart.org/content/faq) | 社区共享的 2D、3D、音乐和音效库；每个素材页都标明许可证，使用前逐个确认。 |
| <img src="https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/GlassHurricaneCandleHolder/screenshot/screenshot.jpg" alt="KhronosGroup/glTF-Sample-Assets" width="160"> | [KhronosGroup/glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets)<br><sub>图片来源：项目 [KhronosGroup/glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets)</sub> | [按模型单独授权（多为 CC0 / CC-BY-4.0，少数为自定义条款，见 REUSE.toml）](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/LICENSES) | 官方 glTF 参考模型，适合测试加载器、PBR 材质和引擎导入流程。 |
| <img src="https://polyfork.dev/img/og.png" alt="Polyfork" width="160"> | [Polyfork](https://polyfork.dev/assets)<br><sub>图片来源：项目 [Polyfork](https://polyfork.dev/assets)</sub> | [免费低多边形模型文件：CC-BY-4.0 或 Polyfork 许可（二选一）；ES 模块和 HD 版：仅 Polyfork 许可](https://polyfork.dev/licensing) | 3000+ 个免费低多边形 3D 模型，GLB 加 three.js ES 模块；走 CC BY 要署名 Polyfork，走 Polyfork 许可不用署名但不能转发文件。付费档另有 HD 版。 |
| <img src="https://static.wixstatic.com/media/b36d2d_080f2dd3e7cc497cba4f0152b7fefcf5%7Emv2.png/v1/fit/w_2500,h_1330,al_c/b36d2d_080f2dd3e7cc497cba4f0152b7fefcf5%7Emv2.png" alt="The Base Mesh" width="160"> | [The Base Mesh](https://www.thebasemesh.com/)<br><sub>图片来源：项目 [The Base Mesh](https://www.thebasemesh.com/)</sub><br><sub>参考清单 [madjin/awesome-cc0](https://github.com/madjin/awesome-cc0)</sub> | [CC0-1.0](https://www.thebasemesh.com/) | 1250+ 个按真实尺寸做的基础网格，适合白盒搭场景、雕刻起稿和做原型。 |
| <img src="https://raw.githubusercontent.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/master/readme-images/example.png" alt="LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator" width="160"> | [LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator)<br><sub>图片来源：项目 [LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [GPL-3.0（代码）；美术按素材单独授权（CC0 / CC-BY / CC-BY-SA / OGA-BY / GPL）](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator#licensing-and-attribution-credits) | 网页版 RPG 角色精灵表生成器，分层拼装，含行走、劈砍、施法动画，可导出署名清单。 |
| <img src="docs/images/entry-makehuman.webp" alt="makehumancommunity/makehuman (示意图)" width="160"> | [makehumancommunity/makehuman](https://github.com/makehumancommunity/makehuman)<br><sub>*示意图*</sub> | [AGPL-3.0（代码）/ CC0-1.0（自带素材）](https://github.com/makehumancommunity/makehuman) | 参数化 3D 人物角色生成器；导出的角色和自带素材为 CC0。 |
| <img src="https://vrm.dev/en/images/vrm/card.png" alt="vrm-c/UniVRM" width="160"> | [vrm-c/UniVRM](https://github.com/vrm-c/UniVRM)<br><sub>图片来源：项目 [vrm-c/UniVRM](https://vrm.dev/en)</sub> | [MIT](https://github.com/vrm-c/UniVRM) | Unity 的 VRM 人形角色导入导出工具（基于 glTF），支持弹簧骨骼和表情。 |
| <img src="https://raw.githubusercontent.com/PolygonalMind/initiative-opensource-release/main/images/PolygonalMind_Logo.jpg" alt="PolygonalMind/initiative-opensource-release" width="160"> | [PolygonalMind/initiative-opensource-release](https://github.com/PolygonalMind/initiative-opensource-release)<br><sub>图片来源：项目 [PolygonalMind/initiative-opensource-release](https://github.com/PolygonalMind/initiative-opensource-release)</sub> | [CC0-1.0](https://github.com/PolygonalMind/initiative-opensource-release) | Polygonal Mind 的 CC0 开源发布，含 100 Avatars 角色包和 3D 场景。 |

## UI、图标与 HUD

<img src="docs/images/cover-ui.webp" alt="分类封面（原创示意图）: UI、图标与 HUD" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://game-icons.net/icons/ffffff/000000/1x1/caro-asercion/tarot-21-the-world.svg" alt="Game-icons.net" width="160"> | [Game-icons.net](https://game-icons.net/)<br><sub>图片来源：项目 [Game-icons.net](https://game-icons.net/)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [CC-BY-3.0](https://game-icons.net/about.html) | 4000+ 个 SVG/PNG 游戏图标（技能、道具、状态），按要求给每个图标作者署名。 |
| <img src="docs/images/entry-controller-prompts.webp" alt="Those Awesome Guys: Controller & Keyboard Prompts (示意图)" width="160"> | [Those Awesome Guys: Controller & Keyboard Prompts](https://thoseawesomeguys.com/prompts/)<br><sub>*示意图*</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [CC0-1.0](https://thoseawesomeguys.com/prompts/) | 键盘、鼠标和常见手柄的按键提示图标，做新手引导和操作提示用。 |
| <img src="https://github.com/user-attachments/assets/6c76658c-302f-403b-af26-d517e2bfb0d4" alt="ocornut/imgui" width="160"> | [ocornut/imgui](https://github.com/ocornut/imgui)<br><sub>图片来源：项目 [ocornut/imgui](https://github.com/ocornut/imgui)</sub> | [MIT](https://github.com/ocornut/imgui) | 即时模式 GUI 库（Dear ImGui），做调试菜单、游戏内工具和编辑器。 |
| <img src="https://kenney.nl/media/pages/assets/ui-pack/ab9e396e4d-1718203978/preview.png" alt="Kenney UI Pack" width="160"> | [Kenney UI Pack](https://kenney.nl/assets/ui-pack)<br><sub>图片来源：项目 [Kenney UI Pack](https://kenney.nl/assets/ui-pack)</sub> | [CC0-1.0](https://kenney.nl/assets/ui-pack) | 430 个 UI 元素（按钮、滑条、面板），多种配色，做菜单和 HUD。 |

## 贴图与材质

<img src="docs/images/cover-textures.webp" alt="分类封面（原创示意图）: 贴图与材质" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://cdn.polyhaven.com/site_images/home/window_rend.jpg?width=630&quality=95" alt="Poly Haven" width="160"> | [Poly Haven](https://polyhaven.com/)<br><sub>图片来源：项目 [Poly Haven](https://polyhaven.com/)</sub> | [CC0-1.0](https://polyhaven.com/license) | 高质量 PBR 贴图、HDRI 环境光和扫描模型，适合写实场景和打光。 |
| <img src="docs/images/entry-ambientcg.webp" alt="ambientCG (示意图)" width="160"> | [ambientCG](https://ambientcg.com/)<br><sub>*示意图*</sub> | [CC0-1.0](https://docs.ambientcg.com/license/) | 大量 CC0 PBR 材质、HDRI 和模型，提供多种分辨率。 |
| <img src="https://raw.githubusercontent.com/kmkolasinski/AwesomeBump/Release/Sources/resources/promo/githubimage5.jpg" alt="kmkolasinski/AwesomeBump" width="160"> | [kmkolasinski/AwesomeBump](https://github.com/kmkolasinski/AwesomeBump)<br><sub>图片来源：项目 [kmkolasinski/AwesomeBump](https://github.com/kmkolasinski/AwesomeBump)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub><br><sub>参考清单 [madjin/awesome-cc0](https://github.com/madjin/awesome-cc0)</sub> | [GPL-3.0](https://github.com/kmkolasinski/AwesomeBump) | 从一张图生成法线、高度、高光、AO、粗糙度和金属度贴图（最后更新 2023 年）。 |
| <img src="https://armorpaint.org/img/git.jpg" alt="armory3d/armorpaint" width="160"> | [armory3d/armorpaint](https://github.com/armory3d/armorpaint)<br><sub>图片来源：项目 [armory3d/armorpaint](https://github.com/armory3d/armorpaint)</sub> | [Zlib](https://github.com/armory3d/armorpaint) | PBR 3D 贴图绘制工具（源码开源，官方预编译版另售）。 |
| <img src="https://user-images.githubusercontent.com/46932830/87454669-acbf9300-c5da-11ea-932a-fa4ec67e705f.png" alt="azagaya/laigter" width="160"> | [azagaya/laigter](https://github.com/azagaya/laigter)<br><sub>图片来源：项目 [azagaya/laigter](https://github.com/azagaya/laigter)</sub> | [GPL-3.0](https://github.com/azagaya/laigter) | 给 2D 精灵生成法线、高光和遮蔽贴图，实现动态光照。 |

## 音效与音频

<img src="docs/images/cover-audio.webp" alt="分类封面（原创示意图）: 音效与音频" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="docs/images/entry-freesound.webp" alt="Freesound (示意图)" width="160"> | [Freesound](https://freesound.org/)<br><sub>*示意图*</sub> | [按音效单独授权（CC0 / CC-BY-4.0 / CC-BY-NC-4.0）](https://freesound.org/help/faq/) | 超大社区音效库；按许可证筛选（商用游戏选 CC0 或 CC-BY），需要署名时照做。 |
| <img src="https://cdn.sonniss.com/storage/2025/03/Sonniss-Metaimage.png" alt="Sonniss #GameAudioGDC Bundles" width="160"> | [Sonniss #GameAudioGDC Bundles](https://sonniss.com/gameaudiogdc)<br><sub>图片来源：项目 [Sonniss #GameAudioGDC Bundles](https://sonniss.com/gameaudiogdc)</sub> | [免版税（Sonniss 许可：可商用，无需署名）](https://sonniss.com/gameaudiogdc) | 每年免费放出的专业音效合集，商用游戏免版税。 |
| <img src="https://raw.githubusercontent.com/chr15m/jsfxr/master/screenshot.png" alt="chr15m/jsfxr" width="160"> | [chr15m/jsfxr](https://github.com/chr15m/jsfxr)<br><sub>图片来源：项目 [chr15m/jsfxr](https://github.com/chr15m/jsfxr)</sub> | [Unlicense](https://github.com/chr15m/jsfxr) | 浏览器里的复古音效生成器（sfxr 移植），一键出跳跃、金币、受击、激光音。 |
| <img src="https://raw.githubusercontent.com/raysan5/rfxgen/master/screenshots/rfxgen_v500_shot01.png" alt="raysan5/rfxgen" width="160"> | [raysan5/rfxgen](https://github.com/raysan5/rfxgen)<br><sub>图片来源：项目 [raysan5/rfxgen](https://github.com/raysan5/rfxgen)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [Zlib](https://github.com/raysan5/rfxgen) | raylib 作者做的小型 sfxr 风格音效生成器，桌面版和网页版都有。 |
| <img src="https://raw.githubusercontent.com/YuriSizov/boscaceoil-blue/main/dist/logo-full.png" alt="YuriSizov/boscaceoil-blue" width="160"> | [YuriSizov/boscaceoil-blue](https://github.com/YuriSizov/boscaceoil-blue)<br><sub>图片来源：项目 [YuriSizov/boscaceoil-blue](https://github.com/YuriSizov/boscaceoil-blue)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [MIT](https://github.com/YuriSizov/boscaceoil-blue/blob/main/LICENSE) | 新手友好的步进音序器作曲工具，是 Terry Cavanagh 的 Bosca Ceoil 现代移植版，适合做游戏循环配乐和短旋律。 |
| <img src="https://miniaud.io/img/miniaudio_wide.png" alt="mackron/miniaudio" width="160"> | [mackron/miniaudio](https://github.com/mackron/miniaudio)<br><sub>图片来源：项目 [mackron/miniaudio](https://github.com/mackron/miniaudio)</sub> | [Unlicense 或 MIT-0（二选一）](https://github.com/mackron/miniaudio) | 单文件 C 音频播放 / 录音库，带混音和效果，好嵌进引擎。 |
| <img src="https://raw.github.com/jarikomppa/soloud/master/soloud.png" alt="jarikomppa/soloud" width="160"> | [jarikomppa/soloud](https://github.com/jarikomppa/soloud)<br><sub>图片来源：项目 [jarikomppa/soloud](https://github.com/jarikomppa/soloud)</sub> | [Zlib](https://github.com/jarikomppa/soloud) | 简单易移植的 C++ 游戏音频引擎，支持 3D 音效、滤波器和语音合成。 |
| <img src="docs/images/entry-tonejs.webp" alt="Tonejs/Tone.js (示意图)" width="160"> | [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)<br><sub>*示意图*</sub> | [MIT](https://github.com/Tonejs/Tone.js) | Web Audio 交互音乐框架：浏览器里的合成器、效果器和节拍调度。 |
| <img src="https://s3.amazonaws.com/howler.js/howler-logo.png" alt="goldfire/howler.js" width="160"> | [goldfire/howler.js](https://github.com/goldfire/howler.js)<br><sub>图片来源：项目 [goldfire/howler.js](https://github.com/goldfire/howler.js)</sub> | [MIT](https://github.com/goldfire/howler.js) | 网页游戏音频库：音频精灵、空间音效、跨浏览器播放。 |
| <img src="https://dev.azure.com/surge-synthesizer/surge/_apis/build/status/surge-synthesizer.surge?branchName=main" alt="surge-synthesizer/surge" width="160"> | [surge-synthesizer/surge](https://github.com/surge-synthesizer/surge)<br><sub>图片来源：项目 [surge-synthesizer/surge](https://github.com/surge-synthesizer/surge)</sub> | [GPL-3.0](https://github.com/surge-synthesizer/surge) | Surge XT，强大的开源合成器，做游戏音乐和音效。 |
| <img src="docs/images/entry-bfxr.webp" alt="increpare/bfxr (示意图)" width="160"> | [increpare/bfxr](https://github.com/increpare/bfxr)<br><sub>*示意图*</sub> | [Apache-2.0（README 中声明）](https://github.com/increpare/bfxr#readme) | 复古音效生成器（sfxr 增强版），做跳跃、拾取、爆炸音。 |
| <img src="docs/images/entry-pixabay-sfx.webp" alt="Pixabay Sound Effects (示意图)" width="160"> | [Pixabay Sound Effects](https://pixabay.com/sound-effects/)<br><sub>*示意图*</sub><br><sub>⚠ 网站对自动检查返回 403，许可证已人工核实</sub> | [Pixabay 内容许可（免费、免署名；不得原样转卖）](https://pixabay.com/service/license-summary/) | 大量免版税音效和音乐，采用 Pixabay 内容许可。 |

## 字体

<img src="docs/images/cover-fonts.webp" alt="分类封面（原创示意图）: 字体" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="docs/images/entry-google-fonts.webp" alt="google/fonts (示意图)" width="160"> | [google/fonts](https://github.com/google/fonts)<br><sub>*示意图*</sub> | [按字体家族单独授权（OFL-1.1 / Apache-2.0 / UFL）](https://github.com/google/fonts#license) | Google Fonts 全部字体源文件；目录名就是许可证，不少支持中日韩。 |
| <img src="https://raw.githubusercontent.com/rektdeckard/departure-mono/main/public/assets/departure-og.png" alt="rektdeckard/departure-mono" width="160"> | [rektdeckard/departure-mono](https://github.com/rektdeckard/departure-mono)<br><sub>图片来源：项目 [rektdeckard/departure-mono](https://github.com/rektdeckard/departure-mono)</sub> | [OFL-1.1（字体）/ MIT（网站）](https://github.com/rektdeckard/departure-mono) | 复古未来感的等宽像素字体，适合 HUD 和终端界面。 |
| <img src="https://raw.githubusercontent.com/TakWolf/fusion-pixel-font/master/docs/logo@2x.png" alt="TakWolf/fusion-pixel-font" width="160"> | [TakWolf/fusion-pixel-font](https://github.com/TakWolf/fusion-pixel-font)<br><sub>图片来源：项目 [TakWolf/fusion-pixel-font](https://github.com/TakWolf/fusion-pixel-font)</sub> | [OFL-1.1（字体）/ MIT（构建程序）](https://github.com/TakWolf/fusion-pixel-font) | 开源泛中日韩像素字体，覆盖中日韩和拉丁字符，有 8/10/12 像素尺寸。 |
| <img src="https://raw.githubusercontent.com/TakWolf/ark-pixel-font/master/docs/readme-banner.png" alt="TakWolf/ark-pixel-font" width="160"> | [TakWolf/ark-pixel-font](https://github.com/TakWolf/ark-pixel-font)<br><sub>图片来源：项目 [TakWolf/ark-pixel-font](https://github.com/TakWolf/ark-pixel-font)</sub> | [OFL-1.1（字体）/ MIT（构建程序）](https://github.com/TakWolf/ark-pixel-font) | 开源中日韩像素字体（方舟像素字体），为像素风游戏设计。 |
| <img src="https://kenney.nl/media/pages/assets/kenney-fonts/703183582c-1677661704/preview.png" alt="Kenney Fonts" width="160"> | [Kenney Fonts](https://kenney.nl/assets/kenney-fonts)<br><sub>图片来源：项目 [Kenney Fonts](https://kenney.nl/assets/kenney-fonts)</sub> | [CC0-1.0](https://kenney.nl/assets/kenney-fonts) | Kenney 的 11 款游戏风格字体，任何项目都能用。 |

## 特效、粒子与着色器

<img src="docs/images/cover-vfx.webp" alt="分类封面（原创示意图）: 特效、粒子与着色器" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Alchemist0823/three.quarks/master/landing.png" alt="Alchemist0823/three.quarks" width="160"> | [Alchemist0823/three.quarks](https://github.com/Alchemist0823/three.quarks)<br><sub>图片来源：项目 [Alchemist0823/three.quarks](https://github.com/Alchemist0823/three.quarks)</sub> | [MIT](https://github.com/Alchemist0823/three.quarks) | three.js 通用粒子 / 特效引擎，带可视化编辑器。 |
| <img src="https://three-nebula.org/og/og-image.jpg" alt="creativelifeform/three-nebula" width="160"> | [creativelifeform/three-nebula](https://github.com/creativelifeform/three-nebula)<br><sub>图片来源：项目 [creativelifeform/three-nebula](https://three-nebula.org/)</sub> | [MIT](https://github.com/creativelifeform/three-nebula) | three.js 的 WebGL 粒子引擎，用 JSON 定义发射器，做火焰、烟雾、魔法特效。 |
| <img src="https://img.youtube.com/vi/WwNX9TO7guA/0.jpg" alt="effekseer/Effekseer" width="160"> | [effekseer/Effekseer](https://github.com/effekseer/Effekseer)<br><sub>图片来源：项目 [effekseer/Effekseer](https://github.com/effekseer/Effekseer)</sub> | [MIT](https://github.com/effekseer/Effekseer) | 粒子特效编辑器和运行时，支持 Unity、Unreal、Godot 和 Web。 |
| <img src="https://kenney.nl/media/pages/assets/particle-pack/d50c7fc9b6-1677578655/preview.png" alt="Kenney Particle Pack" width="160"> | [Kenney Particle Pack](https://kenney.nl/assets/particle-pack)<br><sub>图片来源：项目 [Kenney Particle Pack](https://kenney.nl/assets/particle-pack)</sub> | [CC0-1.0](https://kenney.nl/assets/particle-pack) | 80 张粒子贴图（烟、火、火花、魔法），可直接放进任意粒子系统。 |
| <img src="https://jangafx.com/opengraph-image.png?opengraph-image.2xwmfd9hv7l5u.png" alt="JangaFX Free VDB Animations" width="160"> | [JangaFX Free VDB Animations](https://jangafx.com/software/embergen/download/free-vdb-animations/)<br><sub>图片来源：项目 [JangaFX Free VDB Animations](https://jangafx.com/)</sub><br><sub>参考清单 [madjin/awesome-cc0](https://github.com/madjin/awesome-cc0)</sub> | [CC0-1.0](https://jangafx.com/software/embergen/download/free-vdb-animations/) | 免费体积火焰、烟雾、爆炸模拟（OpenVDB），用于 Blender、Houdini 和离线渲染。 |
| <img src="docs/images/entry-postprocessing.webp" alt="pmndrs/postprocessing (示意图)" width="160"> | [pmndrs/postprocessing](https://github.com/pmndrs/postprocessing)<br><sub>*示意图*</sub> | [Zlib](https://github.com/pmndrs/postprocessing) | three.js 后处理特效库：泛光、景深、SMAA 抗锯齿、色调映射等。 |
| <img src="https://raw.githubusercontent.com/gdquest-demos/godot-shaders/main/img/banner-shader-secrets.png" alt="gdquest-demos/godot-shaders" width="160"> | [gdquest-demos/godot-shaders](https://github.com/gdquest-demos/godot-shaders)<br><sub>图片来源：项目 [gdquest-demos/godot-shaders](https://github.com/gdquest-demos/godot-shaders)</sub> | [MIT（代码）/ CC-BY-NC-SA-4.0（美术）](https://github.com/gdquest-demos/godot-shaders) | 开源 Godot 着色器示例（溶解、描边、水面、卡通渲染等），代码易读。 |
| <img src="https://raw.githubusercontent.com/gdquest-demos/godot-visual-effects/master/img/banner-vfx-secrets.png" alt="gdquest-demos/godot-visual-effects" width="160"> | [gdquest-demos/godot-visual-effects](https://github.com/gdquest-demos/godot-visual-effects)<br><sub>图片来源：项目 [gdquest-demos/godot-visual-effects](https://github.com/gdquest-demos/godot-visual-effects)</sub> | [MIT（代码）/ CC-BY-NC-SA-4.0（美术）](https://github.com/gdquest-demos/godot-visual-effects) | Godot 视觉特效示例：粒子、爆炸、受击、魔法技能，可以照着学。 |
| <img src="https://godotshaders.com/wp-content/uploads/2021/01/godotshaders_logo_blue.png" alt="Godot Shaders" width="160"> | [Godot Shaders](https://godotshaders.com/)<br><sub>图片来源：项目 [Godot Shaders](https://godotshaders.com/)</sub> | [按着色器单独授权（CC0 / MIT / GPL-3.0）；配图不在授权内](https://godotshaders.com/license/) | Godot 着色器社区库；每个帖子标明许可证，只覆盖代码。 |

## 技能 / 施法 / 战斗演示

<img src="docs/images/cover-abilities.webp" alt="分类封面（原创示意图）: 技能 / 施法 / 战斗演示" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/achrefelouafi/LinearAbiltyCastingThreeJS/main/docs/screenshots/nova-beam.jpg" alt="achrefelouafi/LinearAbiltyCastingThreeJS" width="160"> | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS)<br><sub>图片来源：项目 [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS)</sub> | [MIT](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | three.js 技能施法演示：直线施法和远程落点（瞄准箭头、目标圈、光束、冰矛、陨石），带 HUD。 |
| <img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/main/docs/showcase/punchbox-fighter-finisher-flame.gif" alt="jammyfu/open-game-skills" width="160"> | [jammyfu/open-game-skills](https://github.com/jammyfu/open-game-skills)<br><sub>图片来源：项目 [jammyfu/open-game-skills](https://github.com/jammyfu/open-game-skills)</sub> | [MIT](https://github.com/jammyfu/open-game-skills) | 给编程 Agent 用的游戏开发 skill：手感、战斗、镜头、引擎适配，附可运行示例。 |
| <img src="https://github.com/tranek/GASDocumentation/raw/master/Images/gameplaytageditor.png" alt="tranek/GASDocumentation" width="160"> | [tranek/GASDocumentation](https://github.com/tranek/GASDocumentation)<br><sub>图片来源：项目 [tranek/GASDocumentation](https://github.com/tranek/GASDocumentation)</sub> | [MIT](https://github.com/tranek/GASDocumentation) | 非官方的 Unreal Engine 5 Gameplay Ability System 深度指南，附多人示例工程（UE 5.3）。 |
| <img src="https://raw.githubusercontent.com/No78Vino/gameplay-ability-system-for-unity/EX-GAS-1.0/Wiki/QQ20240313114652.png" alt="No78Vino/gameplay-ability-system-for-unity" width="160"> | [No78Vino/gameplay-ability-system-for-unity](https://github.com/No78Vino/gameplay-ability-system-for-unity)<br><sub>图片来源：项目 [No78Vino/gameplay-ability-system-for-unity](https://github.com/No78Vino/gameplay-ability-system-for-unity)</sub> | [MIT](https://github.com/No78Vino/gameplay-ability-system-for-unity) | Unreal Gameplay Ability System 的 Unity 实现（标签、属性、效果、技能），功能部分完成、仍在完善，文档为中文。 |
| <img src="docs/images/entry-gasshooter.webp" alt="tranek/GASShooter (示意图)" width="160"> | [tranek/GASShooter](https://github.com/tranek/GASShooter)<br><sub>*示意图*</sub> | [MIT](https://github.com/tranek/GASShooter) | 进阶 Unreal GAS 示例：多人 FPS/TPS，含武器、技能和预测。 |
| <img src="https://github.com/user-attachments/assets/2518ffc8-ef3b-4bbf-bcce-48d00338237a" alt="Narxim/Narxim-GAS-Example" width="160"> | [Narxim/Narxim-GAS-Example](https://github.com/Narxim/Narxim-GAS-Example)<br><sub>图片来源：项目 [Narxim/Narxim-GAS-Example](https://github.com/Narxim/Narxim-GAS-Example)</sub> | [MIT](https://github.com/Narxim/Narxim-GAS-Example) | 干净的 Unreal Gameplay Ability System 模板工程，已配好属性和技能。 |

## 动画与动捕

<img src="docs/images/cover-animation.webp" alt="分类封面（原创示意图）: 动画与动捕" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://quaternius.com/assets/images/fullres/universalanimationlibrary.jpg" alt="Quaternius Universal Animation Library" width="160"> | [Quaternius Universal Animation Library](https://quaternius.com/packs/universalanimationlibrary.html)<br><sub>图片来源：项目 [Quaternius Universal Animation Library](https://quaternius.com/packs/universalanimationlibrary.html)</sub> | [CC0-1.0](https://quaternius.com/packs/universalanimationlibrary.html) | 120+ 人形动画（移动、战斗、表情动作），通用骨骼，可在 Unity、Unreal、Godot 里重定向。 |
| <img src="https://kenney.nl/media/pages/assets/animated-characters-protagonists/98921ae406-1674931821/preview.png" alt="Kenney Animated Characters" width="160"> | [Kenney Animated Characters](https://kenney.nl/assets/animated-characters-1)<br><sub>图片来源：项目 [Kenney Animated Characters](https://kenney.nl/assets/animated-characters-1)</sub> | [CC0-1.0](https://kenney.nl/assets/animated-characters-1) | 带骨骼和动画的低多边形角色，适合快速做 3D 原型。 |
| <img src="https://www.synfig.org/wp-content/uploads/2018/02/screenshot-07.png" alt="synfig/synfig" width="160"> | [synfig/synfig](https://github.com/synfig/synfig)<br><sub>图片来源：项目 [synfig/synfig](https://www.synfig.org/)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [GPL-3.0](https://github.com/synfig/synfig) | 2D 矢量和骨骼动画软件，做过场和角色动画。 |
| <img src="https://www.piskelapp.com/assets/home/screenshot.png" alt="piskelapp/piskel" width="160"> | [piskelapp/piskel](https://github.com/piskelapp/piskel)<br><sub>图片来源：项目 [piskelapp/piskel](https://www.piskelapp.com/)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [Apache-2.0](https://github.com/piskelapp/piskel) | 网页版精灵编辑器，逐帧做像素动画，可导出 GIF 和精灵表。 |
| <img src="https://raw.githubusercontent.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset/master/src/Bandai-Namco-Research-Motiondataset-1/movie_walk.gif" alt="BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset" width="160"> | [BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset](https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset)<br><sub>图片来源：项目 [BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset](https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset)</sub> | [CC-BY-NC-4.0（数据集）/ MIT（脚本）](https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset#license) | 动捕数据集，含多种风格的走路、格斗和手势动作；仅限非商业使用。 |
| <img src="https://dragonbones.github.io/demo/demos.jpg" alt="DragonBones/DragonBonesJS" width="160"> | [DragonBones/DragonBonesJS](https://github.com/DragonBones/DragonBonesJS)<br><sub>图片来源：项目 [DragonBones/DragonBonesJS](https://github.com/DragonBones/DragonBonesJS)</sub> | [MIT](https://github.com/DragonBones/DragonBonesJS) | DragonBones 2D 骨骼动画的 JavaScript 运行时（支持 Pixi、Phaser、Egret 等）。 |

## 物理

<img src="docs/images/cover-physics.webp" alt="分类封面（原创示意图）: 物理" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="docs/images/entry-box2d.webp" alt="erincatto/box2d (示意图)" width="160"> | [erincatto/box2d](https://github.com/erincatto/box2d)<br><sub>*示意图*</sub> | [MIT](https://github.com/erincatto/box2d) | C 写的 2D 刚体物理引擎，应用很广。 |
| <img src="https://jrouwe.nl/jolt/Horizon_Forbidden_West.png" alt="jrouwe/JoltPhysics" width="160"> | [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics)<br><sub>图片来源：项目 [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics)</sub> | [MIT](https://github.com/jrouwe/JoltPhysics) | 高性能多线程 3D 刚体物理引擎，适合游戏和 VR。 |
| <img src="https://pybullet.org/wordpress/wp-content/uploads/2019/03/cropped-pybullet.png" alt="bulletphysics/bullet3" width="160"> | [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3)<br><sub>图片来源：项目 [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3)</sub> | [Zlib（Extras 和第三方库除外）](https://github.com/bulletphysics/bullet3) | 成熟的 3D 物理 SDK：碰撞检测、刚体和软体。 |
| <img src="https://raw.githubusercontent.com/dimforge/rapier/master/assets/rapier-logo.jpg" alt="dimforge/rapier" width="160"> | [dimforge/rapier](https://github.com/dimforge/rapier)<br><sub>图片来源：项目 [dimforge/rapier](https://github.com/dimforge/rapier)</sub> | [Apache-2.0](https://github.com/dimforge/rapier) | Rust 写的 2D/3D 物理引擎，也能通过 WASM 在 JavaScript 里用。 |
| <img src="https://raw.githubusercontent.com/pmndrs/cannon-es/master/screenshots/docs.png" alt="pmndrs/cannon-es" width="160"> | [pmndrs/cannon-es](https://github.com/pmndrs/cannon-es)<br><sub>图片来源：项目 [pmndrs/cannon-es](https://github.com/pmndrs/cannon-es)</sub> | [MIT](https://github.com/pmndrs/cannon-es) | 轻量网页 3D 物理引擎，常和 three.js 搭配。 |
| <img src="docs/images/entry-matter-js.webp" alt="liabru/matter-js (示意图)" width="160"> | [liabru/matter-js](https://github.com/liabru/matter-js)<br><sub>*示意图*</sub> | [MIT](https://github.com/liabru/matter-js) | 网页 2D 刚体物理引擎，接口简单。 |
| <img src="docs/images/entry-physx.webp" alt="NVIDIA-Omniverse/PhysX (示意图)" width="160"> | [NVIDIA-Omniverse/PhysX](https://github.com/NVIDIA-Omniverse/PhysX)<br><sub>*示意图*</sub> | [BSD-3-Clause](https://github.com/NVIDIA-Omniverse/PhysX) | NVIDIA PhysX SDK，许多商业引擎背后的 3D 物理引擎。 |

## 游戏 AI 与寻路

<img src="docs/images/cover-ai.webp" alt="分类封面（原创示意图）: 游戏 AI 与寻路" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/recastnavigation/recastnavigation/main/Docs/Images/screenshot.png" alt="recastnavigation/recastnavigation" width="160"> | [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation)<br><sub>图片来源：项目 [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation)</sub> | [Zlib](https://github.com/recastnavigation/recastnavigation) | 3D 游戏导航网格生成（Recast）和寻路 / 群体模拟（Detour）。 |
| <img src="docs/images/entry-pathfinding-js.webp" alt="qiao/PathFinding.js (示意图)" width="160"> | [qiao/PathFinding.js](https://github.com/qiao/PathFinding.js)<br><sub>*示意图*</sub> | [MIT（README 中声明）](https://github.com/qiao/PathFinding.js#license) | JavaScript 网格寻路库（A*、Dijkstra、JPS），附在线可视化。 |
| <img src="https://raw.githubusercontent.com/BehaviorTree/BehaviorTree.CPP/master/docs/groot-screenshot.png" alt="BehaviorTree/BehaviorTree.CPP" width="160"> | [BehaviorTree/BehaviorTree.CPP](https://github.com/BehaviorTree/BehaviorTree.CPP)<br><sub>图片来源：项目 [BehaviorTree/BehaviorTree.CPP](https://github.com/BehaviorTree/BehaviorTree.CPP)</sub> | [MIT](https://github.com/BehaviorTree/BehaviorTree.CPP) | C++ 行为树库，XML 定义行为树，配 Groot 可视化编辑器。 |
| <img src="docs/images/entry-yuka.webp" alt="Mugen87/yuka (示意图)" width="160"> | [Mugen87/yuka](https://github.com/Mugen87/yuka)<br><sub>*示意图*</sub> | [MIT](https://github.com/Mugen87/yuka) | JavaScript 游戏 AI 库：转向行为、状态机、目标驱动、导航网格和感知。 |
| <img src="https://raw.githubusercontent.com/limbonaut/limboai/master/doc/images/behavior-tree-editor-debugger.png" alt="limbonaut/limboai" width="160"> | [limbonaut/limboai](https://github.com/limbonaut/limboai)<br><sub>图片来源：项目 [limbonaut/limboai](https://github.com/limbonaut/limboai)</sub> | [MIT](https://github.com/limbonaut/limboai) | Godot 4 的行为树和状态机，带可视化编辑器和调试器。 |
| <img src="https://raw.githubusercontent.com/bitbrain/beehave/godot-4.x/docs/assets/example.png" alt="bitbrain/beehave" width="160"> | [bitbrain/beehave](https://github.com/bitbrain/beehave)<br><sub>图片来源：项目 [bitbrain/beehave](https://github.com/bitbrain/beehave)</sub> | [MIT](https://github.com/bitbrain/beehave) | Godot 行为树插件，带 NPC 逻辑调试视图。 |
| <img src="https://user-images.githubusercontent.com/1848368/34424850-d79e5a24-ebf4-11e7-87c4-afc75cdc41bd.png" alt="donmccurdy/three-pathfinding" width="160"> | [donmccurdy/three-pathfinding](https://github.com/donmccurdy/three-pathfinding)<br><sub>图片来源：项目 [donmccurdy/three-pathfinding](https://github.com/donmccurdy/three-pathfinding)</sub> | [MIT](https://github.com/donmccurdy/three-pathfinding) | three.js 场景的导航网格寻路。 |

## 程序化生成

<img src="docs/images/cover-procgen.webp" alt="分类封面（原创示意图）: 程序化生成" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/mxgmn/WaveFunctionCollapse/master/images/wfc.png" alt="mxgmn/WaveFunctionCollapse" width="160"> | [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)<br><sub>图片来源：项目 [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)</sub> | [MIT](https://github.com/mxgmn/WaveFunctionCollapse) | 原版波函数坍缩算法，从样例生成瓦片地图和纹理。 |
| <img src="docs/images/entry-debroglie.webp" alt="BorisTheBrave/DeBroglie (示意图)" width="160"> | [BorisTheBrave/DeBroglie](https://github.com/BorisTheBrave/DeBroglie)<br><sub>*示意图*</sub> | [MIT](https://github.com/BorisTheBrave/DeBroglie) | C# 约束式程序化生成库（WFC 等），支持多种图块约束。 |
| <img src="https://user-images.githubusercontent.com/1349548/275292148-242e95c7-94e7-4801-bc4a-d683a8822382.png" alt="Auburn/FastNoiseLite" width="160"> | [Auburn/FastNoiseLite](https://github.com/Auburn/FastNoiseLite)<br><sub>图片来源：项目 [Auburn/FastNoiseLite](https://github.com/Auburn/FastNoiseLite)</sub> | [MIT](https://github.com/Auburn/FastNoiseLite) | 多语言可移植噪声库（Perlin、Simplex、Cellular），做地形和纹理。 |
| <img src="https://raw.githubusercontent.com/AlexeyBond/godot-constraint-solving/master/screenshots/2d-tilemap-0.png" alt="AlexeyBond/godot-constraint-solving" width="160"> | [AlexeyBond/godot-constraint-solving](https://github.com/AlexeyBond/godot-constraint-solving)<br><sub>图片来源：项目 [AlexeyBond/godot-constraint-solving](https://github.com/AlexeyBond/godot-constraint-solving)</sub> | [MIT](https://github.com/AlexeyBond/godot-constraint-solving) | Godot 4 的波函数坍缩插件，用于 TileMap 和 GridMap。 |
| <img src="https://raw.githubusercontent.com/a1studmuffin/SpaceshipGenerator/master/screenshots/spaceships_grid.jpg" alt="a1studmuffin/SpaceshipGenerator" width="160"> | [a1studmuffin/SpaceshipGenerator](https://github.com/a1studmuffin/SpaceshipGenerator)<br><sub>图片来源：项目 [a1studmuffin/SpaceshipGenerator](https://github.com/a1studmuffin/SpaceshipGenerator)</sub> | [MIT](https://github.com/a1studmuffin/SpaceshipGenerator) | Blender 脚本，用随机种子生成带贴图的 3D 飞船（较老，最后更新 2024 年）。 |

## 引擎与框架

<img src="docs/images/cover-engines.webp" alt="分类封面（原创示意图）: 引擎与框架" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/godotengine/godot-design/master/screenshots/editor_tps_demo_1920x1080.jpg" alt="godotengine/godot" width="160"> | [godotengine/godot](https://github.com/godotengine/godot)<br><sub>图片来源：项目 [godotengine/godot](https://github.com/godotengine/godot)</sub> | [MIT](https://github.com/godotengine/godot) | 免费开源 2D/3D 游戏引擎，自带编辑器，支持 GDScript/C#。 |
| <img src="docs/images/entry-bevy.webp" alt="bevyengine/bevy (示意图)" width="160"> | [bevyengine/bevy](https://github.com/bevyengine/bevy)<br><sub>*示意图*</sub> | [Apache-2.0 或 MIT](https://github.com/bevyengine/bevy) | Rust 写的数据驱动游戏引擎，基于 ECS。 |
| <img src="https://defold.com/images/logo/others/moonactive-github.png" alt="defold/defold" width="160"> | [defold/defold](https://github.com/defold/defold)<br><sub>图片来源：项目 [defold/defold](https://github.com/defold/defold)</sub> | [Defold 许可 1.0（基于 Apache-2.0）](https://github.com/defold/defold) | 轻量 2D/3D 引擎，Lua 脚本，一键多平台打包。 |
| <img src="https://raw.githubusercontent.com/raysan5/raylib/master/logo/raylib_logo_animation.gif" alt="raysan5/raylib" width="160"> | [raysan5/raylib](https://github.com/raysan5/raylib)<br><sub>图片来源：项目 [raysan5/raylib](https://github.com/raysan5/raylib)</sub> | [Zlib](https://github.com/raysan5/raylib) | 简单的 C 游戏库，适合入门，有 60 多种语言绑定。 |
| <img src="docs/images/entry-love2d.webp" alt="love2d/love (示意图)" width="160"> | [love2d/love](https://github.com/love2d/love)<br><sub>*示意图*</sub> | [Zlib](https://github.com/love2d/love) | LÖVE，Lua 写游戏的 2D 框架。 |
| <img src="https://raw.githubusercontent.com/phaserjs/phaser/master/changelog/v4/assets/phaser4-logo.png" alt="phaserjs/phaser" width="160"> | [phaserjs/phaser](https://github.com/phaserjs/phaser)<br><sub>图片来源：项目 [phaserjs/phaser](https://github.com/phaserjs/phaser)</sub> | [MIT](https://github.com/phaserjs/phaser) | HTML5 2D 游戏框架，桌面和手机浏览器都能跑。 |
| <img src="https://threejs.org/files/share.png" alt="mrdoob/three.js" width="160"> | [mrdoob/three.js](https://github.com/mrdoob/three.js)<br><sub>图片来源：项目 [mrdoob/three.js](https://threejs.org/)</sub> | [MIT](https://github.com/mrdoob/three.js) | JavaScript 3D 库（WebGL/WebGPU），多数网页 3D 游戏和演示都基于它。 |
| <img src="https://dev.azure.com/babylonjs/ContinousIntegration/_apis/build/status/CI?branchName=master" alt="BabylonJS/Babylon.js" width="160"> | [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js)<br><sub>图片来源：项目 [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js)</sub> | [Apache-2.0](https://github.com/BabylonJS/Babylon.js) | 功能完整的网页 3D 游戏 / 渲染引擎，带在线 Playground 和编辑器。 |
| <img src="https://o3de.org/wp-content/uploads/2023/06/black-bg-logo.jpg" alt="o3de/o3de" width="160"> | [o3de/o3de](https://github.com/o3de/o3de)<br><sub>图片来源：项目 [o3de/o3de](https://o3de.org)</sub> | [Apache-2.0 或 MIT](https://github.com/o3de/o3de) | Open 3D Engine，Linux 基金会旗下的模块化 3A 级 3D 引擎。 |
| <img src="https://stride3d.net/images/external/script-editor.png" alt="stride3d/stride" width="160"> | [stride3d/stride](https://github.com/stride3d/stride)<br><sub>图片来源：项目 [stride3d/stride](https://github.com/stride3d/stride)</sub> | [MIT](https://github.com/stride3d/stride) | C# 3D 游戏引擎，带编辑器，前身是 Xenko。 |
| <img src="https://raw.githubusercontent.com/MonoGame/MonoGame.Samples/refs/heads/3.8.2/Images/Platformer2D-Sample.png" alt="MonoGame/MonoGame" width="160"> | [MonoGame/MonoGame](https://github.com/MonoGame/MonoGame)<br><sub>图片来源：项目 [MonoGame/MonoGame](https://github.com/MonoGame/MonoGame)</sub> | [Ms-PL](https://github.com/MonoGame/MonoGame) | C# 跨平台 2D/3D 游戏框架（XNA 继任者）。 |
| <img src="https://raw.githubusercontent.com/libgdx/libgdx/master/libgdx_logo.svg#gh-light-mode-only" alt="libgdx/libgdx" width="160"> | [libgdx/libgdx](https://github.com/libgdx/libgdx)<br><sub>图片来源：项目 [libgdx/libgdx](https://github.com/libgdx/libgdx)</sub> | [Apache-2.0](https://github.com/libgdx/libgdx) | Java 游戏框架，支持桌面、安卓、iOS 和网页。 |
| <img src="https://raw.githubusercontent.com/excaliburjs/Excalibur/main/assets/logo.png" alt="excaliburjs/Excalibur" width="160"> | [excaliburjs/Excalibur](https://github.com/excaliburjs/Excalibur)<br><sub>图片来源：项目 [excaliburjs/Excalibur](https://github.com/excaliburjs/Excalibur)</sub> | [BSD-2-Clause](https://github.com/excaliburjs/Excalibur) | TypeScript 写的网页 2D 游戏引擎。 |
| <img src="https://pixijs.io/create-pixi/img/demo.gif" alt="pixijs/pixijs" width="160"> | [pixijs/pixijs](https://github.com/pixijs/pixijs)<br><sub>图片来源：项目 [pixijs/pixijs](https://github.com/pixijs/pixijs)</sub> | [MIT](https://github.com/pixijs/pixijs) | 高速 2D WebGL/WebGPU 渲染器，做网页游戏和交互图形。 |
| <img src="https://s3-eu-west-1.amazonaws.com/images.playcanvas.com/projects/14705/319531/O4J4VU-image-25.jpg" alt="playcanvas/engine" width="160"> | [playcanvas/engine](https://github.com/playcanvas/engine)<br><sub>图片来源：项目 [playcanvas/engine](https://github.com/playcanvas/engine)</sub> | [MIT](https://github.com/playcanvas/engine) | 网页 WebGL/WebGPU 3D 游戏引擎（运行时）。 |
| <img src="https://raw.githubusercontent.com/kaplayjs/kaplay/master/kaplay.webp" alt="kaplayjs/kaplay" width="160"> | [kaplayjs/kaplay](https://github.com/kaplayjs/kaplay)<br><sub>图片来源：项目 [kaplayjs/kaplay](https://github.com/kaplayjs/kaplay)</sub> | [MIT](https://github.com/kaplayjs/kaplay) | 新手友好的 JavaScript 游戏库（Kaboom.js 的继任者）。 |
| <img src="https://ebitengine.org/images/overview2.png" alt="hajimehoshi/ebiten" width="160"> | [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten)<br><sub>图片来源：项目 [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten)</sub> | [Apache-2.0](https://github.com/hajimehoshi/ebiten) | Ebitengine，Go 语言的简单 2D 游戏引擎。 |
| <img src="https://raw.githubusercontent.com/FyroxEngine/Fyrox/master/pics/logo.png" alt="FyroxEngine/Fyrox" width="160"> | [FyroxEngine/Fyrox](https://github.com/FyroxEngine/Fyrox)<br><sub>图片来源：项目 [FyroxEngine/Fyrox](https://github.com/FyroxEngine/Fyrox)</sub> | [MIT](https://github.com/FyroxEngine/Fyrox) | Rust 写的 3D/2D 游戏引擎，带场景编辑器。 |
| <img src="https://raw.githubusercontent.com/HeapsIO/heaps.io/master/assets/logo/logo-heaps-color.png" alt="HeapsIO/heaps" width="160"> | [HeapsIO/heaps](https://github.com/HeapsIO/heaps)<br><sub>图片来源：项目 [HeapsIO/heaps](https://github.com/HeapsIO/heaps)</sub> | [MIT](https://github.com/HeapsIO/heaps) | Haxe 语言的跨平台 2D/3D 游戏引擎。 |

## 工具与管线

<img src="docs/images/cover-tools.webp" alt="分类封面（原创示意图）: 工具与管线" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://code.blender.org/wp-content/uploads/2018/12/springrg.jpg" alt="Blender" width="160"> | [Blender](https://www.blender.org/)<br><sub>图片来源：项目 [Blender](https://github.com/blender/blender)</sub><br><sub>⚠ 官网对自动检查返回 403，许可证已人工核实</sub> | [GPL-3.0-or-later（发行版）](https://www.blender.org/about/license/) | 免费 3D 全家桶：建模、绑骨、动画、烘焙；做出来的作品归你。 |
| <img src="https://raw.githubusercontent.com/RodZill4/material-maker/master/material_maker/doc/images/screenshot.png" alt="RodZill4/material-maker" width="160"> | [RodZill4/material-maker](https://github.com/RodZill4/material-maker)<br><sub>图片来源：项目 [RodZill4/material-maker](https://github.com/RodZill4/material-maker)</sub> | [MIT](https://github.com/RodZill4/material-maker) | 基于 Godot 的节点式程序化贴图 / 材质制作工具。 |
| <img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2779170/ss_54395040c25b243cb82a3bd68778e19e04b43ade.1920x1080.jpg?t=1719424898" alt="Orama-Interactive/Pixelorama" width="160"> | [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama)<br><sub>图片来源：项目 [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama)</sub> | [MIT](https://github.com/Orama-Interactive/Pixelorama) | 像素画编辑器，画精灵、图块和逐帧动画；桌面和网页都能用。 |
| <img src="docs/images/entry-tiled.webp" alt="mapeditor/tiled (示意图)" width="160"> | [mapeditor/tiled](https://github.com/mapeditor/tiled)<br><sub>*示意图*</sub> | [GPL-2.0（编辑器）/ BSD-2-Clause（libtiled）](https://github.com/mapeditor/tiled/blob/master/COPYING) | 灵活的瓦片地图 / 关卡编辑器，导出的 TMX/JSON 被大多数 2D 引擎支持。 |
| <img src="https://ldtk.io/wp-content/uploads/2021/05/open-graph.png" alt="deepnight/ldtk" width="160"> | [deepnight/ldtk](https://github.com/deepnight/ldtk)<br><sub>图片来源：项目 [deepnight/ldtk](https://ldtk.io/)</sub> | [MIT](https://github.com/deepnight/ldtk) | 现代轻量 2D 关卡编辑器，支持自动图层铺块和带类型的实体字段。 |
| <img src="https://www.audacityteam.org/og-image.png" alt="audacity/audacity" width="160"> | [audacity/audacity](https://github.com/audacity/audacity)<br><sub>图片来源：项目 [audacity/audacity](https://www.audacityteam.org/)</sub> | [GPL-3.0](https://github.com/audacity/audacity/blob/master/LICENSE.txt) | 音频编辑器，剪切、叠加、降噪游戏音效。 |
| <img src="docs/images/entry-lmms.webp" alt="LMMS/lmms (示意图)" width="160"> | [LMMS/lmms](https://github.com/LMMS/lmms)<br><sub>*示意图*</sub> | [GPL-2.0](https://github.com/LMMS/lmms) | 免费编曲软件（音序器、合成器、采样器），做游戏配乐和短提示音。 |
| <img src="docs/images/entry-godot-demos.webp" alt="godotengine/godot-demo-projects (示意图)" width="160"> | [godotengine/godot-demo-projects](https://github.com/godotengine/godot-demo-projects)<br><sub>*示意图*</sub> | [MIT](https://github.com/godotengine/godot-demo-projects) | Godot 官方示例和模板项目（2D、3D、物理、UI），可以照着学或直接起步。 |
| <img src="https://krita.org/images/hero-image-50.webp" alt="KDE/krita" width="160"> | [KDE/krita](https://github.com/KDE/krita)<br><sub>图片来源：项目 [KDE/krita](https://krita.org/en/)</sub><br><sub>参考清单 [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)</sub> | [GPL-3.0](https://github.com/KDE/krita) | 数字绘画软件，画概念图、贴图和手绘动画。 |
| <img src="https://i.imgur.com/UOLKpPA.png" alt="LibreSprite/LibreSprite" width="160"> | [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite)<br><sub>图片来源：项目 [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite)</sub> | [GPL-2.0](https://github.com/LibreSprite/LibreSprite) | 免费像素画和精灵动画编辑器（从最后一个 GPL 版 Aseprite 分叉）。 |
| <img src="https://raw.githubusercontent.com/odrick/free-tex-packer/master/electron/build/icons/96x96.png" alt="odrick/free-tex-packer" width="160"> | [odrick/free-tex-packer](https://github.com/odrick/free-tex-packer)<br><sub>图片来源：项目 [odrick/free-tex-packer](https://github.com/odrick/free-tex-packer)</sub> | [MIT](https://github.com/odrick/free-tex-packer) | 免费图集打包工具，可导出 Phaser、Pixi、Unity、Godot 等格式。 |
| <img src="https://raw.githubusercontent.com/Ogmo-Editor-3/OgmoEditor3-CE/master/assets/gfx/logo.png" alt="Ogmo-Editor-3/OgmoEditor3-CE" width="160"> | [Ogmo-Editor-3/OgmoEditor3-CE](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE)<br><sub>图片来源：项目 [Ogmo-Editor-3/OgmoEditor3-CE](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE)</sub> | [MIT](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE) | 免费、不绑引擎的 2D 关卡编辑器，支持图块、实体和贴花（最后更新 2024 年）。 |
| <img src="https://raw.githubusercontent.com/TrenchBroom/TrenchBroom/master/app/TrenchBroom/resources/graphics/images/AppIcon.png" alt="TrenchBroom/TrenchBroom" width="160"> | [TrenchBroom/TrenchBroom](https://github.com/TrenchBroom/TrenchBroom)<br><sub>图片来源：项目 [TrenchBroom/TrenchBroom](https://github.com/TrenchBroom/TrenchBroom)</sub> | [GPL-3.0](https://github.com/TrenchBroom/TrenchBroom) | Quake 风格的笔刷式 3D 关卡编辑器，可借插件用于 Godot。 |
| <img src="https://web.blockbench.net/content/front_page_app.png" alt="JannisX11/blockbench" width="160"> | [JannisX11/blockbench](https://github.com/JannisX11/blockbench)<br><sub>图片来源：项目 [JannisX11/blockbench](https://github.com/JannisX11/blockbench)</sub> | [GPL-3.0](https://github.com/JannisX11/blockbench) | 低多边形 / 方块风 3D 模型编辑器，可画贴图、做动画。 |
| <img src="https://goxel.xyz/gallery/thibault-fisherman-house.jpg" alt="guillaumechereau/goxel" width="160"> | [guillaumechereau/goxel](https://github.com/guillaumechereau/goxel)<br><sub>图片来源：项目 [guillaumechereau/goxel](https://github.com/guillaumechereau/goxel)</sub> | [GPL-3.0](https://github.com/guillaumechereau/goxel) | 开源体素编辑器，做 3D 模型和场景。 |
| <img src="https://gltf-transform.dev/media/kicker.jpg" alt="donmccurdy/glTF-Transform" width="160"> | [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform)<br><sub>图片来源：项目 [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform)</sub> | [MIT](https://github.com/donmccurdy/glTF-Transform) | 优化 glTF/GLB 的命令行和 SDK：压缩、缩贴图、去重。 |
| <img src="docs/images/entry-meshoptimizer.webp" alt="zeux/meshoptimizer (示意图)" width="160"> | [zeux/meshoptimizer](https://github.com/zeux/meshoptimizer)<br><sub>*示意图*</sub> | [MIT](https://github.com/zeux/meshoptimizer) | 网格优化库和 gltfpack 工具，让 3D 资产更小更快。 |
| <img src="https://www.assimp.org/dragonsplash.png" alt="assimp/assimp" width="160"> | [assimp/assimp](https://github.com/assimp/assimp)<br><sub>图片来源：项目 [assimp/assimp](https://www.assimp.org)</sub> | [BSD-3-Clause（修改版）](https://github.com/assimp/assimp) | 开放资产导入库：把 40 多种 3D 格式读成统一数据结构。 |

## AI 素材生成与 Agent Skill

<img src="docs/images/cover-aigen.webp" alt="分类封面（原创示意图）: AI 素材生成与 Agent Skill" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://raw.githubusercontent.com/microsoft/TRELLIS/main/assets/logo.webp" alt="microsoft/TRELLIS" width="160"> | [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS)<br><sub>图片来源：项目 [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS)</sub> | [MIT](https://github.com/microsoft/TRELLIS) | 微软的图像 / 文本生成 3D 模型（网格、辐射场、高斯）。 |
| <img src="https://raw.githubusercontent.com/VAST-AI-Research/TripoSR/main/figures/teaser800.gif" alt="VAST-AI-Research/TripoSR" width="160"> | [VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)<br><sub>图片来源：项目 [VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)</sub> | [MIT](https://github.com/VAST-AI-Research/TripoSR) | 单张图快速重建 3D 网格的模型。 |
| <img src="docs/images/entry-instantmesh.webp" alt="TencentARC/InstantMesh (示意图)" width="160"> | [TencentARC/InstantMesh](https://github.com/TencentARC/InstantMesh)<br><sub>*示意图*</sub> | [Apache-2.0](https://github.com/TencentARC/InstantMesh) | 单张图生成 3D 网格，基于多视角扩散。 |
| <img src="https://github.com/user-attachments/assets/36e065e0-bfae-4456-8c7f-8369d5ea48a2" alt="Comfy-Org/ComfyUI" width="160"> | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)<br><sub>图片来源：项目 [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)</sub> | [GPL-3.0](https://github.com/Comfy-Org/ComfyUI) | 扩散模型的节点式界面，生成贴图、精灵和概念图。 |
| <img src="docs/images/entry-audiocraft.webp" alt="facebookresearch/audiocraft (示意图)" width="160"> | [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)<br><sub>*示意图*</sub> | [MIT（代码）；模型权重 CC-BY-NC-4.0](https://github.com/facebookresearch/audiocraft) | Meta 的音频生成库（MusicGen、AudioGen），生成音乐和音效；权重仅限非商业。 |
| <img src="https://github.com/user-attachments/assets/efb402a1-0b09-41e0-a6cb-259d442e76aa" alt="Tencent-Hunyuan/Hunyuan3D-2" width="160"> | [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)<br><sub>图片来源：项目 [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)</sub> | [腾讯混元 3D 2.0 社区许可（不适用于欧盟、英国、韩国）](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 文本 / 图像生成带贴图的 3D 网格；使用前看清许可里的地区和用途限制。 |
| <img src="https://skills.sh/b/gamedev-skills/awesome-gamedev-agent-skills" alt="gamedev-skills/awesome-gamedev-agent-skills" width="160"> | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)<br><sub>图片来源：项目 [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)</sub> | [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 给 AI 编程 Agent 用的游戏开发 skill 合集和路由。 |

## 其他清单与设计参考

<img src="docs/images/cover-lists.webp" alt="分类封面（原创示意图）: 其他清单与设计参考" width="640">

| 预览 | 项目 | 许可证 | 适合做什么 |
| --- | --- | --- | --- |
| <img src="https://cdn.rawgit.com/ellisonleao/magictools/7d8012bc/magicbg.jpg" alt="ellisonleao/magictools" width="160"> | [ellisonleao/magictools](https://github.com/ellisonleao/magictools)<br><sub>图片来源：项目 [ellisonleao/magictools](https://github.com/ellisonleao/magictools)</sub> | [MIT](https://github.com/ellisonleao/magictools) | 老牌游戏开发资源清单：引擎、美术、音频、工具。 |
| <img src="docs/images/entry-awesome-gamedev.webp" alt="Calinou/awesome-gamedev (示意图)" width="160"> | [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)<br><sub>*示意图*</sub> | [CC-BY-SA-4.0](https://github.com/Calinou/awesome-gamedev) | 制作游戏用的自由软件和自由文化资源清单。 |
| <img src="docs/images/entry-awesome-cc0.webp" alt="madjin/awesome-cc0 (示意图)" width="160"> | [madjin/awesome-cc0](https://github.com/madjin/awesome-cc0)<br><sub>*示意图*</sub> | [CC0-1.0](https://github.com/madjin/awesome-cc0) | 全网 CC0 素材清单：模型、贴图、声音。 |
| <img src="https://raw.githubusercontent.com/FronkonGames/Awesome-Gamedev/main/images/banner.png" alt="FronkonGames/Awesome-Gamedev" width="160"> | [FronkonGames/Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev)<br><sub>图片来源：项目 [FronkonGames/Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev)</sub> | [MIT](https://github.com/FronkonGames/Awesome-Gamedev) | 精选游戏开发资源：工具、教程、库。 |
| <img src="https://raw.githubusercontent.com/dawdle-deer/awesome-learn-gamedev/main/images/KittyIcon.png" alt="dawdle-deer/awesome-learn-gamedev" width="160"> | [dawdle-deer/awesome-learn-gamedev](https://github.com/dawdle-deer/awesome-learn-gamedev)<br><sub>图片来源：项目 [dawdle-deer/awesome-learn-gamedev](https://github.com/dawdle-deer/awesome-learn-gamedev)</sub> | [CC0-1.0](https://github.com/dawdle-deer/awesome-learn-gamedev) | 游戏开发学习资源精选。 |
| <img src="docs/images/entry-awesome-godot.webp" alt="Calinou/awesome-godot (示意图)" width="160"> | [Calinou/awesome-godot](https://github.com/Calinou/awesome-godot)<br><sub>*示意图*</sub> | [CC-BY-4.0](https://github.com/Calinou/awesome-godot) | Godot 插件、脚本、模板和项目精选清单。 |
| <img src="docs/images/entry-gpp.webp" alt="munificent/game-programming-patterns (示意图)" width="160"> | [munificent/game-programming-patterns](https://github.com/munificent/game-programming-patterns)<br><sub>*示意图*</sub> | [MIT（代码）/ CC-BY-NC-ND-4.0（书的正文）](https://github.com/munificent/game-programming-patterns) | 免费在线书《游戏编程模式》的源码（游戏代码设计模式）。 |

## 致谢 / 参考清单

部分条目是从下面这些清单里发现的。我们只借了线索：每个来源都重新核实了许可证和可达性，描述全部为本清单重写，没有整份照搬。通过它们找到的条目会写「参考清单」并链接原清单。

| 清单 | 许可证 |
| --- | --- |
| [Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev) | CC-BY-SA-4.0 |
| [madjin/awesome-cc0](https://github.com/madjin/awesome-cc0) | CC0-1.0 |

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。改 `data/entries.json`，再跑 `python3 tools/render_readme.py` 和 `python3 tools/verify.py`。

## 许可证

清单文字采用 [CC0 1.0](LICENSE)。链接的素材和工具各自沿用原许可证。预览图归原项目所有，只引用不复制。
