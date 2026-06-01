# surface-recovery-hardening Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `scripts/fix_mint_scaling_theme.sh`: add_path, xfconf_set, log, get_value, display0_panel_pids, physical_session_env_value, start_display0_panel
- `scripts/screen_watchdog.sh`: timestamp, now_s, log, event, event_limited, save_state, telegram_env_args, notify
- `scripts/show_scaling_theme_status.sh`: value
- `scripts/freeze_reboot_monitor.sh`: timestamp, stamp_file, ensure_layout, write_readme, log_event, rotate_one, rotate_logs, safe_cmd
- `scripts/low_memory_mode.sh`: timestamp, log, cmdline_for_pid, is_gradle_pid
- `scripts/memory_pressure_guardian.sh`: timestamp, stamp_file, usage, log, run_or_log, meminfo_mb, psi_value_hundredths, decimal_to_hundredths
- `scripts/recovery_dump.sh`: run
- `scripts/recovery_status.sh`: once
- `scripts/remote_recovery_tmux.sh`: ensure_window, ensure_session
- `scripts/rsync_uptime_kuma_push.sh`: log, read_state, write_state, cmdline_for_pid, is_target_rsync_cmdline, proc_state, rsync_active, push_kuma
- `scripts/source_cleanup_analyzer.py`: StopRequested, RunState, request_stop, now_iso, gb, safe_rel, atomic_write_json, open_db
- `scripts/surface_recovery_rollback.sh`: log, restore_file
- `scripts/transfer_usb_io_diag.sh`: run
- `scripts/transfer_usb_io_watchdog.sh`: timestamp, now_s, log, save_state, sanitize_output, run_root, cmdline_for_pid, is_target_rsync_cmdline
- `scripts/transfer_vecchio_disco_adaptive_throttle.sh`: log, run_root, cmdline_for_pid, is_target_rsync_cmdline, unique_lines, target_rsync_pids, current_bwlimit, meminfo_mb
- `scripts/transfer_vecchio_disco_phase2_limited.sh`: timestamp, log_full, decode_findmnt_target, mountpoint_for_source, resolve_destination_device, write_status, classify_rsync_line
- `scripts/transfer_vecchio_disco_recovery_commands.sh`: usage, cmdline_for_pid, is_target_rsync_cmdline, target_rsync_pids, run_root, assert_no_running_rsync, status, pause_rsync

## Confini operativi
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
