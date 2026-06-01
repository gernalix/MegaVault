# chatgpt-chrome-debug Roadmap

## Segnali dal codice
- no tests detected by static scan

## Debito/rischi da considerare
- scripts/snapshot_environment.sh:2:set -euo pipefail
- scripts/snapshot_environment.sh:138:echo "== chrome crash directories =="
- scripts/snapshot_environment.sh:139:find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -iname '*crash*' -o -iname '*.dmp' \) -printf '%TY-%Tm-%Td %TH:%T
- scripts/snapshot_environment.sh:142:journalctl --user --since '-24 hours' 2>/dev/null / grep -Ei 'chrome/chromium/gpu/oom/renderer/crash' / tail -200 // true
- scripts/snapshot_environment.sh:143:} > "$OUT/crash_and_logs.txt"
- dev/project.metadata.json:2:"project_name": "chatgpt-chrome-debug",
- dev/project.metadata.json:3:"project_slug": "chatgpt-chrome-debug",
- dev/project.metadata.json:4:"project_root": "~/cw/chatgpt-chrome-debug",
- scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // [])) / tostring) / test("tabs/webRequest/webNavigation/scripting/sto
- scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") / ascii_downcase) / test("chatgpt/refresh/tab/cookie/script/style/monitor/ghostery/ublock"))
- scripts/snapshot_environment.sh:149:curl -4 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cookie:).*/\1 [redacted]/Ig' // true
- scripts/snapshot_environment.sh:150:curl -6 -I --max-time 15 https://chatgpt.com/ 2>&1 / sed -E 's/(cookie:/set-cookie:).*/\1 [redacted]/Ig' // true
- package-lock.json:4:"lockfileVersion": 3,
- scripts/live_chrome_logger.sh:12:[[ -r "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
