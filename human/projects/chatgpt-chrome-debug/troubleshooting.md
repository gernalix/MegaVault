# chatgpt-chrome-debug Troubleshooting

## Problemi e sintomi rilevati nel codice
- scripts/snapshot_environment.sh:2:set -euo pipefail
- scripts/snapshot_environment.sh:138:echo "== chrome crash directories =="
- scripts/snapshot_environment.sh:139:find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -iname '*crash*' -o -iname '*.dmp' \) -printf '%TY-%Tm-%Td %TH:%T
- scripts/snapshot_environment.sh:142:journalctl --user --since '-24 hours' 2>/dev/null / grep -Ei 'chrome/chromium/gpu/oom/renderer/crash' / tail -200 // true
- scripts/snapshot_environment.sh:143:} > "$OUT/crash_and_logs.txt"
- dev/project.metadata.json:2:"project_name": "chatgpt-chrome-debug",
- dev/project.metadata.json:3:"project_slug": "chatgpt-chrome-debug",
- dev/project.metadata.json:4:"project_root": "~/cw/chatgpt-chrome-debug",
- dev/project.metadata.json:6:"ai_doc": "~/cw/MegaVault/ai/projects/chatgpt-chrome-debug.md",
- dev/project.metadata.json:7:"human_doc": "~/cw/MegaVault/human/projects/chatgpt-chrome-debug",
- package-lock.json:2:"name": "chatgpt-chrome-debug",
- package-lock.json:8:"name": "chatgpt-chrome-debug",
- START_DEBUGGING.sh:2:set -euo pipefail
- START_DEBUGGING.sh:22:exec npm run monitor -- --url="${CHATGPT_URL:-https://chatgpt.com/}" --profile="${CHATGPT_PROFILE:-manual_debug}"
- scripts/common.sh:2:set -euo pipefail
- scripts/dashboard.sh:2:set -euo pipefail
- scripts/dashboard.sh:9:echo "ChatGPT Chrome Debug Dashboard - $(ts)"
- scripts/dashboard.sh:14:echo "== Chrome renderer/crash signals =="

## Comandi/verifiche utili trovati
- START_DEBUGGING.sh:1:#!/usr/bin/env bash
- START_DEBUGGING.sh:10:./scripts/snapshot_environment.sh
- START_DEBUGGING.sh:13:./scripts/live_chrome_logger.sh start
- START_DEBUGGING.sh:17:npm install
- START_DEBUGGING.sh:22:exec npm run monitor -- --url="${CHATGPT_URL:-https://chatgpt.com/}" --profile="${CHATGPT_PROFILE:-manual_debug}"
- scripts/common.sh:1:#!/usr/bin/env bash
- scripts/dashboard.sh:1:#!/usr/bin/env bash
- scripts/dashboard.sh:4:source "$(dirname "$0")/common.sh"
- scripts/dashboard.sh:14:echo "== Chrome renderer/crash signals =="
- scripts/dashboard.sh:15:grep -Eih 'renderer/crash/segfault/oom/out of memory/gpu reset/discard' "$DIAG_DIR/live/"*.log 2>/dev/null / tail -8 // true
- scripts/install_user_services.sh:1:#!/usr/bin/env bash
- scripts/install_user_services.sh:4:source "$(dirname "$0")/common.sh"
- scripts/install_user_services.sh:18:ExecStart=$ROOT_DIR/scripts/live_chrome_logger.sh run
- scripts/install_user_services.sh:26:systemctl --user daemon-reload
- scripts/install_user_services.sh:27:systemctl --user enable --now chatgpt-chrome-live-logger.service
- scripts/install_user_services.sh:28:systemctl --user status --no-pager chatgpt-chrome-live-logger.service // true

## Safety prima di correggere
- scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // [])) / tostring) / test("tabs/webRequest/webNavigation/scripting/sto
- scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") / ascii_downcase) / test("chatgpt/refresh/tab/cookie/script/style/monitor/ghostery/ublock"))
- scripts/snapshot_environment.sh:149:curl -4 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cookie:).*/\1 [redacted]/Ig' // true
- scripts/snapshot_environment.sh:150:curl -6 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cookie:).*/\1 [redacted]/Ig' // true
- package-lock.json:4:"lockfileVersion": 3,
- scripts/live_chrome_logger.sh:12:[[ -r "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
- scripts/live_chrome_logger.sh:32:kill "$pid" 2>/dev/null // true
- scripts/live_chrome_logger.sh:47:dmesg -w --time-format iso 2>/dev/null / grep --line-buffered -Ei 'oom/out of memory/chrome/chromium/renderer/gpu/drm/i915/mesa/segfault/killed pro
- scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
- scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
- scripts/snapshot_environment.sh:66:--user-data-dir="$DIAG_DIR/profiles/chrome_version_probe" \
- scripts/snapshot_environment.sh:67:--dump-dom chrome://version 2>&1 // true
