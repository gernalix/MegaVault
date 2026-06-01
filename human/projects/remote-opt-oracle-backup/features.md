# remote_opt_oracle_backup Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- backup.sh: # Use sqlite online backup API
- backup.sh: # Now run restic backup to each repo
- backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- check_backup_health.py: import os, time, sys, traceback
- prune.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- prune_local_snapshots.sh: STATE_DIR="/var/lib/oracle_backup"

## Useful Limits And Boundaries
- backup.sh: echo "[*] oracle-backup @ $ts"
- backup.sh: echo "[!] Another oracle-backup restic job is already running."
- backup.sh: # Use sqlite online backup API
- backup.sh: sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- backup.sh: # Now run restic backup to each repo
- backup.sh: echo "[*] Restic backup..."
- backup.sh: if ! rclone copyto "$preflight_file" "$remote_path/.oracle-backup-write-test" --retries 1 --low-level-retries 1; then
- backup.sh: rclone deletefile "$remote_path/.oracle-backup-write-test" // true
- backup.sh: restic -r "$repo" backup \
- backup.sh: echo "[!] all backup repos failed"
- backup.sh: echo "[!] backup OK with repo_success=$repo_success repo_fail=$repo_fail"
- check_backup_health.py: def notify(msg: str, title: str = "Backup alert"):

## Where The Feature Code Appears To Live
- `check_backup_health.py`
- `backup.sh`
- `backup.sh.bak.20260331_220235`
- `backup.sh.bak.20260502_025422`
- `prune.sh`
- `prune.sh.bak.20260331_220235`
- `prune.sh.bak.20260502_032503`
- `prune_local_snapshots.sh`
- `prune_local_snapshots.sh.bak.20260502_025422`
