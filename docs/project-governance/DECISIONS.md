# DECISIONS.md

## 2026-11-12

### 公开仓 + CC0 清单许可

- 用户明确要求公开开源仓；清单文字用 CC0-1.0（awesome 清单惯例），链接的素材各自沿用原许可证。

### README 即内容

- skill 默认 README 轻量；本仓是 awesome 清单，README 就是产品本体。为避免手改漂移，README 由 `data/entries.json` 生成，规则细节仍下沉到 `docs/` 与 `AGENTS.md`。

### 配图只引用不复制

- 收录项目优先用其原图，直接引用原地址并注明出处，不存进仓库。
- 分类封面与找不到原图的条目，用原创生成图（不画真人脸、不仿商标或他人 IP），提示词存 `docs/image-prompts.md`。

### 按素材授权的来源

- OpenGameArt、Freesound、glTF-Sample-Assets 每个素材 / 模型单独标注许可证，属于「许可证清楚」，收录并标明需逐个确认。

### 参考他人清单的方式

- Calinou/awesome-gamedev 是 CC-BY-SA-4.0：只把它当线索（链接和事实），不复制其文字，描述全部重写，并在 Credits 署名，避免把本清单变成其衍生作品。
- madjin/awesome-cc0 是 CC0：同样只借线索、重写描述并署名。

### 警示清单（WARNING.md）

- 搜到的盗版、破解、付费素材二次分发、刷星、疑似恶意软件仓库不进主清单，单独收进 `WARNING.md` / `WARNING.zh-CN.md`，由 `data/warnings.json` 生成，用户已知悉风险。
- 每条：⚠️ + 仓名 + 只到仓库/站点首页的可点链接 + 问题类型 + 风险说明；文件开头 `> [!CAUTION]` 警告框。不写下载或安装步骤，不链 release/安装包。
- 配图只引用其原图地址（只取 GitHub 托管的图，不取可疑外站），绝不存进仓库；没原图就不配，不用 Codex 生成。
- 关键词黑名单检查对这两个文件例外；链接检查仍测可达性，死链条目剔除。

### agy 搜索结果只当线索

- agy 给的名称、许可证、found_via 都要重新核实；found_via 在原清单里找不到就不写「参考清单」，也不进 Credits。
