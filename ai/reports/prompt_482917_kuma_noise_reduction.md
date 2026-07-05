# Prompt 482917 Uptime Kuma Noise Reduction

META:
prompt=482917
date=2026-06-06
scope=Uptime Kuma VM + local heartbeat pushers; os-observer explicitly excluded and removed from live MegaVault project indexes
protocol=MEGAVAULT_PROTOCOL.md:v2
follow_up=prompt_618903_mint_home_backup_rsync137.md resolves mint-home-backup rsync_exit=137 as ABORTED_SAFE load-guard classification bug; this report remains the historical #482917 baseline.

KUMA:
host=http://150.230.148.128:3001
vm=instance-20260201-1126
container=uptime-kuma
image=louislam/uptime-kuma:2.3.2
db=/opt/uptime-kuma/data/kuma.db
backup=/opt/uptime-kuma/backups/kuma-pre-482917-20260606T181225Z.db
access=SSH with project vm_oracle key; no browser login required

INVENTORY:
| id | monitor | type | active_after | interval | timeout | retries | notification | tags_after | class | historical_7d |
|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| 1 | mint heartbeat | push | 0 | 60 | 48 | 4 | Telegram | 482917-reviewed,push-monitor,obsolete-disabled | OBSOLETE | transitions=63 down_up_10m=3 |
| 2 | rsync-transfer | push | 0 | 178 | 48 | 0 | Telegram | 482917-reviewed,push-monitor,obsolete-disabled | OBSOLETE | transitions=31 down_up_10m=12 |
| 3 | cloud backup | push | 1 | 180 | 60 | 2 | Telegram | 482917-reviewed,push-monitor | NOISY_FIXED | transitions=141 down_up_10m=70 |
| 4 | mint-home-backup | push | 1 | 900 | 60 | 1 | Telegram | 482917-reviewed,push-monitor | BROKEN_REAL | transitions=33 down_up_10m=17 |
| 5 | amici_fb | push | 1 | 86400 | 48 | 2 | Telegram | 482917-reviewed,push-monitor | HEALTHY | transitions=5 |
| 6 | disk-usage-monitor | push | 1 | 420 | 60 | 2 | Telegram | 482917-reviewed,push-monitor | NOISY_FIXED | transitions=596 down_up_10m=19 |
| 7 | parcel-tracker | push | 1 | 2400 | 60 | 2 | Telegram | 482917-reviewed,push-monitor | HEALTHY | transitions=99 |
| 9 | mint-home-backup-retention | push | 1 | 180 | 60 | 2 | Telegram | 482917-reviewed,push-monitor | NOISY_FIXED | transitions=194 down_up_10m=32 |
| 10 | codex-token-watcher | push | 0 | 60 | 48 | 3 | Telegram | 482917-reviewed,push-monitor,obsolete-disabled | OBSOLETE | transitions=34 down_up_10m=1 |
| 11 | software audit mint | push | 1 | 120 | 60 | 2 | Telegram | 482917-reviewed,push-monitor | NOISY_FIXED | transitions=837 down_up_10m=62 |

KUMA_CHANGES:
- Disabled obsolete monitors: id 1 `mint heartbeat`, id 2 `rsync-transfer`, id 10 `codex-token-watcher`.
- Widened active noisy push monitors: cloud backup, disk-usage-monitor, parcel-tracker, retention, software audit mint.
- Added tags `482917-reviewed` and `push-monitor` to all reviewed monitors; added `obsolete-disabled` to disabled obsolete monitors.
- Kept Telegram notification association unchanged to avoid suppressing real alerts.
- Restarted container after DB update; container returned healthy.

CODE_CHANGES:
- mint-cloud-backup: pusher `flock`, object-only dashboard JSON, explicit fallback message, timer every 2 minutes.
- mint-update-tracker: SQLite busy timeout 30000ms, longer retry/backoff, Kuma push lock, locked/busy becomes UP `DB_BUSY retrying`, token moved to local env file.
- home_backup_kuma_push.sh: main backup and retention roles separated; rsync 24 warning/partial, 23/137 real failure; retention no longer duplicates backup failure; main and retention Kuma timers now run every 2min.
- disk_usage_monitor.sh: sends initial RUNNING heartbeat and uses bounded curl connect/max-time.
- rsync-transfer: disabled old pusher service because no live verified transfer was safe to monitor.
- os-observer: not analyzed or fixed; removed from live MegaVault indexes/docs per user instruction.

CURRENT_POSTFIX_STATE:
- cloud backup=UP `backup=idle last_snapshot=cbba8d42 monitor=ok timer=active`
- mint-home-backup=DOWN real `BACKUP_FAILURE ... rsync_exit=137`; intentionally not silenced and no longer `No heartbeat`
- amici_fb=UP
- disk-usage-monitor=UP
- parcel-tracker=UP
- mint-home-backup-retention=UP retention-only
- software audit mint=UP; temporary SQLite busy reports UP

TESTS:
- python3 -m py_compile mint_update_tracker.py
- bash -n cloud backup pusher, home backup pusher, disk usage monitor
- sudo /usr/local/bin/mint-cloud-backup-kuma-push --dry-run
- home_backup_kuma_push.sh --dry-run for main and retention roles
- disk_usage_monitor.sh live RUNNING and OK pushes
- mint_update_tracker.py push-kuma real HTTP 200
- systemctl user/system status for changed units/timers
- remote SQLite query against Kuma DB after restart

OPEN:
- mint-home-backup remains BROKEN_REAL until backup failure `rsync_exit=137` is investigated separately.
- Historical generated MegaVault migration/audit reports may still mention os-observer; live index and project docs no longer register it.
