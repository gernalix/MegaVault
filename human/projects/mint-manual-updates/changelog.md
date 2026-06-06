# mint-manual-updates Changelog

## Eventi MegaVault

- 2026-06-06: `#618472` ha consolidato definitivamente il duplicato dentro `bin/mint-manual-updates --run`, rimosso script/unit duplicate e aggiornato docs AI/Human.
- 2026-06-06: `#927384` ha aggiunto guardia Android Studio anti-download inutile: niente tarball 1+ GB se release/build installata e gia corrente o build remota non determinabile.
- 2026-06-06: `#482917` ha portato `bin/mint-manual-updates` a `v5`, aggiungendo venv Python locali; superseded da `#618472`, che rende i venv parte del run normale.
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.

## Evidenza audit

- Duplicazione rimossa: `removed duplicate script`, `removed duplicate service`, `removed duplicate timer`.
- Comando ufficiale unico: `bin/mint-manual-updates --run`.
