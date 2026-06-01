# oracle-backup-service Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/docs/OPERATIONS.md` | Give SSH priority and demote any currently running backup until the deployed |
| `dev/legacy/docs/OPERATIONS.md` | For the persistent SSH priority override: |
| `scripts/oracle-backup-healthcheck.sh` | f"/ usage {root_used_pct}% >= {ROOT_USAGE_WARN_PCT}% first observation; warning deferred unless persistent for {ROOT_USAGE_WARN_PERSIST_SECONDS}s or worsens by {ROOT_USAGE_WORSEN_PCT_POINTS} points", |
| `scripts/oracle-backup-healthcheck.sh` | "root_usage:PENDING", |

## Deferred Or Risky Work
- dev/legacy/docs/TROUBLESHOOTING.md: The failure happened even for a 1-byte `rclone copyto` test, so restic could not reliably create locks or write pack data. The remote repo was effectively write-blocked by quota.
- dev/legacy/docs/OPERATIONS.md: sudo dmesg -T / egrep -i 'oom/out of memory/killed process/blocked for more/hung task/throttl/i/o error' / tail -120
- scripts/backup.sh: record_remote_failure "$repo" "${last_repo_error:-unknown repo failure}"
- scripts/backup.sh: echo "[!] local fallback repo failed: $LOCAL_FALLBACK_REPO (${last_repo_error:-unknown repo failure})"
- scripts/check_remote_quota.py: print(f"REMOTE_QUOTA UNKNOWN path={path} error={exc}")
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/README.md: - `Backup remote degraded` warning when the remote is blocked but emergency repo protection is recent
- dev/legacy/README.md: `/var/lib/oracle_backup/sqlite_snapshots` contains temporary SQLite online-backup copies created before restic runs. They are safe to prune after restic has had a chance to back up recent copies; live databases are outside this directory.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
