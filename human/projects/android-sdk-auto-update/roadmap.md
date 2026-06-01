# android-sdk-auto-update Roadmap

## Segnali dal codice
- android_sdk_auto_update.sh:354:/^Available Updates:/ { in_updates=1; next }
- android_sdk_auto_update.sh:371:/^Installed packages:/ // /^Installed Packages:/ { in_installed=1; next }
- android_sdk_auto_update.sh:387:/^Available Updates:/ { in_updates=1; print; next }

## Debito/rischi da considerare
- android_sdk_auto_update.sh:3:set -Eeuo pipefail
- android_sdk_auto_update.sh:16:RUN_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_TIMEOUT_SECONDS:-3600}"
- android_sdk_auto_update.sh:17:SDKMANAGER_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_SDKMANAGER_TIMEOUT_SECONDS:-1800}"
- android_sdk_auto_update.sh:25:STATUS="ERROR"
- android_sdk_auto_update.sh:71:error() { log "ERROR" "$*"; }
- android_sdk_auto_update.sh:224:warn "Telegram helper failed, trying curl fallback"
- android_sdk_auto_update.sh:238:if curl --fail --silent --show-error --max-time 20 \
- android_sdk_auto_update.sh:246:warn "Telegram curl fallback failed"
- android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
- android_sdk_auto_update.sh:39:android_sdk_auto_update.sh --remove-emulator --yes [--dry-run]
- android_sdk_auto_update.sh:45:--remove-emulator Remove only the Android SDK package named "emulator".
- android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
- android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
