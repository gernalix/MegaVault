META:
name=MultiTimeTracker
slug=multitimetracker
path=/home/daniele/codex-workspace/projects/MultiTimeTracker
remote=https://github.com/gernalix/MultiTimeTracker.git
branch=codex/v488-release-safe-ui-lockdown
verified_commit=2548034f6c4fc7e4950f45600b41101faae7d764
verified_at=2026-06-12T15:50:23+02:00
protocol=MEGAVAULT_PROTOCOL.md:v8
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
device_policy_v527=TCL only for automatic testing/benchmark/stress/debug; Pixel only attempted for final APK install
test_v527=compileDebugKotlin PASS; assembleDebug/deviceTest PASS; check_hardcoded_ui_strings PASS; testDebugUnitTest PASS; lintDebug PASS; assembleDebugAndroidTest PASS
tcl_v527=TCL 192.168.1.200:45699; debug APK v527 installed; clear-data cold start produced NO_DB_FILE; no app AndroidRuntime/FATAL/ANR/lmkd in final logs
tcl_limit_v527=TCL remained mCurrentFocus=NotificationShade and mDreamingLockscreen=true; visual UI scrolling/tap/tab benchmark blocked; benchmark:connectedDeviceTestAndroidTest started 4 tests on TCL then no progress under keyguard
pixel_final_v527=BLOCKED; Pixel 8a 192.168.1.37 refused all known ADB ports and mDNS listed no services after TCL-only testing
perf_v527_baseline=v526 real DB: onCreate avg 79.25ms, ensure_session_tables avg 50.73ms, integrity_gate avg 139.74ms, load_persisted_snapshot avg 654.04ms, cold WaitTime avg 3034.8ms locked TCL, warm avg 30.2ms
perf_v527_after=v527 real DB locked TCL: onCreate avg 30.83ms final, steady ensure avg 2.30ms, warm WaitTime avg 19.6ms, cold WaitTime still ~3029ms because keyguard; no reliable visual screen-load timings while locked
mem_v527=v526 real DB startup/warm PSS 50142/63167KB; v527 final locked real DB PSS 33224KB; synthetic locked PSS 42612KB; debug bg/fg no-data PSS 92425KB
DATA:
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
risk=v527_tcl_keyguard: TCL visual stress testing requires manual unlock or test harness that can dismiss keyguard; do not use Pixel for intermediate performance debugging when TCL policy is active
ROAD:
now=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:98:// Persist permission for future sessions.
next=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:110:// Roll back the saved URI to avoid future "Export fallito" loops.
next=capsules: no feature bridge is currently documented; optional future work is shrinking MainViewModel infrastructure hooks only after preserving composition-root stability
next=v527_followup: repeat visual UI scroll/tap/tab benchmarks on unlocked TCL; investigate incremental snapshot/readiness state only if data-safety contract remains intact
later=app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:32:* - It makes future "Time Travel" (replay log into a past snapshot) possible.
LINK:
meta=../../../projects/MultiTimeTracker/dev/project.metadata.json
human=../../human/projects/multitimetracker/overview.md
legacy=../../../projects/MultiTimeTracker/dev/legacy
repo=../../../projects/MultiTimeTracker
OPEN:
open=capsulization_feature_ownership: 100 percent strict including SINCE_WHEN after prompt #462918; MainViewModel still supplies shared composition/infrastructure APIs to capsules
