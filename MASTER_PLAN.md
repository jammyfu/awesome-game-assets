# MASTER_PLAN.md

## 总目标

做一份可信、可持续维护的开源游戏素材清单：每条都有已核实的许可证，中英文一致，CI 自动把关。

## 当前阶段

Phase 1: Foundations（首批清单 + 校验）

## 阶段路线

### Phase 1: Foundations
- 标准文件集、数据源 `data/entries.json`、生成式中英 README
- 首批 25 条，覆盖 7 个分类；配图出处 / 提示词齐全
- 离线校验 `tools/verify.py` + 联网校验 `tools/check_links.py` + CI

### Phase 2: Coverage
- 每个分类扩到 5–10 条（优先动画、技能演示）
- 每条补「格式 / 引擎」标签

### Phase 3: Upkeep
- 定期复查链接和许可证（手动触发 workflow）
- 社区 PR 模板与审核流程

## 当前阶段的完成定义

- PR 通过 CI，用户确认后合入 main
- `python3 tools/verify.py` 与 `python3 tools/check_links.py` 全绿

## 下一次评审应回答的问题

- 动画、技能演示分类优先补哪些来源
- 是否需要按引擎（Unity / Godot / three.js）再分一层
