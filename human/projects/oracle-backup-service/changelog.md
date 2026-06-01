# oracle-backup-service Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
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
| `dev/legacy/docs/CHANGELOG.md` | - Lowered restic/rclone concurrency defaults with `GOMAXPROCS=1`, |
| `dev/legacy/docs/CHANGELOG.md` | - Moved backup/prune units to idle IO scheduling with low CPU/IO weights, |
| `dev/legacy/docs/CHANGELOG.md` | - Changed prune lock behavior to nonblocking by default so retention does not |
| `dev/legacy/docs/CHANGELOG.md` | - Documented the required persistent `/swapfile` host mitigation for this |
| `dev/legacy/docs/CHANGELOG.md` | 1 GB VM when swap is missing. |
| `dev/legacy/docs/CHANGELOG.md` | ### Prompt #284 runtime deployment verification |

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.
