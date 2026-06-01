# surface-recovery-hardening Troubleshooting

## Problemi e sintomi rilevati nel codice
- scripts/fix_mint_scaling_theme.sh:325:log "error physical panel did not stay running; see /tmp/mint-xfce-layout-guard-panel-start.log"
- scripts/fix_mint_scaling_theme.sh:346:log "error missing default panel XML: $DEFAULT_PANEL"
- scripts/screen_watchdog.sh:2:set -Eeuo pipefail
- scripts/screen_watchdog.sh:25:RSYNC_WARN_LOG="${RSYNC_WARN_LOG:-/home/daniele/transfer_vecchio_disco_phase2_warnings_errors.log}"
- scripts/screen_watchdog.sh:105:log "telegram failed: $title"
- scripts/screen_watchdog.sh:223:if [[ "$low" =~ (gpu/i915/drm) ]] && [[ "$low" =~ (hang/reset/error/fail/timeout) ]]; then
- scripts/screen_watchdog.sh:229:elif [[ "$low" =~ (usb/uas/sdb/dm-0) ]] && [[ "$low" =~ (reset/disconnect/i/o[[:space:]]error/error/failed/abort/offline) ]]; then
- scripts/screen_watchdog.sh:235:elif [[ "$low" =~ (bluetooth/btusb/hci0) ]] && [[ "$low" =~ (error/timeout/failed/reset/unexpected) ]]; then
- scripts/bundle_freeze_reboot_monitor_logs.sh:2:set -Eeuo pipefail
- scripts/freeze_reboot_monitor.sh:2:set -Eeuo pipefail
- scripts/freeze_reboot_monitor.sh:23:DMESG_PATTERN='usb/uas/reset/disconnect/I/O error/Buffer I/O/ext4/jbd2/nvme/sda/sdb/sdc/dm-0/thermal/temperature/critical/watchdog/panic/oom/kil
- scripts/freeze_reboot_monitor.sh:24:JOURNAL_PATTERN='kernel/systemd/NetworkManager/upower/thermald/smartd/ssh/sshd/xrdp/rsync/watchdog/transfer/usb/uas/reset/disconnect/I/O error/B
- scripts/freeze_reboot_monitor.sh:116:"$@" 2>&1 // printf 'command failed: %q\n' "$*"
- scripts/freeze_reboot_monitor.sh:156:safe_cmd "systemd failed units" systemctl --failed --no-pager
- scripts/freeze_reboot_monitor.sh:189:printf '\n-- reboot/shutdown/crash lines --\n'
- scripts/freeze_reboot_monitor.sh:190:last -x 2>/dev/null / grep -Ei 'reboot/shutdown/crash/still running' / head -80 // printf 'no reboot/shutdown/crash lines found by last -x\n'
- scripts/freeze_reboot_monitor.sh:314:log_event "memory guardian failed rc=$? mode=$MEMORY_GUARDIAN_MODE"
- scripts/low_memory_mode.sh:2:set -Eeuo pipefail

## Comandi/verifiche utili trovati
- configs/xrdp_startwm.sh:1:#!/bin/sh
- scripts/bundle_freeze_reboot_monitor_logs.sh:1:#!/usr/bin/env bash
- scripts/freeze_reboot_monitor.sh:1:#!/usr/bin/env bash
- scripts/freeze_reboot_monitor.sh:19:MEMORY_GUARDIAN="$LOG_DIR/memory_pressure_guardian.sh"
- scripts/freeze_reboot_monitor.sh:24:JOURNAL_PATTERN='kernel/systemd/NetworkManager/upower/thermald/smartd/ssh/sshd/xrdp/rsync/watchdog/transfer/usb/uas/reset/disconnect/I/O error/B
- scripts/freeze_reboot_monitor.sh:46:Stato periodico leggero: uptime, load, memoria, swap, temperatura, alimentazione, dischi, processi top, rsync/transfer/watchdog, lsblk e mount s
- scripts/freeze_reboot_monitor.sh:49:Eventi filtrati da dmesg e journal su freeze, reboot, USB/I/O, OOM, thermal, panic, systemd, rsync e watchdog.
- scripts/freeze_reboot_monitor.sh:61:Snapshot diagnostici creati su WARNING, CRITICAL, EMERGENCY e dal comando manuale low_memory_mode.sh.
- scripts/freeze_reboot_monitor.sh:67:/home/daniele/freeze_reboot_monitor/bundle_freeze_reboot_monitor_logs.sh
- scripts/freeze_reboot_monitor.sh:70:/home/daniele/freeze_reboot_monitor/low_memory_mode.sh
- scripts/low_memory_mode.sh:1:#!/usr/bin/env bash
- scripts/low_memory_mode.sh:5:GUARDIAN="${FREEZE_GUARDIAN_SCRIPT:-$LOG_DIR/memory_pressure_guardian.sh}"
- scripts/low_memory_mode.sh:36:[[ "$lower_cmd" == *"org.gradle.launcher.daemon"* // "$lower_cmd" == *"gradledaemon"* // "$lower_cmd" == *"/gradle "* // "$lower_cmd" == *" gradle "* 
- scripts/low_memory_mode.sh:43:log "active rsync processes will not be touched:"
- scripts/low_memory_mode.sh:44:if mapfile -t rsync_pids < <(pgrep -x rsync 2>/dev/null) && ((${#rsync_pids[@]})); then
- scripts/low_memory_mode.sh:57:if command -v gradle >/dev/null 2>&1; then

## Safety prima di correggere
- systemd/mint-xfce-layout-guard.service:6:KillMode=process
- systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
- systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Surface-recovery-hardening-keeps-backend-reachable --mode=block /us
- scripts/fix_mint_scaling_theme.sh:83:kill "$pid" >/dev/null 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:89:pkill -u "$USER" xfconfd >/tmp/xfconfd-kill.log 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
- scripts/fix_mint_scaling_theme.sh:269:mkdir -p "$(dirname "$LOG")" "$(dirname "$LOCK")" "$BACKUP_DIR"
- scripts/fix_mint_scaling_theme.sh:271:exec 9>"$LOCK"
- scripts/restore_mint_scaling_theme_backup.sh:5:printf 'Usage: %s [backup.tar.gz]\n' "$0"
- scripts/restore_mint_scaling_theme_backup.sh:9:BACKUP="${1:-}"
- scripts/restore_mint_scaling_theme_backup.sh:10:if [ -z "$BACKUP" ]; then
- scripts/restore_mint_scaling_theme_backup.sh:11:if [ -r "$HOME/xfce_theme_scaling_latest_backup.txt" ]; then
