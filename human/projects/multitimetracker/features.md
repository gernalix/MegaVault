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
