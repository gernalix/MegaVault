# MultiTimeTracker Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01: `#483921` patch v525 UI: drawer impostazioni scorrevole, hamburger su Since when, focus automatico nei quick event, stato capsule verificato.
- 2026-06-01: `#847261` capsulizzazione: CRUD TAGS migrato nella capsula, runtime reconciliation ALERTS spostata nella capsula, aggiunto test boundary ownership e validazione Pixel clone.
- 2026-06-01: `#539824` capsulizzazione: aggiunti SessionOwner owner API, QUICK_EVENTS/CHAINS/CSV ImportExport owner mutation, snapshot ALERTS boundary e guardrail estesi; commit app `15c1d2246bf641bd21b69d53f7a5a526b900f545`.

## v525 prompt #483921
- Sidebar: la voce Impostazioni resta nel drawer e il drawer ora scorre, quindi la voce rimane raggiungibile anche su viewport bassi.
- Since when: aggiunto hamburger coerente con Now/Events/Tags/Timeline tramite `LocalOpenAppMenu`.
- Events: il dialog "Customize quick event" mette il focus sul primo campo testuale utile; se Title e timestamp sono gia valorizzati, privilegia il primo custom field testuale obbligatorio senza default e apre la tastiera.
- Events: rimosso il campo note ridondante dai Quick Events; eventuale testo aggiuntivo va modellato come campo custom del pulsante.
- Capsule prima di `#847261`: TAGS aveva CRUD e warning in `MainViewModel`; ALERTS riconciliava timer/notifiche nel root; session/timeline CRUD era bridge root.
- Capsule dopo `#847261`: TAGS possiede CRUD/audit/persist/rename-projection; ALERTS possiede mutation+runtime reconciliation; restano bridge root per NOW/TIMELINE session CRUD, QUICK_EVENTS, CHAINS, AUDIT_LOG, IMPORT_EXPORT hooks.
- Test `#847261`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` verdi; Pixel 8a clone `com.example.multitimetracker.devicetest` v525: 53 instrumentation test, 3 skipped, 0 failed.
- Import/export: `SqliteVault` ora forza nomi esatti per i file stabili del vault, incluso `multitimer.db.bak`, evitando normalizzazioni del provider `DocumentFile`.

## prompt #539824
- Capsule dopo `#539824`: NOW/TIMELINE session CRUD e stop policies passano da `SessionOwnerCapsuleViewModel`; QUICK_EVENTS e CHAINS possiedono mutation/hook/state feature; IMPORT_EXPORT possiede CSV manuale; ALERTS possiede anche reconciliation post-snapshot.
- Boundary enforcement: `CapsuleBoundaryOwnershipTest` copre session owner, chains, quick events, CSV ImportExport e snapshot alerts oltre a TAGS/ALERTS.
- Residuo: AUDIT_LOG filters/event refresh/clear/undo resta in `MainViewModel`; capsulizzazione stimata 92 percento.
- Test `#539824`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` verdi; Pixel 8a clone `deviceTest` con 53 instrumentation test, 3 skipped, 0 failed.

## Evidenza audit
- File codice/config/test/script analizzati: 224 / 224.
- Invarianti estratte: 90; data/storage facts: 80; rischi: 70; bug markers: 70.
