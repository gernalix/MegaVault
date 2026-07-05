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
- Autoexport anti-storm `#947381`: mantenere `PersistentMutationTracker` come unico trigger per autoexport. Debounce documentato 1200 ms; gli aggiornamenti sync metadata non devono mai chiamare `record` o generare un nuovo export.
- SQLite SAF `#947381`: nessun percorso dell'app puo esportare, importare, ripristinare o copiare database SQLite senza checkpoint coerente, `integrity_check` riuscito e fallback `.bak` verificato.
- Copertura write path `#947381`: nessuna modifica persistente puo bypassare l'infrastruttura di autoexport; ogni nuovo repository/DAO/setting persistente deve aggiornare `last_database_mutation_at` e accodare autoexport, esclusi solo i metadati sync stessi.
- Parita SAF `#742913/#518204`: il test automatico v530 copre 17 tabelle e import dopo clear interno; il run live TCL e l'ispezione del DB reale sono PASS. Per futuri cambi schema/persistenza, non considerare chiuso un incidente dati senza prova device su `connectedDeviceTestAndroidTest` o ispezione DB reale equivalente.
- Timestamp export `#742913`: mantenere le viste `export_*_utc_z` allineate a ogni nuova tabella/colonna timestamp; le colonne runtime epoch ms UTC restano necessarie per compatibilita import.
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

---

## Merged GitHub Branch Details 20260705

- Incident `#947263` / `wrong_branch_play_store_work_v489_instead_of_v528`: il lavoro Play Store #914506/#517284/#684219 e' stato fatto su `codex/play-store-readiness-roadmap` v489 invece che sulla linea reale piu recente. `master` ora punta a `00ecfd85a50ba30b927e759d4ed766040a25081c` con `MTT_VERSION=534`; il commit storico v528 e' `8061d232e4afbf0e80e2cebbbf76233f7fa2fa18`.
- Regola release permanente: prima di qualsiasi lavoro release/Play Store/MultiTimeTracker verificare branch attuale, branch remoto piu recente, versionCode piu alto in tutti i branch, coerenza con MegaVault e coerenza con roadmap attiva. Se il branch corrente non contiene la versione piu alta nota, fermarsi e chiedere conferma.
- Stato #628914: `master` contiene la linea v535 Play Store readiness, commit `44c2b33e53ce98e02f95437bd5bc7eb3f16aa688`; backup pre-merge `backup/master-before-v535-play-store-merge-20260622-133603`.
- Prossima decisione: usare `master` v535 o superiore come base; eventuale upload AAB a Play Console dopo input owner.
- Play Store readiness dopo #628914: circa 92 percento offline. PASS: docs Play Store, signing locale, APK/AAB firmati, lint/test/build release. NEEDS_USER_INPUT: applicationId definitivo, privacy URL pubblico, publisher/contact, Data Safety finale in Console, store assets, tester list, rollout closed testing.
- Play Store `#684219`: storico su branch v489 sbagliato; release build, upload keystore locale, APK/AAB firmati, copy-paste pack, closed testing steps e release notes erano PASS solo su `codex/play-store-readiness-roadmap` e non provano readiness di `master` v534.
- Stato `#684219`: Play Store readiness 92 percento; `dev/human/play_store/*` contiene template/checklist/copy pronti, ma closed testing effettivo resta bloccato da input umani e Play Console.
