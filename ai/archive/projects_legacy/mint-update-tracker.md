META:
name=mint-update-tracker
slug=mint-update-tracker
path=/home/daniele/codex-workspace/mint-update-tracker
remote=none
branch=master
verified_commit=35a34c53ae58520dc1bf0bc3874250a1f3385cc3
verified_at=2026-06-04T05:21:32+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Read-only software black-box recorder for Linux Mint desktop and Oracle Ubuntu Server; records installs, updates, downgrades, removals, snapshots and historical log backfill.
STACK:
lang=Python
fw=systemd
db=SQLite WAL
platform=Linux Mint desktop,Ubuntu Server headless
tools=apt,dpkg,snap,flatpak,pip,pipx,npm,AppImage,gem,cargo,systemctl,journalctl
MAP:
entry=mint_update_tracker.py
ui=none
core=mint_update_tracker.py
db=/home/ubuntu/sync_root/db/software_audit.db
tests=tests/test_mint_update_tracker.py
scripts=none
build=none
avoid=updates,package_changes,shared_sqlite_network_db,NFS,SMB,system_mutation
ARCH:
daemon=mint_update_tracker.py daemon=>scan+snapshot+heartbeat+native_sd_notify+independent_watchdog_thread+Kuma_push
events=logs/history=>events(event_hash UNIQUE)
snapshot=collect_inventory=>software_snapshots+software_snapshot_items+current_inventory+snapshot_diffs
backfill=apt/dpkg/mintupdate logs + snap changes + flatpak history; idempotent
verify=SQLite integrity+FK+schema+log coverage+systemd user/system watchdog+heartbeat
systemd_user=systemd/user/mint-update-tracker.service + mint-update-tracker.timer
systemd_system=Oracle /opt/software-audit; systemd/system/software-audit.service + software-audit-backfill.timer; User=ubuntu
integration=Mint user unit reads `SOFTWARE_AUDIT_KUMA_PUSH_URL` from `%h/.config/mint-update-tracker/kuma.env`; push health uses SQLite quick_check+counts; failures logged/nonfatal
integration_482917=SQLite busy timeout 30000ms, 8 retry attempts with backoff, Kuma push lock, DB locked/busy maps to UP `DB_BUSY retrying`; Kuma monitor interval=120 timeout=60 maxretries=2 tags=482917-reviewed,push-monitor
FLOW:
startup=ensure_initial_snapshot->parse_logs->optional_snapshot->heartbeat
first_run=full_inventory_required before future-only scan
periodic=daemon interval 300s, snapshot interval 3600s, recovery backfill timer 6h
watchdog=thread sends WATCHDOG independent of slow scan/snapshot; freeze stops thread=>systemd restart
export=export-csv reads events only
vacuum=quick_check->wal_checkpoint(TRUNCATE)->VACUUM->optimize
INV:
data=DB path fixed per-host `/home/ubuntu/sync_root/db/software_audit.db`
data=each machine has independent local SQLite file; host fields identify origin only
security=read-only commands only; no apt/snap/flatpak/pip/npm mutation
resilience=event dedupe by hash; file_state handles log rotation; backfill repeatable
resilience=flatpak history parser normalizes Unicode/variable whitespace timestamps; repair dedupes prior unstable hashes
cross_host=Mint user service; Oracle VM system service; no GUI/session required
version=event_hash includes host_id to keep exported data traceable; DB not shared
perf=low duty cycle; 300s scan; 3600s snapshot; optional managers skipped if absent; size lookup disabled unless SOFTWARE_AUDIT_RESOLVE_SIZES=1
deployment=Oracle live 2026-06-02 host=instance-20260201-1126 os=Ubuntu_22.04.5 path=/opt/software-audit db=/home/ubuntu/sync_root/db/software_audit.db
BUILD:
cmd=python3 -m py_compile mint_update_tracker.py tests/test_mint_update_tracker.py
requirements=python3,sqlite3,systemd; optional managers auto-detected
TEST:
unit=python3 -m unittest -v tests/test_mint_update_tracker.py
coverage=parser_log,snapshot,dedupe,backfill,restart/watchdog-heartbeat,SQLite,recovery,idempotence,headless_optional_absent
oracle=remote unittest OK; backfill OK; verify OK; restart OK; service active/running; timer active/waiting
DATA:
DB=/home/ubuntu/sync_root/db/software_audit.db
Schema=events,runs,file_state,software_snapshots,software_snapshot_items,current_inventory,snapshot_diffs,health_checks,meta
Backup=external only; app does not copy DB by default
Restore=rerun backfill+snapshot when logs/sources still available
Import=historical logs idempotent
Export=export-csv
Migration=additive ALTER TABLE for v1 events
Retention=none yet; years-long append-only event log
Paths=logs/,exports/,state/heartbeat.json,state/kuma_push.json
KumaEnv=/home/daniele/.config/mint-update-tracker/kuma.env mode 0600 local-only; do not commit token
MintCounts_2026-06-04=events=6441,snapshots=9,current_inventory=2344,integrity=ok,range=2026-01-08T19:19:30Z..2026-06-04T03:11:40Z
MintBackfill_2026-06-04=manual_recovery inserted=5 before repair; flatpak duplicate repair deleted=38; final consecutive backfills inserted=0 skipped=4078
MintKuma_2026-06-04=push HTTP200 msg=`OK events=6441 inventory=2344` ping=385ms
OracleCounts=events=4378,snapshots=1,current_inventory=1282,inventory=dpkg:1166+npm_global:1+pip:97+snap:18,integrity=ok
DNB:
dnb=never apply updates or remove packages
dnb=never create shared SQLite/network writer model
dnb=do not move DB outside /home/ubuntu/sync_root/db/software_audit.db
dnb=optional managers missing is warning, not failure
dnb=Oracle mode must work headless via system unit
dnb=do not copy Mint Kuma push URL into Oracle system units
dnb=do not commit Kuma push URLs; user unit must reference the local env file
BUG:
issue=Mint 2026-06-04 service appeared unhealthy
cause=old notify path used systemd-notify subprocess; watchdog notifications could be rejected/non-independent during long inventory cycle
fix=native sd_notify + independent watchdog thread + restart proof
issue=Mint 2026-06-04 backfill inserted repeated flatpak events
cause=flatpak history Unicode/variable whitespace timestamp parsed as utc_now
fix=stable flatpak timestamp parser + DB repair/dedupe; final backfills inserted=0
issue=#482917 false Kuma down DB_ERROR OperationalError
cause=concurrent daemon scan and manual/timer push could see temporary SQLite busy/locked and report DOWN
fix=busy_timeout 30000ms, longer retry/backoff, push lock, locked/busy downgraded to UP `DB_BUSY retrying`, user unit moved Kuma URL to local env file
RISK:
risk=log permissions may hide system logs on restricted users; verify reports unscanned coverage
risk=flatpak/snap history format may vary; parsers are conservative
risk=Oracle system unit assumes stable path `/opt/software-audit`; if moved, update unit before restart
risk=events already rotated/deleted from apt/dpkg/mintupdate/snap/flatpak history cannot be reconstructed
ROAD:
now=Mint user service recovered with Kuma push; Oracle system service deployed with separate local DBs; #482917 Kuma DB_BUSY false down fixed
next=monitor scheduled Mint/Oracle backfills and Kuma freshness
later=separate export/import aggregation if user requests it
LINK:
meta=../../../mint-update-tracker/dev/project.metadata.json
human=../../human/projects/mint-update-tracker/overview.md
legacy=../../../mint-update-tracker/dev/ai,../../../mint-update-tracker/dev/human
repo=../../../mint-update-tracker
OPEN:
open=none
