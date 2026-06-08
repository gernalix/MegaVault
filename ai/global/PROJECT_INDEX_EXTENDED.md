# PROJECT_INDEX_EXTENDED
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=PROJECT_INDEX+PROJECT_INVENTORY+live_systemd+DATA_REGISTRY+ALERT_REGISTRY
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/PROJECT_INDEX_EXTENDED.md

RULES:
rule=PROJECT_INDEX.md remains canonical project list
rule=this_file_maps_cross_project_infra_relations_only
rule=UNKNOWN_when_runtime_relation_not_verified

RELATIONS:
project=android;repo=/home/daniele/codex-workspace/projects/android;service=adb-wifi-autoconnect.service;timer=none;db=none;dashboard=none;monitor=none;alert=none
project=amici-fb;repo=/home/daniele/codex-workspace/scripts/amici_fb;service=amici_fb.service;timer=amici_fb.timer;db=amici_fb.sqlite3;dashboard=none;monitor=amici_fb_id_5;alert=Telegram_snapshot
project=codex-html-live;repo=/home/daniele/codex-workspace/codex-html-live;service=codex-html-live.service;timer=none;db=none;dashboard=html_archive;monitor=none;alert=none
project=codex-token-watcher;repo=/home/daniele/codex-workspace/codex-token-watcher;service=codex-usage-monitor.service;timer=codex-usage-monitor.timer;db=codex_usage.sqlite3;dashboard=none;monitor=codex-token-watcher_id_10_disabled;alert=Telegram_optional
project=facebook-video-archiver;repo=/home/daniele/codex-workspace/facebook-video-archiver;service=facebook-video-archiver.service;timer=facebook-video-archiver.timer_disabled;db=none_verified;dashboard=facebook_archive_dashboard.py;monitor=none;alert=none
project=linux-mint-service-dashboard;repo=/home/daniele/codex-workspace/linux-mint-service-dashboard;service=system-service-dashboard.service;timer=none;db=none_verified;dashboard=http://127.0.0.1:8788;monitor=none;alert=none
project=mint-cloud-backup;repo=/home/daniele/codex-projects/mint-cloud-backup;service=mint-cloud-backup.service,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service;timer=mint-cloud-backup.timer,mint-cloud-backup-kuma-push.timer;db=none;dashboard=http://127.0.0.1:8765;monitor=cloud_backup_id_3;alert=Kuma
project=mint-freeze-forensics;repo=/home/daniele/codex-workspace/mint-freeze-forensics;service=mint-freeze-forensics.service,mint-resource-guardian.service;timer=mint-resource-guardian.timer;db=none;state=jsonl;dashboard=system-service-dashboard_freeze_tab;monitor=Freeze_Gaps_13,PSI_Memory_14,PSI_IO_15,Guardian_Alerts_16,Forensics_Alive_17;alert=Kuma
project=mint-manual-updates;repo=/home/daniele/codex-workspace/mint-manual-updates;service=mint-manual-updates.service;timer=mint-manual-updates.timer;db=android_updates_history.sqlite;dashboard=none;monitor=none;alert=none
project=mint-update-tracker;repo=/home/daniele/codex-workspace/mint-update-tracker;service=mint-update-tracker.service,mint-update-tracker-backfill.service;timer=mint-update-tracker.timer;db=software_audit.db;dashboard=system-service-dashboard;monitor=software_audit_mint_id_11;alert=Kuma
project=oracle-uptime-kuma;repo=/home/daniele/codex-workspace/projects/vm_oracle/oracle-uptime-kuma;service=uptime-kuma_container;timer=UNKNOWN;db=kuma.db;dashboard=http://150.230.148.128:3001;monitor=self;alert=Telegram_notification_id_1
project=parcel-tracker;repo=/home/daniele/codex-workspace/parcel-tracker;service=parcel-tracker.service;timer=parcel-tracker.timer;db=parcel_tracker.sqlite3;dashboard=none;monitor=parcel-tracker_id_7;alert=Kuma,Telegram_update
project=surface-recovery-hardening;repo=/home/daniele/codex-workspace/surface-recovery-hardening;service=transfer-usb-io-watchdog.service,transfer-vecchio-disco-adaptive-throttle.service,remote-recovery-tmux.service,surface-no-suspend.service,rsync-uptime-kuma-push.service_disabled;timer=none;db=source_cleanup_analyzer_SQLite_only;dashboard=transfer_vecchio_disco_dashboard.sh;monitor=rsync-transfer_id_2_disabled;alert=Telegram_watchdog
project=windowtabnotes;repo=/home/daniele/codex-workspace/WindowTabNotes;service=windowtabnotes.service;timer=none;db=windowtabnotes.sqlite3;dashboard=WindowTabNotes_UI;monitor=none;alert=none
project=backup_docs;repo=/home/daniele/backup_docs;service=home-incremental-backup.service,home-backup-kuma-push.service,home-backup-retention-kuma-push.service;timer=home-incremental-backup.timer,home-backup-kuma-push.timer,home-backup-retention-kuma-push.timer;db=none;dashboard=none;monitor=mint-home-backup_id_4,mint-home-backup-retention_id_9;alert=Kuma
project=terminal-logger;repo=UNKNOWN;service=terminal-logger-codex.service,terminal-logger-codex-snapshot.service,terminal-logger-maintenance.service;timer=terminal-logger-codex-snapshot.timer,terminal-logger-maintenance.timer;db=terminal_logger.sqlite;dashboard=none;monitor=none;alert=none
project=activitywatch;repo=UNKNOWN;service=aw-watcher-media-player.service;timer=none;db=peewee-sqlite.v2.db;dashboard=ActivityWatch;monitor=none;alert=none
project=disk-usage-monitor;repo=/home/daniele/disk_usage_monitor;service=disk-usage-monitor.service;timer=disk-usage-monitor.timer;db=UNKNOWN;dashboard=system-service-dashboard;monitor=disk-usage-monitor_id_6;alert=Kuma,Telegram

NO_RUNTIME_RELATION_VERIFIED:
project=supercontacts;runtime_relation=Android_app_only;service=none_verified;db=Room_SQLite_on_device;monitor=none_verified
project=multitimetracker;runtime_relation=Android_app_only;service=none_verified;db=SQLite_on_device;monitor=none_verified
project=soldi;runtime_relation=Android_app_only;service=none_verified;db=UNKNOWN;monitor=none_verified
project=megavault-project-exporter;runtime_relation=CLI_tool;service=none_verified;db=none_verified;monitor=none_verified
project=aw-converter;runtime_relation=UNKNOWN
project=chatgpt-chrome-debug;runtime_relation=chatgpt-chrome-live-logger.service
project=installa-app;runtime_relation=UNKNOWN
project=maintenance-486;runtime_relation=Oracle_report_workspace
project=oracle-backup-service;runtime_relation=Oracle_remote;live_state=UNKNOWN_ssh_timeout
project=owntracks-watcher;runtime_relation=owntracks-sqlite-watcher.service_disabled
project=remote-codex-phone;runtime_relation=UNKNOWN
project=remote-opt-oracle-backup;runtime_relation=Oracle_remote;live_state=UNKNOWN_ssh_timeout

OPEN:
open=remote_Oracle_project_services_not_live_verified_due_ssh_timeout
open=some_local_UNTRACKED_or_UNKNOWN_owners_terminal_logger_activitywatch_disk_usage_monitor
