META:
name=SuperContacts
slug=supercontacts
path=/home/daniele/codex-workspace/SuperContacts
remote=https://github.com/gernalix/SuperContacts.git
branch=codex/prompt-xxx
verified_commit=3aa6287
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Android contacts app backed by Room/SQLite; repo files and tests cover contact CRUD, tags, initiatives, photos, field descriptions, address suggestions, duplicate checks, backup/export, and debug-d
STACK:
lang=Kotlin,Python,Shell
fw=Gradle,Jetpack Compose
db=Room/SQLite,SQLite
platform=Android
tools=ADB,Chrome
MAP:
entry=app/src/main/AndroidManifest.xml,app/src/main/java/com/supercontacts/app/MainActivity.kt,app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt
ui=app/src/main/java/com/supercontacts/app/ui/contacts/ContactTimeFormatter.kt,app/src/main/java/com/supercontacts/app/ui/contacts/ContactsViewModel.kt,app/src/main/java/com/supercontacts/app/ui/theme/Color.kt
core=app/src/main/assets/countries-v1.csv,app/src/main/java/com/supercontacts/app/data/local/ContactAddressSuggestionRow.kt,app/src/main/java/com/supercontacts/app/data/local/ContactEventWithContactName.kt,app/src/main/java/com/supercontacts/app/data/local/ContactFieldSuggestionRow.kt,app/src/main/java/com/supercontacts/app/data/local/ContactHomeMetricRow.kt
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/2.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/3.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/5.json
tests=app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt,app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt,app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt
scripts=tools/build-finalize.ps1,tools/build-finalize.sh,tools/codex_guardrails.ps1,tools/codex_guardrails.py,tools/codex_guardrails.sh
build=app/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
entry=app/src/main/java/com/supercontacts/app/MainActivity.kt:MainActivity,onCreate,onNewIntent
entry=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:SuperContactsApp,ContactListScreen,selectHomeSort,loadPatchVersion,EmojiToolbarButton,HomeSortStatus
data=app/src/main/java/com/supercontacts/app/data/backup/BackupModels.kt:BackupState
data=app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:BackupPreferencesStore,readFolderUri,writeFolderUri,clearFolderUri,readAutoExportEnabled,writeAutoExportEnabled
data=app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:PreparedImport,SuperContactsBackupManager,notifyDatabaseChanged,setBackupFolder,setAutoExportEnabled,exportNow
data=app/src/main/java/com/supercontacts/app/data/local/BackupMetadataEntity.kt:BackupMetadataEntity
data=app/src/main/java/com/supercontacts/app/data/local/ContactEntity.kt:ContactEntity
data=app/src/main/java/com/supercontacts/app/data/local/ContactEventEntity.kt:ContactEventEntity
FLOW:
flow=entry->app/src/main/AndroidManifest.xml=>app/src/main/assets/countries-v1.csv
flow=script->tools/build-finalize.ps1=>app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json
flow=data->app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json
flow=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
flow=app/src/main/AndroidManifest.xml:21:android:exported="true"
flow=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
INV:
arch=app/src/main/java/com/supercontacts/app/MainActivity.kt:MainActivity,onCreate,onNewIntent; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:SuperContactsApp,ContactListScreen,selectHomeSort,loadPatchVersion,EmojiToolbar...
data=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV...
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV...
backup=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:2:"formatVersion": 1,; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:4:"version": 1,
version=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialValue = "", context) {; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:200:value = loadPatchVersion(context)
i18n=app/src/main/java/com/supercontacts/app/ui/app/BackupSettingsScreen.kt:191:text = stringResource(R.string.backup_last_error, lastError),; app/src/main/res/values-it/strings.xml:88:<string name="distance_geocoding_failed">Indirizzo non lo...
security=app/src/main/AndroidManifest.xml:5:<uses-permission android:name="android.permission.INTERNET" />; app/src/main/AndroidManifest.xml:6:<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
perf=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:200:value = loadPatchVersion(context); app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context: Context): Stri...
BUILD:
files=app/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts
cmd_hint=gradlew=present
TEST:
files=app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt,app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt,app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt
cmd=UNKNOWN
DATA:
db=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT EXISTS `${TABLE_...
paths=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
backup=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
restore=app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:46:private const val ROLLBACK_DB_NAME = "super_contacts_pre_restore.sqlite"; app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager...
import=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT EXISTS `${TABLE_...
export=app/src/main/AndroidManifest.xml:21:android:exported="true"; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:9:"createSql": "CREATE TABLE IF NOT EXISTS `${TABLE_...
retention=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::de...
DNB:
dnb=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
dnb=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
dnb=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
dnb=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
dnb=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context: Context): String =
dnb=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:185:"onDelete": "CASCADE",
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:362:errorMessage = uiState.errorMessage,
issue=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:417:errorMessage = uiState.errorMessage,
issue=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:463:errorMessage = uiState.errorMessage,
issue=app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:33:fun readLastError(): String? = prefs.getString(KEY_LAST_ERROR, null)
issue=app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt:36:prefs.edit().putString(KEY_LAST_ERROR, error).apply()
RISK:
risk=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
risk=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
risk=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
risk=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
risk=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context: Context): String =
risk=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json:185:"onDelete": "CASCADE",
ROAD:
now=app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:403:copyPhotoDocuments(sourcePhotos, targetPhotos)
next=app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:431:private fun copyPhotoDocuments(
later=app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoStore.kt:163:val ratio = ceil(largestSide.toDouble() / maxSizePx.toDouble()).roundToInt()
LINK:
meta=../../../SuperContacts/dev/project.metadata.json
human=../../human/projects/supercontacts/overview.md
legacy=../../../SuperContacts/dev/legacy
repo=../../../SuperContacts
OPEN:
open=none
