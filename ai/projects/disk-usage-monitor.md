META:
name=disk-usage-monitor
slug=disk-usage-monitor
path=/home/daniele/disk_usage_monitor
repo=/home/daniele/disk_usage_monitor
branch=master
updated=2026-06-13 prompt_729184
protocol=MEGAVAULT_PROTOCOL.md:v8

PURPOSE:
purpose=Linux Mint canonical 3-disk monitor with SQLite state, clean Telegram alerts, and Oracle Uptime Kuma push heartbeat.
truth=local SQLite/log decide disk alert semantics; Kuma is heartbeat/state-change alerting only.

STACK:
lang=Bash,Python_inline,SQLite
systemd=system oneshot service+timer;timer_is_24x7_component;service_inactive_dead_between_runs_is_normal
kuma=Oracle_VM_Uptime_Kuma monitor_id=6 name=disk-usage-monitor type=push active=1 interval=420 timeout=60 retry=300 maxretries=2 notification=Telegram_id_1
telegram=helper /home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py plus /home/daniele/.config/environment.d/telegram.conf

MAP:
script=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh
dashboard=/home/daniele/disk_usage_monitor/disk_usage_dashboard.sh
env=/home/daniele/disk_usage_monitor/.env secrets_no_commit
db=/home/daniele/sync_root/db/disk_usage_monitor.sqlite
service=/etc/systemd/system/disk-usage-monitor.service
timer=/etc/systemd/system/disk-usage-monitor.timer
docs=/home/daniele/disk_usage_monitor/README.md,/home/daniele/disk_usage_monitor/docs
avoid=printing_Kuma_push_URL,Telegram_token,Telegram_chat_id,destructive_disk_ops,stopping_backup_or_rsync

ARCH:
run=timer_5min->oneshot_service->disk_usage_monitor.sh->lsblk/findmnt_R/kernel_journal->canonical_3_disk_match->SQLite->Telegram_change_or_low_space->Kuma_RUNNING_OK_compact
systemd_resilience=timer enabled;OnBootSec=2min;OnUnitActiveSec=5min;Persistent=true;AccuracySec=30s;service Restart=on-failure;RestartSec=30s;TimeoutStartSec=3min;StartLimitIntervalSec=0;After=local-fs.target+network-online.target
inventory_cmd=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh inventory
dry_run_cmd=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh dry-run
status_cmd=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh status
notify_test_cmd=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh notify-test
db_tables=disk_space_samples,disk_events,disk_alerts,run_status,kuma_pushes,notification_state,monitored_disk_state,delta_notification_state
identity=canonical_slug backed_by_uuid_serial_model_mapper
monitored_2026-06-11=T7_sistema root / /dev/sda2 serial=S6YGNS0Y903440H uuid=a4bf0d13-b036-490e-9a14-aea83baf37a6;Seagate_4TB mapper=/dev/mapper/source_bitlocker serial=WFF0FEX8 uuid=22E02106E020E1B1;Seagate_6TB /dev/sdc1 serial=ZCT3KG54 uuid=75e5363d-6736-4a7e-84be-5242f4735a27
excluded=virtual_fs,autofs_wrapper,/boot/efi,Windows_Local_Disk,Veracrypt,random_mounts,non_whitelisted_disks
kuma_semantics=UP means recent heartbeat received; it does not mean Telegram is sent for every OK heartbeat.
telegram_semantics=clean_3_line_message; notify on connection_change or low_space_threshold; daily OK digest optional; delta notification on >=1GiB used change since delta_notification_state; no mountpoints/devices/used_GB in normal Telegram.

FLOW:
success=send_kuma up/RUNNING at start; persist canonical samples/state/events/delta baselines; send Telegram only if delta>=1GiB, connection/low_space, or digest; update delta_notification_state only after successful delta Telegram; send_kuma up/"OK T7=N% free SG4=N% free SG6=N% free"
failure=log run.error; send_kuma down/ERROR; systemd service exits nonzero
prompt_492817=real cause was no Kuma state change plus script default Telegram threshold 2GiB suppressing 1.1-1.6GiB deltas; fixed in v5 to threshold 500MiB and daily no-delta OK digest.
prompt_748263=script already sampled multiple disks in DB but UI/Kuma/alerts made it look Seagate-only; fixed in v6 with explicit inventory, findmnt -R, checked-count heartbeat, current-run dashboard, /boot/efi exclusion, and fuller Telegram delta text.
prompt_836204=v7 restricts monitoring/Telegram to exactly T7 sistema, Seagate 4TB, Seagate 6TB; clean Telegram body and compact Kuma heartbeat; dashboard separates canonical summary from technical/excluded mounts.
prompt_384729=real state was active timer+successful oneshot; apparent not-active cause was interpreting service inactive/dead as failure; v8 adds status/dry-run/logged disk_state and stronger systemd retry/boot semantics.
prompt_729184=v9 adds delta_notification_state and aggregated Telegram `Disk delta detected` when any connected canonical disk changes used_bytes by >=1073741824 bytes since saved delta reference; delta-test-plus/minus simulate without writes.

INV:
ops=do not treat Kuma green as Telegram delivery proof.
security=never print or commit .env push URL or Telegram secrets.
storage=read-only monitoring; no rsync/backup/mount stop.
noise=do not notify every heartbeat; use state changes, delta cooldown, or daily digest.
version=every touched project file increments vN.

TEST:
syntax=bash -n /home/daniele/disk_usage_monitor/disk_usage_monitor.sh
dashboard_syntax=bash -n /home/daniele/disk_usage_monitor/disk_usage_dashboard.sh
inventory=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh inventory shows only T7 sistema, Seagate 4TB, Seagate 6TB in MONITORED; virtual/autofs/boot_efi excluded
status=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh status shows systemd timer/service plus DB run_status, monitored_disk_state, recent Kuma pushes
dry_run=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh dry-run reads live mount state without DB/Telegram/Kuma writes
delta_test=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh delta-test-plus and delta-test-minus simulate +/-1.1GiB message without DB/Telegram/Kuma writes
systemd=sudo systemctl start disk-usage-monitor.service; systemctl status disk-usage-monitor.service disk-usage-monitor.timer --no-pager
local_db=2026-06-11 run_status version=v7 sample_count=3 alert_count=0 event_count=0; monitored_disk_state rows=3
kuma=remote readonly monitor id 6 latest heartbeat status=1 msg="OK T7=84% free SG4=8% free SG6=53% free"; duplicate_named_monitors=1; notification_id=1
telegram=2026-06-11 log shows telegram.sent title=Disk usage delta after v5 run
telegram_748263=2026-06-11 OK digest sent once, next run suppressed by 86400s cooldown; delta cooldown preserved
telegram_836204=2026-06-11 notify-test sent clean body: Disk monitor + exactly T7 sistema/Seagate 4TB/Seagate 6TB lines.

DATA:
DB=/home/daniele/sync_root/db/disk_usage_monitor.sqlite
DeltaState=delta_notification_state stores per-slug used_bytes/used_gib/used_percent/free_percent; first v9 run seeds baseline notified=0; successful delta Telegram updates changed disks to notified=1.
Backup=cp -a DB DB.$(date -u +%Y%m%dT%H%M%SZ).bak before destructive DB work
Retention=UNKNOWN

DNB:
dnb=do not lower Kuma interval below timer cadence.
dnb=do not enable DELTA_KUMA_EVENT_PUSH unless event-level Kuma noise is wanted.
dnb=do not rely on systemctl oneshot inactive/dead as failure; require exit status and DB/log/Kuma heartbeat.
dnb=do not compare delta alerts to previous tick; compare to delta_notification_state used_bytes and skip missing disks.

RISK:
risk=Seagate 4TB is below default low-space threshold; mitigation=per-disk low_space cooldown and no per-heartbeat notifications.
risk=Kuma only notifies state changes; mitigation=local Telegram delta and daily no-delta digest.

ROAD:
now=v9 live; canonical 3-disk whitelist, clean Telegram, compact Kuma heartbeat, status/dry-run, resilient timer+oneshot, and 1GiB delta notification baseline verified for prompt_729184.
next=observe Seagate 4TB low-space notifications; adjust threshold only if user requests.

LINK:
oracle_kuma=oracle-uptime-kuma.md
alert_registry=../global/ALERT_REGISTRY.md
service_registry=../global/SERVICE_REGISTRY.md
