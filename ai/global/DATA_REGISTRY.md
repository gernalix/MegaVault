# DATA_REGISTRY
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=filesystem_live_2026-06-08+sqlite_readonly_tables+project_ai_docs
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/DATA_REGISTRY.md

RULES:
rule=do_not_modify_databases_for_docs_tasks
rule=read_sqlite_readonly_when_possible
rule=secrets_and_browser_cookies_are_sensitive
unknown=remote_Oracle_DB_live_state_except_documented_paths

SQLITE_PROJECT_DBS:
db=software_audit.db;owner=mint-update-tracker;type=sqlite;path=/home/ubuntu/sync_root/db/software_audit.db;size=64323584;wal=yes;tables=current_inventory,events,file_state,health_checks,meta,runs,snapshot_diffs,software_snapshot_items,software_snapshots
db=codex_usage.sqlite3;owner=codex-token-watcher;type=sqlite;path=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3;tables=monitor_state,notification_events,observations
db=terminal_logger.sqlite;owner=terminal-logger;type=sqlite;path=/home/daniele/.local/share/terminal-logger/db/terminal_logger.sqlite;wal=yes;tables=commands,events,messages,pty_processes,sessions,snapshots
db=windowtabnotes.sqlite3;owner=windowtabnotes;type=sqlite;path=/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3;tables=app_profiles,browser_tabs,events,metadata,notes,window_contexts,workspaces
db=amici_fb.sqlite3;owner=amici-fb;type=sqlite;path=/home/daniele/codex-workspace/scripts/amici_fb/amici_fb.sqlite3;tables=diff_events,eccezioni,friend_requests,friends,snapshot_friends,snapshots
db=parcel_tracker.sqlite3;owner=parcel-tracker;type=sqlite;path=/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.sqlite3;tables=checks,state
db=peewee-sqlite.v2.db;owner=activitywatch;type=sqlite;path=/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db;tables=bucketmodel,eventmodel
db=android_updates_history.sqlite;owner=mint-extra-updater;type=sqlite;path=/home/daniele/.local/state/mint-extra-updater/android-sdk-history/android_updates_history.sqlite;tables=UNKNOWN
db=android_updates_history.sqlite;owner=mint-manual-updates;type=sqlite;path=/home/daniele/.local/state/mint-manual-updates/android-sdk-history/android_updates_history.sqlite;tables=UNKNOWN
db=kuma.db;owner=oracle-uptime-kuma;type=sqlite;path=/opt/uptime-kuma/data/kuma.db;host=ubuntu@150.230.148.128;tables=documented_monitor,monitor_notification,notification;live_read=UNKNOWN_ssh_timeout

NON_SQLITE_STATE:
state=mint-freeze-forensics;owner=mint-freeze-forensics;type=jsonl;path=/home/daniele/.local/state/mint-freeze-forensics;files=events.jsonl,history.jsonl,freeze-evidence
state=mint-cloud-backup;owner=mint-cloud-backup;type=json;path=/var/lib/mint-cloud-backup;files=health.json,progress.json,dashboard-status.json,uptime-kuma-push-state.json,last-backup-summary.json
state=home-backup;owner=backup_docs;type=rsync_snapshots;path=/media/daniele/Seagate6TB2/home-backups
state=transfer_dest;owner=surface-recovery-hardening;type=filesystem_copy;path=/media/daniele/Seagate6TB2/vecchio disco

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
project=oracle-uptime-kuma;db=kuma.db;service=uptime-kuma_container;dashboard=http://150.230.148.128:3001
project=mint-freeze-forensics;db=none;state=jsonl;service=mint-freeze-forensics.service;monitor=freeze_monitors_13_17
project=mint-cloud-backup;db=none;state=json;service=mint-cloud-backup-monitor.service;dashboard=http://127.0.0.1:8765;monitor=cloud_backup_id_3

OPEN:
open=remote_kuma_db_live_query_timeout_2026-06-08
open=Android_update_history_tables_not_read_in_this_prompt
