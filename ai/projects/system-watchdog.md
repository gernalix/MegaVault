META:
name=system_watchdog
slug=system-watchdog
path=/home/daniele/codex-workspace/system_watchdog
remote=none
branch=master
verified_commit=d93002d
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Persistent heartbeat sender for a Uptime Kuma push monitor.
STACK:
lang=Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=Uptime Kuma,systemd
MAP:
entry=UNKNOWN
core=dev/project.metadata.json,systemd/system-watchdog.service,watchdog.py
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=install.sh,logs.sh,status.sh,uninstall.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- watchdog.py=>utc_now,utc_iso,local_iso,read_text,boot_id,uptime_seconds,connect_db
- systemd/system-watchdog.service:5:StartLimitIntervalSec=0
- systemd/system-watchdog.service:17:ExecStart=/usr/bin/python3 ~/cw/system_watchdog/watchdog.py run
- systemd/system-watchdog.service:18:Restart=always
- systemd/system-watchdog.service:19:RestartSec=10
- watchdog.py:2:import argparse
- watchdog.py:3:import json
FLOW:
- systemd/system-watchdog.service:5:StartLimitIntervalSec=0
- systemd/system-watchdog.service:17:ExecStart=/usr/bin/python3 ~/cw/system_watchdog/watchdog.py run
- systemd/system-watchdog.service:18:Restart=always
- systemd/system-watchdog.service:19:RestartSec=10
- watchdog.py:2:import argparse
- watchdog.py:3:import json
- watchdog.py:4:import os
- watchdog.py:5:import signal
- watchdog.py:6:import sqlite3
- watchdog.py:7:import sys
- watchdog.py:8:import time
- watchdog.py:9:import urllib.error
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
arch=watchdog.py:144:def push(url, timeout):
arch=watchdog.py:148:with urllib.request.urlopen(req, timeout=timeout) as resp:
arch=watchdog.py:183:ok, status, error, response_ms = push(args.push_url, args.timeout)
arch=watchdog.py:202:ok, status, error, response_ms = push(args.push_url, args.timeout)
data=systemd/system-watchdog.service:12:Environment=WATCHDOG_DB=~/cw/system_watchdog/watchdog.sqlite
data=watchdog.py:2:import argparse
data=watchdog.py:3:import json
data=watchdog.py:4:import os
safety=install.sh:10:sudo install -m 0644 "$SERVICE_SRC" "$SERVICE_DST"
safety=install.sh:11:sudo systemctl daemon-reload
safety=install.sh:12:sudo systemctl enable --now system-watchdog.service
safety=install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
safety=uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
safety=uninstall.sh:5:sudo rm -f /etc/systemd/system/system-watchdog.service
safety=uninstall.sh:6:sudo systemctl daemon-reload
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
version=watchdog.py:144:def push(url, timeout):
version=watchdog.py:183:ok, status, error, response_ms = push(args.push_url, args.timeout)
version=watchdog.py:202:ok, status, error, response_ms = push(args.push_url, args.timeout)
i18n=UNKNOWN
BUILD:
- install.sh:1:#!/usr/bin/env bash
- install.sh:8:python3 --version >/dev/null
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- logs.sh:1:#!/usr/bin/env bash
- logs.sh:4:journalctl -u system-watchdog.service -n "${1:-100}" --no-pager
- status.sh:1:#!/usr/bin/env bash
- status.sh:5:systemctl --no-pager --full status system-watchdog.service // true
- status.sh:7:python3 "$ROOT/watchdog.py" last // true
- uninstall.sh:1:#!/usr/bin/env bash
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
TEST:
- UNKNOWN
DATA:
db=systemd/system-watchdog.service:12:Environment=WATCHDOG_DB=~/cw/system_watchdog/watchdog.sqlite
db=watchdog.py:2:import argparse
db=watchdog.py:3:import json
db=watchdog.py:4:import os
backup=UNKNOWN
import=watchdog.py:2:import argparse
import=watchdog.py:3:import json
import=watchdog.py:4:import os
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- install.sh:10:sudo install -m 0644 "$SERVICE_SRC" "$SERVICE_DST"
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
- uninstall.sh:5:sudo rm -f /etc/systemd/system/system-watchdog.service
- uninstall.sh:6:sudo systemctl daemon-reload
- dev/project.metadata.json:9:"metadata_version": 1,
- install.sh:8:python3 --version >/dev/null
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
BUG:
- systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
- systemd/system-watchdog.service:21:StandardError=journal
- watchdog.py:9:import urllib.error
- watchdog.py:38:except OSError:
- watchdog.py:50:except (ValueError, IndexError):
- watchdog.py:67:error TEXT,
- watchdog.py:100:except ValueError:
- watchdog.py:140:except OSError:
- watchdog.py:144:def push(url, timeout):
- watchdog.py:148:with urllib.request.urlopen(req, timeout=timeout) as resp:
RISK:
- install.sh:10:sudo install -m 0644 "$SERVICE_SRC" "$SERVICE_DST"
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
- uninstall.sh:5:sudo rm -f /etc/systemd/system/system-watchdog.service
- uninstall.sh:6:sudo systemctl daemon-reload
ROAD:
now=systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
next=systemd/system-watchdog.service:21:StandardError=journal
later=watchdog.py:9:import urllib.error
LINK:
meta=../../../system_watchdog/dev/project.metadata.json
human=../../human/projects/system-watchdog/overview.md
legacy=../../../system_watchdog/dev/legacy
repo=../../../system_watchdog
OPEN:
- no tests detected by static scan
