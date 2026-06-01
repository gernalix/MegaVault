META:
name=android-sdk-auto-update
slug=android-sdk-auto-update
path=/home/daniele/codex-workspace/android-sdk-auto-update
remote=none
branch=master
verified_commit=7d6a23b
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Servizio giornaliero per aggiornare i pacchetti Android SDK gestiti da `sdkmanager` su Linux Mint/Ubuntu.
STACK:
lang=Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=UNKNOWN
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=android_sdk_auto_update.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- android_sdk_auto_update.sh:49:--run Backward-compatible alias for "--install --yes" used by the user timer.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
- android_sdk_auto_update.sh:114:export "$key=$value"
- android_sdk_auto_update.sh:207:send_telegram() {
- android_sdk_auto_update.sh:242:"https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" >>"$LOG_FILE" 2>&1; t
- android_sdk_auto_update.sh:436:local update_count start end exit_status timestamp package old_version new_version si
FLOW:
- android_sdk_auto_update.sh:49:--run Backward-compatible alias for "--install --yes" used by the user timer.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
- android_sdk_auto_update.sh:114:export "$key=$value"
- android_sdk_auto_update.sh:207:send_telegram() {
- android_sdk_auto_update.sh:242:"https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" >>"$LOG_FILE" 2>&1; t
- android_sdk_auto_update.sh:436:local update_count start end exit_status timestamp package old_version new_version si
- android_sdk_auto_update.sh:467:start="$(epoch_now)"
- android_sdk_auto_update.sh:483:append_history "$timestamp" "$package" "$old_version" "$new_version" "$operation" "$s
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
arch=android_sdk_auto_update.sh:16:RUN_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_TIMEOUT_SECONDS:-3600}"
arch=android_sdk_auto_update.sh:17:SDKMANAGER_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_SDKMANAGER_TIMEOUT_SECONDS:-
arch=android_sdk_auto_update.sh:23:DRY_RUN=0
arch=android_sdk_auto_update.sh:37:android_sdk_auto_update.sh [--check] [--dry-run]
data=android_sdk_auto_update.sh:11:SQLITE_FILE="$HISTORY_DIR/android_updates_history.sqlite"
data=android_sdk_auto_update.sh:64:SQLite: logs/android_updates_history.sqlite
safety=android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
safety=android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
safety=android_sdk_auto_update.sh:45:--remove-emulator Remove only the Android SDK package named "emulator".
safety=android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
safety=android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
safety=android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
safety=android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- android_sdk_auto_update.sh:1:#!/usr/bin/env bash
- android_sdk_auto_update.sh:37:android_sdk_auto_update.sh [--check] [--dry-run]
- android_sdk_auto_update.sh:38:android_sdk_auto_update.sh --install --yes [--dry-run]
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:40:android_sdk_auto_update.sh --test-telegram
- android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets
- android_sdk_auto_update.sh:142:if command -v sqlite3 >/dev/null 2>&1; then
- android_sdk_auto_update.sh:143:sqlite3 "$SQLITE_FILE" >/dev/null <<'SQL'
TEST:
- UNKNOWN
DATA:
db=android_sdk_auto_update.sh:10:CSV_FILE="$HISTORY_DIR/android_updates_history.csv"
db=android_sdk_auto_update.sh:11:SQLITE_FILE="$HISTORY_DIR/android_updates_history.sqlite"
db=android_sdk_auto_update.sh:64:SQLite: logs/android_updates_history.sqlite
db=android_sdk_auto_update.sh:65:CSV: logs/android_updates_history.csv
backup=UNKNOWN
import=UNKNOWN
export=android_sdk_auto_update.sh:114:export "$key=$value"
migration=UNKNOWN
retention=android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
retention=android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
retention=android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save sec
DNB:
- android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:45:--remove-emulator Remove only the Android SDK package named "emulator".
- android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
- android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
- android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets
- dev/project.metadata.json:9:"metadata_version": 1,
- android_sdk_auto_update.sh:23:DRY_RUN=0
BUG:
- android_sdk_auto_update.sh:3:set -Eeuo pipefail
- android_sdk_auto_update.sh:16:RUN_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_TIMEOUT_SECONDS:-3600}"
- android_sdk_auto_update.sh:17:SDKMANAGER_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_SDKMANAGER_TIMEOUT_SECONDS:-1800
- android_sdk_auto_update.sh:25:STATUS="ERROR"
- android_sdk_auto_update.sh:71:error() { log "ERROR" "$*"; }
- android_sdk_auto_update.sh:224:warn "Telegram helper failed, trying curl fallback"
- android_sdk_auto_update.sh:238:if curl --fail --silent --show-error --max-time 20 \
- android_sdk_auto_update.sh:246:warn "Telegram curl fallback failed"
RISK:
- android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:45:--remove-emulator Remove only the Android SDK package named "emulator".
- android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
- android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
- android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets
ROAD:
now=android_sdk_auto_update.sh:354:/^Available Updates:/ { in_updates=1; next }
next=android_sdk_auto_update.sh:371:/^Installed packages:/ // /^Installed Packages:/ { in_installed=1; next }
later=android_sdk_auto_update.sh:387:/^Available Updates:/ { in_updates=1; print; next }
LINK:
meta=../../../android-sdk-auto-update/dev/project.metadata.json
human=../../human/projects/android-sdk-auto-update/overview.md
legacy=../../../android-sdk-auto-update/dev/legacy
repo=../../../android-sdk-auto-update
OPEN:
- no tests detected by static scan
