# CURRENT_PLAN.md

## Plan ID

PLAN-001

## Goal

首批清单上线为 PR：7 个分类、25 条、中英 README、CI 绿。

## Current Focus

Initial list

## In Scope

- `data/entries.json` 首批条目（许可证逐条核实）
- 中英 README、`docs/image-prompts.md` 由脚本生成
- 分类封面与无原图条目的原创配图
- 离线 / 联网校验与 GitHub Actions

## Out of Scope

- 托管第三方素材或图片
- 网站、统计、遥测

## Tasks

- [x] 按 multi-project-program-management 搭标准骨架
- [x] 收录首批 25 条并核实许可证
- [x] 生成中英 README 与配图提示词文档
- [x] 校验脚本与 CI
- [ ] 用户审阅 PR 后合入 main

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- 扩充动画、技能 / 施法演示分类
- 给条目加引擎 / 格式标签
