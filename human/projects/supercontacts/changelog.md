# SuperContacts Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01: `#184926` ha portato la capsulizzazione a 100% reale: `ContactsViewModel` e root restano wiring/facade, le feature sono assegnate a capsule owner esplicite, i bridge feature residui sono zero, e sono stati aggiunti test di enforcement permanenti.

## Evidenza audit
- File codice/config/test/script analizzati: 96 / 96.
- Invarianti estratte: 90; data/storage facts: 80; rischi: 70; bug markers: 70.

## Capsulizzazione #184926
- Versione: 20.
- Branch: `codex/prompt-184926-capsules`.
- Capsule owner: `ContactHomeCapsule`, `ContactDetailCapsule`, `ContactHistoryCapsule`, `ContactInitiativeCapsule`, `ContactSuggestionCapsule`, `ContactDuplicateCapsule`, `ContactBackupCapsule`, `ContactOperationStatusCapsule`.
- Bridge residui: nessun bridge feature residuo; solo wiring infrastrutturale documentato in `ContactsViewModel`, `SuperContactsApp`, `MainActivity`, `AppContainer`.
- Enforcement: `CapsuleArchitectureEnforcementTest` e `ContactFieldDescriptionUiTest`.
