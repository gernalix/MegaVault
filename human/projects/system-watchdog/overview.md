# system_watchdog Overview

system_watchdog is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Persistent heartbeat sender for a Uptime Kuma push monitor.

## Why It Exists
- dev/legacy/README.md: Persistent heartbeat sender for a Uptime Kuma push monitor.
- dev/legacy/docs/ARCHITECTURE.md: The Mint watchdog is intentionally small:
- dev/legacy/docs/TROUBLESHOOTING.md: If HTTP push fails, the service continues retrying. Check network reachability to:
- dev/legacy/docs/CODEX_CONTEXT.md: `/home/daniele/codex-workspace/system_watchdog`
- dev/legacy/docs/UPDATE_PROCEDURE.md: sudo systemctl restart system-watchdog.service
- requirements.txt: # No third-party Python packages are required.
- install.sh: ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

## Current State
- Repository: `/home/daniele/codex-workspace/system_watchdog`
- Branch at enrichment: `master`
- Latest local commit at enrichment: `d93002d`
- Stack signals: Python, Shell, Python tooling, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/system-watchdog.md)
- Metadata: [dev/project.metadata.json](../../../../system_watchdog/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../system_watchdog/dev/legacy)
- Repository: [repo path](../../../../system_watchdog)
