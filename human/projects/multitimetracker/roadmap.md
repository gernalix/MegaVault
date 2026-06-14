# MultiTimeTracker Roadmap

## Segnali dal codice
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:124:// we won't receive ON_RESUME and the "app usage" counter would stay frozen until the next resume.
- app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:98:// Persist permission for future sessions.
- app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:110:// Roll back the saved URI to avoid future "Export fallito" loops.
- app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt:250:// clear the saved URI so the next tap will re-open the folder picker.
- app/src/main/java/com/example/multitimetracker/export/CsvImporter.kt:920:val next = if (i + 1 < line.length) line[i + 1] else null
- app/src/main/java/com/example/multitimetracker/export/CsvImporter.kt:921:if (next == '"') {
- app/src/main/java/com/example/multitimetracker/export/ZipBackupExporter.kt:54:zos.putNextEntry(entry)
- app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:32:* - It makes future "Time Travel" (replay log into a past snapshot) possible.
- app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:33:* - It makes future Multi-DB isolation possible (state vaults vs log streams).
- app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:79:while (c.moveToNext()) {
- app/src/main/java/com/example/multitimetracker/persistence/AuditLogSqlite.kt:93:fun hasLaterEventsForEntity(
- app/src/main/java/com/example/multitimetracker/persistence/IntegrityStatsSqlite.kt:169:while (c.moveToNext()) {

## Debito/rischi da considerare
- Integrita dati `#418762`: distinguere sempre snapshot runtime/candidati temporanei/DB completi. I salvataggi runtime non devono usare `tasks` legacy come fonte autorevole; import/replace completi devono continuare a bloccare veri drop critici.
- Export SAF `#418762`: non usare `DocumentFile.renameTo` come unica promozione del primario stabile. Ogni export deve validare tmp, `.bak` e primario finale prima di dichiarare successo.
- Test persistence gate `#418762`: ogni patch che tocca persistenza, DB, export, import, recovery, backup, integrity check o guardie dati richiede creazione reale UI o device-equivalent di sessione/task, evento, Since When, Parent Tag, modifica entita, export SAF e restart persistence.
- Integrita dati `#739284`: mantenere il guard current->candidate su ogni futuro import/restore/vault switch; non aggiungere import automatici silenziosi da snapshot storiche.
- Export SAF `#739284`: eventuali future snapshot storiche devono restare max 10, validate prima della promozione, e non devono poter sovrascrivere DB piu nuovi senza log esplicito.
- Recovery `#739284`: migliorare UI/report forense per mostrare all'utente il motivo specifico del blocco critico, non solo il messaggio generico di import non leggibile.
- Performance `#817463`: integrity/snapshot load resta costo reale ma non blocca piu `onCreate`; ottimizzazioni future devono preservare rollback/import/restore e non introdurre cache fragile.
- Testing TCL `#294816`: benchmark visuali scroll/tap/tab su TCL sbloccato completati; mantenere Pixel fuori da debug/stress quando la policy richiede TCL-only.
- Background closure `#817463/#294816`: non sono emersi crash/ANR app; causa probabile residua e' terminazione processo/sistema sotto pressione. Tenere memoria/lavoro background bassi e continuare a monitorare log lmkd/ActivityManager.
- Capsulizzazione `#539824`: session CRUD/stop policy, QUICK_EVENTS, CHAINS, snapshot ALERTS reconciliation e CSV ImportExport sono dietro capsule owner/API esplicite.
- Capsulizzazione `#728419`: AUDIT_LOG filters/event refresh/clear/undo sono in `AuditLogCapsuleViewModel` con API esplicita verso session/tag owner e guardrail in `CapsuleBoundaryOwnershipTest`.
- Capsulizzazione `#462918`: SINCE_WHEN/LifePeriod CRUD e duplicate-submit guard sono in `SinceWhenCapsuleViewModel`; il gap trovato nell'audit post-refactor e' chiuso.
- Residuo MainViewModel: hook infrastrutturali comuni per composition root (state update, persistence, context, logging, core access), non business logic di feature documentata.
- Stato `#462918`: capsulizzazione stimata 100 percento strict per ownership feature auditata dopo test JVM e Pixel clone verdi; future riduzioni devono riguardare solo il peso infrastrutturale della shell.
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:67:// v138 Capsule Audit Engine: emit known capsule boundary leaks in Logcat (debug only)
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:254:is FirstRunSetupState.RestoreFailed -> context.getString(R.string.first_run_restore_failed_title)
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:296:is FirstRunSetupState.RestoreFailed -> context.getString(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:298:R.string.first_run_restore_failed_keep_current_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:300:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:325:FirstRunFallbackReason.RESTORE_FAILED -> context.getString(
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:327:R.string.first_run_restore_failed_keep_current_body_fmt
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:329:R.string.first_run_restore_failed_empty_body_fmt
- app/src/main/AndroidManifest.xml:53:android:showWhenLocked="true"
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:46:import com.example.multitimetracker.perf.StartupPerfTrace
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:55:private enum class FirstRunWorkStep {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:66:StartupPerfTrace.section("main_activity_on_create") {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:72:val schemaChanged = StartupPerfTrace.section("ensure_session_tables") {
- app/src/main/java/com/example/multitimetracker/MainActivity.kt:98:private fun MultiTimeTrackerApp(
