# SuperContacts Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01: `#184926` ha portato la capsulizzazione a 100% reale: `ContactsViewModel` e root restano wiring/facade, le feature sono assegnate a capsule owner esplicite, i bridge feature residui sono zero, e sono stati aggiunti test di enforcement permanenti.
- 2026-06-02: `#729604` ha auditato la v20; `ContactsViewModel` è zero-logic, ma i test non coprivano ancora root/cross-capsule in modo sufficiente. Correzione v21: enforcement esteso a `SuperContactsApp`, `MainActivity`, `AppContainer`, contratti owner e boundary cross-capsule.
- 2026-06-02: `#384729` ha consegnato v25 Home UX: ricerche salvate fuori dalla lista Home principale, dialog dedicato con apply/copy/delete confermato, scroll top su ogni cambio sort/direzione, titolo ricerca evidenziato senza riga Name duplicata e indicatore ASC/DESC singolo.
- 2026-06-02: `#620622` ha consegnato v26 link messaggistica: generazione locale WhatsApp/Telegram/Signal da numeri internazionali salvati, trigger incrementale su aggiunta/modifica/rimozione telefono, stato `link_generated`/`unverified` e conferme/rifiuti manuali preservati. La funzione non certifica la presenza reale del numero sulle piattaforme.
- 2026-06-02: follow-up UX v27: la sezione Messaging Links compare solo per link ancora `unverified`; i link `manually_confirmed` diventano icone rapide nel dettaglio contatto, i `manually_rejected` spariscono dalla scheda, e la gestione stati resta in dialog non permanente.
- 2026-06-08: `#739284` ha consegnato v29 SAF root contract: la root scelta dall'utente deve contenere solo `photos/` e `super_contacts_backup.sqlite`. Le cartelle `photos (N)` vengono migrate in `photos`, i conflitti foto sono rinominati stabilmente senza perdita dati, l'export sovrascrive il backup canonico e non genera piu file temporanei o backup numerati nella root.
- 2026-06-21: `#918406` continua `#742913` e consegna v31: Home con selezione multipla, seleziona/deseleziona tutti, tag e archivio bulk; archiviazione con tag esatto `archivio`; overlay chiamata persistente con X e apertura contatto trovato; schede in lettura senza campi vuoti; header Home piu compatto; eliminazione iniziative con conferma; scroll top su sort e pulsante su quando la lista e scesa.

## Evidenza audit
- File codice/config/test/script analizzati: 96 / 96.
- Invarianti estratte: 90; data/storage facts: 80; rischi: 70; bug markers: 70.

## Capsulizzazione #184926
- Versione: 21.
- Branch: `codex/prompt-729604-capsule-audit`.
- Capsule owner: `ContactHomeCapsule`, `ContactDetailCapsule`, `ContactMessagingCapsule`, `ContactHistoryCapsule`, `ContactInitiativeCapsule`, `ContactSuggestionCapsule`, `ContactDuplicateCapsule`, `ContactBackupCapsule`, `ContactOperationStatusCapsule`.
- Bridge residui: nessun bridge feature residuo; solo wiring infrastrutturale documentato in `ContactsViewModel`, `SuperContactsApp`, `MainActivity`, `AppContainer`.
- Enforcement: `CapsuleArchitectureEnforcementTest` copre facade, root wiring, AppContainer, owner/contract presence, cross-capsule implementation references e reading-mode descriptions; `ContactFieldDescriptionUiTest` copre la UI strumentale.
