META:
name=mint-update-tracker
slug=mint-update-tracker
path=/home/daniele/codex-workspace/mint-update-tracker
remote=none
branch=master
verified_commit=UNKNOWN
verified_at=2026-06-02T00:00:00+02:00
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
daemon=mint_update_tracker.py daemon=>scan+snapshot+heartbeat+systemd_notify
events=logs/history=>events(event_hash UNIQUE)
snapshot=collect_inventory=>software_snapshots+software_snapshot_items+current_inventory+snapshot_diffs
backfill=apt/dpkg/mintupdate logs + snap changes + flatpak history; idempotent
verify=SQLite integrity+FK+schema+log coverage+systemd user/system watchdog+heartbeat
systemd_user=systemd/user/mint-update-tracker.service + mint-update-tracker.timer
systemd_system=systemd/system/software-audit.service + software-audit-backfill.timer
FLOW:
startup=ensure_initial_snapshot->parse_logs->optional_snapshot->heartbeat
first_run=full_inventory_required before future-only scan
periodic=daemon interval 300s, snapshot interval 3600s, recovery backfill timer 6h
export=export-csv reads events only
vacuum=quick_check->wal_checkpoint(TRUNCATE)->VACUUM->optimize
INV:
data=DB path fixed per-host `/home/ubuntu/sync_root/db/software_audit.db`
data=each machine has independent local SQLite file; host fields identify origin only
security=read-only commands only; no apt/snap/flatpak/pip/npm mutation
resilience=event dedupe by hash; file_state handles log rotation; backfill repeatable
cross_host=Mint user service; Oracle VM system service; no GUI/session required
version=event_hash includes host_id to keep exported data traceable; DB not shared
perf=low duty cycle; 300s scan; 3600s snapshot; optional managers skipped if absent
BUILD:
cmd=python3 -m py_compile mint_update_tracker.py tests/test_mint_update_tracker.py
requirements=python3,sqlite3,systemd; optional managers auto-detected
TEST:
unit=python3 -m unittest -v tests/test_mint_update_tracker.py
coverage=parser_log,snapshot,dedupe,backfill,restart/watchdog-heartbeat,SQLite,recovery,idempotence,headless_optional_absent
DATA:
DB=/home/ubuntu/sync_root/db/software_audit.db
Schema=events,runs,file_state,software_snapshots,software_snapshot_items,current_inventory,snapshot_diffs,health_checks,meta
Backup=external only; app does not copy DB by default
Restore=rerun backfill+snapshot when logs/sources still available
Import=historical logs idempotent
Export=export-csv
Migration=additive ALTER TABLE for v1 events
Retention=none yet; years-long append-only event log
Paths=logs/,exports/,state/heartbeat.json
DNB:
dnb=never apply updates or remove packages
dnb=never create shared SQLite/network writer model
dnb=do not move DB outside /home/ubuntu/sync_root/db/software_audit.db
dnb=optional managers missing is warning, not failure
dnb=Oracle mode must work headless via system unit
BUG:
issue=systemd install not auto-applied by code; operator copies chosen user/system units
RISK:
risk=log permissions may hide system logs on restricted users; verify reports unscanned coverage
risk=flatpak/snap history format may vary; parsers are conservative
risk=Oracle clone path may differ from Mint path; system unit ExecStart must match deployed project path
ROAD:
now=install local Mint user service and verify DB/live heartbeat
next=deploy same project to Oracle with system unit and local DB
later=separate export/import aggregation if user requests it
LINK:
meta=../../../mint-update-tracker/dev/project.metadata.json
human=../../human/projects/mint-update-tracker/overview.md
legacy=../../../mint-update-tracker/dev/ai,../../../mint-update-tracker/dev/human
repo=../../../mint-update-tracker
OPEN:
open=Oracle VM live deployment not executed in this Mint-local run
