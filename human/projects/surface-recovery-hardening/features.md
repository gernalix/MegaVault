# surface-recovery-hardening Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/docs/ARCHITECTURE.md: ## Failure Model
- dev/legacy/docs/TROUBLESHOOTING.md: ## UAS Quirks
- dev/legacy/reports/display_theme_scaling_report_v2.txt: SESSION UID USER SEAT TTY STATE IDLE SINCE
- dev/legacy/reports/display_theme_scaling_report_v2.txt: # ~/.profile: executed by the command interpreter for login shells.
- dev/legacy/reports/REPORT_v4_usb_io_hardening.md: ## Rischi Residui
- dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md: ## Recovery Commands Created
- dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md: ## Services Touched
- dev/legacy/docs/OPERATIONS.md: /home/daniele/transfer_vecchio_disco_dashboard.sh --once
- dev/legacy/reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_af_rsync_required.txt: 84085 /bin/bash -c set -euo pipefail logdir=$(cat /tmp/prompt418_logdir) kill -TERM 63966 2>/dev/null // true sleep 1 pgrep -af rsync > "$logdir/pre_start_pgre
- dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_mapper_lsblk_after_open.txt: NAME FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS
- dev/legacy/reports/prompt684_did_error_20260514_070407/user_services_status.txt: ● transfer-vecchio-disco-adaptive-throttle.service - Adaptive conservative throttle for transfer_vecchio_disco phase 2
- dev/legacy/reports/prompt734_post_crash_20260510_222255/dmesg_filtered_usb_io_before_quirk.txt: [Sun May 10 22:16:01 2026] Command line: BOOT_IMAGE=/boot/vmlinuz-6.19.8-surface-3 root=UUID=a4bf0d13-b036-490e-9a14-aea83baf37a6 ro quiet splash rootdelay=10 i915.
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 07:05:13 daniele-Surface-Pro kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-6.19.8-surface-2 root=UUID=a4bf0d13-b036-490e-9a14-aea83baf37a6 ro quiet splash
- configs/xrdp_startwm.sh: if command -v startxfce4 >/dev/null 2>&1; then

## Useful Limits And Boundaries
- dev/legacy/README.md: abort journal, read-only filesystem, errori xHCI/UAS, oppure reset USB ripetuti
- dev/legacy/README.md: 5. Se appaiono `read-only filesystem`, `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect, fermare solo dopo decisione esplicita e pianificare recovery offline.
- dev/legacy/README.md: Il rollback ripristina i backup in `/home/daniele/surface_recovery_backups/...`, rimuove i servizi recovery e rigenera GRUB.
- dev/legacy/docs/ARCHITECTURE.md: - source disk: Seagate Expansion `0bc2:2322`, internal model `ST4000LM024-2AN17V`, serial `WFF0FEX8`, USB path `2-1.2`, driver `usb-storage`, BitLocker mapper mounted read-only at `/media/daniele/Seagate Expansion Drive`.
- dev/legacy/docs/ARCHITECTURE.md: Safety invariants:
- dev/legacy/docs/ARCHITECTURE.md: - source mount is read-only;
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_phase2_limited.sh`: rsync launcher and UUID safety gate.
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_recovery_commands.sh`: explicit recovery command entrypoint. It prepares resume but never runs it unless called with `resume`.
- dev/legacy/docs/TROUBLESHOOTING.md: - less likely: filesystem corruption, because ext4 stayed mounted read-write and no `JBD2 abort`, `EXT4-fs error`, read-only remount or disconnect was observed;
- dev/legacy/docs/TROUBLESHOOTING.md: journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed'
- dev/legacy/docs/TROUBLESHOOTING.md: 4. If only USB reset plus read error is present and mounts remain healthy, do not fsck live. Keep stopped or resume only after operator decision.
- dev/legacy/docs/TROUBLESHOOTING.md: Do not send `SIGCONT` while the operator instruction says rsync must stay stopped.

## Where The Feature Code Appears To Live
- `scripts/source_cleanup_analyzer.py`
- `configs/xrdp_startwm.sh`
- `scripts/bundle_freeze_reboot_monitor_logs.sh`
- `scripts/fix_mint_scaling_theme.sh`
- `scripts/freeze_reboot_monitor.sh`
- `scripts/low_memory_mode.sh`
- `scripts/memory_pressure_guardian.sh`
- `scripts/mint-xfce-layout-guard`
- `scripts/recovery_dump.sh`
- `scripts/recovery_status.sh`
- `scripts/remote_recovery_tmux.sh`
- `scripts/restore_mint_scaling_theme_backup.sh`
- `scripts/rsync_uptime_kuma_push.sh`
