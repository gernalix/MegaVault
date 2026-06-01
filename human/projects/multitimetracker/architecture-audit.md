# MultiTimeTracker Architecture Audit

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
