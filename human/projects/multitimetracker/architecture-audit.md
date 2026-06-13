# MultiTimeTracker Architecture Audit

## Prompt #739284
- Scope: incidente P0 integrita dati Since When/Parent Tag, export/backup SAF e accumulo tmp/bak.
- Code commit: `8061d232e4afbf0e80e2cebbbf76233f7fa2fa18` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Found: nessun Room/DAO/migration/fallbackToDestructiveMigration; la persistenza autorevole e' SQLite custom `SnapshotStore`/`SnapshotSqlite`.
- Found: un DB importato valido ha passato integrity e conteggi con `lifePeriods=7` e `tagParents=6`, poi `activation-signature` runtime ha causato rollback automatico al backup pre-import vuoto.
- Found: `SqliteVault.exportToUserFolderIfConfigured` ingoiava eccezioni; export/tmp/promozione non verificavano conteggi critici prima di sostituire lo stable SAF DB.
- Fixed: `CriticalDataGuard` confronta conteggi critici da snapshot/DB/file e blocca drop N>0->0 prima di snapshot overwrite, import/restore promotion e export promotion.
- Fixed: `ForensicLog` scrive JSONL interno e best-effort SAF per export/import/recovery/critical drop con timestamp UTC, file sorgente/destinazione, conteggi e stacktrace.
- Fixed: import DB validato non viene piu rollbackato per fallimento runtime activation; il DB resta, il report indica attivazione runtime rinviata.
- Fixed: restore interno confronta current->candidate prima del move, preserva settings mirror nei backup storici e lascia il DB corrente se il candidato causerebbe perdita.
- Validation: `testDebugUnitTest` PASS; targeted `connectedDeviceTestAndroidTest` TCL su recovery/import/export PASS 26 test, 1 skip fixture, 0 failure; `assembleDebug` PASS.

## Prompt #817463
- Scope: audit performance/stabilita completo con policy test automatici solo su TCL.
- Code commit: `2548034f6c4fc7e4950f45600b41101faae7d764` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Found: `MainActivity.onCreate` eseguiva ancora hardening schema SQLite; `MainViewModel.initialize` caricava integrity/snapshot sul percorso startup UI.
- Fixed: onCreate resta sottile; schema ensure, integrity gate, snapshot load e vault auto-restore girano su `Dispatchers.IO`.
- Fixed: `SnapshotSqlite.ensureStartupSchemas` usa cache per DB version e invalidazione su import/restore/vault switch/fresh clear.
- Fixed: Events evita sort recent entries quando collassato e sort macro actions ripetuto; Since When evita map tag per card.
- Evidence TCL: real DB v526 onCreate medio 79.25 ms, ensure schema medio 50.73 ms; v527 finale onCreate medio circa 30.8 ms, ensure schema steady circa 2.3 ms; `#294816` TCL sbloccato clone cold medio 669 ms e warm medio 10.2 ms.
- Stability: log finali TCL senza `AndroidRuntime`, `FATAL EXCEPTION`, ANR, lmkd o `am_proc_died` app; clear-data/reinstall non crea dati utente (`sessions=0`, `session_tags=0`, `snapshot=0`).
- UI validation: `#294816` completa su TCL sbloccato; tap sessione, long press edit, Active tags, Eventi, Timeline, Since When, Settings, scroll rapido e background/foreground PASS. Pixel solo install/smoke finale v527 PASS.

## Prompt #847261
- Scope: capsule boundary audit and partial decomposition of legacy MainViewModel bridges.
- Code commit: `6ddeebb` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Before: TAGS CRUD, ALERTS reconciliation, NOW/TIMELINE session CRUD, QUICK_EVENTS, CHAINS, AUDIT_LOG and IMPORT_EXPORT hooks all crossed through MainViewModel.
- Fixed: TAGS owns CRUD/audit/persist/rename-projection through `TagsCapsuleViewModel` and owner primitives in `TagsCapsuleAccess`.
- Fixed: ALERTS owns rule mutation, runtime evaluation, timer schedule/cancel and notification reconciliation in `AlertsCapsuleViewModel`.
- Fixed: import/export device regression from the clone run by forcing exact stable vault names in `SqliteVault` for `multitimer.db`, `multitimer.db.tmp` and `multitimer.db.bak`.
- Guard: `CapsuleBoundaryOwnershipTest` prevents TAGS CRUD warnings from returning to MainViewModel and prevents ALERTS runtime reconciliation from moving back to MainViewModel.
- Validation: `compileDebugKotlin`, `testDebugUnitTest` and `assembleDebug` passed locally.
- Validation: Pixel 8a ran `connectedDeviceTestAndroidTest` through `connectedAndroidTest -Pmtt.testBuildType=deviceTest` on clone `com.example.multitimetracker.devicetest` v525: 53 tests, 3 skipped, 0 failed.
- Residual: NOW/TIMELINE session CRUD and stop policies still run through MainViewModel legacy wrappers.
- Residual: QUICK_EVENTS, CHAINS, AUDIT_LOG, IMPORT_EXPORT still use MainViewModel state/persistence hooks.
- Estimate: capsulization after prompt `#847261` is about 72 percent; 100 percent requires a session owner API and migration of remaining feature mutation bridges.

## Prompt #539824
- Scope: remove remaining legacy bridges where risk was bounded, keep MainViewModel as composition shell/infrastructure adapter.
- Code commit: `15c1d2246bf641bd21b69d53f7a5a526b900f545` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Before: capsulization estimated at 72 percent after `#847261`.
- Fixed: introduced `SessionOwnerCapsuleViewModel` and `SessionOwnerCapsuleAccess`; NOW/TIMELINE session CRUD and stop policies no longer live in MainViewModel business logic.
- Fixed: `ChainsCapsuleViewModel` owns chain create/update/delete/restore/purge/start/stop/advance; MainViewModel wrappers only delegate.
- Fixed: `QuickEventsCapsuleViewModel` owns template/entry/macro mutation and quick-event screen refresh.
- Fixed: `ImportExportCapsule` owns manual CSV export/import in addition to backup/import/restore flows.
- Fixed: `MainViewModelSnapshotCoordinator` no longer imports ALERTS reconciliation helpers directly; post-snapshot alarm reconciliation is behind `AlertsCapsuleViewModel.reconcileSnapshotRuntimeAlarms`.
- Guard: `CapsuleBoundaryOwnershipTest` now checks TAGS, ALERTS, session owner, CHAINS, QUICK_EVENTS and CSV ImportExport boundaries.
- Residual: AUDIT_LOG filters, event refresh, clear and undo orchestration still live in MainViewModel; this remains because undo crosses session restore, tag hierarchy, time-machine/history replay and audit DB semantics.
- Residual: MainViewModel still provides infrastructure hooks for state update, persistence, logging, context and shared cores to capsules.
- Estimate: capsulization after prompt `#539824` is about 92 percent. The missing 8 percent is mainly AUDIT_LOG owner extraction and further reduction of composition-root hooks.
- Validation: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` passed locally.
- Validation: Pixel 8a ran `connectedAndroidTest -Pmtt.testBuildType=deviceTest` on clone `com.example.multitimetracker.devicetest` / test app `com.example.multitimetracker.devicetest.test`: 53 tests, 3 skipped, 0 failed.

## Prompt #728419
- Scope: remove the last AUDIT_LOG legacy bridge from MainViewModel without changing DB compatibility or UX.
- Code commit: `d7f347e155e32757a23a968391fbcd5b15fe4060` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Before: capsulization estimated at 92 percent after `#539824`; remaining bridge was AUDIT_LOG filter state, event refresh, clear and undo orchestration in MainViewModel.
- Fixed: `AuditLogCapsuleViewModel` now owns audit event state, filters, preference persistence, event refresh/projection, clear, undo, audit DB writes and undo write suppression.
- Fixed: undo calls session/tag owners only through `AuditLogCapsuleAccess`: session delete, tag delete, tag parent restore, stopped-session restore and post-undo runtime refresh.
- Fixed: MainViewModel no longer owns `_auditEvents`, audit filter flows, `refreshAuditEvents`, `undoAuditEvent`, `clearAuditLog`, `setAuditUndoEnabled` or `suppressAuditLog`; it only wires context, write guard, time-machine target and owner capsule APIs.
- Guard: `CapsuleBoundaryOwnershipTest` now fails if AUDIT_LOG state/undo/clear/refresh logic returns to MainViewModel.
- Guard: `AuditLogCapsuleViewModelTest` covers action category mapping, filter projection, system/undone visibility, undo flag gating and time-machine historical undone projection.
- Estimate: capsulization after prompt `#728419` is 100 percent for documented feature ownership. Remaining MainViewModel code is composition/infrastructure wiring, not feature business ownership.
- Validation: `compileDebugKotlin`, `testDebugUnitTest` and `assembleDebug` passed locally.
- Validation: Pixel 8a ran `connectedAndroidTest -Pmtt.testBuildType=deviceTest` on clone `com.example.multitimetracker.devicetest` / test app `com.example.multitimetracker.devicetest.test`: 53 tests, 3 skipped, 0 failed.

## Prompt #462918
- Scope: post-capsulization regression/stabilization audit, with no UX or DB compatibility changes.
- Code commit: `7186e9a22041582bf903e6545d4b722bf61bea37` in `/home/daniele/codex-workspace/projects/MultiTimeTracker`.
- Found: strict audit list included `SINCE_WHEN`, but LifePeriod create/update/delete still lived directly in MainViewModel and the AI doc did not list a SINCE_WHEN capsule.
- Fixed: added `SinceWhenCapsuleViewModel` and `SinceWhenCapsuleAccess`; MainViewModel keeps only compatibility wrappers delegating add/update/delete LifePeriod to the capsule.
- Fixed: moved LifePeriod duplicate-submit key out of MainViewModel source into `SinceWhenSubmitKey.kt`; the duplicate-submit guard now belongs to the SINCE_WHEN capsule.
- Guard: `CapsuleBoundaryOwnershipTest` now covers SINCE_WHEN and fails if LifePeriod mutation state returns to MainViewModel.
- Guard: `SinceWhenCapsuleViewModelTest` covers create/update/delete, write blocking, valid-tag filtering and default display units.
- Estimate: capsulization after prompt `#462918` is 100 percent strict for the audited capsule list: NOW, TAGS, TIMELINE, QUICK_EVENTS, CHAINS, ALERTS, IMPORT_EXPORT, AUDIT_LOG and SINCE_WHEN.
- Validation: `compileDebugKotlin`, `testDebugUnitTest` and `assembleDebug` passed locally.
- Validation: Pixel 8a ran `connectedAndroidTest -Pmtt.testBuildType=deviceTest` on clone `com.example.multitimetracker.devicetest` / test app `com.example.multitimetracker.devicetest.test`: 53 tests, 3 skipped, 0 failed.
- Validation: clone APK was installed/launched manually via ADB; `pidof com.example.multitimetracker.devicetest` returned a running process.
