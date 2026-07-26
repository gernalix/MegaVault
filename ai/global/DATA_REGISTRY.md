# DATA_REGISTRY
VERSION=11
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=Fedora_filesystem_checks_2026-07-26+MegaVault_timeline_SQLite+activity_593184+activity_846271+activity_583921+activity_684219+activity_826417+activity_731904
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
db=monitor.sqlite3;owner=fedora-system-monitor;path=/var/lib/fedora-system-monitor/monitor.sqlite3;schema=2;mode=WAL;owner_mode=root:daniele_0640;size_2026-07-26_audit=325328896;integrity=ok;foreign_keys=ok;indexes=ok;live_insert_before_after=PASS;raw_metrics_first=2026-07-10T09:13:01Z;events_first=2026-07-07T22:07:38Z;backup=/var/lib/fedora-system-monitor/backups;retention=complete_UTC_daily_aggregates;projection_14d=484835328;projection_60d=942552152;projection_180d=1075346602;projection_365d=1155609353;backup_365d_upper=39290718002;activity=593184+684219
tsdb=Prometheus;path=/var/lib/prometheus/metrics2;owner=prometheus:prometheus;retention=30d+5GB_first_limit;measured_growth_60s=96974B;projection_about_140MB_per_day+4.2GB_per_30d;raw_copy_to_diagnostics=forbidden;activity=826417
archive=fedora-diagnostics;default_output=user_selected;mode=0600;format=single_root_ZIP+CSV+JSON+SHA256;retention=manual_user_owned;activity=826417
db=incident_registry.sqlite;owner=MegaVault_global_incidents;path=/home/daniele/sync_root/db/incident_registry.sqlite;mode=WAL;owner_mode=daniele:daniele_0600;tables=incidents+incident_events;integrity=ok;bootstrap_activity=593184
db=activitywatch_peewee;owner=ActivityWatch;path=/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db;mode=SQLite;owner_mode=daniele:daniele_0644;tables=bucketmodel+eventmodel;integrity=ok;bucket_count_2026-07-14=3;event_count_2026-07-14=55;program_updates_preserve_data=yes;activity=284617+735804

EXPECTED_PROJECT_DBS_CHECKED:
status=missing_on_current_Fedora
paths=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3,/home/daniele/.local/share/terminal-logger/db/terminal_logger.sqlite,/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3,/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db,/home/daniele/sync_root/db/disk_usage_monitor.sqlite,/home/daniele/sync_root/db/git_change_ledger.sqlite3
meaning=not_migrated_or_not_installed;never_infer_data_loss_without_source_host_or_backup_evidence
exception=/var/lib/fedora-system-monitor/monitor.sqlite3_is_current+verified
windowtabnotes_2026_07_10=original_path_removed_after_backup;backup=/home/daniele/WindowTabNotes-backup-351806;size=132K;notes_total=19;notes_nonempty=0;config_included=yes

BACKUP_CURRENT:
repository=Restic;owner=fedora-t7-backup;path=/mnt/T7_BACKUP/restic-fedora;device=T7;encrypted=yes;repository_id=5872c043e0;snapshots=2;verified=historical_full_read_3955/3955_packs+current_light_198/198_packs_5percent+sample_restore_SHA256_PASS;latest_snapshot=3082eb92;activity=684219
manifest=/var/lib/t7-restic-backup/manifest;contains=RPM+Flatpak+storage+mount+boot+SELinux+systemd+Podman+Git_paths;secret_content=forbidden
monitor_db_consistency=online_SQLite_backup+integrity_check_before_each_Restic_snapshot;raw_live_DB_WAL_SHM_excluded
remote_repository=Restic;owner=oracle-backup-service;host=150.230.148.128;path=rclone:oci:bucket-20260206-0730/oraclevm;id=7fd0c92d9f;snapshots=8_at_2026-07-26;latest=186673bf;integrity=ok;restore_SHA256=PASS;rollback_archives=present;quota=4.53GiB_OK;activity=731904+731842
remote_incident_db=/home/ubuntu/sync_root/db/incident_registry.sqlite;host=150.230.148.128;owner=oracle-backup-service;integrity=live_tool_operational;activity=731904

RULES:
rule=do_not_modify_project_databases_for_docs_tasks
rule=read_SQLite_readonly_when_possible
rule=secrets+browser_profiles+cookies=sensitive
rule=verify_path+owner+schema+backup_before_registering_data_as_current
rule=Fedora_current_paths_only

OPEN:
open=project_database_migration_state_UNKNOWN
open=T7_Restic_password_external_escrow_pending_user
