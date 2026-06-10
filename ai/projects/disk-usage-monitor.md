META:
name=disk-usage-monitor
slug=disk-usage-monitor
path=/home/daniele/disk_usage_monitor
repo=/home/daniele/disk_usage_monitor
branch=master
updated=2026-06-11 prompt_492817
protocol=MEGAVAULT_PROTOCOL.md:v8

PURPOSE:
purpose=Linux Mint disk usage sampler with SQLite history, delta Telegram alerts, and Oracle Uptime Kuma push heartbeat.
truth=local SQLite/log decide disk alert semantics; Kuma is heartbeat/state-change alerting only.

STACK:
lang=Bash,Python_inline,SQLite
systemd=system service+timer
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
run=timer_5min->oneshot_service->disk_usage_monitor.sh->lsblk/findmnt/kernel_journal->SQLite->Telegram_delta_if_needed->Kuma_RUNNING_OK
db_tables=disk_space_samples,disk_events,disk_alerts,run_status,kuma_pushes,notification_state
identity=uuid > serial+partition > label+model+size
kuma_semantics=UP means recent heartbeat received; it does not mean Telegram is sent for every OK heartbeat.
telegram_semantics=delta alert >=500MiB with 6h cooldown per disk/direction; OK digest daily only on no-delta runs.

FLOW:
success=send_kuma up/RUNNING at start; persist samples/events/alerts; send Telegram delta if threshold+cooldown; send optional OK digest if no alert; send_kuma up/OK
failure=log run.error; send_kuma down/ERROR; systemd service exits nonzero
prompt_492817=real cause was no Kuma state change plus script default Telegram threshold 2GiB suppressing 1.1-1.6GiB deltas; fixed in v5 to threshold 500MiB and daily no-delta OK digest.

INV:
ops=do not treat Kuma green as Telegram delivery proof.
security=never print or commit .env push URL or Telegram secrets.
storage=read-only monitoring; no rsync/backup/mount stop.
noise=do not notify every heartbeat; use state changes, delta cooldown, or daily digest.
version=every touched project file increments vN.

TEST:
syntax=bash -n /home/daniele/disk_usage_monitor/disk_usage_monitor.sh
systemd=sudo systemctl start disk-usage-monitor.service; systemctl status disk-usage-monitor.service disk-usage-monitor.timer --no-pager
local_db=sqlite3 readonly run_status,kuma_pushes,disk_alerts
kuma=remote readonly monitor id 6 latest heartbeat status=1 msg=OK; duplicate_named_monitors=1
telegram=2026-06-11 log shows telegram.sent title=Disk usage delta after v5 run

DATA:
DB=/home/daniele/sync_root/db/disk_usage_monitor.sqlite
Backup=cp -a DB DB.$(date -u +%Y%m%dT%H%M%SZ).bak before destructive DB work
Retention=UNKNOWN

DNB:
dnb=do not lower Kuma interval below timer cadence.
dnb=do not enable DELTA_KUMA_EVENT_PUSH unless event-level Kuma noise is wanted.
dnb=do not rely on systemctl oneshot inactive/dead as failure; require exit status and DB/log/Kuma heartbeat.

RISK:
risk=large active backup/transfer can create repeated deltas; mitigation=Telegram cooldown and no per-heartbeat notifications.
risk=Kuma only notifies state changes; mitigation=local Telegram delta and daily no-delta digest.

ROAD:
now=v5 live; Telegram delta and Kuma heartbeat verified for prompt_492817.
next=observe whether Seagate6TB2 deltas are expected backup activity or need separate backup diagnosis.

LINK:
oracle_kuma=oracle-uptime-kuma.md
alert_registry=../global/ALERT_REGISTRY.md
service_registry=../global/SERVICE_REGISTRY.md
