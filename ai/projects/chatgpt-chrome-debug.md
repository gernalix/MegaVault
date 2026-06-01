META:
name=chatgpt-chrome-debug
slug=chatgpt-chrome-debug
path=/home/daniele/codex-workspace/chatgpt-chrome-debug
remote=none
branch=master
verified_commit=fdd3773
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- ChatGPT Chrome Redirect Debug Toolkit
STACK:
lang=JS/TS,Python,Shell;fw=Playwright;db=UNKNOWN;platform=UNKNOWN;tools=Chrome,systemd
MAP:
entry=UNKNOWN
core=dev/project.metadata.json,package-lock.json
ui=UNKNOWN
db=scripts/snapshot_environment.sh
tests=UNKNOWN
scripts=START_DEBUGGING.sh
scripts=scripts/common.sh
scripts=scripts/dashboard.sh
scripts=scripts/install_user_services.sh
scripts=scripts/live_chrome_logger.sh
scripts=scripts/monitor_chatgpt_tab.js
scripts=scripts/run_differential_tests.sh
scripts=scripts/stress_memory.py
build=package.json
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- START_DEBUGGING.sh:13:./scripts/live_chrome_logger.sh start
- scripts/install_user_services.sh:18:ExecStart=$ROOT_DIR/scripts/live_chrome_logger.sh run
- scripts/install_user_services.sh:19:Restart=always
- scripts/install_user_services.sh:20:RestartSec=10
- scripts/live_chrome_logger.sh:15:start_logger() {
- scripts/live_chrome_logger.sh:22:echo "started pid=$(cat "$PID_FILE")"
FLOW:
- START_DEBUGGING.sh:13:./scripts/live_chrome_logger.sh start
- scripts/install_user_services.sh:18:ExecStart=$ROOT_DIR/scripts/live_chrome_logger.sh run
- scripts/install_user_services.sh:19:Restart=always
- scripts/install_user_services.sh:20:RestartSec=10
- scripts/live_chrome_logger.sh:15:start_logger() {
- scripts/live_chrome_logger.sh:22:echo "started pid=$(cat "$PID_FILE")"
- scripts/live_chrome_logger.sh:27:log_line "$MAIN_LOG" "live logger foreground started root=$ROOT_DIR"
- scripts/live_chrome_logger.sh:68:stop_logger() {
- scripts/live_chrome_logger.sh:73:echo "stopped"
- scripts/live_chrome_logger.sh:87:case "${1:-start}" in
- scripts/live_chrome_logger.sh:88:start) start_logger ;;
- scripts/live_chrome_logger.sh:90:stop) stop_logger ;;
INV:
arch=scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
arch=scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
arch=scripts/snapshot_environment.sh:66:--user-data-dir="$DIAG_DIR/profiles/chrome_version_probe" \
arch=scripts/snapshot_environment.sh:67:--dump-dom chrome://version 2>&1 // true
arch=scripts/snapshot_environment.sh:68:} > "$OUT/chrome_version_page.html"
arch=scripts/snapshot_environment.sh:94:(.value.manifest.version // "unknown"),
data=UNKNOWN
safety=scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions //
safety=scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") / ascii_downcase) / test("chatgpt/refresh/
safety=scripts/snapshot_environment.sh:149:curl -4 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-
safety=scripts/snapshot_environment.sh:150:curl -6 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-
safety=package-lock.json:4:"lockfileVersion": 3,
safety=scripts/live_chrome_logger.sh:12:[[ -r "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
safety=scripts/live_chrome_logger.sh:32:kill "$pid" 2>/dev/null // true
ux=scripts/monitor_chatgpt_tab.js:4:const fs = require('fs');
ux=scripts/monitor_chatgpt_tab.js:5:const path = require('path');
ux=scripts/monitor_chatgpt_tab.js:6:const { chromium } = require('playwright');
ux=scripts/monitor_chatgpt_tab.js:98:await safeEvaluate(page, () => performance.getEntries().map((entry) => entry.t
version=scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
version=scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
version=scripts/snapshot_environment.sh:66:--user-data-dir="$DIAG_DIR/profiles/chrome_version_probe" \
version=scripts/snapshot_environment.sh:67:--dump-dom chrome://version 2>&1 // true
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- START_DEBUGGING.sh:1:#!/usr/bin/env bash
- START_DEBUGGING.sh:10:./scripts/snapshot_environment.sh
- START_DEBUGGING.sh:13:./scripts/live_chrome_logger.sh start
- START_DEBUGGING.sh:17:npm install
- START_DEBUGGING.sh:22:exec npm run monitor -- --url="${CHATGPT_URL:-https://chatgpt.com/}" --profile="${CHATGPT_PROF
- scripts/common.sh:1:#!/usr/bin/env bash
- scripts/dashboard.sh:1:#!/usr/bin/env bash
- scripts/dashboard.sh:4:source "$(dirname "$0")/common.sh"
- scripts/dashboard.sh:14:echo "== Chrome renderer/crash signals =="
- scripts/dashboard.sh:15:grep -Eih 'renderer/crash/segfault/oom/out of memory/gpu reset/discard' "$DIAG_DIR/live/"*.l
- scripts/install_user_services.sh:1:#!/usr/bin/env bash
- scripts/install_user_services.sh:4:source "$(dirname "$0")/common.sh"
TEST:
- UNKNOWN
DATA:
db=scripts/snapshot_environment.sh:83:} > "$OUT/chrome_flags.json"
backup=scripts/snapshot_environment.sh:83:} > "$OUT/chrome_flags.json"
import=scripts/stress_memory.py:2:import sys
import=scripts/stress_memory.py:3:import time
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // []))
- scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") / ascii_downcase) / test("chatgpt/refresh/tab/
- scripts/snapshot_environment.sh:149:curl -4 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cook
- scripts/snapshot_environment.sh:150:curl -6 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cook
- package-lock.json:4:"lockfileVersion": 3,
- scripts/live_chrome_logger.sh:12:[[ -r "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
- scripts/live_chrome_logger.sh:32:kill "$pid" 2>/dev/null // true
- scripts/live_chrome_logger.sh:47:dmesg -w --time-format iso 2>/dev/null / grep --line-buffered -Ei 'oom/out of memor
- scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
- scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
BUG:
- scripts/snapshot_environment.sh:2:set -euo pipefail
- scripts/snapshot_environment.sh:138:echo "== chrome crash directories =="
- scripts/snapshot_environment.sh:139:find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -
- scripts/snapshot_environment.sh:142:journalctl --user --since '-24 hours' 2>/dev/null / grep -Ei 'chrome/chromium/gp
- scripts/snapshot_environment.sh:143:} > "$OUT/crash_and_logs.txt"
- dev/project.metadata.json:2:"project_name": "chatgpt-chrome-debug",
- dev/project.metadata.json:3:"project_slug": "chatgpt-chrome-debug",
- dev/project.metadata.json:4:"project_root": "~/cw/chatgpt-chrome-debug",
- dev/project.metadata.json:6:"ai_doc": "~/cw/MegaVault/ai/projects/chatgpt-chrome-debug.md",
- dev/project.metadata.json:7:"human_doc": "~/cw/MegaVault/human/projects/chatgpt-chrome-debug",
RISK:
- scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // []))
- scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") / ascii_downcase) / test("chatgpt/refresh/tab/
- scripts/snapshot_environment.sh:149:curl -4 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cook
- scripts/snapshot_environment.sh:150:curl -6 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cook
- package-lock.json:4:"lockfileVersion": 3,
- scripts/live_chrome_logger.sh:12:[[ -r "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
- scripts/live_chrome_logger.sh:32:kill "$pid" 2>/dev/null // true
- scripts/live_chrome_logger.sh:47:dmesg -w --time-format iso 2>/dev/null / grep --line-buffered -Ei 'oom/out of memor
- scripts/live_chrome_logger.sh:70:kill "$(cat "$PID_FILE")" 2>/dev/null // true
- scripts/monitor_chatgpt_tab.js:92:fs.writeFileSync(path.join(dir, 'cookies.json'), JSON.stringify(await context.cook
ROAD:
now=scripts/snapshot_environment.sh:2:set -euo pipefail
next=scripts/snapshot_environment.sh:138:echo "== chrome crash directories =="
later=scripts/snapshot_environment.sh:139:find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -
LINK:
meta=../../../chatgpt-chrome-debug/dev/project.metadata.json
human=../../human/projects/chatgpt-chrome-debug/overview.md
legacy=../../../chatgpt-chrome-debug/dev/legacy
repo=../../../chatgpt-chrome-debug
OPEN:
- no tests detected by static scan
