# remote_opt_oracle_backup Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `check_backup_health.py` | notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error") |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `backup.sh` | #!/usr/bin/env bash |
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `check_backup_health.py` | #!/usr/bin/env python3 |
| `check_backup_health.py` | f"Controlla: journalctl -u oracle-backup.service -n 200 --no-pager\n" |
| `prune.sh` | #!/usr/bin/env bash |
| `prune_local_snapshots.sh` | #!/usr/bin/env bash |

## Safety Checks Before Fixing
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
- check_backup_health.py: telegram_notify.notify(msg, title=title, prefix="oracle-backup")
- check_backup_health.py: f"⚠️ Nessun marker di backup trovato ({STATE_FILE}). "
