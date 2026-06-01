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
