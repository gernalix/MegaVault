PROJECT: MultiTimeTracker
SLUG: multitimetracker
PATH: /home/daniele/codex-workspace/projects/MultiTimeTracker
REMOTE: https://github.com/gernalix/MultiTimeTracker.git
BRANCH: codex/v488-release-safe-ui-lockdown

STACK:
- gradle/android-or-jvm

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 97
- dirty_docs_skipped: 0

DB:
- multitimer_20260529_122059.db
- forensic/914683_20260529_154033/chosen_candidate/MTT524_multitimer_best_candidate.db
- forensic/914683_20260529_154033/chosen_candidate/repo_multitimer_20260529_122059_reference.db
- forensic/914683_20260529_154033/phone/current_internal_multitimer.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_150544.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_145942.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_145943.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_145823.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_145824.db
- forensic/914683_20260529_154033/phone_external/MTT524/multitimer_20260529_145745.db

BUILD:
- ./gradlew <task>

TEST:
- app/src/test
- app/src/androidTest
- gradle test/check tasks if needed

VERSIONING:
- git_branch: codex/v488-release-safe-ui-lockdown
- git_remote: https://github.com/gernalix/MultiTimeTracker.git
- preexisting_status_count: 9

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118
- ?? forensic/
- ?? multitimer_20260529_122059.db

KNOWN_BUGS:
- dev/legacy/dev/BUG_REGISTRY.md
- dev/legacy/dev/ai/BUG_REGISTRY.md
- dev/legacy/dev/human/TROUBLESHOOTING.md
- dev/legacy/en/Troubleshooting/Troubleshooting.md

ROADMAP:
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_HISTORY.md
- dev/legacy/dev/ROADMAP_ACTIVE.md
- dev/legacy/dev/ROADMAP_HISTORY.md
- dev/legacy/dev/ai/ROADMAP_ACTIVE.md
- dev/legacy/dev/ai/ROADMAP_HISTORY.md
- dev/legacy/dev/human/ROADMAP.md
- dev/legacy/dev/human/ROADMAP_EXPLAINED.md

LEGACY_DOCS:
- .codex_patch_current_v474/dev/ROADMAP_ACTIVE.md -> dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md
- .codex_patch_current_v474/dev/ROADMAP_HISTORY.md -> dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md
- .codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md -> dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md
- .codex_patch_snapshot_v474/dev/ROADMAP_HISTORY.md -> dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_HISTORY.md
- dev/AGENT_RULES.md -> dev/legacy/dev/AGENT_RULES.md
- dev/ARCHITECTURE_LOCK.md -> dev/legacy/dev/ARCHITECTURE_LOCK.md
- dev/BUG_REGISTRY.md -> dev/legacy/dev/BUG_REGISTRY.md
- dev/CAPSULE_INDEX.md -> dev/legacy/dev/CAPSULE_INDEX.md
- dev/CODEBASE_MAP.md -> dev/legacy/dev/CODEBASE_MAP.md
- dev/CONTRACT.md -> dev/legacy/dev/CONTRACT.md
- dev/ROADMAP_ACTIVE.md -> dev/legacy/dev/ROADMAP_ACTIVE.md
- dev/ROADMAP_HISTORY.md -> dev/legacy/dev/ROADMAP_HISTORY.md
- dev/WORKFLOW.md -> dev/legacy/dev/WORKFLOW.md
- dev/ai/AGENT_RULES.md -> dev/legacy/dev/ai/AGENT_RULES.md
- dev/ai/ARCHITECTURE_LOCK.md -> dev/legacy/dev/ai/ARCHITECTURE_LOCK.md
- dev/ai/BUG_REGISTRY.md -> dev/legacy/dev/ai/BUG_REGISTRY.md
- dev/ai/CAPSULES.md -> dev/legacy/dev/ai/CAPSULES.md
- dev/ai/CAPSULE_INDEX.md -> dev/legacy/dev/ai/CAPSULE_INDEX.md
- dev/ai/DB_SCHEMA.md -> dev/legacy/dev/ai/DB_SCHEMA.md
- dev/ai/INDEX.md -> dev/legacy/dev/ai/INDEX.md
- dev/ai/OPERATING_RULES.md -> dev/legacy/dev/ai/OPERATING_RULES.md
- dev/ai/PLAYSTORE_GATEKEEPER.md -> dev/legacy/dev/ai/PLAYSTORE_GATEKEEPER.md
- dev/ai/RELEASE_PROTOCOL.md -> dev/legacy/dev/ai/RELEASE_PROTOCOL.md
- dev/ai/RISK_REGISTER.md -> dev/legacy/dev/ai/RISK_REGISTER.md
- dev/ai/ROADMAP_ACTIVE.md -> dev/legacy/dev/ai/ROADMAP_ACTIVE.md
- dev/ai/ROADMAP_HISTORY.md -> dev/legacy/dev/ai/ROADMAP_HISTORY.md
- dev/ai/TEST_GATES.md -> dev/legacy/dev/ai/TEST_GATES.md
- dev/archive/AGENTS.md -> dev/legacy/dev/archive/AGENTS.md
- dev/archive/FUTURE_PATCHES.md -> dev/legacy/dev/archive/FUTURE_PATCHES.md
- dev/archive/INDEX.md -> dev/legacy/dev/archive/INDEX.md
- dev/archive/UI_CONTRACT.md -> dev/legacy/dev/archive/UI_CONTRACT.md
- dev/human/CHANGELOG.md -> dev/legacy/dev/human/CHANGELOG.md
- dev/human/FEATURES.md -> dev/legacy/dev/human/FEATURES.md
- dev/human/INDEX.md -> dev/legacy/dev/human/INDEX.md
- dev/human/PLAYSTORE_READINESS_REPORT.md -> dev/legacy/dev/human/PLAYSTORE_READINESS_REPORT.md
- dev/human/PROJECT_OVERVIEW.md -> dev/legacy/dev/human/PROJECT_OVERVIEW.md
- dev/human/ROADMAP.md -> dev/legacy/dev/human/ROADMAP.md
- dev/human/ROADMAP_EXPLAINED.md -> dev/legacy/dev/human/ROADMAP_EXPLAINED.md
- dev/human/TROUBLESHOOTING.md -> dev/legacy/dev/human/TROUBLESHOOTING.md
- en/Core Concepts/Continuity.md -> dev/legacy/en/Core Concepts/Continuity.md
- en/Core Concepts/Core Concepts.md -> dev/legacy/en/Core Concepts/Core Concepts.md
- en/Core Concepts/Session.md -> dev/legacy/en/Core Concepts/Session.md
- en/Core Concepts/Tag.md -> dev/legacy/en/Core Concepts/Tag.md
- en/Core Concepts/Time Machine.md -> dev/legacy/en/Core Concepts/Time Machine.md
- en/Core Concepts/Time Reconstruction.md -> dev/legacy/en/Core Concepts/Time Reconstruction.md
- en/FAQ/FAQ.md -> dev/legacy/en/FAQ/FAQ.md
- en/Features/Chains.md -> dev/legacy/en/Features/Chains.md
- en/Features/Features.md -> dev/legacy/en/Features/Features.md
- en/Features/Home Screen Widget.md -> dev/legacy/en/Features/Home Screen Widget.md
- en/Features/Import, Export, and Vaults.md -> dev/legacy/en/Features/Import, Export, and Vaults.md
- en/Features/Life Periods.md -> dev/legacy/en/Features/Life Periods.md
- en/Features/Timed Sessions and Alerts.md -> dev/legacy/en/Features/Timed Sessions and Alerts.md
- en/Getting Started/First Launch and Setup.md -> dev/legacy/en/Getting Started/First Launch and Setup.md
- en/Getting Started/Start Here.md -> dev/legacy/en/Getting Started/Start Here.md
- en/Getting Started/Your First Session.md -> dev/legacy/en/Getting Started/Your First Session.md
- en/Home.md -> dev/legacy/en/Home.md
- en/Interface/Chronology.md -> dev/legacy/en/Interface/Chronology.md
- en/Interface/Interface.md -> dev/legacy/en/Interface/Interface.md
- en/Interface/Now.md -> dev/legacy/en/Interface/Now.md
- en/Interface/Secondary Areas and Settings.md -> dev/legacy/en/Interface/Secondary Areas and Settings.md
- en/Interface/Tags.md -> dev/legacy/en/Interface/Tags.md
- en/Philosophy/Philosophy.md -> dev/legacy/en/Philosophy/Philosophy.md
- en/Troubleshooting/Troubleshooting.md -> dev/legacy/en/Troubleshooting/Troubleshooting.md
- en/Use Cases/Real-World Scenarios.md -> dev/legacy/en/Use Cases/Real-World Scenarios.md
- en/Use Cases/Use Cases.md -> dev/legacy/en/Use Cases/Use Cases.md
- en/Workflows/Common Tracking Workflows.md -> dev/legacy/en/Workflows/Common Tracking Workflows.md
- en/Workflows/Workflows.md -> dev/legacy/en/Workflows/Workflows.md
- forensic/914683_20260529_154033/db_report.md -> dev/legacy/forensic/914683_20260529_154033/db_report.md
- it/Casi d'Uso/Casi d'Uso.md -> dev/legacy/it/Casi d'Uso/Casi d'Uso.md
- it/Casi d'Uso/Scenari Reali.md -> dev/legacy/it/Casi d'Uso/Scenari Reali.md
- it/Concetti Base/Concetti Base.md -> dev/legacy/it/Concetti Base/Concetti Base.md
- it/Concetti Base/Continuita.md -> dev/legacy/it/Concetti Base/Continuita.md
- it/Concetti Base/Macchina del Tempo.md -> dev/legacy/it/Concetti Base/Macchina del Tempo.md
- it/Concetti Base/Ricostruzione del Tempo.md -> dev/legacy/it/Concetti Base/Ricostruzione del Tempo.md
- it/Concetti Base/Sessione.md -> dev/legacy/it/Concetti Base/Sessione.md
- it/Concetti Base/Tag.md -> dev/legacy/it/Concetti Base/Tag.md
- it/FAQ/Domande Frequenti.md -> dev/legacy/it/FAQ/Domande Frequenti.md
- it/Filosofia/Filosofia.md -> dev/legacy/it/Filosofia/Filosofia.md
- it/Flussi di Lavoro/Flussi di Lavoro.md -> dev/legacy/it/Flussi di Lavoro/Flussi di Lavoro.md
- it/Flussi di Lavoro/Flussi di Tracciamento Comuni.md -> dev/legacy/it/Flussi di Lavoro/Flussi di Tracciamento Comuni.md
- it/Funzioni/Catene.md -> dev/legacy/it/Funzioni/Catene.md
- it/Funzioni/Funzioni.md -> dev/legacy/it/Funzioni/Funzioni.md
- it/Funzioni/Importazione, Esportazione e Vault.md -> dev/legacy/it/Funzioni/Importazione, Esportazione e Vault.md
- it/Funzioni/Periodi di Vita.md -> dev/legacy/it/Funzioni/Periodi di Vita.md
- it/Funzioni/Sessioni Temporizzate e Alert.md -> dev/legacy/it/Funzioni/Sessioni Temporizzate e Alert.md
- it/Funzioni/Widget Schermata Home.md -> dev/legacy/it/Funzioni/Widget Schermata Home.md
- it/Guida Introduttiva/Inizia da Qui.md -> dev/legacy/it/Guida Introduttiva/Inizia da Qui.md
- it/Guida Introduttiva/La Prima Sessione.md -> dev/legacy/it/Guida Introduttiva/La Prima Sessione.md
- it/Guida Introduttiva/Primo Avvio e Configurazione.md -> dev/legacy/it/Guida Introduttiva/Primo Avvio e Configurazione.md
- it/Home.md -> dev/legacy/it/Home.md
- it/Interfaccia/Adesso.md -> dev/legacy/it/Interfaccia/Adesso.md
- it/Interfaccia/Aree Secondarie e Impostazioni.md -> dev/legacy/it/Interfaccia/Aree Secondarie e Impostazioni.md
- it/Interfaccia/Cronologia.md -> dev/legacy/it/Interfaccia/Cronologia.md
- it/Interfaccia/Interfaccia.md -> dev/legacy/it/Interfaccia/Interfaccia.md
- it/Interfaccia/Tag.md -> dev/legacy/it/Interfaccia/Tag.md
- it/Risoluzione Problemi/Risoluzione Problemi.md -> dev/legacy/it/Risoluzione Problemi/Risoluzione Problemi.md
- submission/v493_submission_checklist.md -> dev/legacy/submission/v493_submission_checklist.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
