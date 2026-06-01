# amici_fb Overview

amici_fb is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Linux Mint user-level Facebook automation that opens Facebook with a browser profile, processes friends/URLs, and records local state in SQLite; treat credentials and browser session data as sensitive.

## Why It Exists
- dev/legacy/README.md: `amici_fb` is a Linux Mint user-level automation that opens Facebook with
- dev/legacy/docs/ARCHITECTURE.md: - `amici_fb.py`: main scraper and data pipeline.
- dev/legacy/docs/TROUBLESHOOTING.md: Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`,
- dev/legacy/CHANGELOG.md: - Repaired the Linux Mint user-level `amici_fb.service` and
- dev/legacy/docs/OPERATIONS.md: Use the same runner as systemd:
- dev/legacy/AGENTS.md: This repo runs a real Facebook scraper on the local Linux Mint machine. Treat it
- _shared/__init__.py: """Local shared helpers for amici_fb."""

## Current State
- Repository: `/home/daniele/codex-workspace/scripts/amici_fb`
- Branch at enrichment: `master`
- Latest local commit at enrichment: `0e021f6`
- Stack signals: Python, Shell, Python tooling, playwright, requests, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/amici-fb.md)
- Metadata: [dev/project.metadata.json](../../../../scripts/amici_fb/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../scripts/amici_fb/dev/legacy)
- Repository: [repo path](../../../../scripts/amici_fb)
