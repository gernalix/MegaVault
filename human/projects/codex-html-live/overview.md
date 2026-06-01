# codex-html-live Overview

codex-html-live is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Live HTML archive for Codex JSONL sessions: watches session files and renders browser-readable chat archives without relying on tmux.

## Why It Exists
- dev/legacy/README.md: Live HTML archive for Codex JSONL sessions without tmux.
- dev/legacy/dev/ARCHITECTURE.md: - `codex_html_live.py`: Python standard-library CLI, renderer, daemon loop, installer.
- dev/legacy/dev/AGENT_RULES.md: These rules are binding for future Codex sessions working on this project.
- dev/legacy/dev/TEST_PLAN.md: python3 -m py_compile codex_html_live.py
- dev/legacy/dev/CHANGELOG.md: - Fixed dashboard UX so session IDs and an explicit `Open` column link to chat HTML files, with full-row hover and pointer affordance.
- codex_html_live.py: from dataclasses import dataclass, field
- tests/test_codex_html_live.py: ROOT = Path(__file__).resolve().parents[1]

## Current State
- Repository: `/home/daniele/codex-workspace/codex-html-live`
- Branch at enrichment: `master`
- Latest local commit at enrichment: `1e8ecaa`
- Stack signals: Python, UNKNOWN, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/codex-html-live.md)
- Metadata: [dev/project.metadata.json](../../../../codex-html-live/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../codex-html-live/dev/legacy)
- Repository: [repo path](../../../../codex-html-live)
