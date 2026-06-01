# oracle-backup-service AI OPERATIONS

PROJECT
- name: oracle-backup-service
- slug: oracle-backup-service
- purpose: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least on
- current_status: Working tree has 15 non-clean entries; do not mix unrelated changes. First entries: M config/oracle_backup.env.example, M scripts/backup.sh, M scripts/check_backup_health.py, M scripts/oracle-backup-healthcheck.sh, M systemd/oracle-backup.timer
- repo_path: `/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service`
- remote: `https://github.com/gernalix/oracle-backup-service.git`
- branch: `fix/degraded-healthcheck-state`
- last_verified_commit/date: `058c59b` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `scripts/check_backup_health.py`
- `scripts/check_remote_quota.py`
important_folders:
- `config`
- `dev`
- `scripts`
- `systemd`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `scripts/backup.sh`
- `scripts/check_backup_health.py`
- `scripts/check_remote_quota.py`
- `scripts/oracle-backup-healthcheck.sh`
- `scripts/prune.sh`
- `scripts/prune_local_snapshots.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/docs/TROUBLESHOOTING.md: - `[oracle-backup] Healthcheck`
- dev/legacy/docs/CHANGELOG.md: ### Prompt #739 running backup healthcheck noise
- dev/legacy/docs/OPERATIONS.md: last=$(sudo cat /var/lib/oracle_backup/last_any_success_epoch 2>/dev/null // sudo cat /var/lib/oracle_backup/last_successful_epoch)
- scripts/backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/check_backup_health.py: ENV_FILE = os.environ.get("ORACLE_BACKUP_ENV_FILE", "/etc/oracle_backup/oracle_backup.env")
- scripts/check_remote_quota.py: ENV_PATH = Path("/etc/oracle_backup/oracle_backup.env")
- scripts/oracle-backup-healthcheck.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/prune.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/prune_local_snapshots.sh: STATE_DIR="/var/lib/oracle_backup"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # oracle-backup-service |
| `dev/legacy/README.md` | ## Architecture |
| `dev/legacy/README.md` | ## Runtime Paths |
| `dev/legacy/README.md` | ## Backup Flow |
| `dev/legacy/README.md` | ## Local Fallback Guardrails |
| `dev/legacy/README.md` | ## VM Resource Guardrails |
| `dev/legacy/README.md` | ## Alert Deduplication |
| `dev/legacy/README.md` | ## SQLite Snapshot Retention |
| `dev/legacy/README.md` | ## Systemd |
| `dev/legacy/README.md` | ## Restic Checks |
| `dev/legacy/docs/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Incident Symptoms |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Root Cause |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Fix Applied |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Current Expected Behavior |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Healthcheck Severity |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Repeated Telegram Warnings |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Useful Commands |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # oracle-backup-service |
| `dev/legacy/README.md` | Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least  |
| `dev/legacy/README.md` | - `scripts/backup.sh`: main oneshot job for `oracle-backup.service`. |
| `dev/legacy/README.md` | - `scripts/prune.sh`: restic retention job for `oracle-backup-prune.service`. |
| `dev/legacy/README.md` | - `scripts/check_backup_health.py`: freshness monitor used by `oracle-backup-monitor.service`. |
| `dev/legacy/README.md` | - `scripts/oracle-backup-healthcheck.sh`: preventive read-only healthcheck used by `oracle-backup-healthcheck.service`. |
| `dev/legacy/README.md` | - Any successful backup marker: `/var/lib/oracle_backup/last_any_success_epoch` |
| `dev/legacy/README.md` | - Last backup status: `/var/lib/oracle_backup/last_backup_status` |
| `dev/legacy/README.md` | - Healthcheck alert lock: `/run/oracle-backup-healthcheck-alert.lock` |
| `dev/legacy/README.md` | - Freshness monitor alert lock: `/run/lock/oracle-backup-monitor-alert.lock` |
| `dev/legacy/README.md` | The VM runtime is a flat install, not a git checkout. Deploy `scripts/backup.sh` |
| `dev/legacy/README.md` | to `/opt/oracle_backup/backup.sh`, `scripts/check_backup_health.py` to |
| `dev/legacy/README.md` | `scripts/oracle-backup-healthcheck.sh` to |
| `dev/legacy/README.md` | `/usr/local/bin/oracle-backup-healthcheck.sh`. Always confirm the active paths |
| `dev/legacy/README.md` | ## Backup Flow |
| `dev/legacy/README.md` | 2. Prune local SQLite snapshots within configured safety limits. |
| `dev/legacy/README.md` | 5. For `rclone:` repos, run a 1-byte write preflight first. If the backend rejects writes, skip expensive restic upload attempts. |
| `dev/legacy/README.md` | The emergency repo defaults to `/var/lib/oracle_backup/emergency_repo`. When fallback succeeds, `backup.sh` applies local restic retention with: |
| `dev/legacy/README.md` | Retention warnings are written to `/var/lib/oracle_backup/local_fallback_retention_status` and do not turn a successful fallback backup into a failed backup. |
| `dev/legacy/README.md` | The read-only healthcheck reports emergency repo size with configurable thresholds: |
| `dev/legacy/README.md` | - `OK`: recent successful backup and no current remote failure marker. |
| `dev/legacy/README.md` | - `CRITICAL`: neither remote nor local fallback success is fresh enough, or the emergency repo exceeds the critical size guard. |
| `dev/legacy/README.md` | - `BACKUP_ACTIVE_GRACE_MINUTES=60`: grace window while `oracle-backup.service` is still running. |
| `dev/legacy/README.md` | - `BACKUP_RUNNING_WARNING_MINUTES=30`: active backup duration that separates normal running from long-running warning. |
| `dev/legacy/README.md` | - `BACKUP_HEARTBEAT_STALE_SECONDS=300`: heartbeat age after which an active backup is suspicious. |
| `dev/legacy/README.md` | - `MIN_BACKUP_INTERVAL_SECONDS=900`: timer runs skip quickly when a recent success already exists. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/README.md` | The VM runtime is a flat install, not a git checkout. Deploy `scripts/backup.sh` |
| `dev/legacy/README.md` | with `systemctl cat`; a correct git branch alone does not prove the VM is using |
| `dev/legacy/README.md` | sudo systemctl daemon-reload |
| `dev/legacy/README.md` | sudo systemctl enable --now oracle-backup.timer |
| `dev/legacy/README.md` | sudo systemctl status oracle-backup.service --no-pager |
| `dev/legacy/README.md` | sudo systemctl status oracle-backup.timer --no-pager |
| `dev/legacy/README.md` | systemctl list-timers --all --no-pager / grep oracle-backup |
| `dev/legacy/README.md` | systemctl list-units 'oracle-backup*' --all --no-pager |
| `dev/legacy/README.md` | systemctl list-timers 'oracle-backup*' --all --no-pager |
| `dev/legacy/README.md` | systemctl cat \ |
| `dev/legacy/README.md` | sudo systemctl start oracle-backup.service |
| `dev/legacy/README.md` | journalctl -u oracle-backup.service -n 200 --no-pager |
| `dev/legacy/README.md` | sudo systemctl start oracle-backup-healthcheck.service |
| `dev/legacy/README.md` | journalctl -u oracle-backup-healthcheck.service -n 80 --no-pager |
| `dev/legacy/README.md` | sudo bash -lc 'source /etc/oracle_backup/oracle_backup.env; export RESTIC_PASSWORD; restic -r /var/lib/oracle_backup/emergency_repo snapshots --compact' |
| `dev/legacy/README.md` | sudo bash -lc 'source /etc/oracle_backup/oracle_backup.env; rclone size oci:bucket-20260206-0730/oraclevm' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl -u oracle-backup.service -n 200 --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - The git checkout under `/opt/oracle_backup` was a root-owned flat local repo |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl cat \ |
| `dev/legacy/docs/TROUBLESHOOTING.md` | sudo python3 -m json.tool /var/lib/oracle_backup/backup_monitor_state.json |
| `dev/legacy/docs/TROUBLESHOOTING.md` | sudo systemctl start oracle-backup-monitor.service |
| `dev/legacy/docs/TROUBLESHOOTING.md` | sudo systemctl start oracle-backup-localprune.service |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl -u oracle-backup-localprune.service -n 80 --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl status oracle-backup.service --no-pager |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/docs/TROUBLESHOOTING.md: The failure happened even for a 1-byte `rclone copyto` test, so restic could not reliably create locks or write pack data. The remote repo was effectively write-blocked by quota.
- dev/legacy/docs/TROUBLESHOOTING.md: Timeout, server not responding
- dev/legacy/docs/OPERATIONS.md: timeout 10 bash -lc 'exec 3<>/dev/tcp/150.230.148.128/22; IFS= read -r -t 5 line <&3; printf "%s\n" "$line"'
- scripts/backup.sh: sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- scripts/backup.sh: if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock >> "$retention_log" 2>&1 && \
- scripts/backup.sh: timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" nice -n 19 ionice -c3 \
- scripts/backup.sh: if ! timeout --kill-after=60s 300 restic -r "$repo" unlock; then
- scripts/backup.sh: if ! timeout --kill-after=60s "$RESTIC_BACKUP_TIMEOUT_SECONDS" nice -n 19 ionice -c3 \
- scripts/check_remote_quota.py: ["timeout", "90", "rclone", "size", path],
- scripts/prune.sh: if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock && \

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/docs/TROUBLESHOOTING.md` | Local fallback retention runs only after a successful fallback backup. Its default policy is `LOCAL_FALLBACK_KEEP_LAST=24` and `LOCAL_FALLBACK_RETENTION_GROUP_BY=host,tags`. Retention failure is recorded as `WARNING` in `/va |
| `dev/legacy/docs/TROUBLESHOOTING.md` | The fix stores a stable alert fingerprint in `/var/lib/oracle_backup/healthcheck_alert_state.json` and serializes alert decisions with `/run/oracle-backup-healthcheck-alert.lock`. Telegram is sent only for state changes, sta |
| `dev/legacy/docs/TROUBLESHOOTING.md` | The separate freshness monitor stores its own deduplication state in `/var/lib/oracle_backup/backup_monitor_state.json` and uses `/run/lock/oracle-backup-monitor-alert.lock`. It sends: |
| `dev/legacy/README.md` | with `systemctl cat`; a correct git branch alone does not prove the VM is using |
| `dev/legacy/docs/OPERATIONS.md` | sudo bash -lc 'source /etc/oracle_backup/oracle_backup.env; printf "keep-last=%s group-by=%s valid=%smin warn=%sGB critical=%sGB\n" "${LOCAL_FALLBACK_KEEP_LAST:-24}" "${LOCAL_FALLBACK_RETENTION_GROUP_BY:-host,tags}" "${LOCAL_FALL |
| `dev/legacy/docs/CHANGELOG.md` | - Telegram now sends only on state change, stable cause change, significant metric worsening, rare reminder, or recovery. |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # oracle-backup-service |
| `dev/legacy/README.md` | Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least  |
| `dev/legacy/README.md` | - `scripts/backup.sh`: main oneshot job for `oracle-backup.service`. |
| `dev/legacy/README.md` | - `scripts/prune.sh`: restic retention job for `oracle-backup-prune.service`. |
| `dev/legacy/README.md` | - `scripts/check_backup_health.py`: freshness monitor used by `oracle-backup-monitor.service`. |
| `dev/legacy/README.md` | - `scripts/oracle-backup-healthcheck.sh`: preventive read-only healthcheck used by `oracle-backup-healthcheck.service`. |
| `dev/legacy/README.md` | - Any successful backup marker: `/var/lib/oracle_backup/last_any_success_epoch` |
| `dev/legacy/README.md` | - Last backup status: `/var/lib/oracle_backup/last_backup_status` |
| `dev/legacy/README.md` | - Healthcheck alert lock: `/run/oracle-backup-healthcheck-alert.lock` |
| `dev/legacy/README.md` | - Freshness monitor alert lock: `/run/lock/oracle-backup-monitor-alert.lock` |
| `dev/legacy/README.md` | The VM runtime is a flat install, not a git checkout. Deploy `scripts/backup.sh` |
| `dev/legacy/README.md` | to `/opt/oracle_backup/backup.sh`, `scripts/check_backup_health.py` to |
| `dev/legacy/README.md` | `scripts/oracle-backup-healthcheck.sh` to |
| `dev/legacy/README.md` | `/usr/local/bin/oracle-backup-healthcheck.sh`. Always confirm the active paths |
| `dev/legacy/README.md` | ## Backup Flow |
| `dev/legacy/README.md` | 2. Prune local SQLite snapshots within configured safety limits. |
| `dev/legacy/README.md` | The emergency repo defaults to `/var/lib/oracle_backup/emergency_repo`. When fallback succeeds, `backup.sh` applies local restic retention with: |
| `dev/legacy/README.md` | Retention warnings are written to `/var/lib/oracle_backup/local_fallback_retention_status` and do not turn a successful fallback backup into a failed backup. |
| `dev/legacy/README.md` | - `OK`: recent successful backup and no current remote failure marker. |
| `dev/legacy/README.md` | - `BACKUP_ACTIVE_GRACE_MINUTES=60`: grace window while `oracle-backup.service` is still running. |
| `dev/legacy/README.md` | - `BACKUP_RUNNING_WARNING_MINUTES=30`: active backup duration that separates normal running from long-running warning. |
| `dev/legacy/README.md` | - `BACKUP_HEARTBEAT_STALE_SECONDS=300`: heartbeat age after which an active backup is suspicious. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Last remote error: `/var/lib/oracle_backup/last_remote_error` |
| `dev/legacy/README.md` | 6. If all configured repos fail, back up to `LOCAL_FALLBACK_REPO`. |
| `dev/legacy/README.md` | - `OK`: recent successful backup and no current remote failure marker. |
| `dev/legacy/README.md` | systemd/PAM and make SSH fail before the banner. The service units therefore run |
| `dev/legacy/README.md` | - stable cause change, for example a different failed repo or different remote error |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Root Cause |
| `dev/legacy/docs/TROUBLESHOOTING.md` | The failure happened even for a 1-byte `rclone copyto` test, so restic could not reliably create locks or write pack data. The remote repo was effectively write-blocked by quota. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - `OK`: recent successful backup and no active remote failure marker. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Local fallback retention runs only after a successful fallback backup. Its default policy is `LOCAL_FALLBACK_KEEP_LAST=24` and `LOCAL_FALLBACK_RETENTION_GROUP_BY=host,tags`. Retention failure is recorded as `WARNING` in `/va |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - `REMOTE_DEGRADED` details included changing values such as backup age and remote failure epoch, so identical degraded state looked different to the old deduplication logic. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | On the VM observed during prompt `#284`, the root cause was not the committed |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Timeout, server not responding |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Observed root cause on the Oracle VM: |
| `dev/legacy/docs/CHANGELOG.md` | - Healthcheck deduplication compared full detail strings. Those details included changing values like backup age and remote failure epoch, making the same stable degraded condition look new. |
| `dev/legacy/docs/CHANGELOG.md` | - Retention warnings are recorded but do not make the successful fallback backup fail. |
| `dev/legacy/docs/CHANGELOG.md` | - Added `last_remote_error` and remote failure timestamp markers. |
| `dev/legacy/docs/CHANGELOG.md` | Known follow-up: |
| `dev/legacy/docs/OPERATIONS.md` | timeout 10 bash -lc 'exec 3<>/dev/tcp/150.230.148.128/22; IFS= read -r -t 5 line <&3; printf "%s\n" "$line"' |
| `dev/legacy/docs/OPERATIONS.md` | - `OK`: a recent backup succeeded and there is no active remote failure marker. |
| `dev/legacy/docs/OPERATIONS.md` | as a service failure. |
| `dev/legacy/docs/OPERATIONS.md` | failure mode was: |
| `dev/legacy/docs/OPERATIONS.md` | sudo dmesg -T / egrep -i 'oom/out of memory/killed process/blocked for more/hung task/throttl/i/o error' / tail -120 |
| `scripts/backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `scripts/backup.sh` | if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock >> "$retention_log" 2>&1 && \ |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: # oracle-backup-service
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/README.md: - `scripts/backup.sh`: main oneshot job for `oracle-backup.service`.
- dev/legacy/README.md: - `scripts/prune.sh`: restic retention job for `oracle-backup-prune.service`.
- dev/legacy/README.md: - `scripts/check_backup_health.py`: freshness monitor used by `oracle-backup-monitor.service`.
- dev/legacy/README.md: - `scripts/oracle-backup-healthcheck.sh`: preventive read-only healthcheck used by `oracle-backup-healthcheck.service`.
- dev/legacy/README.md: - Any successful backup marker: `/var/lib/oracle_backup/last_any_success_epoch`
- dev/legacy/README.md: - Last backup status: `/var/lib/oracle_backup/last_backup_status`
- dev/legacy/README.md: - Healthcheck alert lock: `/run/oracle-backup-healthcheck-alert.lock`
- dev/legacy/README.md: - Freshness monitor alert lock: `/run/lock/oracle-backup-monitor-alert.lock`
- dev/legacy/README.md: The VM runtime is a flat install, not a git checkout. Deploy `scripts/backup.sh`
- dev/legacy/README.md: to `/opt/oracle_backup/backup.sh`, `scripts/check_backup_health.py` to
- dev/legacy/README.md: `scripts/oracle-backup-healthcheck.sh` to
- dev/legacy/README.md: `/usr/local/bin/oracle-backup-healthcheck.sh`. Always confirm the active paths
- dev/legacy/README.md: ## Backup Flow
- dev/legacy/README.md: 2. Prune local SQLite snapshots within configured safety limits.

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/docs/CHANGELOG.md` | # Changelog |
| `dev/legacy/docs/CHANGELOG.md` | ## 2026-05-10 |
| `dev/legacy/docs/CHANGELOG.md` | ### Prompt #739 running backup healthcheck noise |
| `dev/legacy/docs/CHANGELOG.md` | - Healthcheck sent a Telegram warning while `oracle-backup.service` was active, |
| `dev/legacy/docs/CHANGELOG.md` | - The active-backup path treated any stale `last_any_success_epoch` plus recent |
| `dev/legacy/docs/CHANGELOG.md` | - Added `BACKUP_RUNNING_WARNING_MINUTES=30` and |
| `dev/legacy/docs/CHANGELOG.md` | - Healthcheck now reports active backups with fresh heartbeat and duration below |
| `dev/legacy/docs/CHANGELOG.md` | - Long-running active backups still warn, stale heartbeat warns, and active |
| `dev/legacy/docs/CHANGELOG.md` | ### Prompt #611 VM stall and SSH banner responsiveness |
| `dev/legacy/docs/CHANGELOG.md` | - During long oracle-backup/restic fallback runs, SSH frequently reached TCP 22 |
| `dev/legacy/docs/CHANGELOG.md` | - systemd and journald showed watchdog/timeouts while `oracle-backup.service` |
| `dev/legacy/docs/CHANGELOG.md` | - The VM is `VM.Standard.E2.1.Micro` with 1 GB RAM and no swap. |
| `dev/legacy/docs/CHANGELOG.md` | - A long local restic fallback ran on the same root disk while load average was |
| `dev/legacy/docs/CHANGELOG.md` | - `kswapd0` activity and OOM killer events showed real memory pressure. |
| `dev/legacy/docs/CHANGELOG.md` | - `snapd`, `systemd-journald`, PAM/systemd user session startup, and sshd all |
| `dev/legacy/docs/CHANGELOG.md` | - Added backup throttling with `MIN_BACKUP_INTERVAL_SECONDS=900`, so the 5-minute |
| `dev/legacy/docs/CHANGELOG.md` | - Added active backup heartbeat markers: |
| `dev/legacy/docs/CHANGELOG.md` | - Updated monitor and healthcheck to report a recent backup heartbeat as |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/docs/OPERATIONS.md` | Give SSH priority and demote any currently running backup until the deployed |
| `dev/legacy/docs/OPERATIONS.md` | For the persistent SSH priority override: |
| `scripts/oracle-backup-healthcheck.sh` | f"/ usage {root_used_pct}% >= {ROOT_USAGE_WARN_PCT}% first observation; warning deferred unless persistent for {ROOT_USAGE_WARN_PERSIST_SECONDS}s or worsens by {ROOT_USAGE_WORSEN_PCT_POINTS} points", |
| `scripts/oracle-backup-healthcheck.sh` | "root_usage:PENDING", |

LEGACY_SUMMARY
- legacy_docs_read_count: 11
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/docs/TROUBLESHOOTING.md`
- `dev/legacy/docs/CHANGELOG.md`
- `dev/legacy/docs/OPERATIONS.md`
- `scripts/backup.sh`
- `scripts/check_backup_health.py`
- `scripts/check_remote_quota.py`
- `scripts/oracle-backup-healthcheck.sh`
- `scripts/prune.sh`
- `scripts/prune_local_snapshots.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../projects/vm_oracle/oracle-backup-service/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/oracle-backup-service/overview.md)
- human_folder: [human folder](../../human/projects/oracle-backup-service)
- legacy_docs: [dev/legacy](../../../projects/vm_oracle/oracle-backup-service/dev/legacy)
- repo_path: [repo](../../../projects/vm_oracle/oracle-backup-service)

OPEN_QUESTIONS
- scripts/backup.sh: record_remote_failure "$repo" "${last_repo_error:-unknown repo failure}"
- scripts/backup.sh: echo "[!] local fallback repo failed: $LOCAL_FALLBACK_REPO (${last_repo_error:-unknown repo failure})"
- scripts/check_remote_quota.py: print(f"REMOTE_QUOTA UNKNOWN path={path} error={exc}")
