# android-sdk-auto-update Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: In modalità `--check` o `--check-only`, se trova la sezione `Available Updates` la notifica come check-only senza installare. Non usa l’elenco generico `Available Packages`, perché include anche pacchetti non insta
- dev/legacy/TROUBLESHOOTING.md: java -version
- dev/legacy/OPERATIONS.md: Rimozione reale, solo del package SDK `emulator`; non cancella AVD o system-images:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Use the existing installed tool; do not create a duplicate:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Remove only the SDK package `emulator`, never AVDs or system-images:
- dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md: La rimozione controllata riguarda solo il package SDK `emulator` e non cancella AVD o immagini di sistema:
- android_sdk_auto_update.sh: --check Safe default. List installed packages and available SDK updates only.
- android_sdk_auto_update.sh: This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh: What it never does:
- android_sdk_auto_update.sh: COMMIT;"
- android_sdk_auto_update.sh: local timestamp package version size_bytes
- android_sdk_auto_update.sh: while IFS=$'\t' read -r package version; do
- android_sdk_auto_update.sh: append_history "$timestamp" "$package" "$version" "$version" "CHECK" "$size_bytes" 0 0 "$SDK_ROOT"
- android_sdk_auto_update.sh: info "sdkmanager version: $("$SDKMANAGER" --version 2>>"$LOG_FILE" // true)"
