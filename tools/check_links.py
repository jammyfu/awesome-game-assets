#!/usr/bin/env python3
"""Network checks: every link and hotlinked image is reachable, and every
GitHub entry is public, not archived, and its API `license` field matches the
listed license. Standard library only. Sends no data anywhere beyond the
requests themselves (no telemetry).

403/429 answers and timeouts are reported as warnings (kept, marked in the
list when persistent) because some sites block bots and CI IP ranges; 404 and
any other >= 400 or a connection error fails. Failures are retried twice.
"""
from __future__ import annotations

import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from common import load_entries, load_warnings

UA = "Mozilla/5.0 (compatible; awesome-game-assets-linkcheck)"
GH = re.compile(r"^https://github\.com/([^/]+/[^/]+)/?$")


TIMEOUT = -1


def fetch_once(url: str) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Range": "bytes=0-1023"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except (TimeoutError, socket.timeout):
        return TIMEOUT
    except urllib.error.URLError as e:
        return TIMEOUT if isinstance(e.reason, (TimeoutError, socket.timeout)) else 0
    except Exception:
        return 0


def fetch(url: str) -> int:
    code = fetch_once(url)
    for _ in range(2):  # retry transient failures
        if code in (0, TIMEOUT, 429) or code >= 500:
            time.sleep(2)
            code = fetch_once(url)
        else:
            break
    return code


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
    warn = load_warnings()
    for w in warn["entries"]:
        targets.add(w["url"])
        if w.get("image"):
            targets.add(w["image"]["src"])
    with ThreadPoolExecutor(8) as ex:
        results = dict(zip(sorted(targets), ex.map(fetch, sorted(targets))))
    errors, warnings = [], []
    for url, code in results.items():
        if code in (403, 429):
            warnings.append(f"{code} (bot-blocked?) {url}")
        elif code == TIMEOUT:
            warnings.append(f"timeout {url}")
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
        if spdx == "NONE" and (e.get("per_asset_license") or e.get("license_in_readme")):
            warnings.append(f"{e['id']}: no license file detected by GitHub; license verified at {e['license_source']}")
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
