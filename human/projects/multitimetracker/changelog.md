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
- 2026-06-12: `#294816` validazione v527 completata senza patch codice: TCL sbloccato UI/startup/bg-fg/clear-data PASS; Pixel debug v527 install/smoke PASS; docs app commit `5b7e76a2de28d9974235d5f8fcc2623c64251fca`.
- 2026-06-13: `#739284` incidente P0 integrita dati v528: root cause rollback automatico di un DB importato valido dopo `activation-signature`; aggiunti CriticalDataGuard, ForensicLog, export SAF verificato, promozione interna current->candidate, retention/cleanup tmp/bak, test mirati TCL PASS.
- 2026-06-14: `#418762` P0 v529: corretto falso positivo `tasks: 1 -> 0` nei salvataggi runtime senza indebolire import/replace completi; corretto export SAF primario 0 byte e manual export spostato su IO; commit app `90da4c72d0f224f74741ff28fd97d12a69a34169`.
- 2026-06-14: `#742913` v530: aggiunto audit testabile di parita DB interno <-> SAF su 17 tabelle utente, viste UTC/Z `export_*_utc_z`, fixture con archivi/soft-delete/settings/capsule state e import dopo clear interno; primo gate live TCL bloccato per ADB vuoto.
- 2026-06-15: `#518204` v530: sbloccato TCL via ADB `192.168.1.200:33771`; installazione pulita deviceTest, test Gradle connected mirato e run manuale `am instrument` PASS; DB SAF reale estratto e ispezionato, 17 tabelle SAF == 17 interne post-import, nessuna differenza schema/righe, import dopo clear PASS.
- 2026-06-15: `#947381` v531: hardening export/import SQLite SAF con checkpoint WAL obbligatorio, integrity_check sorgente/tmp/bak/finale, restore automatico primario->`.bak`, stato sync UI, copertura autoexport dei write path persistenti e coda single-flight anti-storm con debounce 1200 ms.

## v531 prompt #947381
- Export SQLite SAF: un solo percorso stabile `DB interno -> tmp -> bak -> primario`; ogni fase richiede checkpoint coerente o abort, `integrity_check` PASS e preservazione dell'ultimo export valido in caso di errore.
- Restore: i candidati sono solo `multitimer.db` e `multitimer.db.bak`, in quest'ordine; `multitimer.db.tmp` non e' mai sorgente restore.
- Vault SAF: da cartella pulita l'app mantiene solo `multitimer.db`, `multitimer.db.bak` e `multitimer.db.tmp` temporaneo; non introduce cancellazione aggressiva di file legacy.
- Autoexport: `PersistentMutationTracker` marca ogni modifica persistente e usa una coda single-flight. Debounce scelto: 1200 ms. Richieste ravvicinate sono coalesced; modifiche durante export impostano pending e producono un export successivo finche' `last_successful_export_at >= last_database_mutation_at`.
- Loop prevention: aggiornamenti di `last_export_attempt_at`, `last_successful_export_at`, `last_export_status`, errore/file/integrity non chiamano il mutation tracker e quindi non generano autoexport.
- UI: indicatore sempre visibile in top bar con ✅ sincronizzato, ⟳ export in corso, ❌ modifiche non esportate, ⚠ ultimo export fallito. Il dialog mostra date locali, stato, errore, file SAF e ultimo integrity_check; le date persistite restano UTC/Z.
- Invariant permanente: "Nessun percorso dell'app può esportare, importare, ripristinare o copiare database SQLite senza checkpoint coerente, integrity_check riuscito e fallback .bak verificato."
- Invariant permanente: "Nessuna modifica persistente può bypassare l'infrastruttura di autoexport."
- Verifica TCL: gruppo `PersistenceImportExportTest` mirato PASS 7/7 su `6102H - 12`: stable export, checkpoint failure abort, restore da .bak con tmp ignorato, stati sync, coalescing, follow-up export durante export e parita SAF/import.
- Verifica finale: APK debug v531 installato e avviato su TCL `192.168.1.200:33771` e Pixel 8a `192.168.1.37:34033`; versione installata 531, nessun crash/ANR immediato nel campione logcat.

## v530 prompt #742913
- Risultato codice: il DB SAF resta una copia validata del DB interno; nessuna entita utente risulta esportata in formato parziale separato.
- Copertura test: `PersistenceImportExportTest#sqliteVaultExportCoversAllInternalUserTablesAndImportsBackIdentically` confronta schema e righe di tutte le tabelle utente interne/SAF, verifica viste UTC/Z, cancella il DB interno, importa dal SAF e ricontrolla snapshot/settings/tabelle.
- Entita coperte: sessioni, eventi Quick Events, Since When/life periods, tag, parent tag, alert/time-fence, chains, archivi/soft-delete, impostazioni utente, audit/integrity/history/capsule runtime state.
- Esclusione: location/luoghi non esistono nel modello attivo; `TimeFenceRule` e' temporale/tag-driven.
- Verifica locale: `compileDebugKotlin`, `testDebugUnitTest`, `compileDeviceTestAndroidTestKotlin`, `assembleDebug` PASS.
- Verifica TCL #518204: `connectedDeviceTestAndroidTest` mirato PASS su TCL `6102H - 12`; run manuale `am instrument` PASS dopo installazione pulita e `pm clear`; artefatti DB estratti da `/sdcard/Android/data/com.example.multitimetracker.devicetest/files/full-parity-vault-test-artifacts/`; `quick_check` ok, 17 tabelle confrontate, nessuna differenza schema/righe, import dopo clear PASS.

## v529 prompt #418762
- Causa reale 1: `CriticalDataGuard` confrontava lo snapshot corrente completo con un nuovo snapshot runtime valido in cui il campo legacy `tasks` puo diventare vuoto perche derivato dalle sessioni in esecuzione, non fonte autorevole.
- Causa reale 2: il primario SAF `multitimer.db` poteva restare a 0 byte dopo promozione `DocumentFile.renameTo`; la `.bak` conteneva il DB completo, quindi i Parent Tag erano salvati internamente ma non garantiti nel primario SAF.
- Fix: `SnapshotStore` e `DataIntegrityGate` escludono solo `tasks` legacy dai confronti runtime; import/replace DB completi continuano a bloccare `tasks` N>0->0.
- Fix: export SAF scrive e valida tmp, poi `.bak`, poi copia primaria validata; nessun successo export viene registrato se il primario non e' SQLite valido.
- Fix: export manuale gira su `Dispatchers.IO` con guard anti doppio tap, evitando ANR UI durante hash/copia ZIP/DB.
- Verifica: Pixel main v529 ha creato sessione, evento, Since When, Parent Tag; export SAF manuale produce `multitimer.db` e `.bak` pieni, SHA identico, `quick_check=ok`, snapshot contiene `Pixel529_since_when`, `Pixel529child`, `Pixel529parent`; restart persistence PASS; nessun `Save failed` finale.
- Verifica TCL: targeted deviceTest `PersistenceImportExportTest#sqliteVaultExportUsesSingleStableBackupAndOneEmergencyCopy` PASS riproducendo primario 0 byte prima dell'export.
- Nuova regola test: patch su persistenza/database/export/import/recovery/backup/integrity/guard deve includere creazione reale UI o device-equivalent delle entita critiche, export SAF e restart persistence; test DAO/repository/export isolati non bastano.

## v528 prompt #739284
- Causa reale: l'import DB aveva conteggi coerenti (`lifePeriods=7`, `tagParents=6`) ma l'attivazione runtime ha restituito `activation-signature`; la capsule ha trattato quel mismatch runtime come corruzione e ha fatto rollback automatico al pre-import vuoto.
- Effetto: Since When e Parent Tag sono stati persi nel DB corrente ispezionato, non solo nascosti dalla UI; l'autoexport successivo ha copiato lo stato vuoto anche su SAF `multitimer.db` e `multitimer.db.bak`.
- Fix: un DB importato che passa integrity/schema/conteggi non viene piu rollbackato per mismatch runtime; l'evento viene registrato e l'attivazione puo completarsi al riavvio.
- Fix: `SnapshotStore`, import/restore interno e export SAF bloccano drop critici N>0->0 per entita persistenti; `multitimer.db.tmp` viene validato prima della promozione.
- Fix: il mirror settings viene preservato nei candidati storici che non lo contengono, evitando drop falso senza perdere preferenze.
- Verifica: `compileDebugKotlin`, `compileDebugAndroidTestKotlin`, `testDebugUnitTest`, targeted TCL deviceTest import/export/recovery 26 test con 1 skip fixture e 0 failure, `assembleDebug` PASS. La suite completa TCL e' stata tentata ma il device e' andato offline dopo 12/51 e i test notification timed-session sono andati in timeout.

## v527 prompt #817463
- Causa trovata: `MainActivity.onCreate` faceva ancora hardening schema SQLite e la prima inizializzazione ViewModel caricava integrity/snapshot sul percorso UI startup.
- Correzione: `onCreate` resta sottile; `ensureStartupSchemas`, `vm.initialize` e auto-restore vault girano su `Dispatchers.IO`; i callback UI tornano esplicitamente sul Main.
- Correzione: `SnapshotSqlite` usa guard cache per DB version e la invalida su import, restore, switch vault e fresh clear.
- Correzione UI: Events non ordina recent entries se il log e' collassato, raggruppa/sort macro actions una volta; Since When riusa `visibleTagsById` invece di ricrearlo per card.
- Misure TCL audit real DB: v526 `main_activity_on_create` 79.25 ms e `ensure_session_tables` 50.73 ms medi; v527 `main_activity_on_create` ~30.8 ms finale e schema ensure steady ~2.3 ms.
- Misure TCL sbloccato `#294816`: clone cold WaitTime medio 669 ms, warm medio 10.2 ms; trace `main_activity_on_create` medio 17.96 ms, `ensure_session_tables` medio 3.39 ms.
- Stabilita: nessun `AndroidRuntime`, `FATAL EXCEPTION`, ANR, lmkd o `am_proc_died` app nei log finali TCL; clear-data/reinstall su main debug v527 produce `sessions=0`, `session_tags=0`, `snapshot=0`.
- UI reale: tap sessione stop visibile, long press apre edit, `Active tags` presente, Eventi/Timeline/Since When/Settings visibili, scroll e background/foreground ripetuti completati. Pixel usato solo per install/smoke finale v527, con launch pulito senza crash immediato.

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
