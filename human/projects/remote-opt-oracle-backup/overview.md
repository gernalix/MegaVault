# remote_opt_oracle_backup Overview

remote_opt_oracle_backup is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Remote Oracle backup script set for restic backup/prune/systemd units under the Oracle backup runtime path; source docs are sparse, so verify remote runtime before edits.

## Why It Exists
- backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- check_backup_health.py: import os, time, sys, traceback
- prune.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- prune_local_snapshots.sh: STATE_DIR="/var/lib/oracle_backup"

## Current State
- Repository: `/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup`
- Branch at enrichment: `main`
- Latest local commit at enrichment: `62254c3`
- Stack signals: Python, Shell, UNKNOWN, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/remote-opt-oracle-backup.md)
- Metadata: [dev/project.metadata.json](../../../../projects/vm_oracle/remote_opt_oracle_backup/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/vm_oracle/remote_opt_oracle_backup/dev/legacy)
- Repository: [repo path](../../../../projects/vm_oracle/remote_opt_oracle_backup)
