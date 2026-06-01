META:
name=SuperContacts
slug=supercontacts
path=/home/daniele/codex-workspace/SuperContacts
remote=https://github.com/gernalix/SuperContacts.git
branch=codex/prompt-xxx
verified_commit=3aa6287
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Android contacts app backed by Room/SQLite; repo files and tests cover contact CRUD, tags, initiatives, photos, field descriptions, add...
STACK:
lang=Kotlin,Python,Shell;fw=Gradle,Jetpack Compose;db=Room/SQLite,SQLite;platform=Android;tools=ADB,Chrome
MAP:
entry=app/src/main/AndroidManifest.xml
entry=app/src/main/java/com/supercontacts/app/MainActivity.kt
entry=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt
core=app/src/main/assets/countries-v1.csv
core=app/src/main/java/com/supercontacts/app/data/local/ContactAddressSuggestionRow.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactEventWithContactName.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactFieldSuggestionRow.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactHomeMetricRow.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactInitiativeWithContactName.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactTagCrossRef.kt
core=app/src/main/java/com/supercontacts/app/data/local/ContactWithFields.kt
ui=app/src/main/java/com/supercontacts/app/ui/contacts/ContactTimeFormatter.kt
ui=app/src/main/java/com/supercontacts/app/ui/contacts/ContactsViewModel.kt
ui=app/src/main/java/com/supercontacts/app/ui/theme/Color.kt
ui=app/src/main/java/com/supercontacts/app/ui/theme/Theme.kt
ui=app/src/main/java/com/supercontacts/app/ui/theme/Type.kt
ui=app/src/main/res/values/themes.xml
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/2.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/3.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/5.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/6.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/7.json
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/9.json
tests=app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/ContactFormScrollDeviceTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/ContactPhotoCropUiTest.kt
tests=app/src/androidTest/java/com/supercontacts/app/ContactPhotoDeviceTest.kt
scripts=tools/build-finalize.ps1
scripts=tools/build-finalize.sh
scripts=tools/codex_guardrails.ps1
scripts=tools/codex_guardrails.py
scripts=tools/codex_guardrails.sh
scripts=tools/guardrails/__init__.py
scripts=tools/guardrails/engine.py
build=app/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- app/src/main/java/com/supercontacts/app/MainActivity.kt=>MainActivity,onCreate,onNewIntent
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt=>SuperContactsApp,ContactListScreen,selectHomeSor
- app/src/main/java/com/supercontacts/app/data/backup/BackupModels.kt=>BackupState
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt=>BackupPreferencesStore,readFolderUri,
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt=>PreparedImport,SuperContactsBacku
- app/src/main/java/com/supercontacts/app/data/local/BackupMetadataEntity.kt=>BackupMetadataEntity
- app/src/main/java/com/supercontacts/app/data/local/ContactEntity.kt=>ContactEntity
- app/src/main/java/com/supercontacts/app/data/local/ContactEventEntity.kt=>ContactEventEntity
- app/src/main/java/com/supercontacts/app/data/local/ContactFieldEntity.kt=>ContactFieldEntity
- app/src/main/java/com/supercontacts/app/data/local/ContactInitiativeEntity.kt=>ContactInitiativeEntity
- app/src/main/java/com/supercontacts/app/data/local/ContactsDao.kt=>ContactsDao,insertContact,updateContact,deleteCon
- app/src/main/java/com/supercontacts/app/data/local/SuperContactsDatabase.kt=>SuperContactsDatabase,contactsDao,getIn
- app/src/main/java/com/supercontacts/app/data/local/TagEntity.kt=>TagEntity
- app/src/main/java/com/supercontacts/app/data/repository/AddressAutocompleteRepository.kt=>AddressSuggestion,Resolved
- app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
- app/src/main/AndroidManifest.xml:21:android:exported="true"
FLOW:
- app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
- app/src/main/AndroidManifest.xml:21:android:exported="true"
- app/src/main/java/com/supercontacts/app/MainActivity.kt:3:import android.content.Intent
- app/src/main/java/com/supercontacts/app/MainActivity.kt:4:import android.os.Bundle
- app/src/main/java/com/supercontacts/app/MainActivity.kt:5:import androidx.activity.ComponentActivity
- app/src/main/java/com/supercontacts/app/MainActivity.kt:6:import androidx.activity.compose.setContent
- app/src/main/java/com/supercontacts/app/MainActivity.kt:7:import androidx.activity.enableEdgeToEdge
- app/src/main/java/com/supercontacts/app/MainActivity.kt:8:import androidx.compose.runtime.getValue
- app/src/main/java/com/supercontacts/app/MainActivity.kt:9:import androidx.compose.runtime.mutableStateOf
- app/src/main/java/com/supercontacts/app/MainActivity.kt:10:import androidx.compose.runtime.setValue
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:3:import android.Manifest
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:4:import android.content.ClipData
INV:
arch=app/src/main/AndroidManifest.xml:1:<?xml version="1.0" encoding="utf-8"?>
arch=app/src/main/AndroidManifest.xml:2:<manifest xmlns:android="http://schemas.android.com/apk/res/android"
arch=app/src/main/AndroidManifest.xml:3:xmlns:tools="http://schemas.android.com/tools">
arch=app/src/main/AndroidManifest.xml:5:<uses-permission android:name="android.permission.INTERNET" />
arch=app/src/main/AndroidManifest.xml:6:<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
arch=app/src/main/AndroidManifest.xml:7:<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:3:"database": {
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:3:"database": {
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT E
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:24:"fieldPath": "schemaVersion",
data=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:25:"columnName": "schema_version",
safety=app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(n
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUn
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUn
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewM
safety=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:660:private fun ContactListScreen(
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:180:import kotlinx.coroutines.withTimeoutOrNu
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManage
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:200:value = loadPatchVersion(context)
version=app/src/main/AndroidManifest.xml:1:<?xml version="1.0" encoding="utf-8"?>
version=app/src/main/AndroidManifest.xml:2:<manifest xmlns:android="http://schemas.android.com/apk/res/android"
version=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV
version=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:200:value = loadPatchVersion(context)
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- tools/build-finalize.ps1:124:function Invoke-Git {
- tools/build-finalize.ps1:131:Invoke-LoggedCommand -FilePath "git" -Arguments $gitArguments
- tools/build-finalize.ps1:141:& git @gitArguments
- tools/build-finalize.ps1:143:throw ("git failed: {0}" -f ($Arguments -join " "))
- tools/build-finalize.ps1:170:throw ("Gradle wrapper not found: {0}" -f $GradleWrapper)
- tools/build-finalize.ps1:245:Invoke-Git -Arguments @("archive", "--format=zip", "--output=$zipPath", "HEAD")
- tools/build-finalize.ps1:259:$python = Get-Command python -ErrorAction SilentlyContinue
- tools/build-finalize.ps1:260:if ($python) {
- tools/build-finalize.sh:1:#!/usr/bin/env bash
TEST:
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:3:import androidx.test.platform.
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:6:import org.junit.Assert.assert
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:11:@Test
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:13:assumeTrue(BuildConfig.GOOGLE
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:16:InstrumentationRegistry.getIn
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt:21:assertTrue(suggestions.isNotE
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:4:import androidx.test.platform.app.Ins
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:12:import org.junit.Assert.assertEquals
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:13:import org.junit.Assert.assertTrue
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:23:val context = InstrumentationRegistr
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:24:database = Room.inMemoryDatabaseBuil
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt:27:).build()
DATA:
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:3:"database": {
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:3:"database": {
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT E
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:24:"fieldPath": "schemaVersion",
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:25:"columnName": "schema_version",
backup=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
backup=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT E
backup=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:30:"fieldPath": "backupFormatVersion"
backup=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:31:"columnName": "backup_format_versi
import=app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:3:import android.content.Context
import=app/src/main/java/com/supercontacts/app/MainActivity.kt:3:import android.content.Intent
import=app/src/main/java/com/supercontacts/app/MainActivity.kt:4:import android.os.Bundle
export=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:36:"fieldPath": "exportedAt",
export=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:37:"columnName": "exported_at",
export=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/6.json:36:"fieldPath": "exportedAt",
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:3:"database": {
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:3:"database": {
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT E
retention=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUn
retention=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUn
retention=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
DNB:
- app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(null)
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnused
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnused
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewModel
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:660:private fun ContactListScreen(
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context:
- app/src/main/AndroidManifest.xml:1:<?xml version="1.0" encoding="utf-8"?>
- app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
BUG:
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:180:import kotlinx.coroutines.withTimeoutOrNull
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:348:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:362:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:364:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:417:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:422:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:449:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:463:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/data/backup/BackupModels.kt:9:val lastError: String? = null,
- app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:33:fun readLastError(): String? = pref
RISK:
- app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(null)
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnused
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnused
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewModel
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:660:private fun ContactListScreen(
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context:
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:907:private fun EmojiToolbarButton(
- app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:185:"onDelete": "CASCADE",
ROAD:
now=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:382:onNextMonth = viewModel::nextHistoryMonth,
next=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2027:onNextMonth: () -> Unit,
later=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2062:onNextMonth = onNextMonth,
LINK:
meta=../../../SuperContacts/dev/project.metadata.json
human=../../human/projects/supercontacts/overview.md
legacy=../../../SuperContacts/dev/legacy
repo=../../../SuperContacts
OPEN:
- none
