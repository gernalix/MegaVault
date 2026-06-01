# SuperContacts Troubleshooting

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
