# PROJECTS_LEGACY
VERSION=1
STATUS=CONSOLIDATED_NONAUTHORITATIVE_RUNTIME_REFERENCES
FORMAT=ultracompressed
UPDATED=2026-07-18
RULE=historical_paths_require_live_revalidation;Git_preserves_removed_detail

PROJECTS:
project=android;purpose=ADB_WiFi_autoconnect;repo=/home/daniele/codex-workspace/projects/android;data=~/.config/adb-wifi-autoconnect/config.json+~/.local/state/adb-wifi-autoconnect;dnb=no_adb_kill-server+no_pairing_code_storage;open=Pixel_not_connected_at_2026-06-05;superseded_by=../global/ADB_DEVICE_KEEPER.md
project=android-sdk-auto-update;purpose=daily_sdkmanager_updates;repo=/home/daniele/codex-workspace/android-sdk-auto-update;status=legacy_Mint
project=aw-converter;repo=/home/daniele/codex-workspace/aw-converter;purpose=UNKNOWN;tests=UNKNOWN
project=chatgpt-chrome-debug;repo=/home/daniele/codex-workspace/chatgpt-chrome-debug;purpose=Chrome_redirect_diagnostics;stack=Playwright+Python+Shell;entry=START_DEBUGGING.sh;status=legacy
project=codex-html-live;repo=/home/daniele/codex-workspace/codex-html-live;purpose=Codex_JSONL_to_live_HTML;entry=codex_html_live.py;tests=tests/test_codex_html_live.py;status=legacy
project=codex-wrapper;repo=/home/daniele/codex-workspace/codex-wrapper;purpose=UNKNOWN;tests=UNKNOWN
project=disk-usage-monitor;repo=/home/daniele/disk_usage_monitor;purpose=Mint_3-disk_monitor;db=/home/daniele/sync_root/db/disk_usage_monitor.sqlite;dnb=oneshot_inactive_is_normal+no_rm_open_Codex_WAL+Kuma_interval_not_below_timer;status=legacy_Mint
project=facebook-video-archiver;repo=/home/daniele/codex-workspace/facebook-video-archiver;purpose=authorized_Facebook_video_archive;entry=facebook_video_archiver.sh;status=legacy;tests=UNKNOWN
project=git-change-ledger;repo=/home/daniele/codex-workspace/git-change-ledger;purpose=read_only_Git_state_ledger;db=/home/daniele/sync_root/db/git_change_ledger.sqlite3;dnb=no_repo_writes+no_auto_fetch+no_full_diffs+timer_disabled;status=legacy
project=installa-app;repo=/home/daniele/codex-workspace/installa-app;purpose=UNKNOWN;tests=UNKNOWN
project=linux-mint-service-dashboard;repo=/home/daniele/codex-workspace/linux-mint-service-dashboard;purpose=Mint_read_only_service_dashboard;bind=127.0.0.1:8788;status=legacy_Mint
project=maintenance-486;repo=/home/daniele/codex-workspace/projects/vm_oracle/maintenance-486;purpose=Oracle_VM_diagnostics_workspace;script=scripts/ssh_diag_486.sh;status=legacy
project=megavault-project-exporter;repo=/home/daniele/codex-workspace/megavault-project-exporter;purpose=project+MegaVault_ZIP_export;config=~/.config/megavault-project-exporter/config.env;state=state;output=bundles;dnb=no_.git+no_silent_dirty_or_transfer_success;status=legacy_Mint
project=mint-cloud-backup;repo=/home/daniele/codex-projects/mint-cloud-backup;purpose=Mint_root_restic_to_B2;state=/var/lib/mint-cloud-backup;secret_refs=/etc/mint-cloud-backup/restic.env+/etc/mint-cloud-backup/uptime-kuma.env;status=legacy_Mint
project=mint-freeze-forensics;repo=/home/daniele/codex-workspace/mint-freeze-forensics;purpose=freeze_observability;state=~/.local/state/mint-freeze-forensics;config=~/.config/mint-freeze-forensics;dnb=no_auto_reboot+restart+kill+tuning;status=legacy_Mint
project=mint-manual-updates;repo=/home/daniele/codex-workspace/mint-manual-updates;purpose=manual_Mint+dev+Android_updates;entry=bin/mint-manual-updates;state=~/.local/state/mint-manual-updates;status=legacy_Mint
project=mint-update-tracker;repo=/home/daniele/codex-workspace/mint-update-tracker;purpose=read_only_software_audit;db=remote:/home/ubuntu/sync_root/db/software_audit.db;status=legacy_Mint+Oracle
project=os-observer;repo=/home/daniele/codex-workspace/os-observer;purpose=Mint_black_box_telemetry+bounded_export;status=legacy_Mint
project=parcel-tracker;repo=/home/daniele/codex-workspace/parcel-tracker;purpose=shipment_XT329499807TS_monitor;entry=parcel_tracker.py;status=legacy
project=remote-codex-phone;repo=/home/daniele/codex-workspace/remote-codex-phone;purpose=Android_phone_Codex_control;flow=UNKNOWN;status=legacy
project=remote-opt-oracle-backup;repo=/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup;purpose=Oracle_restic_runtime_scripts;env=/etc/oracle_backup/oracle_backup.env;state=/var/lib/oracle_backup;dnb=flock+preflight+no_destructive_no-lock_prune;superseded_by=oracle-backup-service.md
project=system-watchdog;repo=/home/daniele/codex-workspace/system_watchdog;purpose=generic_Kuma_heartbeat;db=/home/daniele/codex-workspace/system_watchdog/watchdog.sqlite;status=disabled_since_2026-06-05;dnb=do_not_enable_without_operator
project=windowtabnotes;status=Fedora_local_abandoned+uninstalled;remote=https://github.com/gernalix/WindowTabNotes;branch=fedora-current-session-window-detection-927514;commit=40421981911c6d92111e9062eb20c506003d4d97;data_backup=/home/daniele/WindowTabNotes-backup-351806;reason=GNOME_Wayland_native_active_window_unavailable_without_extension_or_privileged_introspection;dnb=preserve_remote+backup

OPEN:
open=UNKNOWN_fields require owner_repo inspection;do_not_infer
open=legacy_Mint paths are not current Fedora truth
