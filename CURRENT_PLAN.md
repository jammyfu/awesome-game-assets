# CURRENT_PLAN.md

## Plan ID

PLAN-006

## Goal

优化 GitHub About、Topics 与五语 SEO/GEO 阅读入口，保持完整素材表格和使用边界。

## Current Focus

About/Topics and evidence-backed discoverability

## In Scope

- 297条、15类、五语表格与现有头图
- 原图来源、热度快照、每类15条默认展示

## Out of Scope

- 不生成替代素材效果，不自动合并

## Tasks

- [x] Inspect screenshot and actual repository metadata
- [x] Apply accurate About description and relevant Topics; read back
- [x] Add five-language reader routes, practical FAQ and generated llms.txt
- [ ] Verify source parity, navigation, actual GitHub rendering and exact-head CI
- [ ] Open PR; no merge without owner approval

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- Further original previews for source-only entries
