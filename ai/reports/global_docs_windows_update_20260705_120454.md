# Global Docs Windows Update

TIMESTAMP=2026-07-05T12:04:54+02:00
SCOPE=global/non-project docs only
PROTOCOL=ai/MEGAVAULT_PROTOCOL.md

## Branch/Commit/Push Status

- Branch: `codex/global-docs-windows-20260705`.
- Commit: pending at report-write time; this report is included in the atomic docs commit.
- Push: pending at report-write time; final push result recorded in assistant final response.
- Git executable: `C:\Program Files\Git\cmd\git.exe` because `git` was not available in the current PowerShell PATH.

## File Analizzati

- Protocol/canonical: `ai/MEGAVAULT_PROTOCOL.md`, `ai/GLOBAL_RULES.md`, `ai/ANDROID_PROTOCOL.md`.
- AI global docs: `ai/global/HOST_PROFILE.md`, `STORAGE_TOPOLOGY.md`, `SOFTWARE_INVENTORY.md`, `NETWORK_TOPOLOGY.md`, `DATA_REGISTRY.md`, `ALERT_REGISTRY.md`, `SERVICE_REGISTRY.md`, `PROJECT_INDEX_EXTENDED.md`.
- Global indexes: `ai/PROJECT_INDEX.md`, `human/INDEX.md`, `human/PROJECTS.md`.
- Human global mirrors: `human/global/*.md`.
- Repo/project docs listed but excluded: `ai/projects/**`, `human/projects/**`, `dev/ai/infrastructure/**`, `dev/human/infrastructure/**`, historical reports/archives.

## File Modificati

- `ai/ANDROID_PROTOCOL.md`
- `ai/GLOBAL_RULES.md`
- `ai/PROJECT_INDEX.md`
- `ai/global/ALERT_REGISTRY.md`
- `ai/global/DATA_REGISTRY.md`
- `ai/global/HOST_PROFILE.md`
- `ai/global/NETWORK_TOPOLOGY.md`
- `ai/global/PROJECT_INDEX_EXTENDED.md`
- `ai/global/SERVICE_REGISTRY.md`
- `ai/global/SOFTWARE_INVENTORY.md`
- `ai/global/STORAGE_TOPOLOGY.md`
- `human/INDEX.md`
- `human/PROJECTS.md`
- `human/global/ALERT_REGISTRY.md`
- `human/global/DATA_REGISTRY.md`
- `human/global/HOST_PROFILE.md`
- `human/global/NETWORK_TOPOLOGY.md`
- `human/global/PROJECT_INDEX_EXTENDED.md`
- `human/global/SERVICE_REGISTRY.md`
- `human/global/SOFTWARE_INVENTORY.md`
- `human/global/STORAGE_TOPOLOGY.md`
- `ai/reports/global_docs_windows_update_20260705_120454.md`

## File Esclusi Perché Project-Specific/Storici/Generati

- `ai/projects/**`, `human/projects/**`: project docs specifici, non toccati.
- `ai/reports/prompt_*`, merge/migration/audit reports: report storici, non toccati.
- `human/system/**`: snapshot/report system storici, non toccati.
- `dev/ai/INCIDENT_REGISTRY.md`, `dev/human/INCIDENT_REGISTRY.md`: registri incidenti storici, non toccati.
- `dev/ai/infrastructure/**`, `dev/human/infrastructure/**`: audit infrastrutturali specifici, non toccati.
- `ai/PROJECT_INVENTORY.md`: inventario generato/statico con path Linux storici; lasciato invariato.

## Cambiamenti Principali

- Promosso host corrente: Windows 11 Pro su Lenovo ThinkPad P14s Gen 5 AMD (`DANIELE_PC`).
- Aggiornati path host canonici: `C:\Users\seste\Documents\...`.
- Inseriti tool Windows verificati: PowerShell 7.6.3, Git 2.55.0, Android Studio, Android SDK/ADB Windows.
- Aggiornato storage corrente: NVMe Kioxia su `C:`, Seagate Expansion su `D:`, `E:` unknown, T7 non connesso nel controllo.
- Aggiornato backup Windows: Veeam Agent service running/automatic; target Veeam unknown; Backblaze Windows non rilevato nei path default.
- Demansionati Surface/Linux Mint/restic/systemd/ext4 a `LEGACY_2026-06` o note project-specific/remote.
- Human global mirrors allineati senza duplicare tutta la verità AI.

## Riferimenti Obsoleti Rimasti E Perché

- `ai/global/HOST_PROFILE.md`, `STORAGE_TOPOLOGY.md`, `NETWORK_TOPOLOGY.md`: restano `legacy_host`/`legacy_root` Surface/Linux Mint in blocchi `LEGACY_2026-06_SURFACE_MINT`.
- `ai/global/DATA_REGISTRY.md`, `SERVICE_REGISTRY.md`, `ALERT_REGISTRY.md`, `PROJECT_INDEX_EXTENDED.md`: restano path `/home` e servizi systemd perché sono snapshot legacy, runtime remoti Linux o relazioni project-specific.
- `ai/PROJECT_INDEX.md`, `human/PROJECTS.md`: restano descrizioni Linux Mint su righe progetto; aggiunta nota che non sovrascrivono `HOST_PROFILE`.
- `ai/PROJECT_INVENTORY.md`, `human/MIGRATION_REPORT.md`, `human/system/**`, report storici: non modificati perché generati/storici.

## Verifiche Eseguite

- PASS: `git status --short --branch` iniziale pulito su branch base.
- PASS: branch dedicato creato `codex/global-docs-windows-20260705`.
- PASS: protocollo letto prima degli update.
- PASS: diff scope mostra solo `.md`; nessun codice sorgente modificato.
- PASS: `git diff --name-only -- ai/projects human/projects dev/ai/infrastructure dev/human/infrastructure` vuoto.
- PASS: controllo project-specific docs: `NO_PROJECT_SPECIFIC_DOCS_TOUCHED`.
- PASS: grep mirato obsoleti primari non trova piu' `role=primary Linux Mint workstation` o frasi host Mint correnti; match rimasti sono `legacy_*` o project-specific/storici.
- PASS: doc AI mantenuti compatti; canonici principali ridotti (`HOST_PROFILE` 96 righe, `NETWORK_TOPOLOGY` 53, `SOFTWARE_INVENTORY` 44, `STORAGE_TOPOLOGY` 46).
- PASS: scansione diff per segreti non ha trovato valori reali; match aggiunti sono regole/no-token o nomi placeholder (`<token>` non introdotto come segreto).
- WARN: Git segnala normalizzazione LF->CRLF al prossimo touch; non corretto qui per evitare churn non richiesto.

## Colli Di Bottiglia

- `git` non era nel PATH PowerShell corrente; usato path completo.
- Alcuni global registries mescolano dati globali e project-specific legacy; aggiornarli riga per riga avrebbe violato lo scope.
- Veeam target, Backblaze policy, GitHub Desktop e Oracle SSH key Windows non verificati in modo completo; marcati `UNKNOWN`.

## TODO

- Verificare target Veeam da DB/log quando il task riguarda backup Windows.
- Verificare stato T7 al prossimo collegamento.
- Decidere se rigenerare `ai/PROJECT_INVENTORY.md` con path Windows in un task dedicato.
- Eseguire inventario Windows servizi/Task Scheduler solo se richiesto.
