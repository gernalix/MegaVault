# chatgpt-chrome-debug Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `scripts/common.sh`: ts, safe_name, mkdirs, chrome_bin, log_line
- `scripts/live_chrome_logger.sh`: is_running, start_logger, run_foreground, stop_logger, status_logger
- `scripts/monitor_chatgpt_tab.js`: arg, ts, mkdirp, appendJSONL, isChatGPTHome, isConversation, stableString, safeEvaluate
- `scripts/run_differential_tests.sh`: run_case
- `package.json`: build

## Confini operativi
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
