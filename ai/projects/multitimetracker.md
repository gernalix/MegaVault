META:
name=MultiTimeTracker
slug=multitimetracker
path=/home/daniele/codex-workspace/projects/MultiTimeTracker
remote=https://github.com/gernalix/MultiTimeTracker.git
branch=codex/v488-release-safe-ui-lockdown
verified_commit=9c7510d
verified_at=2026-06-15T16:02:18+02:00
protocol=MEGAVAULT_PROTOCOL.md:v11
merge_20260705=retains_local_v527_v534_persistence_capsule_device_history_and_adds_github_master_v535_play_store_readiness_below
current_github_branch=master
current_github_commit=44c2b33e53ce98e02f95437bd5bc7eb3f16aa688
PURPOSE:
purpose=local-first Android time tracker. data= the app SQLite database, with sessions and shared tags as the core model
STACK:
lang=Kotlin,Python,Shell
fw=Gradle,Jetpack Compose
db=SQLite
platform=Android
tools=ADB,Chrome
MAP:
entry=app/src/main/AndroidManifest.xml,app/src/main/java/com/example/multitimetracker/MainActivity.kt,benchmark/src/main/AndroidManifest.xml
ui=app/src/main/java/com/example/multitimer/ui/EditSessionDialog.kt,app/src/main/java/com/example/multitimer/viewmodel/TaskViewModel.kt,app/src/main/java/com/example/multitimetracker/MainViewModel.kt
core=app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt,app/src/main/java/com/example/multitimetracker/SessionOnlyGuards.kt,app/src/main/java/com/example/multitimetracker/SingleSubmitGuard.kt,app/src/main/java/com/example/multitimetracker/TagRenameProjection.kt,app/src/main/java/com/example/multitimetracker/TimeFenceNotifier.kt
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt,app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt,app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt,app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsuleAccess.kt
tests=app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt
scripts=dev/tools/check_hardcoded_ui_strings.py,dev/tools/check_single_submit_confirm_buttons.sh,dev/tools/clean_transients.sh,preflight_check.ps1,tools/mtt_helper.py
build=app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts,gradle.properties
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
entry=app/src/main/java/com/example/multitimetracker/MainActivity.kt:FirstRunWorkStep,MainActivity,onCreate,MultiTimeTrackerApp,resolveContinuationMode,refreshSetupState
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:BackupFolderInspection,FolderChosenEmpty,ExistingDataFound,RestoreSucceeded,RestoreFailed,FallbackToContinuation
data=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:PreparedSnapshotRuntimeState,AppliedSnapshotState,MainViewModelSnapshotCoordinator,SnapshotLoadMode,InstallAtMsPolicy,r...
data=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:FinalizedImport,ImportExportCapsuleViewModel,ImportRollbackOutcome,createImportExportCapsule,showLong...
data=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:ImportExportSnapshot,ImportExportCapsule,setBackupRootFolder,inspectBackupFolder,exportBackup,importDatabaseFromUri
data=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsuleAccess.kt:ImportExportCapsuleAccess,exportSnapshot,activateImportedSnapshotFromStore,persist,scheduleAutoBackup,computeB...
data=app/src/main/java/com/example/multitimetracker/data/importexport/FallbackRestoreManager.kt:FallbackRestoreManager,shouldTriggerFallback,buildUserMessage
data=app/src/main/java/com/example/multitimetracker/data/importexport/ImportExportIntegrityValidator.kt:ImportExportCounts,ImportExportIntegrityValidator,compare
capsules=present: NOW,TAGS,TIMELINE,QUICK_EVENTS,CHAINS,AUDIT_LOG,ALERTS,IMPORT_EXPORT,SINCE_WHEN via app/src/main/java/com/example/multitimetracker/capsules/*
capsules=owned: TAGS CRUD policy/audit/persist/rename-projection in capsules/tags/TagsCapsuleViewModel.kt via TagsCapsuleAccess owner primitives; MainViewModel keeps wrappers only
capsules=owned: ALERTS rule mutation plus runtime evaluation/reconciliation/schedule/cancel in capsules/alerts/AlertsCapsuleViewModel.kt; snapshot post-load alarm reconciliation is behind AlertsCapsuleViewModel.reconcileSnapshotRuntimeAlarms
capsules=owned: NOW/TIMELINE session CRUD and stop policies route through SessionOwnerCapsuleViewModel via SessionOwnerCapsuleAccess; Now/Timeline access contracts no longer expose direct session mutation
capsules=owned: QUICK_EVENTS template/entry/macro mutation and screen refresh live in QuickEventsCapsuleViewModel via QuickEventsCapsuleAccess owner primitives
capsules=owned: CHAINS create/update/delete/start/stop/advance live in ChainsCapsuleViewModel via ChainsCapsuleAccess owner primitives
capsules=owned: IMPORT_EXPORT owns backup/import/restore plus manual CSV export/import through ImportExportCapsule; MainViewModel only supplies export snapshot/apply hooks
capsules=owned: AUDIT_LOG owns filter flows, event refresh/projection, clear, undo orchestration, write suppression and audit log state in capsules/auditlog/AuditLogCapsuleViewModel.kt; undo calls session/tag owners through AuditLogCapsuleAccess
capsules=owned: SINCE_WHEN owns LifePeriod create/update/delete, duplicate-submit guard and tag validation in capsules/sincewhen/SinceWhenCapsuleViewModel.kt via SinceWhenCapsuleAccess
capsules=percent: before_prompt_539824=72; after_prompt_539824=92; after_prompt_728419=100_for_documented_features; after_prompt_462918=100_strict_including_SINCE_WHEN; remaining_feature_bridges=none; MainViewModel remains composition shell/infrastructure adapter only
quick_events=v525: removed redundant note/defaultNote fields from QuickEventTemplate, QuickEventEntry, QuickEventMacro and active Quick Events UI/import/export paths; text details now belong in custom fields
quick_events=v526 prompt #394817: startup no longer refreshes QuickEvents DB; Events screen refreshes screen snapshot async on open; UI changed from LazyColumn+per-section FlowRow to keyed LazyVerticalGrid full-span sections
performance=v527 prompt #817463: MainActivity.onCreate is thin; schema guard, integrity gate, snapshot load, and vault auto-restore run off UI path; startup schema guard cached by DB version and invalidated on import/restore/vault switch/fresh clear
events_perf=v527: collapsed recent entries do not sort while hidden; macro actions are grouped/sorted once; custom macro dialog reuses sorted actions
since_when_perf=v527: LifePeriodsScreen builds visibleTagsById once per visible tag state instead of per card
backup=v525: SqliteVault creates stable primary/temp/emergency database files with exact names even when DocumentFile providers add MIME extensions
backup=v528 prompt #739284: root cause was valid DB import rollback on runtime activation-signature after counts matched; import no longer rolls back a validated DB for runtime activation mismatch, export validates tmp/promoted SAF DB with integrity/schema/critical counts, internal restore compares current->candidate before promotion, settings mirror is preserved into old candidates, and ForensicLog records export/import/recovery failures
backup=v529 prompt #418762: runtime snapshot saves ignore only legacy derived `tasks` drops because `tasks` is compatibility data rebuilt from running sessions; complete import/replace candidates still validate `tasks` N>0->0. SAF stable export no longer promotes via DocumentFile.renameTo; it writes/validates tmp, bak, then primary copy, and manual export runs on Dispatchers.IO to avoid UI ANR.
backup=v531 prompt #947381: SQLite SAF export has one safe path: WAL checkpoint or abort, source integrity_check, tmp copy, tmp integrity_check, bak update, bak integrity_check, primary promotion, final integrity_check. Restore tries `multitimer.db` then `multitimer.db.bak`, never tmp. MultiDbVaults uses same stable pipeline. Autoexport is single-flight/coalesced via PersistentMutationTracker with 1200ms debounce; sync metadata writes do not retrigger export loops. SyncStatusStore tracks last_database_mutation_at UTC/Z, last_successful_export_at, last_export_attempt_at, status/error/file/integrity and AppTopBar shows ✅/⟳/❌/⚠.
ui_v532 prompt #284739: Now, Events, Since When, Chains and shared AppTopBar screens show SyncStatusStore-backed sync status persistently; drawer content remains unmounted until user opens it and open is delayed one frame to avoid startup flash while preserving manual drawer open.
picker_v532 prompt #284739: shared MttDateTimePickerDialog replaces Android DatePickerDialog/TimePickerDialog flows in SessionEditDialog, QuickEventsScreen entry/macro timestamps, LifePeriodsScreen start/end, and AppRoot Time Machine. MttDatePickerDialog replaces Timeline date-only filters. Picker UX is calendar above, large hour/minute inputs, numeric keyboard, Enter confirms from time fields, no required OK button.
startup_v533 prompt #739421: first-run SAF/folder prompt rendering is gated by setupCheckComplete. Unknown setup state renders a silent placeholder and cannot compose the choose-folder dialog for a single frame; prompt appears only after BackupFolderStore.ensureSavedTreeWritable completes and a real missing-folder state is stable. Regression is covered by FirstRunSetupPromptGateTest.
picker_v534 prompt #582941: MttDateTimePickerDialog now owns hour/minute TextField inputs instead of Material3 TimeInput, wiring IME Done plus hardware Enter/NumpadEnter to the same valid-time commit path. Invalid hour/minute values keep the dialog open and mark the field error. Shared callers remain SessionEditDialog, QuickEventsScreen, LifePeriodsScreen, and AppRoot Time Machine.
audit_log=v525 prompt #728419: AUDIT_LOG bridge removed from MainViewModel; filters, event refresh, clear and undo moved to AuditLogCapsuleViewModel with source/JVM boundary tests and Pixel clone validation
since_when=v525 prompt #462918: post-capsulization audit found LifePeriod CRUD still root-owned; moved to SinceWhenCapsuleViewModel, extended CapsuleBoundaryOwnershipTest and added SinceWhenCapsuleViewModelTest
FLOW:
flow=entry->app/src/main/AndroidManifest.xml=>app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt
flow=script->dev/tools/check_hardcoded_ui_strings.py=>app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt
flow=data->app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt
flow=app/src/main/AndroidManifest.xml:8:<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
flow=app/src/main/AndroidManifest.xml:9:<!-- Haptic feedback for alerts and quick widget starts. -->
flow=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"
INV:
arch=app/src/main/java/com/example/multitimetracker/MainActivity.kt:FirstRunWorkStep,MainActivity,onCreate,MultiTimeTrackerApp,resolveContinuationMode; app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:BackupFolderInsp...
data=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).; app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val...
ux=app/src/main/AndroidManifest.xml:6:<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />; app/src/main/AndroidManifest.xml:12:<uses-permission android:name="android.permission.USE_FULL_SCREEN_INTENT" />
backup=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"; app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
data_loss=No persistent entity may disappear silently. Every SAF SQLite export must be lossless, atomic, verified, and traceable. Critical drops N>0->0 for tasks,sessions,tags,tagParents,lifePeriods,quick events,chains,settings are blocked/logged before complete DB promotion or import/replace. Runtime snapshot saves compare only authoritative/runtime-complete fields and exclude legacy derived `tasks` to avoid false rollback on valid session-first saves.
sqlite_saf=Nessun percorso dell'app può esportare, importare, ripristinare o copiare database SQLite senza checkpoint coerente, integrity_check riuscito e fallback .bak verificato.
autoexport=Nessuna modifica persistente può bypassare l'infrastruttura di autoexport.
migration=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).; app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val...
version=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).; app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotC...
i18n=app/src/main/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleUi.kt:131:text = stringResource(R.string.placeholder_dash),
security=app/src/main/AndroidManifest.xml:6:<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />; app/src/main/AndroidManifest.xml:8:<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
perf=app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {; app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integr...
BUILD:
files=app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts,gradle.properties
cmd_hint=gradlew=present
TEST:
files=app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt
cmd=./gradlew :app:compileDebugKotlin --console=plain --no-daemon; ./gradlew :app:testDebugUnitTest --console=plain --no-daemon; ./gradlew :app:assembleDebug --console=plain --no-daemon
device=Pixel 8a 192.168.1.37:44861; clone_only appId=com.example.multitimetracker.devicetest version=526; testAppId=com.example.multitimetracker.devicetest.test
device_result_v526=BUILD SUCCESSFUL; connectedDeviceTestAndroidTest ran 53 tests on Pixel 8a, 3 skipped, 0 failed; first attempt blocked by duplicate ADB alias then rerun after adb disconnect mDNS alias
device_cmd=./gradlew :app:connectedAndroidTest -Pmtt.testBuildType=deviceTest -x lintVitalDeviceTest -x lintVitalAnalyzeDeviceTest -x generateDeviceTestLintVitalReportModel --console=plain --no-daemon
device_result=BUILD SUCCESSFUL; connectedDeviceTestAndroidTest ran 53 tests on Pixel 8a, 3 skipped, 0 failed; prompt #462918 also installed/launched clone appId=com.example.multitimetracker.devicetest and verified pid
device_policy_v527=TCL only for automatic testing/benchmark/stress/debug; Pixel only for final APK install/smoke
test_v527=compileDebugKotlin PASS; assembleDebug/deviceTest PASS; check_hardcoded_ui_strings PASS; testDebugUnitTest PASS; lintDebug PASS; assembleDebugAndroidTest PASS
test_v528_prompt_739284=PASS compileDebugKotlin+compileDebugAndroidTestKotlin; PASS testDebugUnitTest; PASS targeted TCL deviceTest MainViewModelRecoveryTest+PersistenceImportExportTest+ImportExportCapsuleViewModelTest 26 tests, 1 fixture skip, 0 failed; PASS assembleDebug. Full connectedAndroidTest attempted first but TCL went offline after 12/51 and timed-session notification tests timed out, so final persistence verdict uses targeted deviceTest.
test_v529_prompt_418762=PASS compileDebugKotlin+compileDeviceTestKotlin+compileDebugAndroidTestKotlin; PASS testDebugUnitTest; PASS hardcoded UI string gate; PASS targeted TCL deviceTest `PersistenceImportExportTest#sqliteVaultExportUsesSingleStableBackupAndOneEmergencyCopy`; PASS Pixel main v529 UI smoke/session/event/Since When/Parent Tag/manual SAF export/restart persistence. Pixel SAF `multitimer.db` and `.bak` 28.5MB, identical sha, quick_check ok, contains `Pixel529_since_when`, `Pixel529child`, `Pixel529parent`, and no final Save failed/critical loss/crash/ANR logcat.
test_v530_prompt_742913=compileDebugKotlin PASS; testDebugUnitTest PASS; compileDeviceTestAndroidTestKotlin PASS; assembleDebug PASS; initial targeted connectedDeviceTestAndroidTest blocked because adb devices empty and TCL 192.168.1.200:5555 refused.
test_v530_prompt_518204=TCL 192.168.1.200:33771 online; clean deviceTest install+pm clear PASS; targeted Gradle connectedDeviceTestAndroidTest PASS 1/1; manual am instrument PASS 1/1; extracted real SAF DB from /sdcard/Android/data/com.example.multitimetracker.devicetest/files/full-parity-vault-test-artifacts/multitimer_saf.db; sqlite quick_check ok; 17 SAF user tables == 17 internal post-import tables; schema/row diff none; import after clear PASS; UTC/Z view scan bad_format=0.
test_v531_prompt_947381=PASS compileDebugKotlin+compileDebugAndroidTestKotlin; PASS testDebugUnitTest; PASS hardcoded UI string gate; PASS TCL connectedDeviceTestAndroidTest 7/7 on 6102H via 192.168.1.200:33771 covering stable export, checkpoint abort, bak restore with tmp ignored, sync states, anti-storm, follow-up export and full SAF parity/import; PASS assembleDebug; PASS final APK v531 install+launch on TCL and Pixel 8a with no immediate crash/ANR logcat.
test_v532_prompt_284739=PASS compileDebugKotlin+testDebugUnitTest+assembleDebug; PASS hardcoded UI string gate; PASS debug APK metadata package=com.example.multitimetracker versionCode/versionName/asset_patch=532; PASS TCL main install/launch; PASS drawer closed on startup and opens by user tap; PASS sync status visible Now/Events/Since When/Chains from SyncStatusStore; PASS session/event/lifePeriod picker UI and Enter confirm on TCL; PASS autoexport after session/event/lifePeriod mutations; PASS TCL targeted deviceTest PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically.
test_v533_prompt_739421=PASS hardcoded UI string gate; PASS compileDebugKotlin+testDebugUnitTest with FirstRunSetupPromptGateTest; PASS assembleDebug and APK metadata versionCode/versionName/asset_patch=533; PASS Pixel v533 install/cold/warm/resume/force-stop/rotation smoke; PASS Pixel screenrecord+rapid dumps show no SAF/folder/vault prompt flash and no drawer flash; PASS sync status Now/Events/Since When/Chains; PASS session/event/lifePeriod mutations and autoexport; PASS Pixel targeted deviceTest PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically.
test_v534_prompt_582941=PASS local gates check_hardcoded_ui_strings, compileDebugKotlin, testDebugUnitTest, assembleDebug, APK metadata versionCode/versionName/asset_patch=534; PASS TCL 192.168.1.200:33771 install v534, clear-data cold start with empty sessions/session_tags/events/snapshot, footer v534; PASS target flow Edit session -> Edit times -> Change start: Android numeric keyboard NumpadEnter on Minutes closed the picker, returned to Edit times with Start: 18:56, Save persisted DB sessions.start_ms=2026-06-17 18:56:00 local; PASS valid hour edit closes picker, invalid values covered by unit parser tests; PASS session tap/Timeline START-STOP visibility, long press edit session, Active tags present, event creation smoke, Since When creation smoke with DB sessions=1 quick_event_templates=1 quick_event_entries=1 lifePeriods=1; final logcat sample no app FATAL/ANR.
versioning_note_v534=OPEN prompt #582941 observed configuration cache invalidation on assembleDebug because app/build.gradle.kts reads providers.gradleProperty("MTT_VERSION").get() during configuration. This conflicts with the Android protocol preference that routine version bumps should not invalidate configuration cache; treat as versioning debt, not fixed in this timestamp-picker patch.
tcl_v527=TCL 192.168.1.200:45699; debug APK v527 installed; clear-data cold start produced NO_DB_FILE; no app AndroidRuntime/FATAL/ANR/lmkd in final logs
tcl_validation_294816=TCL 192.168.1.200:45699 unlocked/testable; synthetic clone cold WaitTime avg 669.0ms min 629 max 763; warm avg 10.2ms min 8 max 13; main_activity_on_create avg 17.96ms; ensure_session_tables avg 3.39ms; tap/long-press/Active tags/Events/Timeline/Since When/Settings PASS
tcl_bgfg_294816=10 home/foreground cycles avg WaitTime 143.3ms min 17 max 447; startup PSS 69412KB/RSS 147735KB; post bgfg PSS 96351KB/RSS 184085KB; final TCL logcat has no app AndroidRuntime/FATAL EXCEPTION/ANR/lmkd/am_proc_died
tcl_clear_data_294816=main debug v527 installed on TCL, pm clear, cold start WaitTime 4917ms, sessions=0 session_tags=0 snapshot=0; no user data spawned
pixel_final_v527=PASS; Pixel 8a 192.168.1.37:36265 installed debug APK v527; versionCode/versionName 527; clean launch WaitTime 1101ms; no immediate app crash/ANR/lmkd signal
repo_docs_294816=project docs committed/pushed at 5b7e76a2de28d9974235d5f8fcc2623c64251fca; validated APK/code remains 2548034f6c4fc7e4950f45600b41101faae7d764
perf_v527_baseline=v526 real DB: onCreate avg 79.25ms, ensure_session_tables avg 50.73ms, integrity_gate avg 139.74ms, load_persisted_snapshot avg 654.04ms, cold WaitTime avg 3034.8ms locked TCL, warm avg 30.2ms
perf_v527_after=v527 real DB final: onCreate avg 30.83ms in audit; steady ensure avg 2.30ms; unlocked #294816 clone cold WaitTime avg 669.0ms and warm avg 10.2ms; real main clear-data cold WaitTime 4917ms while first-run setup creates empty DB/schema only
mem_v527=v526 real DB startup/warm PSS 50142/63167KB; v527 audit final real DB PSS 33224KB; #294816 synthetic startup PSS 69412KB; after prolonged bg/fg PSS 96351KB
DATA:
db_schema_v530=internal_and_SAF_user_tables_identical_copy: snapshot,snapshot_history,snapshot_payloads,audit_events,ui_prefs_mirror,integrity_stats,sessions,session_tags,quick_event_templates,quick_event_template_tags,quick_event_entries,quick_event_entry_tags,quick_event_template_fields,quick_event_entry_field_values,quick_event_macros,quick_event_macro_tags,quick_event_macro_actions
export_matrix_v530=sessions=>sessions+session_tags+snapshot.closedSessions/tagSessions yes_reimport; events=>quick_event_*+snapshot.quickEvent* yes; since_when/lifePeriods=>snapshot.lifePeriods yes; tags=>snapshot.tags+join_tables yes; parent_tags=>snapshot.tagParents yes; settings=>ui_prefs_mirror yes; archived_soft_deleted=>isArchived/isDeleted/deletedAtMs/deleted_at_ms yes; capsule_state=>snapshot activeSessionStart/activeTagStart/chains/activeChainRun+audit_events+integrity_stats+history yes; locations=not_present_in_active_model
utc_export_v530=SAF SQLite is byte-copy of internal DB and adds inspectable UTC/Z views export_*_utc_z for snapshot/history/payloads/audit/settings/integrity/sessions/quick_event timestamp columns; app UI remains local-time formatter based on epoch-ms model.
writepath_autoexport_v531=SnapshotSqlite.writeSnapshot=>record+queue; SnapshotStore.save=>queue; SessionRepository session CRUD=>record+queue; QuickEventRepository templates/entries/macros/replaceAll=>record+queue; AuditLogSqlite insert/clear/undo=>record+queue; UiPrefsStore user settings=>record+queue; import/restore/clear internal DB=>record+queue; export metadata last_export_*=>no record to prevent loops.
db=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:33:fun importDatabaseFromUri(context: Context, uri: Uri, scope: CoroutineScope); app/src/main/AndroidManifest.xml:9:<!-- Haptic feedback for alerts and...
paths=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"; app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
backup=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"; app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
restore=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKind {; app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:13:LEGACY_BACKUP_ONLY,
import=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:10:data class ImportExportSnapshot(; app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:29:interface ImportExportCap...
export=app/src/main/AndroidManifest.xml:31:android:exported="false"; app/src/main/AndroidManifest.xml:40:android:exported="true"
migration=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).; app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val...
retention=app/src/main/java/com/example/multitimetracker/persistence/SnapshotSqlite.kt:500:db.execSQL("CREATE INDEX IF NOT EXISTS idx_${HISTORY_PAYLOAD_TABLE}_hash ON $HISTORY_PAYLOAD_TABLE(hash);"); app/src/main/java/com/example/multitimetracker/...
DNB:
dnb=app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create") {
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAsState()
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:188:// otherwise empty/default state could race against the real restore decision.
dnb=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:63:private val canonicalSupportEntries = setOf("vaults", "exports", "logs", "tmp")
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=app/src/main/java/com/example/multitimetracker/MainActivity.kt:67:// v138 Capsule Audit Engine: emit known capsule boundary leaks in Logcat (debug only)
issue=app/src/main/java/com/example/multitimetracker/MainActivity.kt:254:is FirstRunSetupState.RestoreFailed -> context.getString(R.string.first_run_restore_failed_title)
issue=app/src/main/java/com/example/multitimetracker/MainActivity.kt:298:R.string.first_run_restore_failed_keep_current_body_fmt
issue=app/src/main/java/com/example/multitimetracker/MainActivity.kt:300:R.string.first_run_restore_failed_empty_body_fmt
issue=app/src/main/java/com/example/multitimetracker/MainActivity.kt:325:FirstRunFallbackReason.RESTORE_FAILED -> context.getString(
issue=v528_prompt_739284: import audit showed IMPORT_VERIFY_MISMATCH_ROLLBACK after a valid DB with lifePeriods=7 and tagParents=6 matched expected/actual counts; rollback to preimport empty state caused persisted loss and later SAF export overwrote stable DB/bak with empty lifePeriods/tagParents.
issue=v529_prompt_418762: CriticalDataGuard false-positive `tasks: 1 -> 0` came from comparing complete previous snapshot against a runtime snapshot where legacy `tasks` can be empty while authoritative session/tag/life-period data is valid; separate finding: SAF primary `multitimer.db` could remain 0 bytes while `.bak` held the full DB after DocumentFile promotion.
RISK:
risk=app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
risk=app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create") {
risk=app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {
risk=app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAsState()
risk=app/src/main/java/com/example/multitimetracker/MainActivity.kt:188:// otherwise empty/default state could race against the real restore decision.
risk=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:63:private val canonicalSupportEntries = setOf("vaults", "exports", "logs", "tmp")
risk=capsules: MainViewModel is now composition shell/infrastructure bridge; feature business ownership is inside capsules, with AUDIT_LOG and SINCE_WHEN guarded by source/JVM tests plus Pixel clone gate
risk=events_perf: many buttons must stay lazy-keyed; avoid FlowRow inside lazy item for large sections; avoid startup QuickEvents DB refresh unless app initial tab requires it
risk=v527_snapshot_load_cost: integrity/snapshot load still expensive but no longer blocks onCreate/main startup path; future work needs data-safe generation/cache design
risk=v527_real_device_stability: #294816 unlocked TCL UI validation and Pixel final install/smoke passed; continue monitoring ActivityManager/lmkd because low-memory system pressure can still kill processes independently from app crashes
risk=v530_prompt_742913: live TCL parity proof is complete for current schema; keep this gate mandatory for future persistence/export/import schema changes.
ROAD:
now=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:98:// Persist permission for future sessions.
next=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:110:// Roll back the saved URI to avoid future "Export fallito" loops.
next=capsules: no feature bridge is currently documented; optional future work is shrinking MainViewModel infrastructure hooks only after preserving composition-root stability
next=v527_followup: no immediate code refactor; monitor real-device stability and investigate incremental snapshot/readiness state only if data-safety contract remains intact
next=v529_test_policy: any future persistence/database/export/import/recovery/backup/integrity/guard patch must include real UI or device-equivalent creation of each critical entity through the full app flow, plus SAF export and restart persistence checks; isolated DAO/repository/export tests are not sufficient alone.
next=v530_parity_gate: for future persistence/export/import schema changes, rerun `PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically` on TCL deviceTest clone and extract the SAF DB artifact; expected proof is 17+ internal user tables == SAF user tables, UTC/Z views present, import after internal clear restores identical snapshot/settings/table rows.
next=v533_followup: startup SAF prompt flash closed on Pixel; keep first-run prompt rendering gated on stable SAF verification and do not render user prompts for unknown setup/loading states.
next=v534_followup: keep timestamp picker commit behavior centralized in MttDateTimePickerDialog; Enter/NumpadEnter/IME Done must confirm only valid hour/minute input and must not add per-caller timestamp picker forks.
later=app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:32:* - It makes future "Time Travel" (replay log into a past snapshot) possible.
LINK:
meta=../../../projects/MultiTimeTracker/dev/project.metadata.json
human=../../human/projects/multitimetracker/overview.md
legacy=../../../projects/MultiTimeTracker/dev/legacy
repo=../../../projects/MultiTimeTracker
OPEN:
open=capsulization_feature_ownership: 100 percent strict including SINCE_WHEN after prompt #462918; MainViewModel still supplies shared composition/infrastructure APIs to capsules

---

## MERGED_GITHUB_BRANCH_20260705

local_path=C:/Users/seste/Documents/MTT
branch=master
verified_commit=44c2b33e53ce98e02f95437bd5bc7eb3f16aa688
verified_at=2026-06-22
protocol=MEGAVAULT_PROTOCOL.md:v3
incident=wrong_branch_play_store_work_v489_instead_of_v534; recovery_prompt_395842=port_complete_on_v535; merge_prompt_628914=master_ff_to_v535
version=versionCode=535;versionName=535;asset_patch=535;applicationId=com.example.multitimetracker;namespace=com.example.multitimetracker;minSdk=26;targetSdk=36
release=#628914 PASS on master; Play Store docs/signing/CI ported selectively from v489 to v535 and fast-forwarded into master; commit=44c2b33e53ce98e02f95437bd5bc7eb3f16aa688; backup=backup/master-before-v535-play-store-merge-20260622-133603
signing=PASS_LOCAL; local ignored C:/Users/seste/Documents/MTT/local_signing/mtt-upload.p12 and C:/Users/seste/Documents/MTT/mtt-release.properties used; Gradle auto-loads mtt-release.properties preserving Windows paths; accepts MTT_RELEASE_* and MTT_UPLOAD_*; never commit keystore/secrets
cmd=./gradlew :app:compileDebugKotlin --console=plain --no-daemon; ./gradlew :app:testDebugUnitTest --console=plain --no-daemon; ./gradlew :app:assembleDebug --console=plain --no-daemon; ./gradlew :app:lintDebug --console=plain --no-daemon; ./gradlew :app:assembleRelease --console=plain --no-daemon; ./gradlew :app:bundleRelease --console=plain --no-daemon
result_prompt_947263=PASS on recovered master 00ecfd85; commands=compileDebugKotlin,testDebugUnitTest,assembleDebug; debug APK metadata versionCode=534 versionName=534 asset_patch=534; Pixel not used
result_prompt_684219=INVALID_BASELINE_FOR_MASTER; PASS existed on wrong branch codex/play-store-readiness-roadmap at a8a28e20 with MTT_VERSION=489 and must not be treated as release proof for master 534
result_prompt_395842=PASS on codex/v534-play-store-readiness-port commit 44c2b33e53ce98e02f95437bd5bc7eb3f16aa688; commands=compileDebugKotlin,testDebugUnitTest,assembleDebug,lintDebug,assembleRelease,bundleRelease; APK metadata versionCode=535 versionName=535 package=com.example.multitimetracker; apksigner PASS; jarsigner PASS; APK_SHA256=B9C1FF563FCF517BAE9FA873D887BE236DA8FE7749C8E9A1FF25CBB7ED6CCF33; AAB_SHA256=C90054D4853021525EAAA15F46B238B8C78A4C5483F036414AB0FC58F2323E48; Pixel/TCL/emulator not used
result_prompt_628914=PASS on master commit 44c2b33e53ce98e02f95437bd5bc7eb3f16aa688; fast_forward=yes from 00ecfd85a50ba30b927e759d4ed766040a25081c; backup pushed backup/master-before-v535-play-store-merge-20260622-133603; commands=compileDebugKotlin,testDebugUnitTest,assembleDebug,lintDebug,assembleRelease,bundleRelease; APK metadata versionCode=535 versionName=535 package=com.example.multitimetracker; apksigner PASS; jarsigner PASS; APK_SHA256=06437AE0AD50E748FF12352E5A0C4B1B18F166DAD1E67FA88C9867F4131AFDAB; AAB_SHA256=D89D080CB2DFFEB9D88085B1E9714E87D2386B52A4E1E16E6455CC674726C902; Pixel/TCL/emulator not used; TestAndroidApps skill evaluated but not used because release/signing verification was host-side
device=POLICY #947263: do not use Pixel; use TCL, Emulator, or Test Android Apps plugin only
privacy=local_first; storage=SQLite+SharedPreferences local; export_import=SAF user-selected files/folders; cloud=none in reviewed build; network=INTERNET permission absent; analytics/ads/crash/cloud SDK=not found in prompt_914506 static review
dnb=release:no committed keystore/secrets; backup local upload key before first Play upload; Play first upload locks applicationId; confirm com.example.multitimetracker before closed testing
risk=wrong_branch_play_store_work_v489_instead_of_v528: Play Store work #914506/#517284/#684219 was applied to codex/play-store-readiness-roadmap a8a28e20 MTT_VERSION=489 while real latest line was origin/codex/v488-release-safe-ui-lockdown -> master 00ecfd85 MTT_VERSION=534; backup branches pushed backup/master-before-v528-recovery-20260622-093346 and backup/v489-play-store-work-20260622-093346
risk=play_store_readiness prompt_947263: recovered master has PASS debug compile/unit/assemble, strong P0 import/export/first-run history through v534, but Play Store docs/signing/listing from v489 are not on master and need selective port; readiness about 58 percent until docs/signing/assets are revalidated on v534
risk=prompt_395842_port_scope: recovered=yes docs dev/human/play_store/*, dev/ai/play_store_readiness.md, roadmap readiness docs, CI workflow, release signing wiring, ignore rules, v535 version bump, one missing IT string for lint; recovered=no old v489 MainActivity/MainViewModel/capsule/DB/SAF/import-export code, old whole build files, version 489, generated artifacts, keystore/secrets
now=branch_safety_before_release: always verify current branch, remote latest branch, highest versionCode across all refs, MegaVault branch/commit, active roadmap before Play Store/release work; if current branch lacks highest known version, stop and ask confirmation
next=after_prompt_628914: future MultiTimeTracker work must start from master v535 or higher; Play Console closed-testing upload still needs owner inputs/assets
play_docs=present_on_master_v535; source_ported_from=backup/v489-play-store-work-20260622-093346:dev/human/play_store; integrated_branch=codex/v534-play-store-readiness-port
open=incident_wrong_branch_play_store_work_v489_instead_of_v528: cause=release work started from stale branch; correct_line=master/origin/codex/v488-release-safe-ui-lockdown at 00ecfd85 MTT_VERSION=534; exact_v528_commit=8061d232e4afbf0e80e2cebbbf76233f7fa2fa18; next=port safe docs/build patches only, then rerun release gates
open=prompt_628914_done: master contains v535 Play Store readiness; use master v535 or higher going forward
