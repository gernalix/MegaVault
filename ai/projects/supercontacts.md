META:
name=SuperContacts
slug=supercontacts
path=/home/daniele/codex-workspace/SuperContacts
remote=https://github.com/gernalix/SuperContacts.git
branch=codex/prompt-729604-capsule-audit
verified_commit=b968d9d
verified_at=2026-06-08T19:30:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
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
data=app/src/main/java/com/supercontacts/app/data/storage/SafRootContract.kt:saf_root_contract_photos_plus_single_backup_only
data=app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoResolver.kt:shared_photo_resolver,canonical_photos_dir,duplicate_photos_merge,legacy_backup_file_resolution
data=app/src/main/java/com/supercontacts/app/data/local/BackupMetadataEntity.kt:BackupMetadataEntity
data=app/src/main/java/com/supercontacts/app/data/local/ContactEntity.kt:ContactEntity
data=app/src/main/java/com/supercontacts/app/data/local/ContactEventEntity.kt:ContactEventEntity
data=app/src/main/java/com/supercontacts/app/data/local/ContactMessagingLinkEntity.kt:contact_messaging_links
data=app/src/main/java/com/supercontacts/app/data/local/SavedSearchEntity.kt:SavedSearchEntity,SavedSearchTagCrossRef
FLOW:
flow=entry->app/src/main/AndroidManifest.xml=>app/src/main/assets/countries-v1.csv
flow=script->tools/build-finalize.ps1=>app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json
flow=data->app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json
flow=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
flow=app/src/main/AndroidManifest.xml:21:android:exported="true"
flow=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json:8:"tableName": "backup_metadata",
flow=phone_field_change->ContactsRepository.synchronizeMessagingLinksForContact->contact_messaging_links
INV:
arch=app/src/main/java/com/supercontacts/app/MainActivity.kt:MainActivity,onCreate,onNewIntent; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:SuperContactsApp,ContactListScreen,selectHomeSort,loadPatchVersion,EmojiToolbar...
data=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV...
ux=app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialV...
backup=app/src/main/AndroidManifest.xml:10:android:allowBackup="false"; app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/13.json:2:"formatVersion": 1,; app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/13.json:4:"version": 13,
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
migration=app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/13.json:8:"tableName": "contact_messaging_links",; schema_v13_noop_migration_adds_address_2_as_contact_fields_field_type_not_new_table
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
percentuale_capsulizzazione_finale=100%
capsulizzazione_reale=si_verificata_da_audit_mirato_post_v20
contacts_viewmodel=facade_zero_logic
root_wiring=MainActivity_SuperContactsApp_AppContainer_solo_wiring_infrastrutturale_consentito
bridge_feature_residui=nessuno
enforcement_test=rafforzati_e_passanti
baseline_permanente=100_percent_capsulization_is_blocking_invariant_for_every_future_prompt
baseline=100_percent_minimum
prompt=184926
version=21
branch=codex/prompt-729604-capsule-audit
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
owns=home_search_query,active_tag_filters,home_sort,available_home_tags,contact_list,show_added_edited,saved_searches,home_filter_reset
api=ContactHomeOwner
access=ContactsViewModel_facade_only

owner=ContactDetailCapsule
owns=selected_contact_detail,contact_stats,contact_crud,field_description_mutation,contact_open_events,field_open_events,photo_save_preview_cleanup,legacy_photo_migration
api=ContactDetailOwner
access=ContactsViewModel_facade_only

owner=ContactMessagingCapsule
owns=messaging_link_scan_single,messaging_link_scan_all,manual_confirm_reject_reset
api=ContactMessagingOwner
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
checks=ContactsViewModel_no_viewModelScope_launch_no_runCatching_no_mutableStateOf_no_AppContainer_no_database_constructor
checks=SuperContactsApp_may_use_AppContainer_only_for_generation_and_ViewModel_factory_dependencies
checks=SuperContactsApp_no_direct_repository_database_backup_manager_or_flow_wiring
checks=MainActivity_android_entry_only_no_ViewModel_repository_database_flow_or_coroutine_work
checks=AppContainer_dependency_wiring_only_no_UI_capsule_or_feature_model_knowledge
checks=required_owner_capsule_classes_present
checks=required_owner_contract_interfaces_present
checks=capsules_do_not_directly_reference_other_capsule_implementations_except_status_owner_and_ViewModel_wiring
checks=reading_mode_has_no_field_description_buttons
checks=messaging_link_feature_owned_by_ContactMessagingCapsule_repository_trigger_not_root_UI_logic
required=app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt
checks=field_description_text_visible_in_reading_and_edit_modes_buttons_edit_only
required_command=./gradlew --console=plain --no-daemon --max-workers=2 :app:testDeviceTestUnitTest
missing_task_note=:app:testDebugUnitTest_not_generated_because_testBuildType=deviceTest

UX_INVARIANTS:
field_descriptions=text_visible_in_reading_and_edit_modes_buttons_edit_only
age=field_type_age_source_birth_date_or_manual_age_timestamped
saved_searches=stored_in_sqlite_deeplink_host_search_filters_query_and_tags; v25_home_shows_single_saved_searches_entry_not_inline_list; delete_requires_confirm_and_updates_flow
home_sort=v25_any_criterion_or_ASC_DESC_change_requests_contacts_list_top_scroll; direction_indicator_single_toggle_only
search_results=v25_name_match_highlighted_in_title_no_duplicate_Name_row_when_same_as_card_title
backup=whole_sqlite_db_exported_to_saf_root_contract_only_photos_dir_plus_super_contacts_backup_sqlite
photo_storage=v29_saf_root_contract; photos_(N)_detected_transferred_to_photos_then_duplicate_dirs_deleted_only_after_safe_transfer; collisions_renamed_stably_without_photo_loss; Home+Detail_share_ContactPhotoStore_resolver_path
messaging_links=v27_local_only_generation_from_saved_phone_numbers; no_scraping_no_upload_no_registration_check; statuses=link_generated,unverified,manually_confirmed,manually_rejected,last_scan_at; trigger=ContactsRepository_create_update_phone_incremental; ui_unverified_only_cards; confirmed_quick_action_icon_only; rejected_hidden; manager_dialog_nonpersistent
address_2=v28_simple_contact_field_type_address_2; complements_Address_like_nickname_style_free_text; stored_in_contact_fields; included_in_form_detail_search_history_backup_export_import_via_db_snapshot; not_geocoded_not_duplicate_address_matching
history_timestamp=v28_dialog_uses_full_width_adaptive_dialog_compact_DatePicker_and_UTC_date_markers_for_Material3_selectedDateMillis
android_back=v28_internal_screens_install_BackHandler_matching_internal_Back_or_Cancel

CHANGELOG:
2026-06-01_prompt_184926=v20; split ContactsViewModel feature state into explicit owner capsules; ContactsViewModel now facade/wiring; reading mode no longer exposes field description controls/values; added capsulization enforcement tests; bridge_residue=none_feature_bridge
2026-06-02_prompt_729604=v21; audit found ContactsViewModel zero_logic PASS and root/cross_capsule enforcement_gap FAIL_corrected; strengthened CapsuleArchitectureEnforcementTest for SuperContactsApp/MainActivity/AppContainer/cross_capsule boundaries; app_code_logic_unchanged
2026-06-02_prompt_491837=doc_only; made final capsulization percentage explicit as 100%; confirmed real post_v20 audit, zero_logic facade, root_wiring_only, no feature bridges, passing enforcement tests, and permanent blocking baseline
2026-06-02_prompt_384917=v22; home_count_filtered_contacts, distance_row_real_km_when_origin_available, sort_scroll_top, saved_searches_with_deeplink, reset_search_and_tags, age_field_birthdate_or_manual, PH_Filipino_nationality, edit_mode_description_buttons_restored, schema_v11_saved_searches
2026-06-02_prompt_927463=v23; pixel_smoke_fix_edit_mode_field_description_buttons_for_all_editable_fields_including_empty_targets_and_telegram; field_description_text_visible_in_reading_and_edit_modes; reading_mode_still_hides_description_buttons
2026-06-02_prompt_615284=v24; backup_instrumented_expected_contact_fields_fixed_for_latest_state_without_age; export_regression_asserts_all_application_tables_are_present_and_roundtrip_counts_match; connected_tests_pinned_to_single_pixel_serial; pixel_form_scroll_and_photo_list_tests_stabilized
2026-06-02_prompt_384729=v25; saved_searches_moved_to_home_entry_dialog_with_apply_copy_delete_confirm; repository_delete_saved_search_test; sort_change_scroll_top_for_criterion_and_direction; search_name_match_title_highlight_no_duplicate_name_row; single_ASC_DESC_toggle_indicator
2026-06-02_prompt_620622=v26; messaging_links_auto_generated_for_international_phone_numbers; schema_v12_contact_messaging_links; platforms=whatsapp_telegram_signal_best_effort; no_registration_certification; manual_confirm_reject_preserved_on_identical_scan; ContactMessagingCapsule_owner; repository_incremental_trigger
2026-06-02_prompt_messaging_links_v27_ux=v27; messaging_links_section_visible_only_for_unverified_decisions; manually_confirmed_moves_to_detail_quick_action_icon; manually_rejected_hidden; manage_messaging_links_dialog_nonpersistent; scanner_db_deeplinks_unchanged
2026-06-06_prompt_739516=v28; schema_v13; address_2_simple_complement_field; whatsapp_telegram_signal_quick_actions_moved_from_top_bar_to_phone_row_with_recognizable_vector_icons; email_mailto_clickable_without_visibility_false_negative; history_timestamp_dialog_adaptive_and_UTC_date_marker_fixed; Android_Back_matches_internal_Back_on_internal_screens; contact_stats_removed_added_by; nationality_asset_expanded_to_all_249_ISO_alpha2_codes
2026-06-08_prompt_739284=v29; SAF_ROOT_CONTRACT=root_contains_only_photos_dir_and_super_contacts_backup_sqlite; SafRootContract uses DocumentsContract to find existing documents before create; duplicate photos_(1..N) migrated into photos with stable conflict renames and empty duplicate dirs removed; backup export overwrites canonical sqlite without root tmp or numbered backup; Home+Detail share ContactPhotoStore_to_ContactPhotoResolver path; Pixel tests cover backup root contract and photo resolver

SAF_ROOT_CONTRACT:
root_allowed=photos/,super_contacts_backup.sqlite
root_forbidden=photos_N,super_contacts_backup_N_sqlite,super_contacts_backup_sqlite_tmp,automatic_root_legacy_files
rule=any_automatic_root_entry_outside_contract_is_bug
owner=SafRootContract
backup_export=overwrite_super_contacts_backup_sqlite_via_existing_document_no_root_tmp_no_numbered_copy
photo_storage=single_canonical_photos_dir_migrates_photos_N_before_missing_photo
photo_lookup=home_and_detail_share_ContactPhotoStore_to_ContactPhotoResolver_to_SafRootContract
data_loss_policy=never_delete_photo; duplicate_dirs_deleted_only_when_empty_after_verified_transfer
version=29
prompt=739284

VERIFICATION:
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:compileDebugKotlin
result=PASS
scope=prompt_739516_final
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:testDeviceTestUnitTest
result=PASS
cmd=./gradlew --console=plain --no-daemon --max-workers=2 :app:assembleDebug
result=PASS
apk=app/build/outputs/apk/debug/app-debug.apk
device_tcl=ANDROID_SERIAL=192.168.1.200:34125; model=TCL_6102H; ro.serialno=QCGADUVOSSEYFES4
manual_tcl=PASS_pre_final_reinstall:phone_row_shows_call_sms_whatsapp_telegram_signal; icons_recognizable; email_mailto_opened_Gmail_ComposeActivityGmailExternal_with_recipient_tcl.qa@example.com; address_2_saved_and_visible_as_Door_code_2468; stats_dialog_no_added_by; history_timestamp_dialog_showed_Jun_6_2026_not_day_before_and_not_right_clipped
manual_tcl_blocker=after_final_DatePicker_compaction_patch_TCL_ADB_endpoint_192.168.1.200:34125_disconnected_and_IP_ping_failed; final_APK_built_but_reinstall/manual_rerun_blocked_until_TCL_returns_online; Android_Back_specific_manual_rerun_blocked_after_code_implementation
root_cause_nationality_missing=countries-v1.csv_was_a_curated_partial_seed_asset_49_lines_not_full_ISO_catalog; autocomplete_only_loaded_that_asset_so_missing_nationalities_were_absent_by_data_coverage_not_UI_filtering
root_cause_history_calendar=Material3_DatePicker_selectedDateMillis_is_a_UTC_day_marker_but_old_initialization_used_local_midnight_epoch; Europe_Copenhagen_positive_offset_mapped_local_midnight_to_previous_UTC_day; old_platform_default_width_dialog_also_clipped_DatePicker_on_TCL_width
