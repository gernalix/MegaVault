META:
name=SuperContacts
slug=supercontacts
path=/home/daniele/codex-workspace/SuperContacts
remote=https://github.com/gernalix/SuperContacts.git
branch=codex/prompt-184926-capsules
verified_commit=fbe61e2
verified_at=2026-06-01T23:58:00+02:00
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

CAPSULE_ENFORCEMENT:
status=100_percent_capsulization
baseline=100_percent_minimum
prompt=184926
version=20
branch=codex/prompt-184926-capsules
invariant=capsulization_is_architectural_invariant
rule=no_future_prompt_may_reduce_capsulization
rule=every_new_feature_must_start_with_explicit_capsule_owner
rule=feature_logic_forbidden_in_MainViewModel_root_application_global_screens_unowned_shared_components
rule=temporary_bridges_forbidden
rule=architectural_shortcuts_forbidden
rule=ambiguous_ownership_forbidden
rule=direct_cross_capsule_internal_access_forbidden
rule=future_changes_must_preserve_100_percent_capsulization
rule=functionality_prompts_must_verify_capsule_ownership_before_completion
rule=if_change_risks_capsule_regression_Codex_must_fix_architecture_before_finishing_task
rule=capsulization_regression_is_blocking_bug
rule=future_audits_must_treat_100_percent_capsulization_as_minimum_baseline

CAPSULE_OWNERS:
owner=ContactHomeCapsule
owns=home_search_query,active_tag_filters,home_sort,available_home_tags,contact_list,show_added_edited
api=ContactHomeOwner
access=ContactsViewModel_facade_only

owner=ContactDetailCapsule
owns=selected_contact_detail,contact_stats,contact_crud,field_description_mutation,contact_open_events,field_open_events,photo_save_preview_cleanup,legacy_photo_migration
api=ContactDetailOwner
access=ContactsViewModel_facade_only

owner=ContactHistoryCapsule
owns=contact_history,global_history,history_filters,history_sort,history_calendar,history_range,history_timestamp_edit
api=ContactHistoryOwner
access=ContactsViewModel_facade_only

owner=ContactInitiativeCapsule
owns=home_initiatives,contact_initiatives,global_initiatives,initiative_sort,initiative_calendar,initiative_day,initiative_record,initiative_undo
api=ContactInitiativeOwner
access=ContactsViewModel_facade_only

owner=ContactSuggestionCapsule
owns=tag_suggestions,tag_add_remove,address_local_suggestions,address_google_autocomplete,address_resolution,field_value_suggestions
api=ContactSuggestionOwner
access=ContactsViewModel_facade_only

owner=ContactDuplicateCapsule
owns=duplicate_candidates,strong_duplicate_pre_save_check,duplicate_clear
api=ContactDuplicateOwner
access=ContactsViewModel_facade_only

owner=ContactBackupCapsule
owns=backup_state,backup_running_state,set_backup_folder,auto_export,manual_export,import_file,import_folder
api=ContactBackupOwner
access=ContactsViewModel_facade_only

owner=ContactOperationStatusCapsule
owns=is_saving,error_message,shared_operation_status
api=OperationStatusOwner
access=owner_capsules_only

ROOT_WIRING_ALLOWED:
MainActivity=Android_entry_only
SuperContactsApp=Compose_navigation_and_callbacks_only_no_feature_state_ownership
ContactsViewModel=facade_composes_capsule_state_and_delegates_public_UI_callbacks
AppContainer=dependency_wiring_only
allowed_bridge=wiring_only
feature_bridge_residue=none

CROSS_CAPSULE_ACCESS_RULES:
rule=UI_may_call_ContactsViewModel_facade_only
rule=ViewModel_may_delegate_to_capsule_owner_contracts_only
rule=capsules_may_call_repository_or_manager_only_for_owned_feature
rule=capsules_must_not_mutate_other_capsule_state_directly
rule=shared_status_writes_go_through_ContactOperationStatusCapsule
rule=backup_photo_migration_access_is_explicit_callback_from_ContactBackupCapsule_to_ContactDetailCapsule
rule=history_and_initiatives_may_read_current_contact_id_only_through_explicit_supplier_contract
rule=no_direct_access_to_other_capsule_internal_MutableStateFlow_Job_or_private_state

ENFORCEMENT_TESTS:
required=app/src/test/java/com/supercontacts/app/CapsuleArchitectureEnforcementTest.kt
checks=ContactsViewModel_facade_only_no_MutableStateFlow_no_MutableSharedFlow_no_Job_no_repository_calls_no_manager_calls
checks=required_owner_capsule_classes_present
checks=reading_mode_has_no_field_description_buttons_or_values
required=app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt
checks=field_descriptions_persist_but_do_not_appear_in_reading_mode
required_command=./gradlew --console=plain --no-daemon --max-workers=2 :app:testDeviceTestUnitTest
missing_task_note=:app:testDebugUnitTest_not_generated_because_testBuildType=deviceTest

UX_INVARIANTS:
field_descriptions=edit_mode_only_never_reading_mode
dob_age=ignored_by_user_request_2026-06-01

CHANGELOG:
2026-06-01_prompt_184926=v20; split ContactsViewModel feature state into explicit owner capsules; ContactsViewModel now facade/wiring; reading mode no longer exposes field description controls/values; added capsulization enforcement tests; bridge_residue=none_feature_bridge

VERIFICATION:
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:compileDebugKotlin
result=PASS
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:testDebugUnitTest
result=BLOCKED_TASK_NOT_GENERATED
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:testDeviceTestUnitTest
result=PASS
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:assembleDebug
result=PASS
