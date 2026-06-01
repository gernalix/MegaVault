# surface-recovery-hardening Roadmap

## Segnali dal codice
- scripts/screen_watchdog.sh:218:local line key low since next_epoch
- scripts/screen_watchdog.sh:220:next_epoch="$(now_s)"
- scripts/screen_watchdog.sh:243:LAST_DMESG_EPOCH="$next_epoch"
- scripts/memory_pressure_guardian.sh:310:[[ "$lcomm" =~ ^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$ // "$lcmd" == *"node "* // "$lcmd" == *"python"* ]] // return 1
- scripts/memory_pressure_guardian.sh:333:if (pid !~ /^[0-9]+$/ // rss !~ /^[0-9]+$/) next
- scripts/memory_pressure_guardian.sh:339:if (protected_process(pid, lcomm, lcmd)) next
- scripts/memory_pressure_guardian.sh:347:} else if (rss_mb >= codex_min && lcmd ~ /codex/ && (lcomm ~ /^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$/ // lcmd ~ /node /
- scripts/source_cleanup_analyzer.py:2:from __future__ import annotations
- scripts/transfer_usb_io_watchdog.sh:225:next_epoch="$(now_s)"
- scripts/transfer_usb_io_watchdog.sh:233:LAST_DMESG_EPOCH="$next_epoch"
- scripts/transfer_vecchio_disco_dashboard.sh:4:from __future__ import annotations
- scripts/transfer_vecchio_disco_phase2_limited.sh:113:next

## Debito/rischi da considerare
- scripts/fix_mint_scaling_theme.sh:325:log "error physical panel did not stay running; see /tmp/mint-xfce-layout-guard-panel-start.log"
- scripts/fix_mint_scaling_theme.sh:346:log "error missing default panel XML: $DEFAULT_PANEL"
- scripts/screen_watchdog.sh:2:set -Eeuo pipefail
- scripts/screen_watchdog.sh:25:RSYNC_WARN_LOG="${RSYNC_WARN_LOG:-/home/daniele/transfer_vecchio_disco_phase2_warnings_errors.log}"
- scripts/screen_watchdog.sh:105:log "telegram failed: $title"
- scripts/screen_watchdog.sh:223:if [[ "$low" =~ (gpu/i915/drm) ]] && [[ "$low" =~ (hang/reset/error/fail/timeout) ]]; then
- scripts/screen_watchdog.sh:229:elif [[ "$low" =~ (usb/uas/sdb/dm-0) ]] && [[ "$low" =~ (reset/disconnect/i/o[[:space:]]error/error/failed/abort/offline) ]]; then
- scripts/screen_watchdog.sh:235:elif [[ "$low" =~ (bluetooth/btusb/hci0) ]] && [[ "$low" =~ (error/timeout/failed/reset/unexpected) ]]; then
- systemd/mint-xfce-layout-guard.service:6:KillMode=process
- systemd/surface_recovery_configs_no-suspend.service:2:Description=Block sleep/idle during Surface recovery hardening
- systemd/surface_recovery_configs_no-suspend.service:8:ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle --why=Surface-recovery-hardening-keeps-backend-reachable --mode=block /us
- scripts/fix_mint_scaling_theme.sh:83:kill "$pid" >/dev/null 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:89:pkill -u "$USER" xfconfd >/tmp/xfconfd-kill.log 2>&1 // true
- scripts/fix_mint_scaling_theme.sh:260:LOCK="$HOME/.cache/mint-xfce-layout-guard.lock"
