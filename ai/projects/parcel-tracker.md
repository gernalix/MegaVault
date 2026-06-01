META:
name=parcel-tracker
slug=parcel-tracker
path=/home/daniele/codex-workspace/parcel-tracker
remote=none
branch=master
verified_commit=0fea1eb
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Servizio leggero user-level per monitorare la spedizione `XT329499807TS`.
STACK:
lang=Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=Uptime Kuma
MAP:
entry=UNKNOWN
core=dev/project.metadata.json,parcel-tracker.service,parcel-tracker.timer,parcel_tracker.py
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=parcel_tracker.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- parcel_tracker.py=>TrackingSnapshot,utc_now,log,db,get_state,set_state,fetch_url
- parcel-tracker.service:9:ExecStart=/usr/bin/env bash ~/cw/parcel-tracker/parcel_tracker.sh --run
- parcel-tracker.timer:4:[Timer]
- parcel-tracker.timer:12:WantedBy=timers.target
- parcel_tracker.py:2:from __future__ import annotations
- parcel_tracker.py:4:import argparse
- parcel_tracker.py:5:import hashlib
FLOW:
- parcel-tracker.service:9:ExecStart=/usr/bin/env bash ~/cw/parcel-tracker/parcel_tracker.sh --run
- parcel-tracker.timer:4:[Timer]
- parcel-tracker.timer:12:WantedBy=timers.target
- parcel_tracker.py:2:from __future__ import annotations
- parcel_tracker.py:4:import argparse
- parcel_tracker.py:5:import hashlib
- parcel_tracker.py:6:import html
- parcel_tracker.py:7:import json
- parcel_tracker.py:8:import os
- parcel_tracker.py:9:import re
- parcel_tracker.py:10:import sqlite3
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:
arch=parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
arch=parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
arch=parcel_tracker.py:215:timeout=40,
arch=parcel_tracker.py:223:subprocess.run([sys.executable, str(TELEGRAM_HELPER), "--check"], check=True, timeout=20)
data=parcel_tracker.py:2:from __future__ import annotations
data=parcel_tracker.py:4:import argparse
data=parcel_tracker.py:5:import hashlib
data=parcel_tracker.py:6:import html
safety=dev/project.metadata.json:9:"metadata_version": 1,
safety=preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
version=parcel_tracker.py:234:urllib.request.urlopen(KUMA_PUSH_URL, timeout=20).read()
i18n=UNKNOWN
BUILD:
- parcel_tracker.sh:2:#!/usr/bin/env bash
- parcel_tracker.sh:6:PYTHON_BIN="${PYTHON_BIN:-python3}"
TEST:
- UNKNOWN
DATA:
db=parcel_tracker.py:2:from __future__ import annotations
db=parcel_tracker.py:4:import argparse
db=parcel_tracker.py:5:import hashlib
db=parcel_tracker.py:6:import html
backup=UNKNOWN
import=parcel_tracker.py:2:from __future__ import annotations
import=parcel_tracker.py:4:import argparse
import=parcel_tracker.py:5:import hashlib
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- dev/project.metadata.json:9:"metadata_version": 1,
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
BUG:
- parcel_tracker.py:14:import urllib.error
- parcel_tracker.py:76:error TEXT
- parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:
- parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
- parcel_tracker.py:109:return resp.read().decode(charset, errors="replace")
- parcel_tracker.py:145:except json.JSONDecodeError:
- parcel_tracker.py:192:digest = hashlib.sha256(page.encode("utf-8", errors="replace")).hexdigest()
- parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
- parcel_tracker.sh:3:set -euo pipefail
RISK:
- UNKNOWN
ROAD:
now=parcel_tracker.py:2:from __future__ import annotations
next=parcel_tracker.py:137:next_data = re.search(r"<script[^>]+id=[\"']__NEXT_DATA__[\"'][^>]*>(.*?)</script>", page, re.
later=parcel_tracker.py:138:if next_data:
LINK:
meta=../../../parcel-tracker/dev/project.metadata.json
human=../../human/projects/parcel-tracker/overview.md
legacy=../../../parcel-tracker/dev/legacy
repo=../../../parcel-tracker
OPEN:
- no tests detected by static scan
