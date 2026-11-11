#!/usr/bin/env python3
"""Write the next CURRENT_PLAN.md template, or --check its structure."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_PLAN = ROOT / "CURRENT_PLAN.md"
SECTIONS = ["## Plan ID", "## Goal", "## Current Focus", "## In Scope", "## Out of Scope", "## Tasks", "## Verification", "## Next Candidates"]

TEMPLATE = """# CURRENT_PLAN.md

## Plan ID

PLAN-NEXT

## Goal

基于上一轮结果推进下一个最小稳定闭环（见 TODO_BACKLOG.md 的 Next）。

## Current Focus

Next iteration

## In Scope

- 收敛新的最小闭环

## Out of Scope

- 不并行扩张多个大方向

## Tasks

- [ ] 根据上一轮 worklog 补充下一轮任务

## Verification

- `python3 tools/verify.py`
- `python3 tools/check_links.py`

## Next Candidates

- 根据 backlog 与验证结果继续细化
"""


def check(text: str) -> list[str]:
    return [s for s in SECTIONS if s not in text]


def main() -> int:
    if "--check" in sys.argv:
        missing = check(CURRENT_PLAN.read_text(encoding="utf-8"))
        if missing:
            print("CURRENT_PLAN.md missing sections: " + ", ".join(missing))
            return 1
        print("CURRENT_PLAN.md structure OK.")
        return 0
    CURRENT_PLAN.write_text(TEMPLATE, encoding="utf-8")
    print(f"Updated {CURRENT_PLAN.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
