# DATA_REGISTRY
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=Fedora_filesystem_checks_2026-07-09+MegaVault_timeline_SQLite
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/DATA_REGISTRY.md

CURRENT_FEDORA:
host=fedora
home=/home/daniele
megavault=/home/daniele/MegaVault
project_data_migration=not_revalidated

SQLITE_CURRENT:
db=codex_global_timeline.sqlite;owner=MegaVault;path=/home/daniele/MegaVault/codex_global_timeline.sqlite;size=1671168;canonical=yes;integrity=pending_final_builder_gate

EXPECTED_PROJECT_DBS_CHECKED:
status=missing_on_current_Fedora
paths=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3,/home/daniele/.local/share/terminal-logger/db/terminal_logger.sqlite,/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3,/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db,/home/daniele/sync_root/db/disk_usage_monitor.sqlite,/home/daniele/sync_root/db/git_change_ledger.sqlite3
meaning=not_migrated_or_not_installed;never_infer_data_loss_without_source_host_or_backup_evidence

RULES:
rule=do_not_modify_project_databases_for_docs_tasks
rule=read_SQLite_readonly_when_possible
rule=secrets+browser_profiles+cookies=sensitive
rule=verify_path+owner+schema+backup_before_registering_data_as_current
rule=Fedora_current_paths_only

OPEN:
open=project_database_migration_state_UNKNOWN
open=backup_status_for_MegaVault_timeline_DB_UNKNOWN
