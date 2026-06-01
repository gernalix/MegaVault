# android-sdk-auto-update Troubleshooting

## Problemi e sintomi rilevati nel codice
- android_sdk_auto_update.sh:3:set -Eeuo pipefail
- android_sdk_auto_update.sh:16:RUN_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_TIMEOUT_SECONDS:-3600}"
- android_sdk_auto_update.sh:17:SDKMANAGER_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_SDKMANAGER_TIMEOUT_SECONDS:-1800}"
- android_sdk_auto_update.sh:25:STATUS="ERROR"
- android_sdk_auto_update.sh:71:error() { log "ERROR" "$*"; }
- android_sdk_auto_update.sh:224:warn "Telegram helper failed, trying curl fallback"
- android_sdk_auto_update.sh:238:if curl --fail --silent --show-error --max-time 20 \
- android_sdk_auto_update.sh:246:warn "Telegram curl fallback failed"

## Comandi/verifiche utili trovati
- android_sdk_auto_update.sh:1:#!/usr/bin/env bash
- android_sdk_auto_update.sh:37:android_sdk_auto_update.sh [--check] [--dry-run]
- android_sdk_auto_update.sh:38:android_sdk_auto_update.sh --install --yes [--dry-run]
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:40:android_sdk_auto_update.sh --test-telegram
- android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets.
- android_sdk_auto_update.sh:142:if command -v sqlite3 >/dev/null 2>&1; then
- android_sdk_auto_update.sh:143:sqlite3 "$SQLITE_FILE" >/dev/null <<'SQL'

## Safety prima di correggere
- android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:45:--remove-emulator Remove only the Android SDK package named "emulator".
- android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
- android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
- android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets.
- dev/project.metadata.json:9:"metadata_version": 1,
- android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
- android_sdk_auto_update.sh:23:DRY_RUN=0
- android_sdk_auto_update.sh:37:android_sdk_auto_update.sh [--check] [--dry-run]
