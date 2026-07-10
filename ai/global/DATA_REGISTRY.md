# DATA_REGISTRY
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=Fedora_filesystem_checks_2026-07-09+MegaVault_timeline_SQLite+activity_593184
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/DATA_REGISTRY.md

CURRENT_FEDORA:
host=fedora
home=/home/daniele
megavault=/home/daniele/MegaVault
project_data_migration=not_revalidated

SQLITE_CURRENT:
db=codex_global_timeline.sqlite;owner=MegaVault;path=/home/daniele/MegaVault/codex_global_timeline.sqlite;size=live_dynamic;canonical=yes;integrity=ok_task_714283_final_builder_gate
db=monitor.sqlite3;owner=fedora-system-monitor;path=/var/lib/fedora-system-monitor/monitor.sqlite3;schema=2;mode=WAL;owner_mode=root:daniele_0640;size_2026-07-10=4136960;integrity=ok;backup=/var/lib/fedora-system-monitor/backups;retention=aggregated;activity=593184
db=incident_registry.sqlite;owner=MegaVault_global_incidents;path=/home/daniele/sync_root/db/incident_registry.sqlite;mode=WAL;owner_mode=daniele:daniele_0600;tables=incidents+incident_events;integrity=ok;bootstrap_activity=593184

EXPECTED_PROJECT_DBS_CHECKED:
status=missing_on_current_Fedora
paths=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3,/home/daniele/.local/share/terminal-logger/db/terminal_logger.sqlite,/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3,/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db,/home/daniele/sync_root/db/disk_usage_monitor.sqlite,/home/daniele/sync_root/db/git_change_ledger.sqlite3
meaning=not_migrated_or_not_installed;never_infer_data_loss_without_source_host_or_backup_evidence
exception=/var/lib/fedora-system-monitor/monitor.sqlite3_is_current+verified
windowtabnotes_2026_07_10=original_path_removed_after_backup;backup=/home/daniele/WindowTabNotes-backup-351806;size=132K;notes_total=19;notes_nonempty=0;config_included=yes

RULES:
rule=do_not_modify_project_databases_for_docs_tasks
rule=read_SQLite_readonly_when_possible
rule=secrets+browser_profiles+cookies=sensitive
rule=verify_path+owner+schema+backup_before_registering_data_as_current
rule=Fedora_current_paths_only

OPEN:
open=project_database_migration_state_UNKNOWN
open=backup_status_for_MegaVault_timeline_DB_UNKNOWN

FILE_DATA_CURRENT:
dataset=Codex_session_logs;owner=codex-session-logger;path=/home/daniele/.local/state/codex-session-logger/sessions;layout=YYYY/MM/DD/session;permissions=0700_dirs+0600_files;retention=manual;canonical_raw=terminal.raw;live_text=transcript.log;live_screen=screen.txt;registered=task_714283
