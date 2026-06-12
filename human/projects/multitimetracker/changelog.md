# MultiTimeTracker Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01: `#483921` patch v525 UI: drawer impostazioni scorrevole, hamburger su Since when, focus automatico nei quick event, stato capsule verificato.
- 2026-06-01: `#847261` capsulizzazione: CRUD TAGS migrato nella capsula, runtime reconciliation ALERTS spostata nella capsula, aggiunto test boundary ownership e validazione Pixel clone.
- 2026-06-01: `#539824` capsulizzazione: aggiunti SessionOwner owner API, QUICK_EVENTS/CHAINS/CSV ImportExport owner mutation, snapshot ALERTS boundary e guardrail estesi; commit app `15c1d2246bf641bd21b69d53f7a5a526b900f545`.
- 2026-06-01: `#728419` capsulizzazione: eliminato il bridge AUDIT_LOG da MainViewModel; `AuditLogCapsuleViewModel` possiede filtri, refresh eventi, clear, undo e state audit log; commit app `d7f347e155e32757a23a968391fbcd5b15fe4060`.
- 2026-06-01: `#462918` stabilizzazione post-capsulizzazione: audit ha trovato SINCE_WHEN/LifePeriod ancora root-owned; aggiunta `SinceWhenCapsuleViewModel` con boundary/test e validazione Pixel clone; commit app `7186e9a22041582bf903e6545d4b722bf61bea37`.
- 2026-06-08: `#394817` patch v526 performance Eventi: refresh DB Eventi spostato fuori dallo startup e griglia Eventi resa lazy/keyed per evitare layout di intere sezioni durante lo scroll.
- 2026-06-12: `#817463` patch v527 performance/stability: startup schema/init spostati fuori da `onCreate`, guard schema cache invalidata su import/restore/switch DB, ridotte allocazioni Events/Since When, test runtime TCL con limite keyguard; commit app `2548034f6c4fc7e4950f45600b41101faae7d764`.

## v527 prompt #817463
- Causa trovata: `MainActivity.onCreate` faceva ancora hardening schema SQLite e la prima inizializzazione ViewModel caricava integrity/snapshot sul percorso UI startup.
- Correzione: `onCreate` resta sottile; `ensureStartupSchemas`, `vm.initialize` e auto-restore vault girano su `Dispatchers.IO`; i callback UI tornano esplicitamente sul Main.
- Correzione: `SnapshotSqlite` usa guard cache per DB version e la invalida su import, restore, switch vault e fresh clear.
- Correzione UI: Events non ordina recent entries se il log e' collassato, raggruppa/sort macro actions una volta; Since When riusa `visibleTagsById` invece di ricrearlo per card.
- Misure TCL locked real DB: v526 `main_activity_on_create` 79.25 ms e `ensure_session_tables` 50.73 ms medi; v527 `main_activity_on_create` ~30.8 ms finale e schema ensure steady ~2.3 ms. Il cold `am start -W` resta ~3.0 s per lockscreen/NotificationShade, quindi non e' una misura UI utile.
- Stabilita: nessun `AndroidRuntime`, `FATAL EXCEPTION`, ANR o lmkd dell'app nei log finali TCL; fresh clear-data su debug non crea `databases/multitimer.db`.
- Limite: TCL rimasto in `mCurrentFocus=NotificationShade` e `mDreamingLockscreen=true`; benchmark visuale scroll/tap/tab bloccato. Pixel non usato per test; install finale Pixel bloccata da ADB connection refused/offline.

## v526 prompt #394817
- Causa trovata: la tab Events usava `LazyColumn`, ma ogni sezione conteneva una `FlowRow` che componeva e misurava tutte le card della sezione; con molte card la laziness era solo per sezione, non per item.
- Causa startup trovata: `MainViewModel.initialize` lanciava sempre `quickEventsCapsule.refreshFromDb` subito dopo l'avvio, aggiornando lo stato globale anche quando l'utente restava su Now.
- Correzione: Events usa `LazyVerticalGrid` a 2 colonne con header full-span e chiavi stabili per sezioni, template, macro e recent entries; le mappe campi/template/macro sono preparate con `remember`.
- Correzione: il refresh SQLite screen-bounded degli Events parte in IO quando si apre la schermata Eventi, con trace clone `quick_events_screen_snapshot`.
- Misure Pixel clone: baseline cold 376/252/220 ms, warm 61/39/37 ms; post-fix cold 457/222/221 ms, warm 43/65/46 ms. Il primo post cold includeva reinstall recente; i run 2-3 restano ~221 ms.
- Test Pixel clone: v526 installato come `com.example.multitimetracker.devicetest`; tap evento, menu tre puntini, edit button e edit recent entry verificati via UI. `connectedAndroidTest` su Pixel 8a: 53 test, 3 skipped, 0 failed.

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

## prompt #728419
- Capsule dopo `#728419`: AUDIT_LOG possiede filtri, refresh/proiezione eventi, clear, undo, state audit log e soppressione write ricorsive durante undo.
- Boundary/API: `AuditLogCapsuleAccess` espone solo hook infrastrutturali e API owner verso sessioni/tag/time-machine; MainViewModel non contiene piu business logic AUDIT_LOG.
- Boundary enforcement: `CapsuleBoundaryOwnershipTest` copre anche AUDIT_LOG; `AuditLogCapsuleViewModelTest` protegge filtri, category mapping, undo flag e proiezione time-machine.
- Stato: capsulizzazione stimata 100 percento per ownership feature documentata; restano solo hook infrastrutturali della shell.
- Test `#728419`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` verdi; Pixel 8a clone `deviceTest` con 53 instrumentation test, 3 skipped, 0 failed.

## prompt #462918
- Regressione/gap trovato: `SINCE_WHEN` era richiesto nell'audit ma LifePeriod create/update/delete vivevano ancora in `MainViewModel`.
- Correzione: `SinceWhenCapsuleViewModel` possiede LifePeriod CRUD, duplicate-submit guard e filtro tag validi; MainViewModel resta wrapper delegante.
- Boundary enforcement: `CapsuleBoundaryOwnershipTest` copre SINCE_WHEN; `SinceWhenCapsuleViewModelTest` copre create/update/delete, write guard e default display units.
- Stato: capsulizzazione stimata 100 percento strict per NOW, TAGS, TIMELINE, QUICK_EVENTS, CHAINS, ALERTS, IMPORT_EXPORT, AUDIT_LOG e SINCE_WHEN.
- Test `#462918`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` verdi; Pixel 8a clone `deviceTest` con 53 instrumentation test, 3 skipped, 0 failed; clone install/launch ADB verificato con PID.

## Evidenza audit
- File codice/config/test/script analizzati: 224 / 224.
- Invarianti estratte: 90; data/storage facts: 80; rischi: 70; bug markers: 70.
