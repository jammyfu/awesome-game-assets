# CURRENT_PLAN.md

## Plan ID

PLAN-003

## Goal

恢复用户要求的完整素材对照表格，并加入原创游戏梗头图。

## Current Focus

Restore comparison tables and original hero

## In Scope

- 中英 README 与目录中的 297 条真实表格
- 原创头图、来源记录与实际 GitHub 展示验证

## Out of Scope

- 不并行扩张多个大方向

## Tasks

- [x] Restore all resources as category tables with full metadata
- [ ] Generate and verify an original game-themed hero
- [ ] Verify GitHub rendering and CI, then open a PR for owner review

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- 根据 backlog 与验证结果继续细化
