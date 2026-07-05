META:
name=mint-cloud-backup
slug=mint-cloud-backup
path=/home/daniele/codex-projects/mint-cloud-backup
remote=none
branch=master
verified_commit=8f0fe06
verified_at=2026-06-02T06:54:28+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2

PURPOSE:
purpose=Linux Mint root filesystem backup to Backblaze B2 via restic, with local health monitor, localhost dashboard, and Uptime Kuma push heartbeat.

STACK:
lang=Bash,Python
tools=restic,Backblaze B2,systemd,Uptime Kuma,jq,curl,NetworkManager
platform=Linux Mint host
db=none; state JSON under /var/lib/mint-cloud-backup
secrets=/etc/mint-cloud-backup/restic.env,/etc/mint-cloud-backup/uptime-kuma.env

MAP:
entry=mint-cloud-backup
monitor=mint-cloud-backup-monitor
dashboard=mint-cloud-backup-dashboard
kuma=scripts/uptime-kuma-push.sh
systemd=systemd/mint-cloud-backup.service,systemd/mint-cloud-backup.timer,systemd/mint-cloud-backup-monitor.service,systemd/mint-cloud-backup-dashboard.service,systemd/mint-cloud-backup-kuma-push.service,systemd/mint-cloud-backup-kuma-push.timer
docs=docs/README_CODEX.md,docs/OPERATIONS.md,docs/TROUBLESHOOTING.md
status=scripts/restic-backblaze-status.sh
avoid=secrets,tokens,real Uptime Kuma push URL,restic prune/forget/unlock/check unless explicitly approved

ARCH:
runner=/usr/local/bin/mint-cloud-backup; repo copy=mint-cloud-backup
runner_behavior=Type=oneshot; safe inactive/dead after success; active/activating during backup
timer=mint-cloud-backup.timer daily randomized delay
monitor=/usr/local/bin/mint-cloud-backup-monitor; long-running system service; writes health.json
dashboard=/usr/local/bin/mint-cloud-backup-dashboard; localhost 127.0.0.1:8765; read-only status surface
kuma_push=/usr/local/bin/mint-cloud-backup-kuma-push; oneshot timer; reads dashboard/status JSON; never starts backups
kuma_push_482917=single-run flock lock; dashboard JSON must be object; empty/null message becomes explicit status_json_unexpected_shape; system timer every 2min; Kuma monitor id=3 interval=180 timeout=60 maxretries=2 tags=482917-reviewed,push-monitor
lock_local=/run/lock/mint-cloud-backup.lock via flock
lock_remote=restic repo locks; diagnostic only; unlock only after no live restic backup

FLOW:
backup=timer/manual -> mint-cloud-backup.service -> mint-cloud-backup -> restic backup / --one-file-system -> Backblaze B2
progress=restic JSON -> progress-*.jsonl -> progress.json -> dashboard/status/Kuma
health=monitor -> restic list locks/snapshots read-only + systemctl state -> health.json
kuma=timer -> dashboard /api/status else status files -> push URL from /etc/mint-cloud-backup/uptime-kuma.env
manual_check=scripts/restic-backblaze-status.sh -> reports/restic-backblaze-status-*.md

INV:
arch=single backup runner; no parallel backup mechanism
backup=do not start duplicate if restic backup / is live
backup=local flock prevents duplicate local runner
backup=remote stale lock must be proven stale before unlock
security=never print restic env or Kuma push URL
security=env files must remain root-only mode 600
data=state JSON/logs are diagnostic; backup data lives in remote restic repository
ops=storage cap/auth/remote lock are not retry-by-reflex conditions
ops=Kuma outage must not block/restart/duplicate backup
ops=Kuma monitor id 3 is active; expected heartbeat is idle/running/degraded/critical from the dedicated pusher, not from the backup runner
version=verified_commit 8f0fe06 includes #739284 hardening

BUILD:
cmd=none
install=copy repo scripts to /usr/local/bin and units to /etc/systemd/system only when explicitly changing runtime
requirements=restic,jq,curl,python3,systemd,NetworkManager

TEST:
static=bash -n mint-cloud-backup mint-cloud-backup-monitor scripts/uptime-kuma-push.sh
python=python3 -m py_compile mint-cloud-backup-dashboard
dryrun=sudo /usr/local/bin/mint-cloud-backup-kuma-push --dry-run
health=sudo sh -c '. /etc/mint-cloud-backup/restic.env; export RESTIC_REPOSITORY RESTIC_PASSWORD B2_ACCOUNT_ID B2_ACCOUNT_KEY RESTIC_CACHE_DIR=/var/cache/mint-cloud-backup/restic; restic cat config >/dev/null'
status=systemctl status mint-cloud-backup.service mint-cloud-backup.timer mint-cloud-backup-monitor.service mint-cloud-backup-dashboard.service mint-cloud-backup-kuma-push.timer --no-pager

DATA:
DB=none
State=/var/lib/mint-cloud-backup
Logs=/var/log/mint-cloud-backup
Cache=/var/cache/mint-cloud-backup/restic
Progress=/var/lib/mint-cloud-backup/progress.json,/var/lib/mint-cloud-backup/progress-*.jsonl
Health=/var/lib/mint-cloud-backup/health.json
DashboardState=/var/lib/mint-cloud-backup/dashboard-status.json
KumaState=/var/lib/mint-cloud-backup/uptime-kuma-push-state.json
Summary=/var/lib/mint-cloud-backup/last-backup-summary.json
Env=/etc/mint-cloud-backup/restic.env
KumaEnv=/etc/mint-cloud-backup/uptime-kuma.env
Report=reports/restic-backblaze-status-*.md
Backup=remote restic repository in Backblaze B2
Restore=RESTORE.md; verify before use
Import=none
Export=none
Migration=none
Retention=UNKNOWN; do not prune without explicit approval

DNB:
* live backup service and timers during docs-only work
* /etc/mint-cloud-backup/restic.env
* /etc/mint-cloud-backup/uptime-kuma.env token
* restic repository locks unless stale proven
* existing Backblaze B2 repository data
* Kuma push URL secrecy

BUG:
issue=#739284 cloud backup DOWN / KUMA cloud backup FAILED
root_cause=false auth classification from restic JSONL current_files path containing authentication/authorization text; actual unread source was /home/daniele/.gvfs; remote stale restic lock remained after failed run
fix=exclude /home/*/.gvfs; classify restic exit 3 with valid snapshot as DEGRADED; filter status/summary JSON before auth regex; count only restic backup / as active backup; robust Kuma env parsing and heartbeat messages
status=post-fix backup restarted controlled; Kuma heartbeat running/up verified; no credentials changed
issue=#482917 cloud backup Kuma flapping
root_cause=push timer and monitor window were too tight for dashboard/status collection; overlapping oneshots and non-object dashboard JSON could emit blank/noisy messages
fix=flock around pusher, object-only dashboard JSON, explicit fallback message, timer set to 2min, Kuma monitor interval 180s timeout 60s retries 2
status=2026-06-06 active/up; dry-run shows backup=idle last_snapshot=cbba8d42 monitor=ok timer=active

RISK:
risk=restic unlock/prune/forget/check can damage or heavily mutate backup repo if run casually
risk=Kuma DOWN may reflect local degraded state, stale lock, push timeout, or real backup failure; diagnose locally first
risk=words inside backed-up file paths can look like auth errors; classify only actual error lines
risk=service active state can be activating/start for long oneshot backups
risk=source virtual paths such as .gvfs can cause restic exit 3 even with snapshot created

ROAD:
now=registered in MegaVault after #739284; #482917 Kuma noise hardening active
next=keep docs aligned when runtime scripts/systemd units change
later=define reviewed retention/prune policy if operator requests it

LINK:
meta=../../../../codex-projects/mint-cloud-backup/dev/project.metadata.json
human=../../human/projects/mint-cloud-backup/overview.md
changelog=../../human/projects/mint-cloud-backup/changelog.md
legacy=../../../../codex-projects/mint-cloud-backup/docs
repo=../../../../codex-projects/mint-cloud-backup

OPEN:
open=no git remote configured
open=no automated runtime tests beyond syntax/py_compile/dry-run/status checks
open=retention/prune policy intentionally UNKNOWN
