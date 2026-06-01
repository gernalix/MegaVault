META:
name=linux-mint-service-dashboard
slug=linux-mint-service-dashboard
path=/home/daniele/codex-workspace/linux-mint-service-dashboard
remote=none
branch=prompt-816-local-dashboard
verified_commit=487ca7e
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
STACK:
lang=JS/TS,Python;fw=Playwright;db=SQLite;platform=UNKNOWN;tools=Uptime Kuma,restic,systemd
MAP:
entry=app/server.py
core=app/__init__.py
core=app/collectors.py
core=dev/project.metadata.json
core=launchers/linux-mint-service-dashboard.desktop
core=systemd/system-service-dashboard.service
ui=app/static/app.js,app/static/index.html,app/static/styles.css
db=UNKNOWN
tests=tests/playwright-smoke.js,tests/test_dashboard.py
scripts=UNKNOWN
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- app/server.py=>DashboardHandler,parse_args,main
- app/collectors.py=>CommandResult,now_local,iso_now,display_now,version,redact_text,redact
- app/static/app.js=>escapeHtml,statusClass,scalar,renderOverview,statCard,renderTabs,renderPanel
- app/server.py:2:from __future__ import annotations
- app/server.py:4:import argparse
- app/server.py:5:import json
- app/server.py:6:import mimetypes
- app/server.py:7:import sys
- app/server.py:8:import time
FLOW:
- app/server.py:2:from __future__ import annotations
- app/server.py:4:import argparse
- app/server.py:5:import json
- app/server.py:6:import mimetypes
- app/server.py:7:import sys
- app/server.py:8:import time
- app/server.py:9:import traceback
- app/server.py:10:from http import HTTPStatus
- app/collectors.py:1:from __future__ import annotations
- app/collectors.py:3:import json
- app/collectors.py:4:import os
- app/collectors.py:5:import re
INV:
arch=app/server.py:18:from app.collectors import collect_all, display_now, redact_text, version
arch=app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"
arch=app/server.py:60:"version": version(),
arch=app/server.py:80:self.send_json({"status": "ok", "version": version(), "refresh_display": display_now(), "read_o
arch=app/server.py:116:parser = argparse.ArgumentParser(description="Linux Mint local read-only service dashboard")
arch=app/server.py:128:print(f"linux-mint-service-dashboard v{version()} listening on http://{args.host}:{args.port}"
data=app/server.py:2:from __future__ import annotations
data=app/server.py:4:import argparse
data=app/server.py:5:import json
data=app/server.py:6:import mimetypes
safety=app/server.py:9:import traceback
safety=app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
safety=app/server.py:86:relative = path.removeprefix("/static/")
safety=app/collectors.py:24:SECRET_PATTERNS = [
safety=app/collectors.py:26:re.compile(r"((?:token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_ke
safety=app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/
safety=app/collectors.py:45:r"storage/lock/TRUE_PRE_EMERGENCY/PRE_EMERGENCY/abort/skipped",
ux=tests/playwright-smoke.js:1:const { chromium } = require("playwright");
version=app/server.py:18:from app.collectors import collect_all, display_now, redact_text, version
version=app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"
version=app/server.py:60:"version": version(),
version=app/server.py:80:self.send_json({"status": "ok", "version": version(), "refresh_display": display_now(), "read_o
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- UNKNOWN
TEST:
- tests/playwright-smoke.js:1:const { chromium } = require("playwright");
- tests/test_dashboard.py:7:import unittest
- tests/test_dashboard.py:17:class DashboardTests(unittest.TestCase):
- tests/test_dashboard.py:18:def test_rsync_progress_parser(self) -> None:
- tests/test_dashboard.py:20:self.assertEqual(parsed["current_file_percent"], 42.0)
- tests/test_dashboard.py:21:self.assertEqual(parsed["current_rate"], "5.50 MB/s")
- tests/test_dashboard.py:22:self.assertEqual(parsed["eta_seconds_raw"], 600)
- tests/test_dashboard.py:24:def test_secret_redaction(self) -> None:
- tests/test_dashboard.py:27:self.assertNotIn("super-token", cleaned)
- tests/test_dashboard.py:28:self.assertNotIn("abc", cleaned)
- tests/test_dashboard.py:29:self.assertNotIn("bucket/key", cleaned)
DATA:
db=app/server.py:2:from __future__ import annotations
db=app/server.py:4:import argparse
db=app/server.py:5:import json
db=app/server.py:6:import mimetypes
backup=UNKNOWN
import=app/server.py:2:from __future__ import annotations
import=app/server.py:4:import argparse
import=app/server.py:5:import json
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- app/server.py:9:import traceback
- app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
- app/server.py:86:relative = path.removeprefix("/static/")
- app/collectors.py:24:SECRET_PATTERNS = [
- app/collectors.py:26:re.compile(r"((?:token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_key/aw
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degr
- app/collectors.py:45:r"storage/lock/TRUE_PRE_EMERGENCY/PRE_EMERGENCY/abort/skipped",
- app/collectors.py:77:for pattern in SECRET_PATTERNS:
- app/server.py:18:from app.collectors import collect_all, display_now, redact_text, version
- app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"
BUG:
- app/server.py:53:except Exception as exc: # pragma: no cover - defensive server boundary
- app/server.py:56:"status": "error",
- app/server.py:57:"error": redact_text(str(exc)),
- app/server.py:62:HTTPStatus.INTERNAL_SERVER_ERROR,
- app/collectors.py:10:import urllib.error
- app/collectors.py:36:NO_RECENT_ERROR = "nessun errore recente"
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degr
- app/collectors.py:71:except OSError:
- app/collectors.py:98:def run(args: list[str], timeout: float = 2.0) -> CommandResult:
- app/collectors.py:100:proc = subprocess.run(args, text=True, capture_output=True, timeout=timeout, check=False)
RISK:
- app/server.py:9:import traceback
- app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
- app/server.py:86:relative = path.removeprefix("/static/")
- app/collectors.py:24:SECRET_PATTERNS = [
- app/collectors.py:26:re.compile(r"((?:token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_key/aw
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degr
- app/collectors.py:45:r"storage/lock/TRUE_PRE_EMERGENCY/PRE_EMERGENCY/abort/skipped",
- app/collectors.py:77:for pattern in SECRET_PATTERNS:
- app/collectors.py:90:if re.search(r"token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_key/aws_
- app/collectors.py:142:if re.search(r"BLOCKED/ERROR/FAILED/WARNING/CRITICAL/PRE_EMERGENCY", classification, re.I):
ROAD:
now=app/server.py:2:from __future__ import annotations
next=app/collectors.py:1:from __future__ import annotations
later=app/collectors.py:238:"NextElapseUSecRealtime",
LINK:
meta=../../../linux-mint-service-dashboard/dev/project.metadata.json
human=../../human/projects/linux-mint-service-dashboard/overview.md
legacy=../../../linux-mint-service-dashboard/dev/legacy
repo=../../../linux-mint-service-dashboard
OPEN:
- none
