#!/usr/bin/env python3
"""Network checks: every link and hotlinked image is reachable, and every
GitHub entry is public, not archived, and its API `license` field matches the
listed license. Standard library only. Sends no data anywhere beyond the
requests themselves (no telemetry).

403/429 answers are reported as warnings because some sites block bots and CI
IP ranges; anything else >= 400 or a connection error fails.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from common import load_entries

UA = "Mozilla/5.0 (compatible; awesome-game-assets-linkcheck)"
GH = re.compile(r"^https://github\.com/([^/]+/[^/]+)/?$")


def fetch(url: str, method: str = "GET") -> int:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Range": "bytes=0-1023"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def github_repo(full: str) -> dict:
    req = urllib.request.Request(f"https://api.github.com/repos/{full}", headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def main() -> int:
    data = load_entries()
    targets = set()
    for e in data["entries"]:
        targets.update([e["url"], e["license_source"]])
        if e["image"]["type"] == "original":
            targets.update([e["image"]["src"], e["image"]["source"]])
    with ThreadPoolExecutor(8) as ex:
        results = dict(zip(sorted(targets), ex.map(fetch, sorted(targets))))
    errors, warnings = [], []
    for url, code in results.items():
        if code in (403, 429):
            warnings.append(f"{code} (bot-blocked?) {url}")
        elif code == 0 or code >= 400:
            errors.append(f"{code or 'unreachable'} {url}")
    for e in data["entries"]:
        m = GH.match(e["url"])
        if not m:
            continue
        try:
            repo = github_repo(m.group(1))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{e['id']}: GitHub API failed: {exc}")
            continue
        if repo.get("private"):
            errors.append(f"{e['id']}: repository is private")
        if repo.get("archived"):
            warnings.append(f"{e['id']}: repository is archived")
        spdx = (repo.get("license") or {}).get("spdx_id") or "NONE"
        if spdx == "NONE" and e.get("per_asset_license"):
            warnings.append(f"{e['id']}: no repo-level license; per-asset licenses ({e['license_source']})")
        elif spdx == "NONE":
            errors.append(f"{e['id']}: GitHub reports no license")
        elif spdx != "NOASSERTION" and spdx not in e["license"]:
            errors.append(f"{e['id']}: GitHub license {spdx} != listed {e['license']}")
    for w in warnings:
        print("WARN:", w)
    for er in errors:
        print("ERROR:", er)
    print(f"Checked {len(results)} URLs; {len(errors)} errors, {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
