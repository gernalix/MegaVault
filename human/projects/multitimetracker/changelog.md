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
- 2026-06-22: `#914506` Play Store closed-testing handoff: release APK/AAB buildabili ma unsigned, signing pipeline pronta con secret esterni, privacy/Data Safety/store listing/assets template creati nel repo app; commit app `89257cd96233ac0a28e65535c5c03f41178eca62`.
- 2026-06-22: `#517284` chiusura offline Play Store: upload keystore locale ignorato creato, APK/AAB release firmati e verificati, checklist release aggiunta; commit app `f5938e537ccc94007dd5ed9da6eb0ec643a44a8d`.
- 2026-06-22: `#684219` Play Console package finale: copy-paste pack, closed testing steps e release notes aggiunti; signing/properties/hash ricontrollati; commit app `a8a28e20a4be8fab0439ba28fb7f491b32747c9c`.

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

## prompt #914506
- Build/test: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`, `lintDebug`, `assembleRelease`, `bundleRelease` verdi.
- Release: `app-release-unsigned.apk` e `app-release.aab` prodotti; firma release bloccata da keystore/password mancanti (`NEEDS_SECRET`).
- Play docs: privacy policy, Data Safety, store listing, assets checklist e release signing handoff creati in `dev/human/play_store`.
- Stato: Play Store readiness stimata 70 percento; closed testing non ancora ready finche mancano upload key, decisione definitiva su `applicationId`, URL privacy, dati publisher/contact, Data Safety finale e asset Play.

## prompt #517284
- Signing: creato keystore locale ignorato `local_signing/mtt-upload.p12` con alias `mtt-upload`, PKCS12, RSA-4096; password solo in `mtt-release.properties` ignorato.
- Release: `app-release.apk` firmato e `app-release.aab` firmato prodotti; `apksigner` e `jarsigner` PASS.
- Handoff: aggiunto `dev/human/play_store/release_checklist.md` e aggiornati readiness/release signing/assets/roadmap.
- Stato: offline work PASS; restano input Play Console, backup chiave, privacy URL, Data Safety finale e asset.

## prompt #684219
- Verifica: `mtt-release.properties` punta a `local_signing/mtt-upload.p12`; keystore, segreti e build outputs sono ignorati.
- Release: `compileDebugKotlin`, `testDebugUnitTest`, `assembleRelease`, `bundleRelease`, `apksigner` e `jarsigner` PASS.
- Handoff: aggiunti `closed_testing_steps.md`, `play_console_copy_paste.md`, `release_notes.md`; aggiornati privacy, Data Safety, listing, assets, checklist e AI readiness.
- Stato: readiness 92 percento; resta solo input proprietario in Play Console e asset grafici.
