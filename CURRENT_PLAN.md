# CURRENT_PLAN.md

## Plan ID

PLAN-008

## Goal

从已合并的 320 条清单同步 README：目录分类计数、特色入口、许可/排序日期与贡献入口与 `data/entries.json` 实数相符。

## Current Focus

README catalog count sync

## In Scope

- 五语 README / catalog 目录与特色入口显示由数据计算的分类条数
- 许可核验与星标快照说明覆盖 2026-11-12 清单快照及后续新增日期
- 同步 CONTRIBUTING / discovery / llms.txt 等文档入口
- 重新生成 README/catalog 并跑仓内校验

## Out of Scope

- 不合并 PR、不部署、不新建仓库
- 不新增素材、不改 15 类骨架与表格视觉、不重排已有热度快照
- 不改 About/Topics，不复用或追加已合 PR #8

## Tasks

- [x] Inspect latest main READMEs against live `entries.json` counts and dates
- [x] Add live category counts to Contents and featured routes; keep heading anchors stable
- [x] Update license/sort copy from recorded dates; sync related doc entry points
- [x] Run `python3 tools/verify.py` and `python3 tools/check_links.py`
- [ ] Open independent PR for owner review; no merge

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- Further original previews for source-only entries
- Animation and ability/combat demo sources with clear licenses
