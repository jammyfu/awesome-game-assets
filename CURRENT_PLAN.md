# CURRENT_PLAN.md

## Plan ID

PLAN-005

## Goal

完整支持英、简中、台湾繁中、日文、韩文五语素材目录。

## Current Focus

Complete localized catalogs with source-drift validation

## In Scope

- 297条、15类、五语表格与现有头图
- 原图来源、热度快照、每类15条默认展示

## Out of Scope

- 不生成替代素材效果，不自动合并

## Tasks

- [x] Translate all 297 descriptions, categories, practical license notes and interface strings
- [x] Add five-language generator and source-drift validation
- [ ] Verify complete navigation, images, expansion and narrow-screen rendering
- [ ] Open PR and verify CI; do not merge without approval

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- Further original previews for source-only entries
