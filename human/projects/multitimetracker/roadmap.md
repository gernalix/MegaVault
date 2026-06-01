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
- Capsulizzazione `#539824`: session CRUD/stop policy, QUICK_EVENTS, CHAINS, snapshot ALERTS reconciliation e CSV ImportExport sono dietro capsule owner/API esplicite.
- Capsulizzazione `#728419`: AUDIT_LOG filters/event refresh/clear/undo sono in `AuditLogCapsuleViewModel` con API esplicita verso session/tag owner e guardrail in `CapsuleBoundaryOwnershipTest`.
- Residuo MainViewModel: hook infrastrutturali comuni per composition root (state update, persistence, context, logging, core access), non business logic di feature documentata.
- Stato `#728419`: capsulizzazione stimata 100 percento per ownership feature documentata dopo test JVM e Pixel clone verdi; future riduzioni devono riguardare solo il peso infrastrutturale della shell.
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
