META:
name=surface-recovery-hardening
slug=surface-recovery-hardening
path=/home/daniele/codex-workspace/surface-recovery-hardening
remote=git@github.com:gernalix/surface-recovery-hardening.git
branch=main
verified_commit=a7d791d
verified_at=2026-06-03T01:37:21+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Linux Mint Surface recovery + rsync-transfer operations for Seagate 4TB BitLocker -> Seagate6TB2 ext4 copy.
STACK:
lang=Shell,Python
db=SQLite for source_cleanup_analyzer only
platform=Linux Mint/XFCE,systemd,user-systemd,USB storage,Uptime Kuma
tools=cryptsetup bitlk,ntfs-3g/fuseblk,rsync,systemd-run,journalctl,findmnt,lsblk,lsusb
MAP:
entry=/home/daniele/transfer_vecchio_disco_phase2_limited.sh
ui=/home/daniele/transfer_vecchio_disco_dashboard.sh
core=scripts/transfer_vecchio_disco_recovery_commands.sh,scripts/transfer_usb_io_watchdog.sh,scripts/transfer_vecchio_disco_adaptive_throttle.sh,scripts/rsync_uptime_kuma_push.sh
db=scripts/source_cleanup_analyzer.py
tests=UNKNOWN
scripts=scripts/transfer_vecchio_disco_phase2_limited.sh,scripts/transfer_vecchio_disco_recovery_commands.sh,scripts/transfer_usb_io_watchdog.sh,scripts/transfer_vecchio_disco_adaptive_throttle.sh,scripts/rsync_uptime_kuma_push.sh
build=UNKNOWN
avoid=secrets,tokens,cookies,generated reports,untracked .codexmeta backups
ARCH:
transfer_logic=/home/daniele/transfer_vecchio_disco_phase2_limited.sh -> sudo -> rsync --append-verify
dashboard_unit=transfer-vecchio-disco-adaptive-throttle.service is the visible/monitored user systemd unit for the dashboard transfer card
historical=rsync-transfer.service was transient systemd-run unit; 2026-06-10 static alias removed again to eliminate dashboard/systemctl ambiguity
support_system=transfer-usb-io-watchdog.service(enabled):kernel USB/I/O monitor; pauses target rsync on transfer-storage critical events
support_user=rsync-uptime-kuma-push.service(disabled 2026-06-06 #482917): old Kuma heartbeat for exact target rsync cmdline; no live rsync-transfer runner/source verified during Kuma cleanup
support_user=transfer-vecchio-disco-adaptive-throttle.service(enabled):renice/ionice/bw profile control
manual_cmd=rsync-transfer-start:/home/daniele/.local/bin/rsync-transfer-start starts transfer-vecchio-disco-adaptive-throttle.service only
manual_status=rsync-transfer-status:/home/daniele/.local/bin/rsync-transfer-status prints throttle systemd state, PID, target rsync process, throughput/stale reason
anti_freeze_removed=2026-06-07 prompt_847261 removed screen-watchdog/freeze-reboot-monitor legacy artifacts; transfer-usb-io-watchdog.service intentionally remains enabled as rsync safety guard, not generic anti-freeze
mount_dest=media-daniele-Seagate6TB2.automount(enabled)+.mount(disabled,triggered)
mount_source=cryptsetup open --type bitlk --readonly /dev/sdb2 source_bitlocker; mount ro at /media/daniele/Seagate Expansion Drive
FLOW:
preflight=read metadata+AI doc; verify no active target rsync; verify SOURCE mapper ro; verify DEST uuid rw; scan recent kernel USB/I/O
start=systemctl --user start transfer-vecchio-disco-adaptive-throttle.service; this starts/keeps throttle service only and does not start rsync copy logic
rsync=source:/media/daniele/Seagate Expansion Drive/ -> dest:/media/daniele/Seagate6TB2/vecchio disco/
resume=append-verify; verify mapping+ext4 clean+no recent transfer-storage error; SIGCONT paused target pids; launcher rerun exits 0 via lock
monitor=journalctl + transfer logs + Kuma dry-run health + pgrep exact cmdline
ops_cmd=rsync-transfer-start verifies transfer-vecchio-disco-adaptive-throttle.service; prints before/after systemctl show; systemctl --user start is idempotent and does not create rsync workers
INV:
backup=source BitLocker must be mounted read-only; never write source
data=destination UUID must be 75e5363d-6736-4a7e-84be-5242f4735a27
data=findmnt -T can return root or automount wrapper; reject / and select real last mount row
arch=no rsync-transfer.service installed; dashboard/service truth is transfer-vecchio-disco-adaptive-throttle.service; support watchdog/throttle services are persistent; Kuma pusher remains disabled obsolete
watchdog=usb 1-5 Marvell WLAN disconnect is non-transfer; must not pause rsync
kuma_482917=Kuma monitor id=2 `rsync-transfer` disabled as obsolete/no active transfer; service reset to inactive/dead disabled; tags=482917-reviewed,push-monitor,obsolete-disabled
security=do not print BitLocker key or Kuma push URL
perf=default BW_LIMIT=5120 KiB/s; timeout=900; nice=19; ionice low priority
recovery=critical USB/I/O events pause target rsync; do not auto-resume after storage error
version=repo commits 3f455ea+2bcbd5a+6c3868c+a7d791d fix mapping validation,Kuma health,watchdog filtering
BUILD:
cmd=UNKNOWN
env=sudo -n required; key file local only; user systemd active; source/dest USB present
requirements=cryptsetup bitlk,ntfs/fuseblk mount support,rsync,systemd user session
TEST:
syntax=bash -n transfer_vecchio_disco_recovery_commands.sh
smoke=transfer_vecchio_disco_recovery_commands.sh verify-mapping
integration=UNKNOWN
runtime=systemctl --user status transfer-vecchio-disco-adaptive-throttle.service; rsync-transfer-status; DRY_RUN=1 RUN_ONCE=1 LOCK_FILE=/tmp/rsync_uptime_kuma_push_check.lock rsync_uptime_kuma_push.sh
DATA:
SourceDev=/dev/sdb2 BitLocker ST4000LM024-2AN17V serial=WFF0FEX8
SourceMapper=/dev/mapper/source_bitlocker readonly
SourceMount=/media/daniele/Seagate Expansion Drive fuseblk ro
DestDev=/dev/sdc1 ext4 label=Seagate6TB serial=ZCT3KG54
DestMount=/media/daniele/Seagate6TB2 rw,noatime
DestDir=/media/daniele/Seagate6TB2/vecchio disco
UnitThrottle=/home/daniele/.config/systemd/user/transfer-vecchio-disco-adaptive-throttle.service ExecStart=/home/daniele/transfer_vecchio_disco_adaptive_throttle.sh enabled
ManualStart=/home/daniele/.local/bin/rsync-transfer-start
ManualStatus=/home/daniele/.local/bin/rsync-transfer-status
Logs=/home/daniele/transfer_vecchio_disco_phase2.log,/home/daniele/transfer_vecchio_disco_phase2_warnings_errors.log,/home/daniele/rsync_uptime_kuma_push.log,/home/daniele/transfer_usb_io_watchdog.log,/home/daniele/transfer_vecchio_disco_adaptive_throttle.log
State=/home/daniele/transfer_vecchio_disco_phase2_status.env,/home/daniele/transfer_vecchio_disco_phase2_rsync.pid,/home/daniele/transfer_vecchio_disco_phase2_script.pid,/home/daniele/.rsync_uptime_kuma_push.state
Backup=/home/daniele/transfer_vecchio_disco_recovery_commands.sh.bak-20260601-141559,/home/daniele/rsync_uptime_kuma_push.sh.bak-20260601-142223,/home/daniele/transfer_usb_io_watchdog.sh.bak-20260603-013451
DNB:
dnb=do not create persistent rsync-transfer.service duplicate
dnb=do not use rsync --delete
dnb=do not classify helper-only rsync_uptime_kuma_push as data transfer
dnb=do not trust findmnt -T if it resolves source path to /
dnb=do not restart after recent DEST USB/I/O/JBD2/EXT4 errors without storage verification
dnb=do not disable transfer-usb-io-watchdog.service under generic anti-freeze cleanup; it is transfer data-safety guard
dnb=never commit secrets or local reports/backups unless explicitly scoped
BUG:
issue=verify-mapping failed under DEST automount because findmnt returned systemd-1 and /dev/sdc1 rows
cause=script compared multiline UUID/SOURCE as single value
fix=3f455ea selects real final mount row and validates source mapper
issue=unmount_safe only closed old bitlk mapper name
fix=3f455ea closes source_bitlocker and legacy mapper if active
issue=Kuma pusher returned down log_stale while rsync was alive and scanning without progress log writes
fix=2bcbd5a treats stale-log rsync as up when exact target pid gains CPU ticks and mounts remain safe
issue=Kuma pusher exited on curl rc=7/28 before logging nonfatal push failure
fix=6c3868c wraps curl with set +e/set -e and returns success after logging failure
issue=watchdog paused transfer on usb 1-5 Marvell WLAN disconnect
cause=usb disconnect matched broad critical regex without transfer-storage context
fix=a7d791d gates usb disconnect/reset pause to transfer storage markers or usb 2-1.[123]; Telegram notify nonfatal under set -e
RISK:
risk=multi-TB USB transfer stresses hub/cable/controller; watch kernel USB/I/O
risk=stale pid/status/log files can survive crash; require live /proc cmdline validation
risk=Kuma push service may restart on network timeout; runtime dry-run health verifies local truth
risk=disabled rsync-transfer Kuma monitor must not be used as transfer health evidence; verify live transfer process/mounts before re-enabling
risk=source key exists locally; path may be documented, value must not
test_2026-06-10=rsync-transfer-start starts/keeps throttle service active/running pid=1186; rsync-transfer-status reports process=absent,current_throughput=stale,metrics_status=stale/no live rsync process; no rsync started
ROAD:
now=rsync-transfer Kuma pusher disabled after #482917 cleanup; before any future transfer, verify source/dest/process and re-enable only if the transfer is intentionally active
next=consider persistent documented helper for source read-only mount only if repeated manual remounts continue
later=clean generated legacy reports from repo policy if user requests
LINK:
meta=../../../surface-recovery-hardening/dev/project.metadata.json
human=../../human/projects/surface-recovery-hardening/overview.md
legacy=../../../surface-recovery-hardening/dev/legacy
repo=../../../surface-recovery-hardening
OPEN:
open=tests absent
open=source BitLocker currently not mounted; no rsync-transfer.service installed by design
