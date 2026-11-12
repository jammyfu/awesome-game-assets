# CURRENT_PLAN.md

## Plan ID

PLAN-004

## Goal

恢复原项目预览、人话许可与按分类折叠表格。

## Current Focus

Original previews, practical use conditions and compact browsing

## In Scope

- 297条、15类、双语表格与现有头图
- 原图来源、热度快照、每类15条默认展示

## Out of Scope

- 不生成替代素材效果，不自动合并

## Tasks

- [x] Restore credited original images and audit replacements
- [x] Add plain-language license summaries and total-star snapshot
- [x] Preserve full tables behind per-category disclosures
- [ ] Verify GitHub expansion, images, narrow-screen scrolling and final CI

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- Further original previews for source-only entries
