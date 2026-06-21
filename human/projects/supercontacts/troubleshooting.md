# SuperContacts Troubleshooting

## SAF root contract
- Stato atteso v29: nella root SAF devono esistere solo `photos/` e `super_contacts_backup.sqlite`.
- Se compaiono `photos (1)`, `photos (2)`, `super_contacts_backup (1).sqlite` o `.tmp`, verificare `SafRootContract` e `SuperContactsBackupManager`: il codice deve cercare e riusare i documenti esistenti prima di creare.
- Se una foto non compare in Home o nel dettaglio, controllare il valore DB `contact_fields.field_type='photo'`: il riferimento atteso e `photos/<file>.jpg`; il resolver deve cercare anche nelle cartelle legacy `photos (N)` e migrare il file in `photos/`.
- Non cancellare manualmente foto dai duplicati prima della migrazione: le cartelle duplicate vanno eliminate solo quando risultano vuote dopo trasferimento verificato.

## Overlay chiamata
- Stato atteso v33: l'overlay chiamata deve essere una finestra di sistema sopra Dialer/altre app, non un banner visibile solo dentro SuperContacts.
- Permesso necessario: Android deve consentire `Display over other apps` / `SYSTEM_ALERT_WINDOW` per SuperContacts.
- Se l'overlay non compare durante una chiamata reale, verificare `appops get <package> SYSTEM_ALERT_WINDOW`, permessi `READ_PHONE_STATE`/`READ_CALL_LOG`, logcat tag `SC_CallOverlay`, e che `CallStateReceiver` riceva `PHONE_STATE`.
- Il receiver diagnostico `CallOverlayDebugReceiver` serve solo per QA adb delle build debug: deve restare disabilitato fuori debug e non sostituisce il percorso reale da chiamata.

## Problemi e sintomi rilevati nel codice
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:180:import kotlinx.coroutines.withTimeoutOrNull
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:348:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:362:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:364:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:417:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:422:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:449:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:463:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/data/backup/BackupModels.kt:9:val lastError: String? = null,
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:33:fun readLastError(): String? = prefs.getString(KEY_LAST_ERROR, null)
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:35:fun writeLastError(error: String?) {
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:36:prefs.edit().putString(KEY_LAST_ERROR, error).apply()
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:44:private const val KEY_LAST_ERROR = "last_error"
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:74:}.onFailure { error ->
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:75:recordError(error.message ?: appContext.getString(R.string.backup_export_failed))
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:93:prefs.writeLastError(null)
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:95:} catch (error: Throwable) {
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:97:recordError(error.message ?: appContext.getString(R.string.backup_folder_access_failed))

## Comandi/verifiche utili trovati
- tools/build-finalize.ps1:124:function Invoke-Git {
- tools/build-finalize.ps1:131:Invoke-LoggedCommand -FilePath "git" -Arguments $gitArguments
- tools/build-finalize.ps1:141:& git @gitArguments
- tools/build-finalize.ps1:143:throw ("git failed: {0}" -f ($Arguments -join " "))
- tools/build-finalize.ps1:170:throw ("Gradle wrapper not found: {0}" -f $GradleWrapper)
- tools/build-finalize.ps1:245:Invoke-Git -Arguments @("archive", "--format=zip", "--output=$zipPath", "HEAD")
- tools/build-finalize.ps1:259:$python = Get-Command python -ErrorAction SilentlyContinue
- tools/build-finalize.ps1:260:if ($python) {
- tools/build-finalize.sh:1:#!/usr/bin/env bash

## Safety prima di correggere
- app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(null)
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewModel.removeTagFromContact(contactId, tagId) },
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:660:private fun ContactListScreen(
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context: Context): String =
- app/src/main/AndroidManifest.xml:1:<?xml version="1.0" encoding="utf-8"?>
- app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialValue = "", context) {
