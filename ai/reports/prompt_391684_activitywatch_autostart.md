# PROMPT_391684_ACTIVITYWATCH_AUTOSTART
VERSION=1
STATUS=APPLIED
DATE=2026-06-10
HOST=daniele-Surface-Pro
USER=daniele
SCOPE=ActivityWatch_local_install_systemd_user_autostart_autorestart

CAUSE:
real_cause=aw-server,aw-watcher-afk,aw-watcher-window_not_managed_by_systemd;only_aw-watcher-media-player.service_enabled
boot_failure=aw-watcher-media-player.service_started_on_default.target_before_aw-server_listened_on_5600;journal_connection_refused_loop
login_failure=main_ActivityWatch_started_only_from_desktop_launcher/menu;no_~/.config/autostart_activitywatch_entry
wrong_cgroup=manual_activitywatch_processes_observed_under_mint-xfce-layout-guard.service_cgroup_due_desktop/menu_parentage;not_autorestartable
graphical_target=graphical-session.target_inactive_on_XFCE;watchers_cannot_depend_on_that_target_on_this_host
lingering=loginctl_show-user_daniele_Linger=yes;systemd_user_available_for_prelogin_aw-server

FINAL_UNITS:
unit=aw-server.service;path=~/.config/systemd/user/aw-server.service;wanted_by=default.target;exec=~/.local/bin/aw-server;restart=always;purpose=server_boot_prelogin
unit=activitywatch-graphical-session.target;path=~/.config/systemd/user/activitywatch-graphical-session.target;started_by=~/.config/autostart/activitywatch-systemd-session.desktop;purpose=session_watchers_target
unit=aw-watcher-afk.service;path=~/.config/systemd/user/aw-watcher-afk.service;wanted_by=activitywatch-graphical-session.target;exec=~/.local/bin/aw-watcher-afk;requires=XDG_SESSION_TYPE_x11+DISPLAY;restart=always
unit=aw-watcher-window.service;path=~/.config/systemd/user/aw-watcher-window.service;wanted_by=activitywatch-graphical-session.target;exec=~/.local/bin/aw-watcher-window;requires=XDG_SESSION_TYPE_x11+DISPLAY;restart=always
unit=aw-watcher-media-player.service;path=~/.config/systemd/user/aw-watcher-media-player.service;wanted_by=activitywatch-graphical-session.target;exec=/usr/bin/aw-watcher-media-player;requires=DBUS_SESSION_BUS_ADDRESS;restart=always
bridge=~/.local/bin/activitywatch-systemd-session-start;role=import_DISPLAY_XAUTHORITY_DBUS_env+start_aw-server+start_graphical_target+restart_watchers_on_login
desktop=~/.config/autostart/activitywatch-systemd-session.desktop;role=XFCE_login_bridge;NoDisplay=true;not_duplicate_app_launcher

PATHS:
activitywatch=~/.local/bin/activitywatch->~/.local/opt/activitywatch/aw-qt
aw-server=~/.local/bin/aw-server->~/.local/opt/activitywatch/aw-server/aw-server
aw-watcher-afk=~/.local/bin/aw-watcher-afk->~/.local/opt/activitywatch/aw-watcher-afk/aw-watcher-afk
aw-watcher-window=~/.local/bin/aw-watcher-window->~/.local/opt/activitywatch/aw-watcher-window/aw-watcher-window
aw-watcher-media-player=/usr/bin/aw-watcher-media-player
data_db=~/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db;not_modified=yes

OPS:
status=systemctl --user status aw-server.service aw-watcher-afk.service aw-watcher-window.service aw-watcher-media-player.service activitywatch-graphical-session.target
logs=journalctl --user -u aw-server.service -u aw-watcher-afk.service -u aw-watcher-window.service -u aw-watcher-media-player.service -b --no-pager
api=curl -fsS http://127.0.0.1:5600/api/0/info
login_bridge=/home/daniele/.local/bin/activitywatch-systemd-session-start
recovery=systemctl --user reset-failed aw-server.service aw-watcher-afk.service aw-watcher-window.service aw-watcher-media-player.service && /home/daniele/.local/bin/activitywatch-systemd-session-start

TEST:
manual_start_testing=aw-server_--testing_port_5666_ok;aw-watcher-afk_--testing_connected;aw-watcher-window_--testing_connected
enable=aw-server.service,aw-watcher-afk.service,aw-watcher-window.service,aw-watcher-media-player.service_enabled
api_real=http://127.0.0.1:5600/api/0/info_ok_version_v0.13.2_testing_false
autorestart=SIGKILL_all_four_services;NRestarts_0_to_1;new_PIDs_active
login_sim=stop_activitywatch-graphical-session.target_stopped_watchers_only;bridge_restart_restored_target_and_watchers;aw-server_remained_active
failed_units=systemctl_--user_--failed_returned_0_loaded_units
journal_note=only_expected_Failed_with_result_signal_from_deliberate_SIGKILL_test;no_residual_failed_units

INVARIANT:
ops=aw-server_starts_at_user_manager_boot_via_lingering_default.target
ops=watchers_start_at_XFCE_login_after_DISPLAY_XAUTHORITY_DBUS_import
ops=all_four_runtime_processes_are_systemd_user_services_with_Restart_always
ops=no_duplicate_activitywatch_processes_outside_systemd
data=do_not_reinstall_or_modify_ActivityWatch_DB_without_backup
