# chatgpt-chrome-debug Overview

chatgpt-chrome-debug is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: ChatGPT Chrome Redirect Debug Toolkit

## Why It Exists
- dev/legacy/README.md: # ChatGPT Chrome Redirect Debug Toolkit
- dev/legacy/KNOWN_PATTERNS.md: Pattern da riconoscere nei log:
- dev/legacy/QUICK_FIXES.md: Applicare solo dopo avere raccolto almeno uno snapshot di redirect.
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`.
- package.json: "name": "chatgpt-chrome-debug",
- START_DEBUGGING.sh: ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
- scripts/common.sh: ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

## Current State
- Repository: `/home/daniele/codex-workspace/chatgpt-chrome-debug`
- Branch at enrichment: `master`
- Latest local commit at enrichment: `fdd3773`
- Stack signals: JavaScript/TypeScript, Python, Shell, Node/npm, playwright, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/chatgpt-chrome-debug.md)
- Metadata: [dev/project.metadata.json](../../../../chatgpt-chrome-debug/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../chatgpt-chrome-debug/dev/legacy)
- Repository: [repo path](../../../../chatgpt-chrome-debug)
