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

## Performance Events v526
- Sintomo: scroll Eventi janky con molte chip/card raggruppate.
- Causa: `LazyColumn` non bastava perche ogni sezione renderizzava una `FlowRow` completa; sezioni grandi componevano molte card insieme.
- Fix: `QuickEventsScreen` usa `LazyVerticalGrid` con item key stabili e header full-span; stato menu/edit resta locale all'item.
- Startup: il refresh DB Eventi non parte piu in `MainViewModel.initialize`; parte async quando si apre Events.
- Verifica: usare clone `com.example.multitimetracker.devicetest`; controllare logcat tag `MTT_STARTUP` per `quick_events_screen_snapshot` solo dopo apertura Events.

## Performance/stabilita v527
- Sintomo: startup e ritorno app percepiti lenti, rischio ANR/kill in background su device basso.
- Causa verificata: lavoro SQLite/schema e inizializzazione snapshot/integrity sul percorso iniziale; Eventi/Since When avevano allocazioni ripetute nel rendering.
- Fix: `MainActivity.onCreate` resta leggero; schema/init girano su IO; cache schema invalidata su import/restore/switch DB/fresh clear.
- Misura utile: usare logcat `MTT_STARTUP`; in `#294816` su TCL sbloccato il clone ha cold WaitTime medio 669 ms e warm medio 10.2 ms.
- Chiusure in background: in v527 non sono emersi `AndroidRuntime`, `FATAL EXCEPTION`, ANR o lmkd dell'app; distinguere sempre crash reale da `ActivityManager` force-stop/test e low-memory/system pressure.
- TCL: se `dumpsys window` mostra `mCurrentFocus=NotificationShade` e `mDreamingLockscreen=true`, scroll/tap/tab benchmark e Macrobenchmark UIAutomator non misurano la UI reale; in `#294816` il device era sbloccato/testabile.
