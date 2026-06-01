META:
name=surface-recovery-hardening
slug=surface-recovery-hardening
path=/home/daniele/codex-workspace/surface-recovery-hardening
remote=git@github.com:gernalix/surface-recovery-hardening.git
branch=main
verified_commit=0868849
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Kit locale per rendere un Surface Pro con Linux Mint piu recuperabile durante trasferimenti USB pesanti:
STACK:
lang=Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=Chrome,Uptime Kuma,restic,systemd
MAP:
entry=UNKNOWN
core=configs/mint-xfce-layout-guard.desktop
core=dev/project.metadata.json
core=systemd/freeze-reboot-monitor.service
core=systemd/mint-xfce-layout-guard.service
core=systemd/mint-xfce-layout-guard.timer
core=systemd/surface_recovery_configs_no-suspend.service
core=systemd/surface_recovery_configs_remote-recovery-tmux.service
core=systemd/transfer-usb-io-watchdog.service
ui=scripts/fix_mint_scaling_theme.sh
ui=scripts/screen_watchdog.sh
ui=scripts/show_scaling_theme_status.sh
ui=systemd/surface_recovery_configs_screen-watchdog.service
db=scripts/restore_mint_scaling_theme_backup.sh
tests=UNKNOWN
scripts=configs/xrdp_startwm.sh
scripts=scripts/bundle_freeze_reboot_monitor_logs.sh
scripts=scripts/freeze_reboot_monitor.sh
scripts=scripts/low_memory_mode.sh
scripts=scripts/memory_pressure_guardian.sh
scripts=scripts/recovery_dump.sh
scripts=scripts/recovery_status.sh
scripts=scripts/remote_recovery_tmux.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- scripts/fix_mint_scaling_theme.sh=>add_path,xfconf_set,log,get_value,display0_panel_pids,physical_session_env_value,
- scripts/screen_watchdog.sh=>timestamp,now_s,log,event,event_limited,save_state,telegram_env_args
- scripts/show_scaling_theme_status.sh=>value
- scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
- scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
- scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:12:BACKUP="$(cat "$HOME/xfce_theme_scaling_latest_backup.txt")"
- scripts/restore_mint_scaling_theme_backup.sh:14:printf 'No backup specified and latest backup marker is missing.\n'
FLOW:
- scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
- scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
- scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:12:BACKUP="$(cat "$HOME/xfce_theme_scaling_latest_backup.txt")"
- scripts/restore_mint_scaling_theme_backup.sh:14:printf 'No backup specified and latest backup marker is missing.\n'
- scripts/restore_mint_scaling_theme_backup.sh:19:if [ ! -r "$BACKUP" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:20:printf 'Backup not readable: %s\n' "$BACKUP" >&2
- configs/mint-xfce-layout-guard.desktop:7:X-GNOME-Autostart-enabled=true
- systemd/freeze-reboot-monitor.service:5:StartLimitIntervalSec=0
- systemd/freeze-reboot-monitor.service:9:ExecStart=/home/daniele/freeze_reboot_monitor/freeze_reboot_monitor.sh --dae
- systemd/freeze-reboot-monitor.service:10:Restart=always
INV:
arch=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
arch=scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
arch=scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
arch=scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
arch=scripts/restore_mint_scaling_theme_backup.sh:12:BACKUP="$(cat "$HOME/xfce_theme_scaling_latest_backup.txt")"
arch=scripts/restore_mint_scaling_theme_backup.sh:14:printf 'No backup specified and latest backup marker is missing.
data=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
data=scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
data=scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
data=scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
data=scripts/restore_mint_scaling_theme_backup.sh:12:BACKUP="$(cat "$HOME/xfce_theme_scaling_latest_backup.txt")"
data=scripts/restore_mint_scaling_theme_backup.sh:14:printf 'No backup specified and latest backup marker is missing.
safety=systemd/mint-xfce-layout-guard.service:6:KillMode=process
safety=systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery harde
safety=systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why
safety=scripts/fix_mint_scaling_theme.sh:83:kill "$pid" >/dev/null 2>&1 // true
safety=scripts/fix_mint_scaling_theme.sh:89:pkill -u "$USER" xfconfd >/tmp/xfconfd-kill.log 2>&1 // true
safety=scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
safety=scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
ux=scripts/screen_watchdog.sh:182:loginctl unlock-sessions >/dev/null 2>&1 // true
ux=scripts/screen_watchdog.sh:183:notify "display-fix-1" "Surface display fix livello 1" "Tentato wake display/DPMS
ux=scripts/screen_watchdog.sh:223:if [[ "$low" =~ (gpu/i915/drm) ]] && [[ "$low" =~ (hang/reset/error/fail/timeout)
ux=scripts/screen_watchdog.sh:235:elif [[ "$low" =~ (bluetooth/btusb/hci0) ]] && [[ "$low" =~ (error/timeout/failed
version=dev/project.metadata.json:9:"metadata_version": 1,
version=scripts/rsync_uptime_kuma_push.sh:6:LOCK_FILE="/tmp/rsync_uptime_kuma_push.lock"
version=scripts/rsync_uptime_kuma_push.sh:11:CURL_CONNECT_TIMEOUT=3
version=scripts/rsync_uptime_kuma_push.sh:98:--connect-timeout "$CURL_CONNECT_TIMEOUT" \
i18n=UNKNOWN
BUILD:
- configs/xrdp_startwm.sh:1:#!/bin/sh
- scripts/bundle_freeze_reboot_monitor_logs.sh:1:#!/usr/bin/env bash
- scripts/freeze_reboot_monitor.sh:1:#!/usr/bin/env bash
- scripts/freeze_reboot_monitor.sh:19:MEMORY_GUARDIAN="$LOG_DIR/memory_pressure_guardian.sh"
- scripts/freeze_reboot_monitor.sh:24:JOURNAL_PATTERN='kernel/systemd/NetworkManager/upower/thermald/smartd/ssh/sshd/x
- scripts/freeze_reboot_monitor.sh:46:Stato periodico leggero: uptime, load, memoria, swap, temperatura, alimentazione
- scripts/freeze_reboot_monitor.sh:49:Eventi filtrati da dmesg e journal su freeze, reboot, USB/I/O, OOM, thermal, pan
- scripts/freeze_reboot_monitor.sh:61:Snapshot diagnostici creati su WARNING, CRITICAL, EMERGENCY e dal comando manual
- scripts/freeze_reboot_monitor.sh:67:/home/daniele/freeze_reboot_monitor/bundle_freeze_reboot_monitor_logs.sh
- scripts/freeze_reboot_monitor.sh:70:/home/daniele/freeze_reboot_monitor/low_memory_mode.sh
- scripts/low_memory_mode.sh:1:#!/usr/bin/env bash
- scripts/low_memory_mode.sh:5:GUARDIAN="${FREEZE_GUARDIAN_SCRIPT:-$LOG_DIR/memory_pressure_guardian.sh}"
TEST:
- UNKNOWN
DATA:
db=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
db=scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
db=scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
db=scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
db=scripts/restore_mint_scaling_theme_backup.sh:12:BACKUP="$(cat "$HOME/xfce_theme_scaling_latest_backup.txt")"
db=scripts/restore_mint_scaling_theme_backup.sh:14:printf 'No backup specified and latest backup marker is missing.
backup=scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
backup=scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
backup=scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
backup=scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
import=scripts/screen_watchdog.sh:148:import os, re, sys
import=scripts/freeze_reboot_monitor.sh:157:safe_cmd "important services" systemctl status freeze-reboot-monitor.servic
import=scripts/recovery_status.sh:20:from pathlib import Path
export=scripts/show_scaling_theme_status.sh:114:printf ' WARN: GDK_SCALE is exported; this can double-scale GTK under X
migration=UNKNOWN
retention=scripts/freeze_reboot_monitor.sh:103:find "$LOG_DIR" -maxdepth 1 -type f \( -name '*.log.*.gz' -o -name 'previou
retention=scripts/source_cleanup_analyzer.py:120:def __init__(self, state_dir: Path, source: Path, dest: Path, delete_conf
retention=scripts/source_cleanup_analyzer.py:126:self.delete_confirmed = delete_confirmed
DNB:
- systemd/mint-xfce-layout-guard.service:6:KillMode=process
- systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
- systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Sur
- scripts/fix_mint_scaling_theme.sh:83:kill "$pid" >/dev/null 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:89:pkill -u "$USER" xfconfd >/tmp/xfconfd-kill.log 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
- scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
- scripts/fix_mint_scaling_theme.sh:271:exec 9>"$LOCK"
- scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
- scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
BUG:
- scripts/fix_mint_scaling_theme.sh:325:log "error physical panel did not stay running; see /tmp/mint-xfce-layout-guar
- scripts/fix_mint_scaling_theme.sh:346:log "error missing default panel XML: $DEFAULT_PANEL"
- scripts/screen_watchdog.sh:2:set -Eeuo pipefail
- scripts/screen_watchdog.sh:25:RSYNC_WARN_LOG="${RSYNC_WARN_LOG:-/home/daniele/transfer_vecchio_disco_phase2_warnings
- scripts/screen_watchdog.sh:105:log "telegram failed: $title"
- scripts/screen_watchdog.sh:223:if [[ "$low" =~ (gpu/i915/drm) ]] && [[ "$low" =~ (hang/reset/error/fail/timeout) ]];
- scripts/screen_watchdog.sh:229:elif [[ "$low" =~ (usb/uas/sdb/dm-0) ]] && [[ "$low" =~ (reset/disconnect/i/o[[:space
- scripts/screen_watchdog.sh:235:elif [[ "$low" =~ (bluetooth/btusb/hci0) ]] && [[ "$low" =~ (error/timeout/failed/res
- scripts/bundle_freeze_reboot_monitor_logs.sh:2:set -Eeuo pipefail
- scripts/freeze_reboot_monitor.sh:2:set -Eeuo pipefail
RISK:
- systemd/mint-xfce-layout-guard.service:6:KillMode=process
- systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
- systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Sur
- scripts/fix_mint_scaling_theme.sh:83:kill "$pid" >/dev/null 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:89:pkill -u "$USER" xfconfd >/tmp/xfconfd-kill.log 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
- scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
- scripts/fix_mint_scaling_theme.sh:271:exec 9>"$LOCK"
- scripts/fix_mint_scaling_theme.sh:272:if ! flock -n 9; then
- scripts/fix_mint_scaling_theme.sh:357:kill "$pid" >/dev/null 2>&1 // true
ROAD:
now=scripts/screen_watchdog.sh:218:local line key low since next_epoch
next=scripts/screen_watchdog.sh:220:next_epoch="$(now_s)"
later=scripts/screen_watchdog.sh:243:LAST_DMESG_EPOCH="$next_epoch"
LINK:
meta=../../../surface-recovery-hardening/dev/project.metadata.json
human=../../human/projects/surface-recovery-hardening/overview.md
legacy=../../../surface-recovery-hardening/dev/legacy
repo=../../../surface-recovery-hardening
OPEN:
- no tests detected by static scan
