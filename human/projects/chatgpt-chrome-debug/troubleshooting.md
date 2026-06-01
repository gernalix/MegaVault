# chatgpt-chrome-debug Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/KNOWN_PATTERNS.md` | # Known Patterns |
| `dev/legacy/QUICK_FIXES.md` | - Se Chromium e Chrome differiscono: pin/upgrade/downgrade browser o riportare bug con HAR e crash dump. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | # Root Cause Analysis |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Crash dump Chrome recenti presenti in `~/.config/google-chrome/Crash Reports/completed/`, inclusi dump del 2026-05-10 alle 08:37, 10:09, 12:55, 12:58 e 14:17. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | 3. Crash renderer/Chrome o tab reload causato da crashpad |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Motivo: esistono crash dump Chrome nello stesso giorno del problema; un renderer riavviato puo' far perdere lo stato della conversazione e tornare alla home. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove a favore: crash dump multipli il 2026-05-10. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove mancanti: correlazione temporale fra redirect e nuovo dump, evento `page-crash`, journal o `chrome_process_snapshots.log`. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Fix temporaneo: test su rete alternativa, IPv4-only se emergono failure IPv6, disabilitare VPN/proxy se presenti. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Fix definitivo: tuning memoria/swap solo se i log mostrano OOM/discard/crash. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Motivo: reset GPU o crash renderer puo' causare reload. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | 8. Bug Chrome/Linux Mint/XFCE, sleep/resume o refresh automatico lato sito |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Motivo: meno probabile senza evidenza di suspend/resume o crash globale. |
| `scripts/dashboard.sh` | echo "== Chrome renderer/crash signals ==" |
| `scripts/dashboard.sh` | grep -Eih 'renderer/crash/segfault/oom/out of memory/gpu reset/discard' "$DIAG_DIR/live/"*.log 2>/dev/null / tail -8 // true |
| `scripts/dashboard.sh` | select(.event=="heartbeat" or .event=="navigation" or .event=="websocket-close" or .event=="websocket-error" or .event=="console") |
| `scripts/dashboard.sh` | / [.ts, .event, (.url // .to // .text // .error // "")] / @tsv |
| `scripts/live_chrome_logger.sh` | journalctl -f -o short-iso 2>/dev/null / grep --line-buffered -Ei 'chrome/chromium/oom/out of memory/renderer/gpu/drm/i915/mesa/xid/segfault/crash/discard/network/websocket/suspend/resume' >> "$LOG_DIR/journal_chrome.log" & |
| `scripts/live_chrome_logger.sh` | tail -Fn0 /var/log/syslog 2>/dev/null / grep --line-buffered -Ei 'chrome/chromium/oom/renderer/gpu/segfault/crash/suspend/resume' >> "$LOG_DIR/syslog_chrome.log" & |
| `scripts/live_chrome_logger.sh` | find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -iname '*crash*' -o -iname '*.dmp' \) -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null / sort / tail -50 // true |
| `scripts/run_differential_tests.sh` | stress-ng --vm 1 --vm-bytes 55% --timeout "$DURATION" --metrics-brief > "$OUT/${name}_stress.log" 2>&1 & |
| `scripts/snapshot_environment.sh` | echo "== chrome crash directories ==" |
| `scripts/snapshot_environment.sh` | find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -iname '*crash*' -o -iname '*.dmp' \) -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null / sort // true |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/README.md` | npm install |
| `dev/legacy/README.md` | npm run monitor -- --url https://chatgpt.com/ |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | npm run monitor -- --url='https://chatgpt.com/c/ID_CONVERSAZIONE' --profile=manual_debug |
| `START_DEBUGGING.sh` | #!/usr/bin/env bash |
| `START_DEBUGGING.sh` | npm install |
| `START_DEBUGGING.sh` | exec npm run monitor -- --url="${CHATGPT_URL:-https://chatgpt.com/}" --profile="${CHATGPT_PROFILE:-manual_debug}" |
| `scripts/common.sh` | #!/usr/bin/env bash |
| `scripts/dashboard.sh` | #!/usr/bin/env bash |
| `scripts/install_user_services.sh` | #!/usr/bin/env bash |
| `scripts/install_user_services.sh` | systemctl --user daemon-reload |
| `scripts/install_user_services.sh` | systemctl --user enable --now chatgpt-chrome-live-logger.service |
| `scripts/install_user_services.sh` | systemctl --user status --no-pager chatgpt-chrome-live-logger.service // true |
| `scripts/live_chrome_logger.sh` | #!/usr/bin/env bash |
| `scripts/live_chrome_logger.sh` | journalctl -f -o short-iso 2>/dev/null / grep --line-buffered -Ei 'chrome/chromium/oom/out of memory/renderer/gpu/drm/i915/mesa/xid/segfault/crash/discard/network/websocket/suspend/resume' >> "$LOG_DIR/journal_chrome.log" & |
| `scripts/run_differential_tests.sh` | #!/usr/bin/env bash |
| `scripts/snapshot_environment.sh` | #!/usr/bin/env bash |
| `scripts/snapshot_environment.sh` | journalctl --user --since '-24 hours' 2>/dev/null / grep -Ei 'chrome/chromium/gpu/oom/renderer/crash' / tail -200 // true |
| `scripts/stress_memory.py` | #!/usr/bin/env python3 |

## Safety Checks Before Fixing
- dev/legacy/README.md: - ogni script e' restart-safe e puo' appendere a log esistenti.
- dev/legacy/QUICK_FIXES.md: - Fare backup del profilo.
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: - Fix temporaneo: usare profilo Chrome isolato pulito o rimuovere solo dati sito OpenAI/ChatGPT dopo backup.
- package.json: "version": "0.1.0",
- scripts/snapshot_environment.sh: "$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
- scripts/snapshot_environment.sh: echo "== chrome://version via isolated headless profile =="
- scripts/snapshot_environment.sh: --dump-dom chrome://version 2>&1 // true
- scripts/snapshot_environment.sh: (.value.manifest.version // "unknown"),
- scripts/snapshot_environment.sh: echo "id name version state active_bit disable_reasons api_permissions explicit_hosts scriptable_hosts"
