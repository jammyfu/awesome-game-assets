# AUTOMATION_COMMANDS.md

## 当前唯一计划入口

- `CURRENT_PLAN.md`

## 统一验证命令

```bash
python3 tools/verify.py        # 离线：骨架文件、清单格式、中英一致、去重、遥测、配图、生成文件最新、单元测试
python3 tools/check_links.py   # 联网：链接与图片可达、GitHub 仓公开且许可证与清单一致
```

## 重新生成 README

```bash
python3 tools/render_readme.py
```

## 自动生成下一轮计划

```bash
python3 tools/next_plan.py           # 写入下一轮模板
python3 tools/next_plan.py --check   # 只检查 CURRENT_PLAN.md 格式
```

## 自动化代理推荐执行顺序

1. 读取 `CURRENT_PLAN.md` / `MASTER_PLAN.md` / `TODO_BACKLOG.md` / `docs/project-governance/WORKLOG.md`
2. 完成当前轮最小闭环
3. 运行上面两条验证命令
4. 更新 `docs/project-governance/` 记录
5. 如果当前轮完成，运行 `python3 tools/next_plan.py`
