# android-sdk-auto-update Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `android_sdk_auto_update.sh`: usage, info, warn, error, utc_now, epoch_now, csv_escape, log

## Confini operativi
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
