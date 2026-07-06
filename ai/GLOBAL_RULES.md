# MegaVault Global Rules

## Authority
This file is an operator-readable routing summary. Canonical mandatory rules live in `ai/MEGAVAULT_PROTOCOL.md`; Android-wide rules live in `ai/ANDROID_PROTOCOL.md`; host and system constraints live in `ai/global/HOST_PROFILE.md`. Add new mandatory rules to the canonical protocol first, then keep this file as a navigation layer.

## Resolution Order
1. Open `ai/MEGAVAULT_PROTOCOL.md`.
2. Open `ai/global/HOST_PROFILE.md`.
3. Open the current repo's `dev/project.metadata.json`.
4. Follow `ai_doc` and open the matching project-local `docs/ai/` entry.
5. Use HOST_PROFILE as hardware/system constraint authority.
6. Use project-local `docs/ai/` as the primary project operational source for Codex work.
7. Use project-local `docs/human/` for user-facing explanation only; they are not operational authority.
8. Use `dev/legacy/` only for historical context, missing detail recovery, or audit trails.
9. If architecture, build, tests, safety rules, release rules, data rules, or roadmap change, update the AI doc in the same change.
10. If UX, functionality, user workflows, troubleshooting, or changelog change, update Human docs from the AI doc.
11. Conflict rule: protocol + HOST_PROFILE + metadata + AI doc win over Human docs and legacy docs. If metadata and AI doc conflict, stop and repair metadata/AI doc before continuing.

## Current Host
- Primary host: Windows 11 Pro on Lenovo ThinkPad P14s Gen 5 AMD.
- Canonical Windows paths use `C:\Users\seste\Documents\...`.
- Surface/Linux Mint paths are historical or project-specific unless `HOST_PROFILE.md` says otherwise.

## Global Docs
- HOST_PROFILE_AI: [global/HOST_PROFILE.md](global/HOST_PROFILE.md)
- HOST_PROFILE_HUMAN: [../human/global/HOST_PROFILE.md](../human/global/HOST_PROFILE.md)
- HOST_PROFILE_REQUIRED_FOR: performance, monitoring, automation, service, system tuning, Android tooling, backup, storage, Windows host work, and legacy Linux Mint/freeze investigations.
- SERVICE_REGISTRY_AI: [global/SERVICE_REGISTRY.md](global/SERVICE_REGISTRY.md)
- DATA_REGISTRY_AI: [global/DATA_REGISTRY.md](global/DATA_REGISTRY.md)
- NETWORK_TOPOLOGY_AI: [global/NETWORK_TOPOLOGY.md](global/NETWORK_TOPOLOGY.md)
- STORAGE_TOPOLOGY_AI: [global/STORAGE_TOPOLOGY.md](global/STORAGE_TOPOLOGY.md)
- ALERT_REGISTRY_AI: [global/ALERT_REGISTRY.md](global/ALERT_REGISTRY.md)
- INCIDENT_REGISTRY_AI: [global/INCIDENT_REGISTRY.md](global/INCIDENT_REGISTRY.md)
- SOFTWARE_INVENTORY_AI: [global/SOFTWARE_INVENTORY.md](global/SOFTWARE_INVENTORY.md)
- PROJECT_INDEX_EXTENDED_AI: [global/PROJECT_INDEX_EXTENDED.md](global/PROJECT_INDEX_EXTENDED.md)
- PROJECT_DOCS_MIGRATION_PLAN_AI: [PROJECT_DOCS_MIGRATION_PLAN.md](PROJECT_DOCS_MIGRATION_PLAN.md)
- CODEX_GLOBAL_TIMELINE_DB: [../codex_global_timeline.sqlite](../codex_global_timeline.sqlite)
- CODEX_GLOBAL_TIMELINE_REPORT: [../codex_global_timeline.md](../codex_global_timeline.md)
- CODEX_GLOBAL_TIMELINE_AI: [../codex_global_timeline_ai.md](../codex_global_timeline_ai.md)

## Write Policy
- Do not delete legacy docs casually.
- Do not modify application code or databases for documentation-only tasks.
- Prefer `UNKNOWN`, `TODO`, or `OPEN QUESTION` over invented facts.
- MegaVault stores global/aspecific documentation only: protocols, registries, indices, host profile, topology, service/data/network/storage registries, and global guides.
- Keep project-specific AI/project-operational docs under the project repo's `docs/ai/`.
- Keep project-specific readable docs under the project repo's `docs/human/`.
- Keep AI docs ai-friendly and ultra-compressed: key=value, high density, one fact per line, no filler prose.
- Derive Human docs from AI docs, code, and real state; never use Human docs as the primary operational source.
- Do not accumulate project-specific docs in MegaVault except global indices/registries pointing to projects.
- Every completed Codex task must update the Global Codex Timeline with `build_codex_global_timeline.py` before final response.
- The SQLite timeline is canonical; Markdown timeline files are generated views only; JSON/JSONL exports are optional.
- Timeline events contain synthetic metadata only, must keep source references, must be deduplicated, and must not contain secrets.

## Next-Prompt Rule
For every future Codex prompt inside an indexed repo: `ai/MEGAVAULT_PROTOCOL.md` -> `ai/global/HOST_PROFILE.md` -> `dev/project.metadata.json` -> project-local `docs/ai/` -> task files -> legacy only if the AI docs lack required history -> update project docs -> run `build_codex_global_timeline.py` from MegaVault -> final response.

LAST_UPDATED: 2026-07-06T00:00:00+02:00 by global_codex_timeline
