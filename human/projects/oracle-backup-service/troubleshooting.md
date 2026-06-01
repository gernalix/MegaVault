# oracle-backup-service Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
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
