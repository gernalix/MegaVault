# MultiTimeTracker Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `app/src/main/java/com/example/multitimetracker/MainActivity.kt`: FirstRunWorkStep, MainActivity, onCreate, MultiTimeTrackerApp, resolveContinuationMode, refreshSetupState, onReceive, requiresExactAlarmPermission
- `app/src/main/java/com/example/multitimetracker/capsules/tags/TagsCapsuleViewModel.kt`: owner CRUD TAGS, audit/persist, hierarchy validation, rename session title projection.
- `app/src/main/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModel.kt`: owner ALERTS rule mutation, runtime evaluation, timer/notification reconciliation.
- `app/src/main/java/com/example/multitimetracker/capsules/sessions/SessionOwnerCapsuleViewModel.kt`: owner NOW/TIMELINE session CRUD, running-session creation and stop policies.
- `app/src/main/java/com/example/multitimetracker/capsules/quickevents/QuickEventsCapsuleViewModel.kt`: owner QUICK_EVENTS template/entry/macro mutation and DB refresh.
- `app/src/main/java/com/example/multitimetracker/capsules/chains/ChainsCapsuleViewModel.kt`: owner CHAINS mutation, start/stop and session-stop auto advance.
- `app/src/main/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModel.kt`: owner AUDIT_LOG filters, event refresh/projection, clear, undo, audit state and undo write suppression.
- `app/src/main/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModel.kt`: owner SINCE_WHEN LifePeriod create/update/delete, duplicate-submit guard and valid-tag filtering.
- `app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt`: source-level guard for TAGS, ALERTS, session owner, CHAINS, QUICK_EVENTS, CSV ImportExport, AUDIT_LOG and SINCE_WHEN ownership boundaries.
- `app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt`: JVM guard for AUDIT_LOG category mapping, filters, undo flag and time-machine projection.
- `app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt`: JVM guard for SINCE_WHEN LifePeriod mutation, write guard and tag filtering.
- `app/src/main/java/com/example/multitimetracker/persistence/SqliteVault.kt`: stable vault export con nomi esatti per database primario, temporaneo ed emergency copy; v528 valida tmp/promoted DB con integrity/schema/conteggi critici e non promuove candidati con perdita N>0->0.
- `app/src/main/java/com/example/multitimetracker/persistence/PersistentMutationTracker.kt`: coda autoexport single-flight con debounce 1200 ms, coalescing richieste ravvicinate e follow-up export per mutazioni arrivate durante export.
- `app/src/main/java/com/example/multitimetracker/persistence/SyncStatusStore.kt`: stato sync persistito in UTC/Z (`last_database_mutation_at`, `last_successful_export_at`, `last_export_attempt_at`, status, errore, file SAF, integrity_check) per indicatore UI ✅/⟳/❌/⚠.
- `app/src/main/java/com/example/multitimetracker/persistence/CriticalDataGuard.kt`: guardia conteggi critici per tasks, sessions, tags, tagParents, lifePeriods, quick events, chains e settings.
- `app/src/main/java/com/example/multitimetracker/persistence/ForensicLog.kt`: log persistente JSONL per export/import/recovery/critical drop con timestamp UTC, file coinvolti, conteggi e stacktrace.
- `app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt`: BackupFolderInspection, FolderChosenEmpty, ExistingDataFound, RestoreSucceeded, RestoreFailed, FallbackToContinuation, FirstRunContinuationMode, BackupFolderInspectionKind
- `app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt`: PreparedSnapshotRuntimeState, AppliedSnapshotState, MainViewModelSnapshotCoordinator, SnapshotLoadMode, InstallAtMsPolicy, reconcileSnapshotTagsForPersistence, unionTotalMs
- `app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt`: FinalizedImport, ImportExportCapsuleViewModel, ImportRollbackOutcome, createImportExportCapsule, showLongToast, setBackupRootFolder, inspectBackupFolder, exportBackup, exportCsv, importCsv
- `app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsule.kt`: ImportExportSnapshot, ImportExportCapsule, setBackupRootFolder, inspectBackupFolder, exportBackup, exportCsv, importCsv, importDatabaseFromUri, restoreLastPreImportBackup, importBackup
- `app/src/main/java/com/example/multitimetracker/capsules/system/ImportExportCapsuleAccess.kt`: ImportExportCapsuleAccess, exportSnapshot, activateImportedSnapshotFromStore, persist, scheduleAutoBackup, computeBackupSignature, setLastBackupSignature, buildManualExportZipName
- `app/src/main/java/com/example/multitimetracker/data/importexport/FallbackRestoreManager.kt`: FallbackRestoreManager, shouldTriggerFallback, buildUserMessage
- `app/src/main/java/com/example/multitimetracker/data/importexport/ImportExportIntegrityValidator.kt`: ImportExportCounts, ImportExportIntegrityValidator, compare
- `app/src/main/java/com/example/multitimetracker/export/AuthoritativeExportPayload.kt`: AuthoritativeExportPayload, SignatureMode, AuthoritativeExportPayloadBuilder, buildSessionOnlyRuntimeTasks, fromLegacyState, fromSessionTables, fromSnapshot, signature
- `app/src/main/java/com/example/multitimetracker/export/BackupFolderStore.kt`: DataDirDescriptor, BackupFolderStore, safeRoot, safeCanRead, safeCanWrite, getTreeUri, saveTreeUri, clearTreeUri
- `app/src/main/java/com/example/multitimetracker/export/BackupMetaWriter.kt`: BackupMetaWriter, write
- `app/src/main/java/com/example/multitimetracker/export/BackupSchema.kt`: Entry, ParsedManifest, BackupSchema, buildManifestJson, parseManifestJson
- `app/src/main/java/com/example/multitimetracker/export/CsvExporter.kt`: TagTotalRow, CsvExporter, csvEscape, shareExportDir, shareExportFile, buildDictJson, buildRuntimeJson, buildQuickEventsJson
- `app/src/main/java/com/example/multitimetracker/export/CsvImporter.kt`: DictPayload, RuntimePayload, QuickEventsPayload, ImportedSnapshot, CsvImporter, pickByNameOrPrefix, pickDocByNameOrPrefix, i
- `app/src/main/java/com/example/multitimetracker/export/DocHash.kt`: DocHash, sha256Hex
- `app/src/main/java/com/example/multitimetracker/export/ShareUtils.kt`: ShareUtils, shareFiles
- `app/src/main/java/com/example/multitimetracker/export/SnapshotExportAdapter.kt`: SnapshotExportAdapter, exportAllToDirectoryFromSnapshot
- `app/src/main/java/com/example/multitimetracker/export/VaultFolders.kt`: Root, VaultFolders, ensureRoot, dir, ensureNamedVaultDir, ensureAutoexportsDir
- `app/src/main/java/com/example/multitimetracker/export/VaultIndex.kt`: Kind, VaultIndex, record, computeSha256Hex, readArrayOrEmpty, writeArray
- `app/src/main/java/com/example/multitimetracker/export/VaultManifest.kt`: VaultManifest, ensureManifestFile, appendEntry, readJsonArray, writeJsonArray
- `app/src/main/java/com/example/multitimetracker/export/VaultRetention.kt`: Bucket, VaultRetention, pruneSnapshots, keepBuckets, bucketKey, parseMsFromName
- `app/src/main/java/com/example/multitimetracker/export/ZipBackupExporter.kt`: Result, ZipBackupExporter, exportCsvJsonZip

## Confini operativi
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
- app/src/main/java/com/example/multitimetracker/MainActivity.kt: `onCreate` resta leggero; lo schema ensure v527 gira in IO tramite `ensureStartupSchemasForLaunch`.

## Parita DB interno <-> SAF v530 (`#742913`)
- Il file SAF stabile `multitimer.db` e' una copia SQLite validata del DB interno dopo checkpoint WAL; non e' un export parziale.
- Tabelle utente analizzate e reimportabili: `snapshot`, `snapshot_history`, `snapshot_payloads`, `audit_events`, `ui_prefs_mirror`, `integrity_stats`, `sessions`, `session_tags`, `quick_event_templates`, `quick_event_template_tags`, `quick_event_entries`, `quick_event_entry_tags`, `quick_event_template_fields`, `quick_event_entry_field_values`, `quick_event_macros`, `quick_event_macro_tags`, `quick_event_macro_actions`.
- Matrice copertura: sessioni -> `sessions`/`session_tags` e snapshot JSON `closedSessions`/`tagSessions`; eventi -> `quick_event_*` e snapshot JSON Quick Events; Since When/life periods -> snapshot JSON `lifePeriods`; tag -> snapshot JSON `tags` piu join tables; parent tag -> snapshot JSON `tagParents`; impostazioni -> `ui_prefs_mirror`; archivi/soft-delete -> `isArchived`/`isDeleted`/`deletedAtMs` e colonne `is_archived`/`deleted_at_ms`; capsule/state -> snapshot JSON runtime state, `audit_events`, `integrity_stats`, history tables.
- Location/luoghi: nessuna entita location/geofence geografica e' presente nel modello attivo; `TimeFenceRule` e' temporale/tag-driven, non location-driven.
- Timestamp: le colonne autorevoli restano epoch ms UTC per compatibilita runtime/import; il DB esportato contiene viste `export_*_utc_z` per ispezione UTC/Z di snapshot, history, audit, settings, integrity, sessions e Quick Events.
- Test aggiunto: `PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically` crea fixture con sessioni, eventi, Since When, tag, parent tag, archivi/soft-delete, settings e capsule state; esporta SAF; confronta schema+righe di tutte le tabelle; cancella DB interno; importa dal SAF; ricontrolla snapshot, settings e tabelle.

## Autoexport/restore SQLite SAF v531 (`#947381`)
- Export obbligatorio: checkpoint WAL riuscito o abort; `integrity_check` del DB sorgente prima di toccare SAF; copia temporanea `multitimer.db.tmp`; validazione tmp; aggiornamento e validazione `multitimer.db.bak`; promozione primaria; `integrity_check` finale.
- Restore automatico: prova `multitimer.db`, poi `multitimer.db.bak`; ogni candidato deve esistere, aprirsi come SQLite e passare `integrity_check`; `multitimer.db.tmp` e' solo file temporaneo e viene ignorato.
- UI sync: top bar sempre visibile; ✅ solo se l'ultimo export riuscito copre l'ultima mutazione DB con tolleranza massima 3 secondi, ❌ per modifiche ancora non esportate, ⚠ per ultimo export fallito, ⟳ durante export.
