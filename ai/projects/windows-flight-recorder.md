META:
name=Windows Flight Recorder
slug=windows-flight-recorder
path=C:\Users\seste\Documents\windows\system_logger
remote=none
branch=UNKNOWN
verified_commit=UNKNOWN
verified_at=2026-06-27T13:22:30Z
protocol=MEGAVAULT_PROTOCOL.md:VERSION=3
PURPOSE:
purpose=Windows 11 autonomous flight-recorder logger: system events+metrics -> SQLite, heartbeat -> Uptime Kuma, watchdog recovery, CLI inspection
STACK:
lang=Python 3
shell=PowerShell 7
db=SQLite stdlib
platform=Windows 11
deps=stdlib-only
MAP:
entry=logger.py,watchdog.py,systemlog.py
ui=CLI via systemlog.py/systemlog.ps1/systemlog.cmd
core=system_logger_core.py
db=system_events.sqlite
tests=test_system_logger.py,run_tests.ps1,systemlog doctor,systemlog audit,systemlog watch smoke,systemlog taillog smoke
scripts=install_tasks.ps1,start_logger.ps1,stop_logger.ps1,restart_logger.ps1,status_logger.ps1,backup_now.ps1,vacuum_database.ps1,export_csv.ps1,export_json.ps1,uninstall_logger.ps1
avoid=system_events.sqlite,*.sqlite-wal,*.sqlite-shm,logs,backup,exports,__pycache__,*.pid
ARCH:
logger=logger.py:long_running_collector
watchdog=watchdog.py:independent_liveness_recovery
core=system_logger_core.py:sqlite,collectors,heartbeat,task_status,export
cli=systemlog.py:user_commands_no_sql
FLOW:
event_flow=Windows APIs/EventLog/PowerShell collectors -> logger.py -> Database.insert_event -> events.payload_json
heartbeat_flow=logger.py -> send_heartbeat -> Uptime Kuma -> heartbeat table; failures -> logger_errors
recovery_flow=watchdog.py -> metadata logger.pid/logger.last_seen_utc -> start_detached_python(logger.py)
INV:
data=timestamps_utc_iso_z_only
data=payload_json_stable_json
db=WAL+synchronous_FULL+foreign_keys+busy_timeout
backup=sqlite_connection_backup_api_only
migration=schema_version monotonic; no destructive migrations
security=no secrets beyond user-provided Kuma push URL in config.json
perf=no external Python deps; low-frequency polling; EventLog checkpoint by RecordId
ops=uninstall preserves DB/logs/backups unless explicit delete flags
BUILD:
cmd=python -m py_compile logger.py watchdog.py system_logger_core.py systemlog.py test_system_logger.py
env=Windows 11 + Python 3 + PowerShell
requirements=no pip install
TEST:
smoke=pwsh -NoProfile -ExecutionPolicy Bypass -File .\run_tests.ps1
manual=manual_test_guide.md
audit=systemlog audit
doctor=systemlog doctor
DATA:
DB=C:\Users\seste\Documents\windows\system_logger\system_events.sqlite
Schema=events,heartbeat,logger_errors,metadata,schema_version
Backup=C:\Users\seste\Documents\windows\system_logger\backup
Export=C:\Users\seste\Documents\windows\system_logger\exports
Migration=schema_version
Retention=text_logs>=30d; DB historical append-only
Paths=config.json controls paths
DNB:
dnb=do_not_delete_db_logs_backups_config
dnb=do_not_break_timestamp_utc_z
dnb=do_not_block_logger_on_heartbeat_failure
dnb=watchdog_must_not_depend_on_logger_process
dnb=CLI must not require SQL from user
BUG:
issue=Task Scheduler creation denied in current non-elevated/policy-restricted session
cause=Access denied from Register-ScheduledTask and schtasks; exact policy/admin status to audit
workaround=Startup folder VBS fallback starts logger/watchdog at user logon
RISK:
risk=Security Event Log may require admin; session logon/lock events can be NOT_TESTABLE without privilege
risk=temperature/SMART availability depends on firmware/drivers
risk=Winget has no universal event source; coverage relies on MSI/AppX/EventLog signals
ROAD:
now=production-ready except Scheduled Tasks blocked by current permissions; Startup fallback active
next=run fix_task_scheduler_admin.ps1 from elevated PowerShell
later=optional service wrapper if task policy remains blocked
LINK:
meta=../../../windows/system_logger/dev/project.metadata.json
human=../../human/projects/windows-flight-recorder/overview.md
legacy=../../../windows/system_logger/REPORT.md
repo=../../../windows/system_logger
OPEN:
open=manual hardware/user-action tests pending; Task Scheduler admin verification pending
