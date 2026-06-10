# PROMPT_582941_ACTIVITYWATCH_REBOOT_BEFORE
VERSION=1
STATUS=PRE_REBOOT_SNAPSHOT
DATE=2026-06-10T19:41:00+02:00
HOST=daniele-Surface-Pro
USER=daniele
SOURCE_REPORT=ai/reports/prompt_391684_activitywatch_autostart.md

OBJECTIVE:
goal=verify_after_physical_reboot_that_ActivityWatch_autostart_and_autorestart_really_work
method=pre_reboot_snapshot+physical_reboot+post_login_XFCE_one_shot_verifier

PRE_REBOOT_CONTEXT:
whoami=daniele
id=uid=1000(daniele),gid=1000(daniele),groups=sudo_and_desktop_groups
hostname=daniele-Surface-Pro
uptime=2026-06-10_19:39:31 up_44min
megavault_branch=codex/prompt-731845-kuma-operational-runbook
megavault_sync=HEAD...upstream_0_0_before_new_docs
megavault_dirty_preexisting=ai/PROJECT_INDEX.md,ai/PROJECT_INVENTORY.md,ai/projects/git-change-ledger.md,human/projects/git-change-ledger/

LOGINCTL:
State=active
Service=user@1000.service
RuntimePath=/run/user/1000
Sessions=c2
Linger=yes

SYSTEMD_USER_PRE_REBOOT:
aw-server.service=active/running;enabled=enabled;MainPID=603007;FragmentPath=/home/daniele/.config/systemd/user/aw-server.service
activitywatch-graphical-session.target=active/active;enabled=static;FragmentPath=/home/daniele/.config/systemd/user/activitywatch-graphical-session.target
aw-watcher-afk.service=active/running;enabled=enabled;MainPID=607723;FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-afk.service
aw-watcher-window.service=active/running;enabled=enabled;MainPID=607696;FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-window.service
aw-watcher-media-player.service=active/running;enabled=enabled;MainPID=607729;FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-media-player.service
failed_units=0_loaded_units_listed

GRAPHICAL_ENV_PRE_REBOOT:
DISPLAY=:0.0
XAUTHORITY=/home/daniele/.Xauthority
XDG_SESSION_TYPE=x11
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
graphical-session.target=known_inactive_on_XFCE_from_391684

ACTIVITYWATCH_API_PRE_REBOOT:
info={"hostname":"daniele-Surface-Pro","version":"v0.13.2","testing":false,"device_id":"bf9949f3-475c-40b4-aa59-f7e2fcea16df"}
bucket=aw-watcher-afk_daniele-Surface-Pro
bucket=aw-watcher-media-player_daniele-Surface-Pro
bucket=aw-watcher-window_daniele-Surface-Pro

PROCESS_CHECK_PRE_REBOOT:
systemd_process=603007 /home/daniele/.local/bin/aw-server cgroup=aw-server.service
systemd_process=607696 /home/daniele/.local/bin/aw-watcher-window cgroup=aw-watcher-window.service
systemd_process=607723 /home/daniele/.local/bin/aw-watcher-afk cgroup=aw-watcher-afk.service
systemd_process=607729 /usr/bin/aw-watcher-media-player cgroup=aw-watcher-media-player.service
manual_process_found=662117 /home/daniele/.local/bin/activitywatch cgroup=mint-xfce-layout-guard.service
manual_process_action=terminated_before_reboot_to_avoid_measuring_manual_GUI_session_restore_as_autostart
manual_process_after=none;only_systemd_ActivityWatch_processes_remained

PRE_REBOOT_OBSERVATION:
service_autostart_state=ready_for_reboot_test
data_db=~/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db;not_modified
reinstall=no
duplicates=no_server_or_watcher_duplicates_after_manual_aw_qt_termination

POST_REBOOT_VERIFIER:
script=~/.local/bin/activitywatch-postreboot-582941-check
unit=~/.config/systemd/user/activitywatch-postreboot-582941.service
trigger=activitywatch-graphical-session.target_after_XFCE_login_bridge
report=~/codex-workspace/MegaVault/ai/reports/prompt_582941_activitywatch_reboot_after.md
