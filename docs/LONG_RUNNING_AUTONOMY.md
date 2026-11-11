# LONG_RUNNING_AUTONOMY.md

本文档面向定时任务、heartbeat automation、长任务自主开发代理。

## 唯一计划入口

- `CURRENT_PLAN.md`

## 每次唤醒后的固定顺序

1. 读取 `AGENTS.md`、`PROJECT_BRIEF.md`、`MASTER_PLAN.md`、`CURRENT_PLAN.md`
2. 若需求有更新，先同步长期规划
3. 完成当前轮一个最小稳定闭环（改 `data/entries.json` → `python3 tools/render_readme.py`）
4. 运行 `python3 tools/verify.py` 和 `python3 tools/check_links.py`
5. 更新 `docs/project-governance/WORKLOG.md`、`DECISIONS.md`、`CHANGELOG.md`
6. 若当前轮完成，运行 `python3 tools/next_plan.py`

## 长任务自主开发规则

- 不创建并行计划入口
- 不跳过验证直接宣称完成
- 不手改生成文件；不编造许可证或数据
- 本仓是用户明确要求的公开仓；内容改动走 PR，不直推 main
- 零遥测
