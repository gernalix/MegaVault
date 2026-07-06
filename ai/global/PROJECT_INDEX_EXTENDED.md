# PROJECT_INDEX_EXTENDED
VERSION=1
STATUS=ACTIVE_REFERENCE
MODE=codex_first
FORMAT=ultracompressed
DOC_CLASS=index
LIFECYCLE=REFERENCE
AUTHORITY_LEVEL=L2
SOURCE_OF_TRUTH=no
ROLE=extended_cross_project_relation_reference
CANONICAL_NAVIGATION=../PROJECT_INDEX.md
SOURCE=PROJECT_INDEX+../archive/inventory/PROJECT_INVENTORY.md+live_systemd+DATA_REGISTRY+ALERT_REGISTRY
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/PROJECT_INDEX_EXTENDED.md

CURRENT_HOST_NOTE:
primary_host=Windows_11_Pro Lenovo_ThinkPad_P14s_Gen_5_AMD
windows_root=C:\Users\seste\Documents
rule=project_rows_may_describe_legacy_Linux_Mint_or_remote_VM_runtime;do_not_read_as_current_host_profile
project_path_refresh=TODO_per_project_from_metadata_when_project_is_touched

RULES:
rule=PROJECT_INDEX.md remains canonical project list
rule=this_file_maps_cross_project_infra_relations_only
rule=this_file_must_not_override_PROJECT_INDEX_or_project_repo_docs
rule=UNKNOWN_when_runtime_relation_not_verified
rule=PROJECT_VIEW is inverse AI-first relation map

RELATIONS:
project=android;repo=/home/daniele/codex-workspace/projects/android;service=adb-wifi-autoconnect.service;timer=none;db=none;dashboard=none;monitor=none;alert=none
project=amici-fb;repo=/home/daniele/codex-workspace/scripts/amici_fb;service=amici_fb.service;timer=amici_fb.timer;db=amici_fb.sqlite3;dashboard=none;monitor=amici_fb_id_5;alert=Telegram_snapshot
project=codex-html-live;repo=/home/daniele/codex-workspace/codex-html-live;service=codex-html-live.service;timer=none;db=none;dashboard=html_archive;monitor=none;alert=none
project=codex-token-watcher;repo=/home/daniele/codex-workspace/codex-token-watcher;service=codex-usage-monitor.service;timer=codex-usage-monitor.timer;db=codex_usage.sqlite3;dashboard=none;monitor=codex-token-watcher_id_10_disabled;alert=Telegram_optional
project=git-change-ledger;repo=/home/daniele/codex-workspace/git-change-ledger;service=none_enabled;timer=template_only_disabled;db=git_change_ledger.sqlite3;dashboard=none;monitor=none;alert=none
project=grindr-web-exporter;repo=/home/daniele/codex-workspace/grindr-web-exporter;service=none;timer=none;db=grindr_export.sqlite3;dashboard=none;monitor=none;alert=none
project=facebook-video-archiver;repo=/home/daniele/codex-workspace/facebook-video-archiver;service=facebook-video-archiver.service;timer=facebook-video-archiver.timer_disabled;db=none_verified;dashboard=facebook_archive_dashboard.py;monitor=none;alert=none
project=linux-mint-service-dashboard;repo=/home/daniele/codex-workspace/linux-mint-service-dashboard;service=system-service-dashboard.service;timer=none;db=none_verified;dashboard=http://127.0.0.1:8788;monitor=none;alert=none
project=mint-cloud-backup;repo=/home/daniele/codex-projects/mint-cloud-backup;service=mint-cloud-backup.service,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service;timer=mint-cloud-backup.timer,mint-cloud-backup-kuma-push.timer;db=none;dashboard=http://127.0.0.1:8765;monitor=cloud_backup_id_3;alert=Kuma
project=mint-freeze-forensics;repo=/home/daniele/codex-workspace/mint-freeze-forensics;service=mint-freeze-forensics.service,mint-resource-guardian.service;timer=mint-resource-guardian.timer;db=none;state=jsonl;dashboard=system-service-dashboard_freeze_tab;monitor=Freeze_Gaps_13,PSI_Memory_14,PSI_IO_15,Guardian_Alerts_16,Forensics_Alive_17;alert=Kuma
project=mint-manual-updates;repo=/home/daniele/codex-workspace/mint-manual-updates;service=mint-manual-updates.service;timer=mint-manual-updates.timer;db=android_updates_history.sqlite;dashboard=none;monitor=none;alert=none
project=mint-update-tracker;repo=/home/daniele/codex-workspace/mint-update-tracker;service=mint-update-tracker.service,mint-update-tracker-backfill.service;timer=mint-update-tracker.timer;db=software_audit.db;dashboard=system-service-dashboard;monitor=software_audit_mint_id_11;alert=Kuma
project=oracle-uptime-kuma;repo=/home/daniele/codex-workspace/projects/vm_oracle/oracle-uptime-kuma;service=uptime-kuma_container;timer=UNKNOWN;db=kuma.db;dashboard=ssh_tunnel_http://127.0.0.1:3001;public=push_only_proxy_http://150.230.148.128:3001/api/push/<token>;monitor=self;alert=Telegram_notification_id_1
project=parcel-tracker;repo=/home/daniele/codex-workspace/parcel-tracker;service=parcel-tracker.service;timer=parcel-tracker.timer;db=parcel_tracker.sqlite3;dashboard=none;monitor=parcel-tracker_id_7;alert=Kuma,Telegram_update
project=surface-recovery-hardening;repo=/home/daniele/codex-workspace/surface-recovery-hardening;service=transfer-usb-io-watchdog.service,transfer-vecchio-disco-adaptive-throttle.service,remote-recovery-tmux.service,surface-no-suspend.service,rsync-uptime-kuma-push.service_disabled;timer=none;db=source_cleanup_analyzer_SQLite_only;dashboard=transfer_vecchio_disco_dashboard.sh;monitor=rsync-transfer_id_2_disabled;alert=Telegram_watchdog
project=windowtabnotes;repo=/home/daniele/codex-workspace/WindowTabNotes;service=windowtabnotes.service;timer=none;db=windowtabnotes.sqlite3;dashboard=WindowTabNotes_UI;monitor=none;alert=none
project=backup_docs;repo=/home/daniele/backup_docs;service=home-incremental-backup.service,home-backup-kuma-push.service,home-backup-retention-kuma-push.service;timer=home-incremental-backup.timer,home-backup-kuma-push.timer,home-backup-retention-kuma-push.timer;db=none;dashboard=none;monitor=mint-home-backup_id_4,mint-home-backup-retention_id_9;alert=Kuma
project=terminal-logger;repo=/home/daniele/terminal-logger;service=terminal-logger-codex.service,terminal-logger-codex-snapshot.service,terminal-logger-maintenance.service;timer=terminal-logger-codex-snapshot.timer,terminal-logger-maintenance.timer;db=terminal_logger.sqlite;dashboard=none;monitor=none;alert=none
project=activitywatch;repo=UNKNOWN;service=aw-server.service,aw-watcher-afk.service,aw-watcher-window.service,aw-watcher-media-player.service;timer=none;db=peewee-sqlite.v2.db;dashboard=ActivityWatch;monitor=none;alert=none
project=disk-usage-monitor;repo=/home/daniele/disk_usage_monitor;service=disk-usage-monitor.service;timer=disk-usage-monitor.timer;db=disk_usage_monitor.sqlite;dashboard=system-service-dashboard;monitor=disk-usage-monitor_id_6;alert=Kuma,Telegram
project=x11vnc-real-display;repo=/home/daniele/remote_real_display_482;service=x11vnc-real-display.service;timer=none;db=none;dashboard=none;monitor=none;alert=none

PROJECT_VIEW:
project=android;repo=/home/daniele/codex-workspace/projects/android;services=adb-wifi-autoconnect.service;timers=none;databases=none;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=none
project=amici-fb;repo=/home/daniele/codex-workspace/scripts/amici_fb;services=amici_fb.service;timers=amici_fb.timer;databases=amici_fb.sqlite3;kuma_monitors=amici_fb_id_5;dashboards=none;alerts=Telegram_snapshot,Kuma;storage_touchpoints=/home/daniele/codex-workspace/scripts/amici_fb
project=backup_docs;repo=/home/daniele/backup_docs;services=home-incremental-backup.service,home-backup-kuma-push.service,home-backup-retention-kuma-push.service;timers=home-incremental-backup.timer,home-backup-kuma-push.timer,home-backup-retention-kuma-push.timer;databases=none;kuma_monitors=mint-home-backup_id_4,mint-home-backup-retention_id_9;dashboards=none;alerts=Kuma;storage_touchpoints=/media/daniele/Seagate6TB2/home-backups
project=codex-html-live;repo=/home/daniele/codex-workspace/codex-html-live;services=codex-html-live.service;timers=none;databases=none;kuma_monitors=none;dashboards=html_archive;alerts=none;storage_touchpoints=~/.codex/sessions
project=codex-token-watcher;repo=/home/daniele/codex-workspace/codex-token-watcher;services=codex-usage-monitor.service;timers=codex-usage-monitor.timer;databases=codex_usage.sqlite3;kuma_monitors=codex-token-watcher_id_10_disabled;dashboards=none;alerts=Telegram_optional;storage_touchpoints=~/.local/share/codex-usage-monitor
project=disk-usage-monitor;repo=/home/daniele/disk_usage_monitor;services=disk-usage-monitor.service;timers=disk-usage-monitor.timer;databases=disk_usage_monitor.sqlite;kuma_monitors=disk-usage-monitor_id_6;dashboards=system-service-dashboard;alerts=Kuma,Telegram;storage_touchpoints=/home/daniele/sync_root/db/disk_usage_monitor.sqlite
project=git-change-ledger;repo=/home/daniele/codex-workspace/git-change-ledger;services=none_enabled;timers=template_only_disabled;databases=git_change_ledger.sqlite3;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=/home/daniele/sync_root/db/git_change_ledger.sqlite3
project=grindr-web-exporter;repo=/home/daniele/codex-workspace/grindr-web-exporter;services=none;timers=none;databases=grindr_export.sqlite3;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=/home/ubuntu/sync_root/db/grindr_export.sqlite3,repo_exports_media_debug_state_gitignored
project=linux-mint-service-dashboard;repo=/home/daniele/codex-workspace/linux-mint-service-dashboard;services=system-service-dashboard.service;timers=none;databases=none_verified;kuma_monitors=none;dashboards=http://127.0.0.1:8788;alerts=none;storage_touchpoints=none
project=mint-cloud-backup;repo=/home/daniele/codex-projects/mint-cloud-backup;services=mint-cloud-backup.service,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service;timers=mint-cloud-backup.timer,mint-cloud-backup-kuma-push.timer;databases=none;kuma_monitors=cloud_backup_id_3;dashboards=http://127.0.0.1:8765;alerts=Kuma;storage_touchpoints=/var/lib/mint-cloud-backup,/var/cache/mint-cloud-backup/restic,Backblaze_B2
project=mint-freeze-forensics;repo=/home/daniele/codex-workspace/mint-freeze-forensics;services=mint-freeze-forensics.service,mint-resource-guardian.service;timers=mint-resource-guardian.timer;databases=none;state=mint-freeze-forensics_state;kuma_monitors=Freeze_Gaps_13,PSI_Memory_14,PSI_IO_15,Guardian_Alerts_16,Forensics_Alive_17;dashboards=system-service-dashboard_freeze_tab;alerts=Kuma;storage_touchpoints=~/.local/state/mint-freeze-forensics,root_USB_T7
project=mint-manual-updates;repo=/home/daniele/codex-workspace/mint-manual-updates;services=mint-manual-updates.service,android-sdk-auto-update.service;timers=mint-manual-updates.timer,android-sdk-auto-update.timer;databases=android_updates_history.sqlite;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=~/.local/state/mint-manual-updates
project=mint-update-tracker;repo=/home/daniele/codex-workspace/mint-update-tracker;services=mint-update-tracker.service,mint-update-tracker-backfill.service;timers=mint-update-tracker.timer;databases=software_audit.db;kuma_monitors=software_audit_mint_id_11;dashboards=system-service-dashboard;alerts=Kuma;storage_touchpoints=/home/ubuntu/sync_root/db/software_audit.db
project=oracle-uptime-kuma;repo=/home/daniele/codex-workspace/projects/vm_oracle/oracle-uptime-kuma;services=uptime-kuma_container;timers=UNKNOWN;databases=kuma.db;kuma_monitors=self;dashboards=ssh_tunnel_http://127.0.0.1:3001;public=push_only_proxy_http://150.230.148.128:3001/api/push/<token>;alerts=Telegram_notification_id_1;storage_touchpoints=/opt/uptime-kuma/data/kuma.db
project=parcel-tracker;repo=/home/daniele/codex-workspace/parcel-tracker;services=parcel-tracker.service;timers=parcel-tracker.timer;databases=parcel_tracker.sqlite3;kuma_monitors=parcel-tracker_id_7;dashboards=none;alerts=Kuma,Telegram_update;storage_touchpoints=/home/daniele/codex-workspace/parcel-tracker
project=surface-recovery-hardening;repo=/home/daniele/codex-workspace/surface-recovery-hardening;services=transfer-usb-io-watchdog.service,transfer-vecchio-disco-adaptive-throttle.service,remote-recovery-tmux.service,surface-no-suspend.service,rsync-uptime-kuma-push.service_disabled,mint-xfce-layout-guard.service;timers=mint-xfce-layout-guard.timer;databases=source_cleanup_analyzer_SQLite_only;kuma_monitors=rsync-transfer_id_2_disabled;dashboards=transfer_vecchio_disco_dashboard.sh;alerts=Telegram_watchdog;storage_touchpoints=/dev/sdb2,/media/daniele/Seagate6TB2/vecchio_disco,SABRENT_USB_hub
project=terminal-logger;repo=/home/daniele/terminal-logger;services=terminal-logger-codex.service,terminal-logger-codex-snapshot.service,terminal-logger-maintenance.service;timers=terminal-logger-codex-snapshot.timer,terminal-logger-maintenance.timer;databases=terminal_logger.sqlite;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=~/.local/share/terminal-logger
project=windowtabnotes;repo=/home/daniele/codex-workspace/WindowTabNotes;services=windowtabnotes.service;timers=none;databases=windowtabnotes.sqlite3;kuma_monitors=none;dashboards=WindowTabNotes_UI;alerts=none;storage_touchpoints=~/.local/share/windowtabnotes
project=x11vnc-real-display;repo=/home/daniele/remote_real_display_482;services=x11vnc-real-display.service;timers=none;databases=none;kuma_monitors=none;dashboards=none;alerts=none;storage_touchpoints=~/.config/x11vnc-real-display,~/remote_real_display_482

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
open=activitywatch_repo_UNKNOWN_local_tool_install_only
open=activitywatch_watchers_use_XFCE_autostart_bridge_because_graphical-session.target_inactive
