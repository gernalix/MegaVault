META:
name=MultiTimeTracker
slug=multitimetracker
path=/home/daniele/codex-workspace/projects/MultiTimeTracker
remote=https://github.com/gernalix/MultiTimeTracker.git
branch=codex/v488-release-safe-ui-lockdown
verified_commit=80f88c0
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags a...
STACK:
lang=Kotlin,Python,Shell;fw=Gradle,Jetpack Compose;db=SQLite;platform=Android;tools=ADB,Chrome
MAP:
entry=app/src/main/AndroidManifest.xml,app/src/main/java/com/example/multitimetracker/MainActivity.kt,benchmark/src/main/AndroidManifest.xml
core=app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt
core=app/src/main/java/com/example/multitimetracker/SessionOnlyGuards.kt
core=app/src/main/java/com/example/multitimetracker/SingleSubmitGuard.kt
core=app/src/main/java/com/example/multitimetracker/TagRenameProjection.kt
core=app/src/main/java/com/example/multitimetracker/TimeFenceNotifier.kt
core=app/src/main/java/com/example/multitimetracker/TimeFenceTimerReceiver.kt
core=app/src/main/java/com/example/multitimetracker/TimeFenceTimerScheduler.kt
core=app/src/main/java/com/example/multitimetracker/TimedSessionSupport.kt
ui=app/src/main/java/com/example/multitimer/ui/EditSessionDialog.kt
ui=app/src/main/java/com/example/multitimer/viewmodel/TaskViewModel.kt
ui=app/src/main/java/com/example/multitimetracker/MainViewModel.kt
ui=app/src/main/java/com/example/multitimetracker/MainViewModelRecoveryCoordinator.kt
ui=app/src/main/java/com/example/multitimetracker/TimeFenceFullScreenActivity.kt
ui=app/src/main/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModel.kt
ui=app/src/main/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModel.kt
ui=app/src/main/java/com/example/multitimetracker/capsules/chains/ChainsCapsuleViewModel.kt
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt
db=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt
db=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt
db=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt
db=app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsuleAccess.kt
db=app/src/main/java/com/example/multitimetracker/data/importexport/FallbackRestoreManager.kt
db=app/src/main/java/com/example/multitimetracker/data/importexport/ImportExportIntegrityValidator.kt
db=app/src/main/java/com/example/multitimetracker/export/AuthoritativeExportPayload.kt
tests=app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/export/AuthoritativeExportPayloadBuilderTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/persistence/AuthoritativeSessionRuntimeTest.kt
tests=app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTest.kt
scripts=dev/tools/check_hardcoded_ui_strings.py
scripts=dev/tools/check_single_submit_confirm_buttons.sh
scripts=dev/tools/clean_transients.sh
scripts=preflight_check.ps1
scripts=tools/mtt_helper.py
build=app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- app/src/main/java/com/example/multitimetracker/MainActivity.kt=>FirstRunWorkStep,MainActivity,onCreate,MultiTimeTrac
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt=>BackupFolderInspection,FolderChosenEmpty,
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt=>PreparedSnapshotRuntimeState,App
- app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt=>FinalizedImpor
- app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt=>ImportExportSnapshot,ImportEx
- app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsuleAccess.kt=>ImportExportCapsuleAcce
- app/src/main/java/com/example/multitimetracker/data/importexport/FallbackRestoreManager.kt=>FallbackRestoreManager,s
- app/src/main/java/com/example/multitimetracker/data/importexport/ImportExportIntegrityValidator.kt=>ImportExportCoun
- app/src/main/java/com/example/multitimetracker/export/AuthoritativeExportPayload.kt=>AuthoritativeExportPayload,Sign
- app/src/main/java/com/example/multitimetracker/export/BackupFolderStore.kt=>DataDirDescriptor,BackupFolderStore,safe
- app/src/main/java/com/example/multitimetracker/export/BackupMetaWriter.kt=>BackupMetaWriter,write
- app/src/main/java/com/example/multitimetracker/export/BackupSchema.kt=>Entry,ParsedManifest,BackupSchema,buildManife
- app/src/main/java/com/example/multitimetracker/export/CsvExporter.kt=>TagTotalRow,CsvExporter,csvEscape,shareExportD
- app/src/main/java/com/example/multitimetracker/export/CsvImporter.kt=>DictPayload,RuntimePayload,QuickEventsPayload,
- app/src/main/AndroidManifest.xml:8:<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
- app/src/main/AndroidManifest.xml:9:<!-- Haptic feedback for alerts and quick widget starts. -->
FLOW:
- app/src/main/AndroidManifest.xml:8:<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
- app/src/main/AndroidManifest.xml:9:<!-- Haptic feedback for alerts and quick widget starts. -->
- app/src/main/AndroidManifest.xml:15:android:allowBackup="false"
- app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
- app/src/main/AndroidManifest.xml:31:android:exported="false"
- app/src/main/AndroidManifest.xml:40:android:exported="true"
- app/src/main/AndroidManifest.xml:50:android:exported="false"
- app/src/main/AndroidManifest.xml:58:android:name=".widget.QuickSessionWidgetClickActivity"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:5:import com.example.multitimetracker.util.CapsuleWri
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:7:import android.Manifest
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:8:import android.content.Intent
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:9:import android.content.Context
INV:
arch=app/src/main/AndroidManifest.xml:2:<manifest xmlns:android="http://schemas.android.com/apk/res/android"
arch=app/src/main/AndroidManifest.xml:3:xmlns:tools="http://schemas.android.com/tools">
arch=app/src/main/AndroidManifest.xml:6:<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
arch=app/src/main/AndroidManifest.xml:8:<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
arch=app/src/main/AndroidManifest.xml:10:<uses-permission android:name="android.permission.VIBRATE" />
arch=app/src/main/AndroidManifest.xml:12:<uses-permission android:name="android.permission.USE_FULL_SCREEN_INTENT" />
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:3:import com.example.multitimetracker.
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKi
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:13:LEGACY_BACKUP_ONLY,
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:17:data class BackupFolderInspection(
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:19:val kind: BackupFolderInspectionKin
data=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:25:LEGACY_BACKUP_ONLY,
safety=app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:46:import com.example.multitimetracker.perf.Start
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:55:private enum class FirstRunWorkStep {
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_cre
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:98:private fun MultiTimeTrackerApp(
safety=app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.colle
ux=app/src/main/AndroidManifest.xml:12:<uses-permission android:name="android.permission.USE_FULL_SCREEN_INTENT" />
ux=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:16:import com.example.multiti
ux=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:36:import kotlinx.coroutines.
ux=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:102:private val currentAppVer
version=app/src/main/AndroidManifest.xml:2:<manifest xmlns:android="http://schemas.android.com/apk/res/android"
version=app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only s
version=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:102:private val currentAppVer
version=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:19:import c
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- app/build.gradle
- app/build.gradle.kts
- benchmark/build.gradle.kts
- build.gradle.kts
- gradle.properties
- settings.gradle.kts
TEST:
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:3:import androidx.test.platform.app
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:9:import org.junit.Assert.*
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:12:* Instrumented test, which will
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:17:class ExampleInstrumentedTest {
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:18:@Test
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:21:val appContext = Instrumentation
- app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt:22:assertEquals(BuildConfig.APPLICA
- app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt:13:import org.junit.Assert.assert
- app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt:14:import org.junit.Assert.assert
- app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt:15:import org.junit.Assert.assert
- app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt:16:import org.junit.Assert.assert
- app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt:17:import org.junit.Assert.assert
DATA:
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:3:import com.example.multitimetracker.
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKi
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:13:LEGACY_BACKUP_ONLY,
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:17:data class BackupFolderInspection(
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:19:val kind: BackupFolderInspectionKin
db=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:25:LEGACY_BACKUP_ONLY,
backup=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:3:import com.example.multitimetracker.
backup=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKi
backup=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:13:LEGACY_BACKUP_ONLY,
backup=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:17:data class BackupFolderInspection(
import=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:3:import com.example.multitimetracker.
import=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:5:import android.content.Cont
import=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:6:import android.widget.Toast
export=app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:14:import com.example.multiti
export=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:3:package c
export=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:5:import co
migration=UNKNOWN
retention=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:3:import com.example.multitimetracker.
retention=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:10:enum class BackupFolderInspectionKi
retention=app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:17:data class BackupFolderInspection(
DNB:
- app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:46:import com.example.multitimetracker.perf.StartupPe
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:55:private enum class FirstRunWorkStep {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensu
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:98:private fun MultiTimeTrackerApp(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAs
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:131:onDispose { lifecycleOwner.lifecycle.removeObserv
- app/src/main/AndroidManifest.xml:15:android:allowBackup="false"
- app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
BUG:
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:67:// v138 Capsule Audit Engine: emit known capsule b
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:254:is FirstRunSetupState.RestoreFailed -> context.ge
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:296:is FirstRunSetupState.RestoreFailed -> context.ge
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:298:R.string.first_run_restore_failed_keep_current_bo
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:300:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:325:FirstRunFallbackReason.RESTORE_FAILED -> context.
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:327:R.string.first_run_restore_failed_keep_current_bo
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:329:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:27:RESTORE_FAILED,
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:49:data class RestoreFailed(
RISK:
- app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:46:import com.example.multitimetracker.perf.StartupPe
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:55:private enum class FirstRunWorkStep {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensu
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:98:private fun MultiTimeTrackerApp(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAs
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:131:onDispose { lifecycleOwner.lifecycle.removeObserv
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:188:// otherwise empty/default state could race again
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:63:private val canonicalSupportEntries = s
ROAD:
now=app/src/main/java/com/example/multitimetracker/MainActivity.kt:124:// we won't receive ON_RESUME and the "app usage"
next=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:98:// Persist p
later=app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:110:// Roll bac
LINK:
meta=../../../projects/MultiTimeTracker/dev/project.metadata.json
human=../../human/projects/multitimetracker/overview.md
legacy=../../../projects/MultiTimeTracker/dev/legacy
repo=../../../projects/MultiTimeTracker
OPEN:
- none
