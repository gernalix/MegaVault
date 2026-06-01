# os-observer Overview

os-observer is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Linux Mint black-box recorder: user-systemd timer records read-only telemetry into SQLite, maintains diagnostic knowledge, exports bounded context for ChatGPT/Codex, and has guarded autofix/heartbeat logic.

## Why It Exists
- dev/legacy/README.md: `os-observer` e un black-box recorder diagnostico leggero per Linux Mint. Mantiene un DB SQLite sempre aggiornato tramite timer systemd user e produce export bounded per ChatGPT/Codex.
- dev/legacy/dev/INDEX.md: # os-observer autofix agent v19
- dev/legacy/ARCHITECTURE.md: `os-observer.timer` avvia `os_observer.sh --once`. Il run prende il lock, inizializza schema/WAL, raccoglie metriche read-only, salva snapshot/eventi in `telemetry.sqlite`, aggiorna memoria diagnostica in `knowledge.sqlite`, valuta 
- dev/legacy/dev/ARCHITECTURE.md: - `os_observer_autofix_agent.py`: correlazione, dedup, fix allowlist, watcher Uptime Kuma dashboard #8, freeze-risk guard locale e heartbeat Kuma indipendente dal ciclo recovery.
- dev/legacy/dev/AGENT_RULES.md: - Usa timeout per comandi lenti.
- dev/legacy/PATCH_WORKFLOW.md: ## Perche non sostituire piu il DB live
- dev/legacy/dev/TEST_PLAN.md: - `python -m py_compile os_observer_autofix_agent.py`

## Current State
- Repository: `/home/daniele/codex-workspace/os-observer`
- Branch at enrichment: `codex/prompt-914582`
- Latest local commit at enrichment: `b1ed3b0`
- Stack signals: Python, Shell, UNKNOWN, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/os-observer.md)
- Metadata: [dev/project.metadata.json](../../../../os-observer/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../os-observer/dev/legacy)
- Repository: [repo path](../../../../os-observer)
