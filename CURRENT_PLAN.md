# CURRENT_PLAN.md

## Plan ID

PLAN-007

## Goal

实质补充至少 20 条许可证明确、可核验的游戏素材，覆盖仓库缺口（贴图、2D/3D、UI、音效音乐、字体、特效、动画），不改分类骨架。

## Current Focus

Verified asset expansion

## In Scope

- 在 `data/entries.json` 新增已核验条目（2026-11-21）
- 五语描述、原项目预览热链、许可证证据与使用限制
- 重新生成 README/catalog 并跑仓内校验

## Out of Scope

- 不合并 PR、不部署、不新建仓库
- 不生成替代预览图，不收录许可证不明或收费再分发资源
- 不改 About/Topics，不重排已有条目热度快照

## Tasks

- [x] Inspect categories, contribution rules, open PRs and existing IDs
- [x] Verify candidate URLs, licenses and original previews
- [x] Add entries plus five-language descriptions
- [x] Run `python3 tools/verify.py` and `python3 tools/check_links.py`; fix issues from this round
- [ ] Open PR for owner review; no merge

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- Further original previews for source-only entries
- Animation and ability/combat demo sources with clear licenses
