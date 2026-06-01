# android-sdk-auto-update Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: ## Scelta user service
- dev/legacy/TROUBLESHOOTING.md: ## Build Android in corso
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: # Android SDK update tool
- dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md: # Android SDK update tool
- dev/legacy/TROUBLESHOOTING.md: ls -l ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Use the existing installed tool; do not create a duplicate:

## Useful Limits And Boundaries
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: In modalità `--check` o `--check-only`, se trova la sezione `Available Updates` la notifica come check-only senza installare. Non usa l’elenco generico `Available Packages`, perché include anche pacchetti non insta
- dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md: Lo schema SQLite viene creato automaticamente con indice su `timestamp_utc`. Il CSV crea l’header se manca ed è append-only.
- dev/legacy/OPERATIONS.md: Rimozione reale, solo del package SDK `emulator`; non cancella AVD o system-images:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Use the existing installed tool; do not create a duplicate:
- dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md: Remove only the SDK package `emulator`, never AVDs or system-images:
- dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md: La rimozione controllata riguarda solo il package SDK `emulator` e non cancella AVD o immagini di sistema:
- android_sdk_auto_update.sh: --check Safe default. List installed packages and available SDK updates only.
- android_sdk_auto_update.sh: This never deletes AVDs, system images, SDK cache, or the SDK root.
- android_sdk_auto_update.sh: What it never does:
- android_sdk_auto_update.sh: local timestamp package version size_bytes
- android_sdk_auto_update.sh: while IFS=$'\t' read -r package version; do
- android_sdk_auto_update.sh: append_history "$timestamp" "$package" "$version" "$version" "CHECK" "$size_bytes" 0 0 "$SDK_ROOT"

## Where The Feature Code Appears To Live
- `android_sdk_auto_update.sh`
