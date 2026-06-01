# chatgpt-chrome-debug AI OPERATIONS

PROJECT
- name: chatgpt-chrome-debug
- slug: chatgpt-chrome-debug
- purpose: ChatGPT Chrome Redirect Debug Toolkit
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/chatgpt-chrome-debug`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `fdd3773` / `2026-06-01T13:20:29+02:00`

STACK
- languages: JavaScript/TypeScript, Python, Shell
- frameworks: Node/npm, playwright
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- `package.json`
important_folders:
- `dev`
- `scripts`
important_files:
- `package.json`
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `START_DEBUGGING.sh`
- `scripts/common.sh`
- `scripts/dashboard.sh`
- `scripts/install_user_services.sh`
- `scripts/live_chrome_logger.sh`
- `scripts/run_differential_tests.sh`
- `scripts/snapshot_environment.sh`
- `scripts/stress_memory.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `node_modules`

ARCH
summary:
- dev/legacy/README.md: # ChatGPT Chrome Redirect Debug Toolkit
- dev/legacy/KNOWN_PATTERNS.md: Pattern da riconoscere nei log:
- dev/legacy/QUICK_FIXES.md: Applicare solo dopo avere raccolto almeno uno snapshot di redirect.
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`.
- package.json: "name": "chatgpt-chrome-debug",
- START_DEBUGGING.sh: ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
- scripts/common.sh: ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
- scripts/dashboard.sh: source "$(dirname "$0")/common.sh"
- scripts/install_user_services.sh: source "$(dirname "$0")/common.sh"
- scripts/live_chrome_logger.sh: source "$(dirname "$0")/common.sh"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # ChatGPT Chrome Redirect Debug Toolkit |
| `dev/legacy/KNOWN_PATTERNS.md` | # Known Patterns |
| `dev/legacy/QUICK_FIXES.md` | # Quick Fixes |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | # Root Cause Analysis |
| `START_DEBUGGING.sh` | #!/usr/bin/env bash |
| `scripts/common.sh` | #!/usr/bin/env bash |
| `scripts/dashboard.sh` | #!/usr/bin/env bash |
| `scripts/install_user_services.sh` | #!/usr/bin/env bash |
| `scripts/install_user_services.sh` | UNIT |
| `scripts/live_chrome_logger.sh` | #!/usr/bin/env bash |
| `scripts/run_differential_tests.sh` | #!/usr/bin/env bash |
| `scripts/snapshot_environment.sh` | #!/usr/bin/env bash |
| `scripts/snapshot_environment.sh` | SUMMARY |
| `scripts/stress_memory.py` | #!/usr/bin/env python3 |
| `dev/legacy/KNOWN_PATTERNS.md` | Pattern da riconoscere nei log: |
| `dev/legacy/QUICK_FIXES.md` | Applicare solo dopo avere raccolto almeno uno snapshot di redirect. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`. |
| `package.json` | "name": "chatgpt-chrome-debug", |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - non modifica il profilo Chrome reale; |
| `dev/legacy/README.md` | - ogni script e' restart-safe e puo' appendere a log esistenti. |
| `dev/legacy/README.md` | Per test brevi non invasivi: |
| `dev/legacy/KNOWN_PATTERNS.md` | - redirect solo nel profilo reale, non nel profilo pulito: estensioni, cookie, IndexedDB, localStorage, service worker o impostazioni profilo. |
| `dev/legacy/KNOWN_PATTERNS.md` | I log non contengono volontariamente token stampati in chiaro. Cookie e storage sono salvati in file locali sotto `diagnostics/redirect_events/`; trattarli come sensibili. |
| `dev/legacy/QUICK_FIXES.md` | - Non farla prima delle prove. |
| `dev/legacy/QUICK_FIXES.md` | - Fare backup del profilo. |
| `dev/legacy/QUICK_FIXES.md` | - Se profilo pulito non riproduce: isolare estensione/storage/cookie/service worker nel profilo reale. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Probe rete: `curl -4 -I https://chatgpt.com/` riceve Cloudflare challenge `HTTP/2 403`; `curl -6` fallisce connessione. Questo prova una differenza IPv4/IPv6 nei probe CLI, non prova da solo un problema nel browser reale. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Smoke test con profilo isolato headless: non ha riprodotto redirect da conversazione perche' non era autenticato e non era su URL `/c/...`; ha comunque prodotto HAR, screenshot, HTML, storage, cookie e heartbeat in `diagnos |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove a favore: problema riferito dentro il profilo reale; il profilo isolato non e' sufficiente a riprodurre perche' non autenticato. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Fix temporaneo: usare profilo Chrome isolato pulito o rimuovere solo dati sito OpenAI/ChatGPT dopo backup. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Nota: uBlock Origin Lite e Ghostery risultano presenti; il fatto che siano state disattivate non elimina la superficie delle altre estensioni. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove a favore: plausibile per web app ChatGPT, non ancora osservato nello smoke test isolato. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove contro: lo smoke test browser isolato non ha mostrato `requestfailed`, ma non era una sessione reale. |
| `package.json` | "version": "0.1.0", |
| `scripts/dashboard.sh` | echo "monitor non ancora avviato" |
| `scripts/snapshot_environment.sh` | "$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true |
| `scripts/snapshot_environment.sh` | echo "== chrome://version via isolated headless profile ==" |
| `scripts/snapshot_environment.sh` | --dump-dom chrome://version 2>&1 // true |
| `scripts/snapshot_environment.sh` | (.value.manifest.version // "unknown"), |
| `scripts/snapshot_environment.sh` | echo "id name version state active_bit disable_reasons api_permissions explicit_hosts scriptable_hosts" |

BUILD_TEST
build_files:
- `package.json`
commands_found:
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
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: - Fix temporaneo: test su rete alternativa, IPv4-only se emergono failure IPv6, disabilitare VPN/proxy se presenti.
- scripts/run_differential_tests.sh: stress-ng --vm 1 --vm-bytes 55% --timeout "$DURATION" --metrics-brief > "$OUT/${name}_stress.log" 2>&1 &

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `package.json` | "version": "0.1.0", |
| `scripts/snapshot_environment.sh` | "$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true |
| `scripts/snapshot_environment.sh` | echo "== chrome://version via isolated headless profile ==" |
| `scripts/snapshot_environment.sh` | --dump-dom chrome://version 2>&1 // true |
| `scripts/snapshot_environment.sh` | (.value.manifest.version // "unknown"), |
| `scripts/snapshot_environment.sh` | echo "id name version state active_bit disable_reasons api_permissions explicit_hosts scriptable_hosts" |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - ogni script e' restart-safe e puo' appendere a log esistenti. |
| `dev/legacy/KNOWN_PATTERNS.md` | - redirect solo nel profilo reale, non nel profilo pulito: estensioni, cookie, IndexedDB, localStorage, service worker o impostazioni profilo. |
| `dev/legacy/KNOWN_PATTERNS.md` | I log non contengono volontariamente token stampati in chiaro. Cookie e storage sono salvati in file locali sotto `diagnostics/redirect_events/`; trattarli come sensibili. |
| `dev/legacy/QUICK_FIXES.md` | - Fare backup del profilo. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Fix temporaneo: usare profilo Chrome isolato pulito o rimuovere solo dati sito OpenAI/ChatGPT dopo backup. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Nota: uBlock Origin Lite e Ghostery risultano presenti; il fatto che siano state disattivate non elimina la superficie delle altre estensioni. |
| `scripts/snapshot_environment.sh` | echo "id name version state active_bit disable_reasons api_permissions explicit_hosts scriptable_hosts" |
| `scripts/install_user_services.sh` | systemctl --user enable --now chatgpt-chrome-live-logger.service |
| `scripts/install_user_services.sh` | systemctl --user status --no-pager chatgpt-chrome-live-logger.service // true |
| `scripts/live_chrome_logger.sh` | #!/usr/bin/env bash |
| `scripts/live_chrome_logger.sh` | journalctl -f -o short-iso 2>/dev/null / grep --line-buffered -Ei 'chrome/chromium/oom/out of memory/renderer/gpu/drm/i915/mesa/xid/segfault/crash/discard/network/websocket/suspend/resume' >> "$LOG_DIR/journal_chrome.log" & |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Prove mancanti: correlazione temporale fra redirect e nuovo dump, evento `page-crash`, journal o `chrome_process_snapshots.log`. |
| `dev/legacy/ROOT_CAUSE_ANALYSIS.md` | - Fix definitivo: tuning memoria/swap solo se i log mostrano OOM/discard/crash. |
| `scripts/dashboard.sh` | grep -Eih 'renderer/crash/segfault/oom/out of memory/gpu reset/discard' "$DIAG_DIR/live/"*.log 2>/dev/null / tail -8 // true |
| `scripts/live_chrome_logger.sh` | tail -Fn0 /var/log/syslog 2>/dev/null / grep --line-buffered -Ei 'chrome/chromium/oom/renderer/gpu/segfault/crash/suspend/resume' >> "$LOG_DIR/syslog_chrome.log" & |
| `scripts/live_chrome_logger.sh` | find "$HOME/.config/google-chrome" "$HOME/.cache/google-chrome" -maxdepth 4 \( -iname '*crash*' -o -iname '*.dmp' \) -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null / sort / tail -50 // true |
| `scripts/run_differential_tests.sh` | stress-ng --vm 1 --vm-bytes 55% --timeout "$DURATION" --metrics-brief > "$OUT/${name}_stress.log" 2>&1 & |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
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

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: - ogni script e' restart-safe e puo' appendere a log esistenti.
- dev/legacy/QUICK_FIXES.md: - Fare backup del profilo.
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: - Fix temporaneo: usare profilo Chrome isolato pulito o rimuovere solo dati sito OpenAI/ChatGPT dopo backup.
- package.json: "version": "0.1.0",
- scripts/snapshot_environment.sh: "$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 // true
- scripts/snapshot_environment.sh: echo "== chrome://version via isolated headless profile =="
- scripts/snapshot_environment.sh: --dump-dom chrome://version 2>&1 // true
- scripts/snapshot_environment.sh: (.value.manifest.version // "unknown"),
- scripts/snapshot_environment.sh: echo "id name version state active_bit disable_reasons api_permissions explicit_hosts scriptable_hosts"

RECENT_DECISIONS
| source | fact |
|---|---|
| `UNKNOWN` | no verified recent decisions found in read sources. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `UNKNOWN` | no verified roadmap found in read sources. |

LEGACY_SUMMARY
- legacy_docs_read_count: 17
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/KNOWN_PATTERNS.md`
- `dev/legacy/QUICK_FIXES.md`
- `dev/legacy/ROOT_CAUSE_ANALYSIS.md`
- `dev/legacy/diagnostics/environment/snapshot_20260510_223934/chrome_version.txt`
- `dev/legacy/diagnostics/environment/snapshot_20260510_224516/chrome_version.txt`
- `dev/legacy/diagnostics/environment/snapshot_20260510_224657/chrome_version.txt`
- `package.json`
- `START_DEBUGGING.sh`
- `scripts/common.sh`
- `scripts/dashboard.sh`
- `scripts/install_user_services.sh`
- `scripts/live_chrome_logger.sh`
- `scripts/run_differential_tests.sh`
- `scripts/snapshot_environment.sh`
- `scripts/stress_memory.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../chatgpt-chrome-debug/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/chatgpt-chrome-debug/overview.md)
- human_folder: [human folder](../../human/projects/chatgpt-chrome-debug)
- legacy_docs: [dev/legacy](../../../chatgpt-chrome-debug/dev/legacy)
- repo_path: [repo](../../../chatgpt-chrome-debug)

OPEN_QUESTIONS
- none detected in extracted sources
