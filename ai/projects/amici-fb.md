META:
name=amici_fb
slug=amici-fb
path=/home/daniele/codex-workspace/scripts/amici_fb
remote=https://github.com/gernalix/amici_fb.git
branch=master
verified_commit=0e021f6
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Linux Mint user-level Facebook automation that opens Facebook with a browser profile, processes friends/URLs, and records local state i...
STACK:
lang=Python,Shell;fw=Playwright;db=SQLite;platform=UNKNOWN;tools=Uptime Kuma,systemd
MAP:
entry=UNKNOWN
core=_shared/__init__.py
core=_shared/telegram_notify.py
core=amici-fb.service
core=amici-fb.timer
core=amici_fb.py
core=amici_fb.service
core=amici_fb.timer
core=amici_fb_task_runner.py
ui=UNKNOWN
db=fb_storage_state.json
tests=UNKNOWN
scripts=install_ubuntu_autorun.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- _shared/telegram_notify.py=>_first_env,_config,validate_config,_masked,config_summary,fix_mojibake,_telegram_url
- amici_fb.py=>DiagLogger,BrowserProcessWatcher,iso_utc_z,filename_stamp_utc,ensure_output_dir,project_path,output_dir
- amici_fb_task_runner.py=>_sanitize_log_text,_failure_reason,_push_url_base,push_kuma,main
- telegram_notify.py=>_load_project_env,_first_env,_config,validate_config,_masked,config_summary,fix_mojibake
- _shared/telegram_notify.py:10:from __future__ import annotations
- _shared/telegram_notify.py:12:import argparse
- _shared/telegram_notify.py:13:import html
- _shared/telegram_notify.py:14:import os
- _shared/telegram_notify.py:15:import sys
- _shared/telegram_notify.py:16:from pathlib import Path
FLOW:
- _shared/telegram_notify.py:10:from __future__ import annotations
- _shared/telegram_notify.py:12:import argparse
- _shared/telegram_notify.py:13:import html
- _shared/telegram_notify.py:14:import os
- _shared/telegram_notify.py:15:import sys
- _shared/telegram_notify.py:16:from pathlib import Path
- _shared/telegram_notify.py:17:from typing import Iterable
- _shared/telegram_notify.py:19:import requests
- amici-fb.service:10:ExecStart=~/cw/scripts/amici_fb/.venv/bin/python -u -X faulthandler ~/cw/scripts/amici_fb/amici_
- amici-fb.timer:4:[Timer]
- amici-fb.timer:10:WantedBy=timers.target
- amici_fb.py:2:import os
INV:
arch=_shared/telegram_notify.py:38:raise RuntimeError(
arch=_shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be s
arch=_shared/telegram_notify.py:85:raise RuntimeError(f"{action} failed: HTTP {response.status_code}: {body}")
arch=_shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20)
arch=_shared/telegram_notify.py:104:timeout=20,
arch=_shared/telegram_notify.py:119:raise FileNotFoundError(str(path))
data=_shared/telegram_notify.py:10:from __future__ import annotations
data=_shared/telegram_notify.py:12:import argparse
data=_shared/telegram_notify.py:13:import html
data=_shared/telegram_notify.py:14:import os
safety=fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "
safety=_shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
safety=_shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
safety=_shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
safety=_shared/telegram_notify.py:37:if not token or not chat_id:
safety=_shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be s
safety=_shared/telegram_notify.py:41:return token, chat_id
ux=data/amici_2025-11-24.csv:73:2025-11-24,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto
ux=data/amici_2025-11-28.csv:73:2025-11-28,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto
ux=data/amici_2025-11-29.csv:73:2025-11-29,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto
ux=data/amici_2025-11-30.csv:73:2025-11-30,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- install_ubuntu_autorun.sh:1:#!/usr/bin/env bash
- install_ubuntu_autorun.sh:7:PYTHON_BIN="$VENV_DIR/bin/python3"
- install_ubuntu_autorun.sh:12:python3 -m venv "$VENV_DIR"
- install_ubuntu_autorun.sh:22:systemctl --user daemon-reload
- install_ubuntu_autorun.sh:23:systemctl --user enable --now amici_fb.timer
- install_ubuntu_autorun.sh:27:systemctl --user start amici_fb.service
- install_ubuntu_autorun.sh:31:systemctl --user list-timers amici_fb.timer --no-pager
TEST:
- UNKNOWN
DATA:
db=_shared/telegram_notify.py:10:from __future__ import annotations
db=_shared/telegram_notify.py:12:import argparse
db=_shared/telegram_notify.py:13:import html
db=_shared/telegram_notify.py:14:import os
backup=UNKNOWN
import=_shared/telegram_notify.py:10:from __future__ import annotations
import=_shared/telegram_notify.py:12:import argparse
import=_shared/telegram_notify.py:13:import html
export=UNKNOWN
migration=UNKNOWN
retention=fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "
DNB:
- fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "doma
- _shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
- _shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
- _shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:37:if not token or not chat_id:
- _shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
- _shared/telegram_notify.py:41:return token, chat_id
- _shared/telegram_notify.py:57:token_name, token = _first_env(TOKEN_ENV_NAMES)
- amici_fb.py:70:"temporarily blocked",
- amici_fb.py:198:self._lock = threading.Lock()
BUG:
- _shared/telegram_notify.py:38:raise RuntimeError(
- _shared/telegram_notify.py:72:except Exception:
- _shared/telegram_notify.py:85:raise RuntimeError(f"{action} failed: HTTP {response.status_code}: {body}")
- _shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20)
- _shared/telegram_notify.py:104:timeout=20,
- _shared/telegram_notify.py:119:raise FileNotFoundError(str(path))
- _shared/telegram_notify.py:133:timeout=60,
- _shared/telegram_notify.py:160:parser.error("title and message are required unless --check is used")
- amici_fb.py:52:DEFAULT_NAVIGATION_TIMEOUT_MS = 120000
- amici_fb.py:53:POST_FRIENDS_GOTO_TIMEOUT_MS = 10000
RISK:
- fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "doma
- _shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
- _shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
- _shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:37:if not token or not chat_id:
- _shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
- _shared/telegram_notify.py:41:return token, chat_id
- _shared/telegram_notify.py:57:token_name, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:60:f"token={token_name or 'missing'}:{_masked(token)} "
- amici_fb.py:14:IMPORT_TRACE = os.getenv("AMICI_FB_IMPORT_TRACE") == "1"
ROAD:
now=_shared/telegram_notify.py:10:from __future__ import annotations
next=amici_fb_task_runner.py:4:from __future__ import annotations
later=amici_fb_task_runner.py:92:faulthandler.dump_traceback_later(dump_seconds, repeat=True)
LINK:
meta=../../../scripts/amici_fb/dev/project.metadata.json
human=../../human/projects/amici-fb/overview.md
legacy=../../../scripts/amici_fb/dev/legacy
repo=../../../scripts/amici_fb
OPEN:
- no tests detected by static scan
