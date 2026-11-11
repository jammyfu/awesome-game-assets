"""Shared helpers. Standard library only, no network, no telemetry."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "entries.json"
PROMPTS = ROOT / "data" / "image-prompts.json"
WARNINGS = ROOT / "data" / "warnings.json"
MAX_IMAGE_BYTES = 300 * 1024


def load_entries() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def load_prompts() -> dict:
    return json.loads(PROMPTS.read_text(encoding="utf-8"))


def image_url(entry: dict) -> str:
    img = entry["image"]
    return img["src"] if img["type"] == "original" else img["file"]


def load_warnings() -> dict:
    return json.loads(WARNINGS.read_text(encoding="utf-8"))
