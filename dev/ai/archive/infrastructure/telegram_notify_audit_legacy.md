META:
prompt=738492
date=2026-06-13
status=audit_only_no_migration
scope=local_host+Oracle_VM+systemd+MegaVault_registered_projects+runtime_projects
csv=telegram_projects_chat_id.csv
canonical_source=/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py
implementations_count_active_code_files=40
projects_count=26
secrets_policy=values_not_recorded; token/chat_id only flagged yes/no

READ:
protocol=/home/daniele/codex-workspace/MegaVault/ai/MEGAVAULT_PROTOCOL.md
host_profile=/home/daniele/codex-workspace/MegaVault/ai/global/HOST_PROFILE.md
ai_docs=HOST_PROFILE,SERVICE_REGISTRY,ALERT_REGISTRY,PROJECT_INDEX,amici-fb,parcel-tracker,disk-usage-monitor,oracle-backup-service,oracle-uptime-kuma,surface-recovery-hardening,mint-manual-updates,owntracks-watcher,codex-token-watcher,facebook-video-archiver
human_docs=not_used_as_operational_source

SCAN:
local_roots=/home/daniele,/home/daniele/codex-workspace,/home/daniele/AndroidStudioProjects,/home/daniele/.local/bin,/home/daniele/.config,/etc/systemd/system
vm_roots=/home/ubuntu,/opt,/etc/systemd/system,/home/ubuntu/.config/systemd/user
local_name_hits=61 includes archives/vendor/desktop artifacts
local_targeted_hits=174 active+doc+config hits
vm_name_hits=55 includes archives/db/zips/snapshots/vendor
vm_content_hits=619 before filtering
excluded_from_active_count=archives,exports,old snapshots,venv/site-packages,binary DBs,docs-only false positives,Android UI links without Bot API
android_false_positive=SuperContacts app UI Telegram contact/deeplink fields are not bot notification infra; SuperContacts build-finalize scripts are infra and included

CANONICAL_SOURCE:
path=/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py
host=local
size_bytes=5692
mtime=2026-05-05T23:15:27
public_functions=8
functions=validate_config,config_summary,fix_mojibake,send_text_raw,send_message,send_file,notify,main
cli=yes; argparse; positional title/message; --file; --check
import_python=yes
send_file=yes via sendDocument
send_image=indirect_as_document_only; no sendPhoto
error_handling=raises RuntimeError/FileNotFoundError; CLI returns rc1; HTTP body capped; timeouts 20s message,60s document
token_hardcoded=no
chat_id_hardcoded=no
dependencies=requests
config=TELEGRAM_BOT_TOKEN+TELEGRAM_CHAT_ID env; additionally loads project-local .env
used_by=amici-fb,parcel-tracker,disk-usage-monitor,home-backup scripts,surface-recovery-hardening,facebook-video-archiver,mint-manual-updates,legacy codex usage watcher
why_selected=best_balance_current_usage+no_hardcoded_secrets+CLI+import+send_file+timeouts+HTML_escape+mojibake_fix+compat_notify_wrapper
known_gap=project-local .env load must be replaced by common config resolver in future library

IMPLEMENTATIONS:
local=/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py|kind=library|version=v13|token_hardcoded=no|chat_hardcoded=no|cli=yes|import=yes|file=yes|direct_api=yes|risk=low|notes=CANONICAL_SOURCE
local=/home/daniele/codex-workspace/scripts/amici_fb/_shared/telegram_notify.py|kind=library_copy|version=v13|token_hardcoded=no|chat_hardcoded=no|cli=yes|import=yes|file=yes|direct_api=yes|risk=low|notes=same API but no project .env load
local=/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup/lib/telegram_notify.py|kind=library_copy|version=v11|token_hardcoded=yes|chat_hardcoded=yes|cli=yes|import=yes|file=yes|direct_api=yes|risk=high|notes=do_not_use_as_source
vm=/opt/oracle_backup/lib/telegram_notify.py|kind=library_runtime|version=v11|token_hardcoded=yes|chat_hardcoded=yes|cli=yes|import=yes|file=yes|direct_api=yes|risk=high|used_by=oracle-backup-service
vm=/home/ubuntu/telegram_notify.py|kind=library_runtime_shared|version=v11|token_hardcoded=yes|chat_hardcoded=yes|cli=yes|import=yes|file=yes|direct_api=yes|risk=high|used_by=telegram-media-monitor,legacy callers
vm=/opt/workflowy_import/telegram_notify.py|kind=library_copy|version=v11|token_hardcoded=yes|chat_hardcoded=yes|cli=yes|import=yes|file=yes|direct_api=yes|risk=high
local=/home/daniele/disk_usage_monitor/disk_usage_monitor.sh|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|cli=yes|import=no|file=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/home_incremental_backup.sh|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/home_seed_critical_backup.sh|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/backup_docs/bin/home_incremental_backup.sh|kind=repo_copy_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/backup_docs/bin/home_seed_critical_backup.sh|kind=repo_copy_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.py|kind=subprocess_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=low
local=/home/daniele/codex-workspace/mint-manual-updates/bin/mint-manual-updates|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/codex-workspace/codex-token-watcher/codex_cli_status_watcher.py|kind=direct_bot_api|token_hardcoded=no|chat_hardcoded=no|urllib=yes|risk=medium
local=/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py|kind=legacy_helper_wrapper+direct_redaction|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
vm=/home/ubuntu/codex-workspace/codex-usage-monitor/codex_cli_status_watcher.py|kind=direct_bot_api|token_hardcoded=no|chat_hardcoded=no|urllib=yes|risk=medium
vm=/home/ubuntu/codex-workspace/codex-usage-monitor/codex_usage_monitor.py|kind=legacy_helper_wrapper+direct_redaction|token_hardcoded=no|chat_hardcoded=no|risk=medium
vm=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py|kind=dynamic_helper_import|token_hardcoded=no|chat_hardcoded=no|helper_search=yes|risk=high
local=/home/daniele/codex-workspace/owntracks-sqlite-watcher/owntracks_sqlite_watcher/notify.py|kind=helper_wrapper|token_hardcoded=no|chat_hardcoded=no|helper_config=OWNTRACKS_TELEGRAM_HELPER|risk=medium
vm=/home/ubuntu/bots/owntracks_http_server/owntracks_http_server.py|kind=optional_import|token_hardcoded=no|chat_hardcoded=no|module_missing_runtime_docs|risk=medium
local=/home/daniele/codex-workspace/facebook-video-archiver/facebook_video_archiver.sh|kind=optional_helper_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=low
local=/home/daniele/codex-workspace/surface-recovery-hardening/scripts/transfer_usb_io_watchdog.sh|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=high
local=/home/daniele/codex-workspace/surface-recovery-hardening/scripts/memory_pressure_guardian.sh|kind=shell_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=high
local=/home/daniele/codex-workspace/surface-recovery-hardening/scripts/transfer_vecchio_disco_watchdog.sh|kind=python_in_sh_wrapper|token_hardcoded=no|chat_hardcoded=no|helper=CANONICAL_SOURCE|risk=medium
local=/home/daniele/codex-workspace/projects/MultiTimeTracker/tools/mtt_helper.py|kind=direct_curl_sendDocument|token_hardcoded=no_code; token_in_ini=yes|chat_hardcoded=config_yes|file=yes|risk=high
local=/home/daniele/codex-workspace/SuperContacts/tools/build-finalize.sh|kind=helper_file_sender|token_hardcoded=no|chat_hardcoded=yes|file=yes|risk=high|helper_repo_missing=yes
local=/home/daniele/codex-workspace/SuperContacts/tools/build-finalize.ps1|kind=helper_file_sender_windows|token_hardcoded=no|chat_hardcoded=param/default_indirect|file=yes|risk=medium
local=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service/scripts/backup.sh|kind=embedded_python_import_helper|helper=/opt/oracle_backup/lib|risk=high
local=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service/scripts/check_backup_health.py|kind=helper_import|helper=/opt/oracle_backup/lib|risk=high
local=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service/scripts/oracle-backup-healthcheck.sh|kind=embedded_python_import_helper|helper=/opt/oracle_backup/lib|risk=high
vm=/opt/oracle_backup/backup.sh|kind=embedded_python_import_helper|helper=/opt/oracle_backup/lib|risk=high
vm=/opt/oracle_backup/check_backup_health.py|kind=helper_import|helper=/opt/oracle_backup/lib|risk=high
vm=/usr/local/bin/oracle-backup-healthcheck.sh|kind=embedded_python_import_helper|helper=/opt/oracle_backup/lib|risk=high
vm=/home/ubuntu/oracle-backup-healthcheck.sh|kind=legacy_embedded_python_import_helper|risk=medium
vm=/home/ubuntu/bots/amici_fb/amici_fb.py|kind=helper_import|token_hardcoded=no|chat_hardcoded=no|file=yes|risk=medium
vm=/home/ubuntu/bots/strano_anello/strano_anello.py|kind=helper_or_direct_bot_api_fallback|token_hardcoded=no|chat_hardcoded=no|direct_api=yes|risk=high
vm=/home/ubuntu/bots/yt_dlp_downloader_oracle_ubuntu/yt_dlp_downloader.py|kind=optional_helper_import|token_hardcoded=no|chat_hardcoded=no|risk=medium
vm=/home/ubuntu/sync_root/bots/telegram_insert_bot-master/telegram_insert_bot.py|kind=full_telegram_bot|python_telegram_bot=yes|token_in_settings_db_or_env=unknown_values_not_printed|risk=high
vm=/home/ubuntu/sync_root/bots/porno_bot/telegram_porno_bot.py|kind=full_telegram_bot|python_telegram_bot=yes|token_env=yes|risk=medium
vm=/opt/telegram-media-monitor/telegram_media_monitor_service.py|kind=telethon_monitor+helper_notify|notify_helper=/home/ubuntu/telegram_notify.py|risk=high

PROJECTS:
project=MultiTimeTracker;host=local;root=/home/daniele/codex-workspace/projects/MultiTimeTracker;mode=tools/mtt_helper.py curl sendDocument;files=tools/mtt_helper.py,tools/mtt_helper.ini;token_hardcoded=config_yes;chat_id_hardcoded=config_yes;risk=high
project=SuperContacts;host=local;root=/home/daniele/codex-workspace/SuperContacts;mode=tools/build-finalize sends APK/ZIP through repo telegram_notify.py if present;files=tools/build-finalize.sh,tools/build-finalize.ps1;token_hardcoded=no;chat_id_hardcoded=yes;risk=high
project=amici-fb;host=local;root=/home/daniele/codex-workspace/scripts/amici_fb;mode=import telegram_notify;files=amici_fb.py,telegram_notify.py,_shared/telegram_notify.py,amici_fb.service;token_hardcoded=no;chat_id_hardcoded=no;risk=low
project=amici-fb-vm-legacy;host=vm;root=/home/ubuntu/bots/amici_fb;mode=import telegram_notify;files=amici_fb.py,/etc/systemd/system/amici-fb.service;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=parcel-tracker;host=local;root=/home/daniele/codex-workspace/parcel-tracker;mode=subprocess CANONICAL_SOURCE;files=parcel_tracker.py,parcel-tracker.service;token_hardcoded=no;chat_id_hardcoded=no;risk=low
project=disk-usage-monitor;host=local;root=/home/daniele/disk_usage_monitor;mode=shell helper via /home/daniele/.config/environment.d/telegram.conf;files=disk_usage_monitor.sh,/etc/systemd/system/disk-usage-monitor.service;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=home-incremental-backup;host=local;root=/home/daniele + /home/daniele/backup_docs;mode=first-success Telegram via helper;files=home_incremental_backup.sh,backup_docs/bin/home_incremental_backup.sh;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=home-seed-critical-backup;host=local;root=/home/daniele + /home/daniele/backup_docs;mode=seed success Telegram via helper;files=home_seed_critical_backup.sh,backup_docs/bin/home_seed_critical_backup.sh;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=surface-recovery-hardening;host=local;root=/home/daniele/codex-workspace/surface-recovery-hardening;mode=watchdog/guardian helpers;files=transfer_usb_io_watchdog.sh,memory_pressure_guardian.sh,transfer_vecchio_disco_watchdog.sh;token_hardcoded=no;chat_id_hardcoded=no;risk=high
project=mint-manual-updates;host=local;root=/home/daniele/codex-workspace/mint-manual-updates;mode=helper notify on updater events;files=bin/mint-manual-updates;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=codex-token-watcher;host=local;root=/home/daniele/codex-workspace/codex-token-watcher;mode=direct Bot API in CLI watcher + legacy helper;files=codex_cli_status_watcher.py,codex_usage_monitor.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=codex-usage-monitor-vm;host=vm;root=/home/ubuntu/codex-workspace/codex-usage-monitor;mode=direct Bot API + helper legacy;files=codex_cli_status_watcher.py,codex_usage_monitor.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=codex-weekly-limit-monitor-vm;host=vm;root=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor;mode=dynamic import telegram_notify;files=codex_weekly_limit_watcher.py;token_hardcoded=no;chat_id_hardcoded=no;risk=high
project=owntracks-sqlite-watcher;host=local;root=/home/daniele/codex-workspace/owntracks-sqlite-watcher;mode=optional helper path OWNTRACKS_TELEGRAM_HELPER;files=notify.py,config.py,mqtt_client.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=owntracks-watcher;host=vm;root=/home/ubuntu/bots/owntracks_http_server;mode=optional import telegram_notify/telegram_notifiy but docs say module missing;files=owntracks_http_server.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=facebook-video-archiver;host=local;root=/home/daniele/codex-workspace/facebook-video-archiver;mode=optional helper when ENABLE_TELEGRAM=1;files=facebook_video_archiver.sh;token_hardcoded=no;chat_id_hardcoded=no;risk=low
project=oracle-backup-service;host=vm+local_repo;root=/opt/oracle_backup and /home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service;mode=helper import for backup/quota/healthcheck alerts;files=backup.sh,check_backup_health.py,oracle-backup-healthcheck.sh,lib/telegram_notify.py;token_hardcoded=runtime_helper_yes;chat_id_hardcoded=runtime_helper_yes;risk=high
project=remote-opt-oracle-backup;host=local_repo;root=/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup;mode=runtime mirror/helper copy;files=lib/telegram_notify.py,check_backup_health.py;token_hardcoded=yes;chat_id_hardcoded=yes;risk=high
project=oracle-uptime-kuma;host=vm;root=/opt/uptime-kuma;mode=Kuma notification id 1 type telegram;files=kuma.db config only,not read raw;token_hardcoded=db_config_yes_values_not_printed;chat_id_hardcoded=db_config_yes_values_not_printed;risk=high
project=telegram-insert-bot;host=vm;root=/home/ubuntu/sync_root/bots/telegram_insert_bot-master;mode=python-telegram-bot full bot;files=telegram_insert_bot.py,/etc/systemd/system/telegram-insert-bot.service;token_hardcoded=unknown_external_settings;chat_id_hardcoded=db_runtime; risk=high
project=telegram-media-monitor;host=vm;root=/opt/telegram-media-monitor;mode=Telethon MTProto monitor + helper notification;files=telegram_media_monitor_service.py,/etc/systemd/system/telegram-media-monitor.*;token_hardcoded=no;chat_id_hardcoded=no;risk=high
project=telegram-bot-vm-disabled;host=vm;root=/home/ubuntu/bots/telegram_bot missing during audit;mode=systemd unit disabled but file path missing;files=/etc/systemd/system/telegram-bot.service;token_hardcoded=unknown;chat_id_hardcoded=unknown;risk=high
project=porno-bot-vm;host=vm;root=/home/ubuntu/sync_root/bots/porno_bot;mode=python-telegram-bot full bot;files=telegram_porno_bot.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=strano-anello-vm;host=vm;root=/home/ubuntu/bots/strano_anello;mode=helper or direct Bot API fallback;files=strano_anello.py;token_hardcoded=no;chat_id_hardcoded=no;risk=high
project=yt-dlp-downloader-oracle-vm;host=vm;root=/home/ubuntu/bots/yt_dlp_downloader_oracle_ubuntu;mode=optional helper import;files=yt_dlp_downloader.py;token_hardcoded=no;chat_id_hardcoded=no;risk=medium
project=workflowy-import-vm;host=vm;root=/opt/workflowy_import;mode=helper copy;files=telegram_notify.py;token_hardcoded=yes;chat_id_hardcoded=yes;risk=high

DIFFERENCES:
v13_local=no_hardcoded_secrets,env_config,HTML_parse_mode,timeouts,RuntimeError,CLI_check,send_text_raw,send_message,send_file,notify
v13_shared=no_project_env_load,otherwise_same_api
v11_vm=hardcoded_token_and_chat_id,Markdown_parse_mode,no_request_timeout,sys.exit_inside_library,larger_comments,send_file_compatible
direct_api_watchers=avoid_helper; each owns timeout/dedup/redaction; harder to centralize without behavior tests
full_bots=not simple notify clients; migration should centralize outbound notification/config only, not rewrite bot frameworks
Kuma=Telegram config lives in DB notification id 1; central Python library cannot replace it without separate Kuma notification strategy

FUTURE_LIBRARY_SPEC:
source_repo=/home/daniele/codex-workspace/telegram-notify-common
local_install=/home/daniele/.local/lib/megavault/telegram_notify.py
local_cli=/home/daniele/.local/bin/telegram-notify
vm_install=/opt/megavault/telegram_notify.py
vm_cli=/usr/local/bin/telegram-notify
config_local=/home/daniele/.config/megavault/telegram/telegram.env
config_vm=/etc/megavault/telegram.env
project_map_local=/home/daniele/.config/megavault/telegram/projects.csv
project_map_vm=/etc/megavault/telegram_projects.csv
minimum_api=send_message(title,message,project=None,chat_id=None,disable_preview=False,parse_mode="HTML")
minimum_api=send_file(filepath,title=None,message=None,caption=None,project=None,chat_id=None)
minimum_api=notify(message,prefix=None,title=None,project=None,chat_id=None)
minimum_api=send_text_raw(message,project=None,chat_id=None,disable_preview=False)
compat=preserve old positional CLI: telegram_notify.py [--file PATH] [--check] TITLE MESSAGE
compat=preserve import names: validate_config,config_summary,fix_mojibake
compat=accept TELEGRAM_BOT_TOKEN,TELEGRAM_CHAT_ID env for legacy callers
project_chat_resolution=explicit chat_id > project map > TELEGRAM_CHAT_ID > error
token_resolution=TELEGRAM_BOT_TOKEN > config file token > error
timeouts=message default 20s,document default 60s,configurable env
errors=library raises exceptions; CLI prints redacted ERROR and returns nonzero; no sys.exit inside send funcs
security=never log token/chat_id; config_summary masks values; redact api.telegram.org/bot URLs
vm_compat=Python3 stdlib+requests if available; optional urllib fallback for minimal VM
linux_mint_compat=works under user/systemd; no interactive prompts; handles env files mode 600

MIGRATION_PLAN_NEXT_RUN:
step1=read telegram_projects_chat_id.csv and fail if required project chat_id blank unless project is intentionally skipped
step2=create telegram-notify-common from CANONICAL_SOURCE v13, removing project-local .env load and adding project map resolver
step3=install local library+CLI without deleting old helpers
step4=install VM library+CLI to /opt/megavault and /usr/local/bin via SSH; backup old /home/ubuntu/telegram_notify.py and /opt/oracle_backup/lib/telegram_notify.py before touching
step5=migrate low-risk local helper callers first: parcel-tracker,facebook-video-archiver,amici-fb
step6=migrate medium local wrappers: disk-usage-monitor,home backups,mint-manual-updates,codex-token-watcher legacy helper paths,owntracks-sqlite-watcher
step7=migrate high-risk/storage/backup services in maintenance windows: surface watchdogs,oracle-backup-service,remote-opt-oracle-backup
step8=handle Android release helpers: MultiTimeTracker mtt_helper,SuperContacts build-finalize scripts; remove hardcoded chat_ids/tokens from config/code only after user-provided CSV mapping is present
step9=handle VM runtime projects individually: codex-weekly-limit-monitor,strano_anello,yt_dlp_downloader,telegram-media-monitor,owntracks-watcher
step10=do not refactor full Telegram bots unless scoped; for telegram-insert-bot/porno-bot centralize token/chat config only if compatible with python-telegram-bot startup
step11=Kuma: do not alter notification id 1 in same pass unless explicit subtask; document manual/UI migration strategy separately
step12=test each migrated project with dry-run/check first, then one controlled notification only when user allows
step13=remove duplicate v11 helpers after all callers prove clean; keep temporary compatibility shim for old imports
step14=update AI/HUMAN docs and service registries; commit/push only in future run if user allows

OPEN:
open=Some VM legacy paths are enabled/disabled inconsistently; verify live service need before migration.
open=telegram-bot.service points to missing /home/ubuntu/bots/telegram_bot during audit.
open=Kuma Telegram notification id 1 stores token/chat in DB; values intentionally not read/printed.
open=Full bot projects may require separate token semantics and should not be converted to simple notify API blindly.
open=Archived copies under /home/daniele/Documents/vecchi file 6TB and VM snapshots were found but excluded from active migration.
