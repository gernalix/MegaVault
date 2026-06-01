META:
name=surface-recovery-hardening
slug=surface-recovery-hardening
path=/home/daniele/codex-workspace/surface-recovery-hardening
remote=git@github.com:gernalix/surface-recovery-hardening.git
branch=main
verified_commit=0868849
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Kit locale per rendere un Surface Pro con Linux Mint piu recuperabile durante trasferimenti USB pesanti:
STACK:
lang=Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=Chrome,Uptime Kuma,restic,systemd
MAP:
entry=UNKNOWN
ui=scripts/fix_mint_scaling_theme.sh,scripts/screen_watchdog.sh,scripts/show_scaling_theme_status.sh
core=configs/mint-xfce-layout-guard.desktop,dev/project.metadata.json,systemd/freeze-reboot-monitor.service,systemd/mint-xfce-layout-guard.service,systemd/mint-xfce-layout-guard.timer
db=scripts/restore_mint_scaling_theme_backup.sh
tests=UNKNOWN
scripts=configs/xrdp_startwm.sh,scripts/bundle_freeze_reboot_monitor_logs.sh,scripts/freeze_reboot_monitor.sh,scripts/low_memory_mode.sh,scripts/memory_pressure_guardian.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
ui=scripts/fix_mint_scaling_theme.sh:add_path,xfconf_set,log,get_value,display0_panel_pids,physical_session_env_value
ui=scripts/screen_watchdog.sh:timestamp,now_s,log,event,event_limited,save_state
ui=scripts/show_scaling_theme_status.sh:value
script=scripts/freeze_reboot_monitor.sh:timestamp,stamp_file,ensure_layout,write_readme,log_event,rotate_one
script=scripts/low_memory_mode.sh:timestamp,log,cmdline_for_pid,is_gradle_pid
script=scripts/memory_pressure_guardian.sh:timestamp,stamp_file,usage,log,run_or_log,meminfo_mb
script=scripts/recovery_dump.sh:run
script=scripts/recovery_status.sh:once
FLOW:
flow=script->configs/xrdp_startwm.sh=>scripts/restore_mint_scaling_theme_backup.sh
flow=data->scripts/restore_mint_scaling_theme_backup.sh
flow=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
flow=scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
flow=scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
INV:
arch=scripts/fix_mint_scaling_theme.sh:add_path,xfconf_set,log,get_value,display0_panel_pids; scripts/screen_watchdog.sh:timestamp,now_s,log,event,event_limited; scripts/show_scaling_theme_status.sh:value; scripts/freeze_reboot_monitor.sh:tim...
data=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"; scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
ux=scripts/screen_watchdog.sh:182:loginctl unlock-sessions >/dev/null 2>&1 || true; scripts/screen_watchdog.sh:183:notify "display-fix-1" "Surface display fix livello 1" "Tentato wake display/DPMS/unlock-session." 300
backup=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"; scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
migration=scripts/source_cleanup_analyzer.py:94:CREATE TABLE IF NOT EXISTS errors (
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=scripts/fix_mint_scaling_theme.sh:173:systemctl --user import-environment QT_AUTO_SCREEN_SCALE_FACTOR QT_ENABLE_HIGHDPI_SCALING QT_SCALE_FACTOR QT_SCREEN_SCALE_FACTORS DISPLAY XAUTHORITY XDG_CURRENT_DESKTOP XDG_SESSIO...; scripts/show_sc...
perf=systemd/freeze-reboot-monitor.service:16:Environment=FREEZE_REBOOT_MEMORY_GUARDIAN_ENABLED=1; systemd/freeze-reboot-monitor.service:17:Environment=FREEZE_GUARDIAN_MODE=active
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=systemd/mint-xfce-layout-guard.timer:12:WantedBy=timers.target; scripts/freeze_reboot_monitor.sh:23:DMESG_PATTERN='usb|uas|reset|disconnect|I/O error|Buffer I/O|ext4|jbd2|nvme|sda|sdb|sdc|dm-0|thermal|temperature|critical|watchdog|panic|...
paths=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"; scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
backup=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"; scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
restore=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"; scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
import=scripts/restore_mint_scaling_theme_backup.sh:20:printf 'Backup not readable: %s\n' "$BACKUP" >&2; scripts/fix_mint_scaling_theme.sh:173:systemctl --user import-environment QT_AUTO_SCREEN_SCALE_FACTOR QT_ENABLE_HIGHDPI_SCALING QT_SCALE_FA...
export=scripts/fix_mint_scaling_theme.sh:153:# GTK is governed by XFCE xsettings; do not export GDK_SCALE globally.; scripts/show_scaling_theme_status.sh:114:printf ' WARN: GDK_SCALE is exported; this can double-scale GTK under XFCE xsettings.\n'
migration=UNKNOWN
retention=scripts/source_cleanup_analyzer.py:56:def safe_rel(path: Path, source: Path) -> str:; scripts/source_cleanup_analyzer.py:130:"mode": "DELETE CONFIRMED" if delete_confirmed else "DRY-RUN",
DNB:
dnb=systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
dnb=systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Surface-recovery-hardening-keeps-backend-reachable --mode=block /usr/bin/sleep infinity
dnb=scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
dnb=scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
dnb=scripts/fix_mint_scaling_theme.sh:271:exec 9>"$LOCK"
dnb=scripts/fix_mint_scaling_theme.sh:272:if ! flock -n 9; then
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=scripts/fix_mint_scaling_theme.sh:346:log "error missing default panel XML: $DEFAULT_PANEL"
issue=scripts/freeze_reboot_monitor.sh:23:DMESG_PATTERN='usb|uas|reset|disconnect|I/O error|Buffer I/O|ext4|jbd2|nvme|sda|sdb|sdc|dm-0|thermal|temperature|critical|watchdog|panic|oom|killed process|hung task|blocked for mor...
RISK:
risk=systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
risk=systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Surface-recovery-hardening-keeps-backend-reachable --mode=block /usr/bin/sleep infinity
risk=scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
risk=scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
risk=scripts/fix_mint_scaling_theme.sh:271:exec 9>"$LOCK"
risk=scripts/fix_mint_scaling_theme.sh:272:if ! flock -n 9; then
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../surface-recovery-hardening/dev/project.metadata.json
human=../../human/projects/surface-recovery-hardening/overview.md
legacy=../../../surface-recovery-hardening/dev/legacy
repo=../../../surface-recovery-hardening
OPEN:
open=tests=UNKNOWN_OR_ABSENT
