# android-sdk-auto-update AI OPERATIONS

PROJECT
- name: android-sdk-auto-update
- slug: android-sdk-auto-update
- purpose: Servizio giornaliero per aggiornare i pacchetti Android SDK gestiti da `sdkmanager` su Linux Mint/Ubuntu.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/android-sdk-auto-update`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `7d6a23b` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- UNKNOWN
important_folders:
- `dev`
- `logs`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `android_sdk_auto_update.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `logs`

ARCH
summary:
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: Servizio giornaliero per aggiornare i pacchetti Android SDK gestiti da `sdkmanager` su Linux Mint/Ubuntu.
- dev/legacy/TROUBLESHOOTING.md: ls -l ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
- dev/legacy/OPERATIONS.md: /home/daniele/bin/android_sdk_auto_update.sh --install --yes
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Use the existing installed tool; do not create a duplicate:
- dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md: Lo script gia installato per gli aggiornamenti Android SDK generici e:
- android_sdk_auto_update.sh: APP_NAME="android-sdk-auto-update"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | # Android SDK Auto Update |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Cosa aggiorna |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Cosa non aggiorna |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## File principali |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Scelta user service |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Rilevamento SDK |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Comandi |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Telegram |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Stati notificati |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Storico SQLite/CSV |
| `dev/legacy/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/TROUBLESHOOTING.md` | ## sdkmanager non trovato |
| `dev/legacy/TROUBLESHOOTING.md` | ## ANDROID_SDK_ROOT mancante |
| `dev/legacy/TROUBLESHOOTING.md` | ## Licenze mancanti |
| `dev/legacy/TROUBLESHOOTING.md` | ## Rete assente |
| `dev/legacy/TROUBLESHOOTING.md` | ## Permessi insufficienti |
| `dev/legacy/TROUBLESHOOTING.md` | ## Java mancante o incompatibile |
| `dev/legacy/TROUBLESHOOTING.md` | ## Build Android in corso |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | ## Cosa non aggiorna |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | - Pacchetti vecchi/obsoleti da rimuovere: lo script non cancella nulla senza autorizzazione esplicita. |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | - AVD, system-images e cache: non vengono cancellati automaticamente. |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | È stato scelto un servizio `systemd --user` perché l’SDK rilevato è nella home di `daniele` (`~/Android/Sdk`) e gli aggiornamenti SDK non richiedono privilegi root. Questo riduce i rischi sui permessi e salva log n |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | Lo script non contiene token o chat id. Carica variabili da: |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | Se l’helper fallisce o non è disponibile, usa `curl` come fallback. |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | - `ERROR`: errore, lock già attivo, SDK non trovato, `sdkmanager` fallito, rete assente, build Android/Gradle già in corso. |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | In modalità `--check` o `--check-only`, se trova la sezione `Available Updates` la notifica come check-only senza installare. Non usa l’elenco generico `Available Packages`, perché include anche pacchetti non insta |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | Lo schema SQLite viene creato automaticamente con indice su `timestamp_utc`. Il CSV crea l’header se manca ed è append-only. |
| `dev/legacy/TROUBLESHOOTING.md` | ## sdkmanager non trovato |
| `dev/legacy/TROUBLESHOOTING.md` | Sintomi tipici: errori HTTPS, timeout, repository XML non scaricabile. Verificare: |
| `dev/legacy/TROUBLESHOOTING.md` | java -version |
| `dev/legacy/TROUBLESHOOTING.md` | ## Notifica Telegram non inviata |
| `dev/legacy/OPERATIONS.md` | Nota: non esiste una vera simulazione completa di `sdkmanager --update`. Lo script usa `sdkmanager --list` e considera aggiornamenti solo la sezione `Available Updates`, quando presente; `--check` controlla e notifica, ma non prova do |
| `dev/legacy/OPERATIONS.md` | Rimozione reale, solo del package SDK `emulator`; non cancella AVD o system-images: |
| `dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md` | Use the existing installed tool; do not create a duplicate: |
| `dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md` | Remove only the SDK package `emulator`, never AVDs or system-images: |
| `dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md` | La rimozione controllata riguarda solo il package SDK `emulator` e non cancella AVD o immagini di sistema: |
| `dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md` | Questo tool non aggiorna roadmap o file interni di app Android come MultiTimeTracker o SuperContacts. |
| `android_sdk_auto_update.sh` | --check Safe default. List installed packages and available SDK updates only. |
| `android_sdk_auto_update.sh` | This never deletes AVDs, system images, SDK cache, or the SDK root. |
| `android_sdk_auto_update.sh` | What it never does: |
| `android_sdk_auto_update.sh` | id INTEGER PRIMARY KEY AUTOINCREMENT, |
| `android_sdk_auto_update.sh` | COMMIT;" |
| `android_sdk_auto_update.sh` | timeout --preserve-status "$timeout_seconds" "$@" |
| `android_sdk_auto_update.sh` | local timestamp package version size_bytes |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user status android-sdk-auto-update.timer |
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user list-timers android-sdk-auto-update.timer |
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) journalctl --user -u android-sdk-auto-update.service -n 80 --no-pager |
| `dev/legacy/OPERATIONS.md` | sqlite3 /home/daniele/codex-workspace/android-sdk-auto-update/logs/android_updates_history.sqlite \ |
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user disable --now android-sdk-auto-update.timer |
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user daemon-reload |
| `dev/legacy/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user enable --now android-sdk-auto-update.timer |
| `dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md` | sqlite3 /home/daniele/codex-workspace/android-sdk-auto-update/logs/android_updates_history.sqlite \ |
| `android_sdk_auto_update.sh` | #!/usr/bin/env bash |
| `android_sdk_auto_update.sh` | if command -v sqlite3 >/dev/null 2>&1; then |
| `android_sdk_auto_update.sh` | sqlite3 "$SQLITE_FILE" >/dev/null <<'SQL' |
| `android_sdk_auto_update.sh` | sqlite3 "$SQLITE_FILE" "BEGIN IMMEDIATE; |
| `android_sdk_auto_update.sh` | if [[ -x "$TELEGRAM_HELPER_DEFAULT" ]] && command -v python3 >/dev/null 2>&1; then |
| `android_sdk_auto_update.sh` | if python3 "$TELEGRAM_HELPER_DEFAULT" "$title" "$message" >>"$LOG_FILE" 2>&1; then |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: - `ERROR`: errore, lock già attivo, SDK non trovato, `sdkmanager` fallito, rete assente, build Android/Gradle già in corso.
- dev/legacy/TROUBLESHOOTING.md: Sintomi tipici: errori HTTPS, timeout, repository XML non scaricabile. Verificare:
- android_sdk_auto_update.sh: timeout --preserve-status "$timeout_seconds" "$@"
- android_sdk_auto_update.sh: if ! command -v timeout >/dev/null 2>&1; then
- android_sdk_auto_update.sh: SUMMARY="timeout command not found"

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/TROUBLESHOOTING.md` | java -version |
| `android_sdk_auto_update.sh` | COMMIT;" |
| `android_sdk_auto_update.sh` | local timestamp package version size_bytes |
| `android_sdk_auto_update.sh` | while IFS=$'\t' read -r package version; do |
| `android_sdk_auto_update.sh` | append_history "$timestamp" "$package" "$version" "$version" "CHECK" "$size_bytes" 0 0 "$SDK_ROOT" |
| `android_sdk_auto_update.sh` | info "sdkmanager version: $("$SDKMANAGER" --version 2>>"$LOG_FILE" // true)" |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | È stato scelto un servizio `systemd --user` perché l’SDK rilevato è nella home di `daniele` (`~/Android/Sdk`) e gli aggiornamenti SDK non richiedono privilegi root. Questo riduce i rischi sui permessi e salva log n |
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | Lo schema SQLite viene creato automaticamente con indice su `timestamp_utc`. Il CSV crea l’header se manca ed è append-only. |
| `android_sdk_auto_update.sh` | info "sdkmanager version: $("$SDKMANAGER" --version 2>>"$LOG_FILE" // true)" |
| `dev/legacy/OPERATIONS.md` | sqlite3 /home/daniele/codex-workspace/android-sdk-auto-update/logs/android_updates_history.sqlite \ |
| `dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md` | sqlite3 /home/daniele/codex-workspace/android-sdk-auto-update/logs/android_updates_history.sqlite \ |
| `android_sdk_auto_update.sh` | if command -v sqlite3 >/dev/null 2>&1; then |
| `android_sdk_auto_update.sh` | sqlite3 "$SQLITE_FILE" >/dev/null <<'SQL' |
| `android_sdk_auto_update.sh` | sqlite3 "$SQLITE_FILE" "BEGIN IMMEDIATE; |
| `android_sdk_auto_update.sh` | if python3 "$TELEGRAM_HELPER_DEFAULT" "$title" "$message" >>"$LOG_FILE" 2>&1; then |
| `android_sdk_auto_update.sh` | error() { log "ERROR" "$*"; } |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md` | - `ERROR`: errore, lock già attivo, SDK non trovato, `sdkmanager` fallito, rete assente, build Android/Gradle già in corso. |
| `dev/legacy/TROUBLESHOOTING.md` | Sintomi tipici: errori HTTPS, timeout, repository XML non scaricabile. Verificare: |
| `android_sdk_auto_update.sh` | STATUS="ERROR" |
| `android_sdk_auto_update.sh` | error() { log "ERROR" "$*"; } |
| `android_sdk_auto_update.sh` | if curl --fail --silent --show-error --max-time 20 \ |
| `android_sdk_auto_update.sh` | timeout --preserve-status "$timeout_seconds" "$@" |
| `android_sdk_auto_update.sh` | error "--install requires --yes for real SDK changes" |
| `android_sdk_auto_update.sh` | error "--remove-emulator requires --yes for real SDK changes" |
| `android_sdk_auto_update.sh` | final_report "Android SDK auto update: ERROR" "$SUMMARY" |
| `android_sdk_auto_update.sh` | if ! command -v timeout >/dev/null 2>&1; then |
| `android_sdk_auto_update.sh` | SUMMARY="timeout command not found" |
| `android_sdk_auto_update.sh` | error "Unsupported mode: $MODE" |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: In modalità `--check` o `--check-only`, se trova la sezione `Available Updates` la notifica come check-only senza installare. Non usa l’elenco generico `Available Packages`, perché include anche pacchetti non insta
- dev/legacy/TROUBLESHOOTING.md: java -version
- dev/legacy/OPERATIONS.md: Rimozione reale, solo del package SDK `emulator`; non cancella AVD o system-images:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Use the existing installed tool; do not create a duplicate:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Remove only the SDK package `emulator`, never AVDs or system-images:
- dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md: La rimozione controllata riguarda solo il package SDK `emulator` e non cancella AVD o immagini di sistema:
- android_sdk_auto_update.sh: --check Safe default. List installed packages and available SDK updates only.
- android_sdk_auto_update.sh: This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh: What it never does:
- android_sdk_auto_update.sh: timeout --preserve-status "$timeout_seconds" "$@"
- android_sdk_auto_update.sh: local timestamp package version size_bytes
- android_sdk_auto_update.sh: while IFS=$'\t' read -r package version; do
- android_sdk_auto_update.sh: append_history "$timestamp" "$package" "$version" "$version" "CHECK" "$size_bytes" 0 0 "$SDK_ROOT"
- android_sdk_auto_update.sh: SUMMARY="Android/Gradle/sdkmanager process already running; skipped to avoid disturbing builds"
- android_sdk_auto_update.sh: info "sdkmanager version: $("$SDKMANAGER" --version 2>>"$LOG_FILE" // true)"

RECENT_DECISIONS
| source | fact |
|---|---|
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; next } |
| `android_sdk_auto_update.sh` | /^Installed packages:/ // /^Installed Packages:/ { in_installed=1; next } |
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; print; next } |
| `android_sdk_auto_update.sh` | info "Accepting pending Android SDK licenses non-interactively" |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md` | Questo tool non aggiorna roadmap o file interni di app Android come MultiTimeTracker o SuperContacts. |
| `android_sdk_auto_update.sh` | --dry-run Show and log the planned mutation without installing/removing. |
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; next } |
| `android_sdk_auto_update.sh` | /^Installed packages:/ // /^Installed Packages:/ { in_installed=1; next } |
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; print; next } |
| `android_sdk_auto_update.sh` | info "Accepting pending Android SDK licenses non-interactively" |

LEGACY_SUMMARY
- legacy_docs_read_count: 7
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md`
- `dev/legacy/TROUBLESHOOTING.md`
- `dev/legacy/OPERATIONS.md`
- `dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md`
- `dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md`
- `android_sdk_auto_update.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../android-sdk-auto-update/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/android-sdk-auto-update/overview.md)
- human_folder: [human folder](../../human/projects/android-sdk-auto-update)
- legacy_docs: [dev/legacy](../../../android-sdk-auto-update/dev/legacy)
- repo_path: [repo](../../../android-sdk-auto-update)

OPEN_QUESTIONS
- none detected in extracted sources
