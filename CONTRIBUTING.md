# Contributing / 参与贡献

**English** · [简体中文](#简体中文)

1. Add or edit an entry in `data/entries.json` (never edit `README.md` / `README.zh-CN.md` by hand).
2. Each entry needs: `url`, `license` + `license_zh`, `license_source` (the page where you checked the license), and what it is good for in English (`en`) and Chinese (`zh`).
3. Only add sources with a clearly stated license. For GitHub repos the API `license` field must match. No pirated, cracked or star-farmed repos. Do not guess or make up data.
4. Image: use the project's own preview image, linked from its original address (`"type": "original"`, with `src` and `source`). Do not copy third-party images into the repo. Original generated images go in `docs/images/` (< 300 KB) with their prompt in `data/image-prompts.json`.
5. Only English and Chinese. No analytics, trackers or visitor counters.
6. Run:

```bash
python3 tools/render_readme.py
python3 tools/verify.py
python3 tools/check_links.py
```

Open a pull request; CI runs the same checks.

## 简体中文

1. 在 `data/entries.json` 里新增或修改条目（不要手改 `README.md` / `README.zh-CN.md`）。
2. 每条必须有：`url`、`license` 和 `license_zh`、`license_source`（你核实许可证的页面），以及英文（`en`）和中文（`zh`）的用途说明。
3. 只收许可证写清楚的来源；GitHub 仓库的 API `license` 字段必须一致。不收盗版、破解或刷星的仓库。不要猜，不要编数据。
4. 配图：优先用项目自己的预览图，直接引用原地址（`"type": "original"`，写 `src` 和 `source`）。不要把第三方图片复制进仓库。原创生成图放 `docs/images/`（< 300 KB），提示词写进 `data/image-prompts.json`。
5. 只用中文和英文。不加统计、追踪或访客计数。
6. 运行上面三条命令，全绿后开 PR；CI 会跑同样的检查。

## Homepage and catalog

Both READMEs and `docs/catalog*.md` are generated. Featured IDs live in `data/entries.json` under `discovery`; keep ordering evidence current. Third-party previews require an explicit `image.reuse_license` and `image.license_source`, not merely a repository code license. Without media rights, use a source-page link.

中英首页与完整目录均自动生成。精选 ID 与排序依据放在 `data/entries.json` 的 `discovery` 中。第三方媒体须记录 `image.reuse_license` 和 `image.license_source`；没有明确媒体授权时只链接来源，代码许可不能替代图片授权。

## Five-language catalogs

The English/Simplified Chinese entry descriptions remain in `data/entries.json`.
Traditional Chinese (Taiwan), Japanese and Korean translations are in
`data/locales/zh-TW.json`, `ja.json` and `ko.json`; shared interface copy also
lives in `data/locales/`. Keep every entry ID, category and practical license
summary covered. Do not translate project names, URLs or canonical license IDs.
Traditional Chinese uses natural Taiwan terminology rather than mechanical
character conversion.

After an English source change, review all three translations before updating
each locale's `source_sha256` to `tools.check_locales.source_digest()`. Never
refresh hashes to bypass incomplete translations. Run `python3 tools/render_readme.py`
and `python3 tools/verify.py`; generated READMEs and catalogs must not be edited
by hand. Contributor, warning and research documents currently remain in their
existing English/Simplified Chinese editions; the five-language scope is the
complete asset directory and its browsing interface.
