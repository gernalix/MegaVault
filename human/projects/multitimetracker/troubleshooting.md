# MultiTimeTracker Troubleshooting

## Problemi e sintomi rilevati nel codice
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:67:// v138 Capsule Audit Engine: emit known capsule boundary leaks in Logcat (debug only)
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:254:is FirstRunSetupState.RestoreFailed -> context.getString(R.string.first_run_restore_failed_title)
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:296:is FirstRunSetupState.RestoreFailed -> context.getString(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:298:R.string.first_run_restore_failed_keep_current_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:300:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:325:FirstRunFallbackReason.RESTORE_FAILED -> context.getString(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:327:R.string.first_run_restore_failed_keep_current_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:329:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:27:RESTORE_FAILED,
- app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt:49:data class RestoreFailed(
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:124:private val setPersistenceFailureReport: (String?) -> Unit,
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:125:private val showPersistenceFailureToast: (Context) -> Unit,
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:242:persistCurrentSnapshotOrThrow(showFailureUi = false, allowDuringPendingRestart = true)
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:252:persistCurrentSnapshotOrThrow(showFailureUi = false, allowDuringPendingRestart = true)
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:309:persistOrThrow(showFailureUi = true)
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:318:showFailureUi = true,
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:326:fun persistOrThrow(showFailureUi: Boolean) {
- app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt:328:showFailureUi = showFailureUi,

## Comandi/verifiche utili trovati
- UNKNOWN: nessun comando rilevato in build/script/CI.

## Safety prima di correggere
- app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:46:import com.example.multitimetracker.perf.StartupPerfTrace
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:55:private enum class FirstRunWorkStep {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create") {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:98:private fun MultiTimeTrackerApp(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:104:val integrityBlock by vm.integrityBlock.collectAsState()
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:131:onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
- app/src/main/AndroidManifest.xml:15:android:allowBackup="false"
- app/src/main/AndroidManifest.xml:17:android:fullBackupContent="@xml/backup_rules"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:39:import com.example.multitimetracker.export.BackupFolderStore
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:71:// v67: Defensive hardening for session-only schema (some DBs may miss tables despite user_version).
