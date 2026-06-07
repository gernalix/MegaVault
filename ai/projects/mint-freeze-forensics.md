META:
name=mint-freeze-forensics
slug=mint-freeze-forensics
path=/home/daniele/codex-workspace/mint-freeze-forensics
repo=/home/daniele/codex-workspace/mint-freeze-forensics
branch=main
prompt=847261
created=2026-06-07
protocol=MEGAVAULT_PROTOCOL.md:v4
PURPOSE:
purpose=Linux Mint freeze forensics + early warning + Kuma telemetry
mode=observability_only
no_auto=reboot,restart,kill,os_tuning
STACK:
lang=Python3 stdlib
service=user systemd
state=~/.local/state/mint-freeze-forensics
config=~/.config/mint-freeze-forensics
kuma=Oracle VM Uptime Kuma push monitors
MAP:
entry=mint_freeze_forensics.py
ui=guardian CLI prompt [K]/[I]/[W]/[D]
core=snapshot(),record_sample(),daemon(),guardian(),human_report(),io_report(),recent(),weekly_report(),dashboard_summary(),score_event_causes()
db=JSONL ring buffer + compact history
tests=py_compile,sample,io-report,recent,dashboard-json,simulate-gap,guardian --simulate-alert,human-report,systemd start/stop/restart
scripts=systemd/user/*.service,systemd/user/*.timer,docs/KUMA.md
avoid=automatic remediation,secret tokens in repo,huge logs
ARCH:
sampler=5s loop; /proc first; vmstat/pidstat/iostat fallback cached every 60s; bounded JSONL
gap_detector=monotonic delta >30s => PROBABLE_FREEZE_OR_STALL
boot_detector=boot_id change + heartbeat wall gap >120s => UNEXPECTED_INTERRUPTION
evidence=journalctl+dmesg around gap window stored under freeze-evidence/<event_id>
storage=root/swap mount + backing block + USB/Samsung/T7 markers + compact lsblk cache
proc_io_delta=/proc/<pid>/io read/write/cancelled-write deltas + /proc/<pid>/stat major fault deltas; rate-limited/skipped under extreme PSI
guardian=separate command/timer; detects pressure; prompts only in terminal; systemd path records/telemeters
timeline=recent merges freeze gaps, unexpected interruptions, PSI/memory/I/O critical events, guardian alerts
correlation=score_event_causes ranks RAM/swap/PSI/CPU/top-process families per freeze
weekly=7d freeze count, avg/longest gap, recurring process, PSI means from compact history
dashboard_json=stable read-only JSON consumed by linux-mint-service-dashboard
io_report=24h freeze I/O/storage report; root/swap T7 detection; kernel keyword evidence; PSI IO correlation; probabilistic causes
kuma=push only; no Kuma remediation
FLOW:
sample=snapshot->boot_check->gap_check->critical_event_check->history_point->append_jsonl->prune/rotate->Kuma push
daemon=sample every 5s
human_report=JSONL->24h freeze count->pressure summary->heuristic causes
io_report=events+evidence+live storage snapshot->top read/write/fault deltas where available->fallback cumulative I/O marked as historical
recent=events.jsonl+guardian-events.jsonl->reverse chronological human timeline
weekly_report=events/history->7d aggregate
guardian=pressure->candidate safe_filter->prompt_or_noninteractive_event->Kuma push
INV:
arch=forensics_before_action
data=ring buffer bounded by retention+size
ux=single-key prompt where TTY exists
backup=no automatic cleanup beyond ring rotation
migration=legacy anti-freeze removed; not reused
version=1.2.0 in CLI
security=Kuma URLs in ~/.config/mint-freeze-forensics/kuma.env only
perf=Nice=10; IOSchedulingClass=idle; observed sample CLI maxrss~29MB; sample elapsed~0.53s after storage/proc-io delta patch
BUILD:
cmd=python3 -m py_compile mint_freeze_forensics.py
env=Linux Mint; Python3; optional sysstat for pidstat/iostat
requirements=no pip deps
TEST:
unit=python3 -m py_compile mint_freeze_forensics.py
smoke=mint-freeze-forensics sample; mint-freeze-forensics io-report; mint-freeze-forensics recent; mint-freeze-forensics dashboard-json; mint-freeze-forensics status
gap=mint-freeze-forensics simulate-gap --seconds 35; simulation=true not counted as real freeze
boot=mint-freeze-forensics simulate-interruption --seconds 180; simulation=true not counted as real freeze
guardian=mint-freeze-forensics guardian --once --non-interactive --simulate-alert
systemd=systemctl --user start/stop/restart/status mint-freeze-forensics.service
DATA:
DB=JSONL
Schema=samples.jsonl/events.jsonl/guardian-events.jsonl/history.jsonl; samples include storage + proc I/O deltas from v1.2.0
Paths=~/.local/state/mint-freeze-forensics
Config=~/.config/mint-freeze-forensics
Retention=samples 3600s default; events >=7d; history 8d compact points; size caps 16MB/4MB/3MB
Rotation=*.jsonl.1 when size cap exceeded
Evidence=freeze-evidence/<event_id>/{journal.txt,dmesg.txt,kernel-storage-keywords.txt,io-storage-snapshot.json}
DNB:
dnb=no automatic reboot
dnb=no automatic service restart
dnb=no automatic kill; [K] prints manual kill command only
dnb=no OS sysctl/zram/power/display behavior changes
dnb=do not commit ~/.config/mint-freeze-forensics/kuma.env
dnb=do not revive freeze_reboot_monitor,system_watchdog,screen-watchdog,os-observer-autofix
BUG:
issue=journal evidence can be empty if no journal rows in gap window
issue=manual service start/stop tests can create intentional gap events
issue=dashboard/API collection under heavy host load can coincide with real logger gaps; keep as evidence, mark only explicit simulations
RISK:
risk=pidstat/iostat/vmstat/proc-io calls can stretch sample duration under pressure; tool/proc-io/Kuma/prune rate-limited to 60s
risk=events before v1.2.0 do not contain read/write deltas or major fault deltas; io-report marks cumulative-only evidence explicitly
risk=guardian TTY prompt unavailable under systemd; timer uses noninteractive alert+Kuma heartbeat
ROAD:
now=observe live freeze patterns for 24-72h with v1.2.0 I/O deltas and storage snapshots
next=run io-report after next real freeze; compare browser RSS, swap-on-T7, read/write deltas, major faults, kernel storage errors
later=optional TUI wrapper for guardian prompt
LINK:
meta=../../../mint-freeze-forensics/dev/project.metadata.json
human=../../human/projects/mint-freeze-forensics/overview.md
repo=../../../mint-freeze-forensics
kuma=oracle-uptime-kuma.md
kuma_doc=../../../mint-freeze-forensics/docs/KUMA.md
dashboard=linux-mint-service-dashboard.md
OPEN:
open=causal percentages heuristic; validate after real freeze corpus
open=Kuma screenshots/browser not used; all config via Oracle VM DB+push
tool_interval=MFF_TOOL_SAMPLE_INTERVAL_SECONDS default 60
status_page=http://150.230.148.128:3001/status/mint-freeze-analysis
