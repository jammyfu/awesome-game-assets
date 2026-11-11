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
