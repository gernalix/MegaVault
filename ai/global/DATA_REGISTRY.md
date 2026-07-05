# DATA_REGISTRY
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=filesystem_live_2026-06-08+sqlite_readonly_tables+project_ai_docs+kuma_sqlite_readonly_2026-06-10+git_change_ledger_2026-06-10
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/DATA_REGISTRY.md

RULES:
rule=do_not_modify_databases_for_docs_tasks
rule=read_sqlite_readonly_when_possible
rule=secrets_and_browser_cookies_are_sensitive
unknown=backup_status_for_non_Kuma_local_SQLite_DBs

SQLITE_PROJECT_DBS:
db=software_audit.db;owner=mint-update-tracker;type=sqlite;path=/home/ubuntu/sync_root/db/software_audit.db;size=64323584;wal=yes;tables=current_inventory,events,file_state,health_checks,meta,runs,snapshot_diffs,software_snapshot_items,software_snapshots
db=codex_usage.sqlite3;owner=codex-token-watcher;type=sqlite;path=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3;tables=monitor_state,notification_events,observations
db=terminal_logger.sqlite;owner=terminal-logger;type=sqlite;path=/home/daniele/.local/share/terminal-logger/db/terminal_logger.sqlite;wal=yes;tables=commands,events,messages,pty_processes,sessions,snapshots
db=windowtabnotes.sqlite3;owner=windowtabnotes;type=sqlite;path=/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3;tables=app_profiles,browser_tabs,events,metadata,notes,window_contexts,workspaces
db=amici_fb.sqlite3;owner=amici-fb;type=sqlite;path=/home/daniele/codex-workspace/scripts/amici_fb/amici_fb.sqlite3;tables=diff_events,eccezioni,friend_requests,friends,snapshot_friends,snapshots
db=parcel_tracker.sqlite3;owner=parcel-tracker;type=sqlite;path=/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.sqlite3;tables=checks,state
db=peewee-sqlite.v2.db;owner=activitywatch;type=sqlite;path=/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db;tables=bucketmodel,eventmodel
db=disk_usage_monitor.sqlite;owner=disk-usage-monitor;type=sqlite;path=/home/daniele/sync_root/db/disk_usage_monitor.sqlite;tables=disk_space_samples,disk_events,disk_alerts,run_status,kuma_pushes,notification_state,monitored_disk_state,delta_notification_state
db=git_change_ledger.sqlite3;owner=git-change-ledger;type=sqlite;path=/home/daniele/sync_root/db/git_change_ledger.sqlite3;size=151552;wal=yes;tables=changed_files,recent_commits,repo_scans,repos,scan_runs,schema_meta
db=grindr_export.sqlite3;owner=grindr-web-exporter;type=sqlite;path=/home/ubuntu/sync_root/db/grindr_export.sqlite3;wal=yes;tables=chats,debug_artifacts,dom_snapshots,export_runs,media,messages,profiles,progress_checkpoints,schema_meta
db=android_updates_history.sqlite;owner=mint-extra-updater;type=sqlite;path=/home/daniele/.local/state/mint-extra-updater/android-sdk-history/android_updates_history.sqlite;tables=android_update_history
db=android_updates_history.sqlite;owner=mint-manual-updates;type=sqlite;path=/home/daniele/.local/state/mint-manual-updates/android-sdk-history/android_updates_history.sqlite;tables=android_update_history
db=kuma.db;owner=oracle-uptime-kuma;type=sqlite;path=/opt/uptime-kuma/data/kuma.db;host=ubuntu@150.230.148.128;size=8806400;wal=yes;wal_path=/opt/uptime-kuma/data/kuma.db-wal;shm_path=/opt/uptime-kuma/data/kuma.db-shm;integrity=ok_2026-06-10;tables=api_key,docker_host,domain_expiry,heartbeat,maintenance,monitor,monitor_group,monitor_notification,monitor_tag,notification,setting,status_page,tag,user,stat_daily,stat_hourly,stat_minutely;live_read=verified_2026-06-10

NON_SQLITE_STATE:
state=mint-freeze-forensics;owner=mint-freeze-forensics;type=jsonl;path=/home/daniele/.local/state/mint-freeze-forensics;files=events.jsonl,history.jsonl,freeze-evidence
state=mint-cloud-backup;owner=mint-cloud-backup;type=json;path=/var/lib/mint-cloud-backup;files=health.json,progress.json,dashboard-status.json,uptime-kuma-push-state.json,last-backup-summary.json
state=home-backup;owner=backup_docs;type=rsync_snapshots;path=/media/daniele/Seagate6TB2/home-backups
state=oracle-vm-offloads;owner=oracle-backup-service;type=sqlite_snapshots+manifests;path=/media/daniele/Seagate6TB2/oracle-vm-offloads;backup_via=home-backup external/oracle-vm-offloads
state=transfer_dest;owner=surface-recovery-hardening;type=filesystem_copy;path=/media/daniele/Seagate6TB2/vecchio disco

DATA_CLASSIFICATION:
data=software_audit.db;owner_project=mint-update-tracker;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=no;restore_source=UNKNOWN
data=codex_usage.sqlite3;owner_project=codex-token-watcher;backup=UNKNOWN;rebuildable=partial;loss_impact=low;contains_secrets=no;restore_source=Codex_session_cache_partial
data=terminal_logger.sqlite;owner_project=terminal-logger;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=UNKNOWN_visible_terminal_output_possible;restore_source=terminal_logs_partial
data=windowtabnotes.sqlite3;owner_project=windowtabnotes;backup=UNKNOWN;rebuildable=no;loss_impact=high;contains_secrets=UNKNOWN_user_notes;restore_source=backup_UNKNOWN
data=amici_fb.sqlite3;owner_project=amici-fb;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=no;restore_source=Facebook_rescan_partial
data=parcel_tracker.sqlite3;owner_project=parcel-tracker;backup=UNKNOWN;rebuildable=partial;loss_impact=low;contains_secrets=no;restore_source=carrier_status_rescan_partial
data=peewee-sqlite.v2.db;owner_project=activitywatch;backup=UNKNOWN;rebuildable=no;loss_impact=medium;contains_secrets=UNKNOWN_activity_history;restore_source=none_verified
data=disk_usage_monitor.sqlite;owner_project=disk-usage-monitor;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=no;restore_source=future_disk_samples_only
data=git_change_ledger.sqlite3;owner_project=git-change-ledger;backup=UNKNOWN;rebuildable=yes;loss_impact=low;contains_secrets=no_file_contents_but_paths_may_be_sensitive;restore_source=rerun_git_change_ledger_scan
data=grindr_export.sqlite3;owner_project=grindr-web-exporter;backup=UNKNOWN;rebuildable=partial;loss_impact=high;contains_secrets=yes_messages_profiles_media_metadata;restore_source=Grindr_Web_rescan_partial_if_session_visible
data=android_updates_history.sqlite;owner_project=mint-extra-updater;backup=UNKNOWN;rebuildable=partial;loss_impact=low;contains_secrets=no;restore_source=legacy_update_logs_partial
data=android_updates_history.sqlite;owner_project=mint-manual-updates;backup=UNKNOWN;rebuildable=partial;loss_impact=low;contains_secrets=no;restore_source=legacy_update_logs_partial
data=kuma.db;owner_project=oracle-uptime-kuma;backup=yes;rebuildable=partial;loss_impact=high;contains_secrets=UNKNOWN_push_tokens_possible;restore_source=/opt/uptime-kuma/backups
data=mint-freeze-forensics_state;owner_project=mint-freeze-forensics;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=no;restore_source=future_samples_only
data=mint-cloud-backup_state;owner_project=mint-cloud-backup;backup=UNKNOWN;rebuildable=partial;loss_impact=medium;contains_secrets=no;restore_source=restic_status_readonly_partial
data=home-backup_snapshots;owner_project=backup_docs;backup=yes;rebuildable=no;loss_impact=high;contains_secrets=UNKNOWN_home_data;restore_source=none_verified
data=oracle-vm-offloads;owner_project=oracle-backup-service;backup=yes_next_home_backup;rebuildable=partial;loss_impact=high;contains_secrets=UNKNOWN_oracle_snapshots_manifests;restore_source=/media/daniele/Seagate6TB2/home-backups/snapshots/*/external/oracle-vm-offloads
data=transfer_dest;owner_project=surface-recovery-hardening;backup=UNKNOWN;rebuildable=partial;loss_impact=high;contains_secrets=UNKNOWN_user_files;restore_source=/dev/sdb2_BitLocker_source_if_available

BROWSER_TOOL_DBS:
db=Firefox_profile_SQLite;owner=Firefox;type=browser_profile;path=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release;status=sensitive_not_project_truth
db=Chrome_profile_DBs;owner=Google_Chrome;type=browser_profile;path=/home/daniele/.config/google-chrome;status=sensitive_not_project_truth
db=AndroidStudio_internal_state;owner=Android_Studio;type=tool_state;path=/home/daniele/.config/Google/AndroidStudio*/app-internal-state.db;status=tool_internal
db=Insync_settings_logs;owner=Insync;type=tool_state;path=/home/daniele/.config/Insync;status=tool_internal

PROJECT_RELATIONS:
project=mint-update-tracker;db=software_audit.db;service=mint-update-tracker.service;monitor=software_audit_mint
project=codex-token-watcher;db=codex_usage.sqlite3;service=codex-usage-monitor.service;monitor=codex-token-watcher_disabled_obsolete
project=windowtabnotes;db=windowtabnotes.sqlite3;service=windowtabnotes.service;dashboard=windowtabnotes_local
project=amici-fb;db=amici_fb.sqlite3;service=amici_fb.service;timer=amici_fb.timer;monitor=amici_fb
project=parcel-tracker;db=parcel_tracker.sqlite3;service=parcel-tracker.service;timer=parcel-tracker.timer;monitor=parcel-tracker
project=disk-usage-monitor;db=disk_usage_monitor.sqlite;service=disk-usage-monitor.service;timer=disk-usage-monitor.timer;monitor=disk-usage-monitor
project=git-change-ledger;db=git_change_ledger.sqlite3;service=none_enabled;timer=template_only_disabled;monitor=none
project=grindr-web-exporter;db=grindr_export.sqlite3;service=none;timer=none;monitor=none
project=oracle-uptime-kuma;db=kuma.db;service=uptime-kuma_container;admin=ssh_tunnel http://127.0.0.1:3001 -> VM 127.0.0.1:3002;public_push_proxy=http://150.230.148.128:3001/api/push/<token>;dashboard_public=403
project=mint-freeze-forensics;db=none;state=jsonl;service=mint-freeze-forensics.service;monitor=freeze_monitors_13_17
project=mint-cloud-backup;db=none;state=json;service=mint-cloud-backup-monitor.service;dashboard=http://127.0.0.1:8765;monitor=cloud_backup_id_3

OPEN:
open=Android_update_history_tables_not_read_in_this_prompt
open=backup_status_for_local_SQLite_DBs_not_verified_in_this_prompt
