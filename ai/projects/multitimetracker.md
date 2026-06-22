META:
name=MultiTimeTracker
slug=multitimetracker
path=/home/daniele/codex-workspace/projects/MultiTimeTracker
remote=https://github.com/gernalix/MultiTimeTracker.git
local_path=C:/Users/seste/Documents/MTT
branch=codex/play-store-readiness-roadmap
verified_commit=89257cd96233ac0a28e65535c5c03f41178eca62
verified_at=2026-06-22
protocol=MEGAVAULT_PROTOCOL.md:v3
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
version=versionCode=489;versionName=489;applicationId=com.example.multitimetracker;namespace=com.example.multitimetracker;minSdk=26;targetSdk=36
release=assembleRelease,bundleRelease PASS; apk=app/build/outputs/apk/release/app-release-unsigned.apk sha256=C70E1F66AA26C9CF7BB1718F63CD337726C9D453A78EDCC0C13640DFAAB8EFFB; aab=app/build/outputs/bundle/release/app-release.aab sha256=BDB14AD3B858D9A5F2CC4F75AD9A16F059E1C62A2BFE743BE976705BD3D705FA
signing=NEEDS_SECRET; supports env/user-gradle-properties MTT_RELEASE_STORE_FILE,MTT_RELEASE_STORE_PASSWORD,MTT_RELEASE_KEY_ALIAS,MTT_RELEASE_KEY_PASSWORD; no keystore/secrets committed; docs=dev/human/play_store/release_signing.md
TEST:
files=app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt
cmd=./gradlew :app:compileDebugKotlin --console=plain --no-daemon; ./gradlew :app:testDebugUnitTest --console=plain --no-daemon; ./gradlew :app:assembleDebug --console=plain --no-daemon; ./gradlew :app:lintDebug --console=plain --no-daemon; ./gradlew :app:assembleRelease --console=plain --no-daemon; ./gradlew :app:bundleRelease --console=plain --no-daemon
result_prompt_914506=PASS all 6 commands; warning only SDK XML version warning; release artifacts unsigned because upload keystore absent
device=Pixel 8a 192.168.1.37:42135; clone_only appId=com.example.multitimetracker.devicetest version=525; testAppId=com.example.multitimetracker.devicetest.test
device_cmd=./gradlew :app:connectedAndroidTest -Pmtt.testBuildType=deviceTest -x lintVitalDeviceTest -x lintVitalAnalyzeDeviceTest -x generateDeviceTestLintVitalReportModel --console=plain --no-daemon
device_result=BUILD SUCCESSFUL; connectedDeviceTestAndroidTest ran 53 tests on Pixel 8a, 3 skipped, 0 failed; prompt #462918 also installed/launched clone appId=com.example.multitimetracker.devicetest and verified pid
DATA:
db=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:33:fun importDatabaseFromUri(context: Context, uri: Uri, scope: CoroutineScope); app/src/main/AndroidManifest.xml:9:<!-- Haptic feedback for alerts and...
paths=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"; app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
backup=app/src/main/AndroidManifest.xml:15:android:allowBackup="false"; app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
restore=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKind {; app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:13:LEGACY_BACKUP_ONLY,
import=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:10:data class ImportExportSnapshot(; app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt:29:interface ImportExportCap...
export=app/src/main/AndroidManifest.xml:31:android:exported="false"; app/src/main/AndroidManifest.xml:40:android:exported="true"
migration=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).; app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val...
retention=app/src/main/java/com/example/multitimetracker/persistence/SnapshotSqlite.kt:500:db.execSQL("CREATE INDEX IF NOT EXISTS idx_${HISTORY_PAYLOAD_TABLE}_hash ON $HISTORY_PAYLOAD_TABLE(hash);"); app/src/main/java/com/example/multitimetracker/...
privacy=local_first; storage=SQLite+SharedPreferences local; export_import=SAF user-selected files/folders; cloud=none in reviewed build; network=INTERNET permission absent; analytics/ads/crash/cloud SDK=not found in prompt_914506 static review
DNB:
dnb=app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create") {
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAsState()
dnb=app/src/main/java/com/example/multitimetracker/MainActivity.kt:188:// otherwise empty/default state could race against the real restore decision.
dnb=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:63:private val canonicalSupportEntries = setOf("vaults", "exports", "logs", "tmp")
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
dnb=release:no committed keystore/secrets; Play first upload locks applicationId; confirm com.example.multitimetracker before closed testing
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
risk=play_store_readiness prompt_914506: 70 percent; blockers=upload keystore,final applicationId decision,privacy URL,publisher/contact,Data Safety final confirmation,target audience/content rating/category,store assets/screenshots
ROAD:
now=closed_testing_blockers: provide upload signing secret; confirm/rename applicationId before first Play upload; publish privacy policy URL; finalize Data Safety/content rating/target audience/category
next=produce signed AAB from app/build/outputs/bundle/release/app-release.aab using configured release signing; upload to Play internal/closed testing after assets complete
later=app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:32:* - It makes future "Time Travel" (replay log into a past snapshot) possible.
LINK:
meta=../../../projects/MultiTimeTracker/dev/project.metadata.json
human=../../human/projects/multitimetracker/overview.md
legacy=../../../projects/MultiTimeTracker/dev/legacy
repo=../../../projects/MultiTimeTracker
play_docs=C:/Users/seste/Documents/MTT/dev/human/play_store
OPEN:
open=capsulization_feature_ownership: 100 percent strict including SINCE_WHEN after prompt #462918; MainViewModel still supplies shared composition/infrastructure APIs to capsules
open=prompt_914506: p0_release_build=NEEDS_SECRET; privacy_policy/data_safety/store_listing/store_assets=NEEDS_USER_INPUT; closed_testing_ready=false until blockers resolved
