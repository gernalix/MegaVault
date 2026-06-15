# MultiTimeTracker Troubleshooting

## Sync status / autoexport v531
- Indicatore top bar: ✅ significa che `last_successful_export_at` copre `last_database_mutation_at` con tolleranza massima 3 secondi; ⟳ indica export in corso; ❌ indica modifiche persistenti non ancora esportate; ⚠ indica ultimo export fallito.
- Debounce autoexport: 1200 ms dopo una mutazione persistente. Durante il debounce e' normale vedere ❌ finche' l'export non parte o termina.
- Anti-loop: se l'indicatore resta su ⟳ o l'export count cresce senza nuove mutazioni utente, controllare che solo `PersistentMutationTracker.record` aggiorni `last_database_mutation_at`; i metadati sync non devono chiamarlo.
- Restore: per diagnosi usare solo `multitimer.db` e `multitimer.db.bak`; ignorare sempre `multitimer.db.tmp` come candidato.
- Query minima file SAF: `sqlite3 multitimer.db 'pragma integrity_check'`; ripetere su `.bak` se il primario fallisce.

## Audit parita DB interno/SAF v530
- Controllo minimo: non basta verificare che `multitimer.db` esista; confrontare schema e righe delle 17 tabelle utente interne contro il file SAF.
- Query utili: `sqlite3 multitimer.db '.tables'`, `sqlite3 multitimer.db 'pragma quick_check'`, `sqlite3 multitimer.db \"select name,type from sqlite_master where type in ('table','view') order by type,name\"`.
- Tabelle attese: `snapshot`, `snapshot_history`, `snapshot_payloads`, `audit_events`, `ui_prefs_mirror`, `integrity_stats`, `sessions`, `session_tags`, `quick_event_templates`, `quick_event_template_tags`, `quick_event_entries`, `quick_event_entry_tags`, `quick_event_template_fields`, `quick_event_entry_field_values`, `quick_event_macros`, `quick_event_macro_tags`, `quick_event_macro_actions`.
- Timestamp: per ispezione usare le viste `export_*_utc_z`; i campi runtime restano epoch ms UTC e la UI continua a renderizzare in timezone locale.
- Test automatico: `./gradlew :app:connectedDeviceTestAndroidTest -Pmtt.testBuildType=deviceTest -Pandroid.testInstrumentationRunnerArguments.class=com.example.multitimetracker.persistence.PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically --console=plain --no-daemon`.
- Nota TCL `#518204`: il gate live e' PASS quando il device appare online via mDNS/TCP, per esempio `192.168.1.200:33771`; se `:5555` rifiuta ma `adb mdns services` mostra `_adb-tls-connect`, collegarsi alla porta mDNS e rieseguire il test mirato prima di dichiarare PASS.

## Save failed `tasks: 1 -> 0` v529
- Sintomo: ogni creazione o salvataggio mostra `Save failed` e `Critical persistent data loss blocked: tasks: 1 -> 0`.
- Causa verificata nel prompt `#418762`: il campo `tasks` e' legacy/compat e puo essere vuoto in uno snapshot runtime valido; non va usato come drop critico nei salvataggi runtime.
- Regola corretta: salvataggi runtime confrontano solo campi autorevoli/runtime-completi; import/replace DB completi continuano a bloccare anche `tasks` N>0->0.
- SAF: se i Parent Tag risultano salvati internamente ma non nel file esterno, controllare il primario `multitimer.db`, non solo `.bak`; in v529 il primario viene copiato e validato esplicitamente.
- Verifica rapida: `sqlite3 multitimer.db 'pragma quick_check'`, poi cercare nel JSON snapshot Since When/Parent Tag e controllare che `multitimer.db` non sia 0 byte.

## Incidente dati/export v528
- Sintomo: tab Since When vuota, Parent Tag persi, export fermo o apparentemente vecchio, molti `.tmp`/`.bak`.
- Causa verificata nel prompt `#739284`: rollback automatico dopo import DB valido; il mismatch era runtime (`activation-signature`), non corruzione del DB.
- Controllo rapido DB interno: leggere `databases/multitimer.db`, tabella `snapshot`, JSON path `lifePeriods` e `tagParents`; usare anche `integrity_stats` per i conteggi.
- Controllo SAF: verificare `multitimer.db`, `multitimer.db.bak`, eventuali `multitimer.db.tmp`; nessun tmp deve essere considerato valido senza integrity/schema/conteggi.
- Nuovo log: `files/forensic_events.jsonl` nel sandbox app e best-effort `logs/forensic_events.jsonl` nel folder SAF.
- Invariante: nessuna entita persistente puo sparire silenziosamente; ogni export SQLite SAF deve essere lossless, atomico, verificato e tracciabile.
- Se una tabella critica passa da N>0 a 0, il file candidato va trattato come incidente, non promosso; preservare l'ultimo DB/snapshot valido.

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
