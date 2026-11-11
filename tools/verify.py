#!/usr/bin/env python3
"""Single offline verification entry point. Uses sys.executable, no PATH lookups."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md", "README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md",
    "PROJECT_BRIEF.md", "MASTER_PLAN.md", "CURRENT_PLAN.md", "TODO_BACKLOG.md",
    "docs/project-governance/WORKLOG.md", "docs/project-governance/DECISIONS.md",
    "docs/project-governance/ACCEPTANCE.md", "docs/project-governance/CHANGELOG.md",
    "docs/AUTOMATION_COMMANDS.md", "docs/LONG_RUNNING_AUTONOMY.md", "docs/image-prompts.md",
    "data/entries.json", "data/image-prompts.json", "data/warnings.json",
    "WARNING.md", "WARNING.zh-CN.md", ".github/workflows/ci.yml",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        print("Missing required files: " + ", ".join(missing))
        return 1
    print("Scaffold files present.")
    steps = [
        [sys.executable, str(ROOT / "tools" / "check_list.py")],
        [sys.executable, str(ROOT / "tools" / "render_readme.py"), "--check"],
        [sys.executable, str(ROOT / "tools" / "next_plan.py"), "--check"],
        [sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"],
    ]
    for cmd in steps:
        if subprocess.run(cmd, cwd=ROOT).returncode != 0:
            print("FAILED:", " ".join(cmd[1:]))
            return 1
    print("All verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
