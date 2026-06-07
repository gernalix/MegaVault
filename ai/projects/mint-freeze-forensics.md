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
core=snapshot(),record_sample(),daemon(),guardian(),human_report(),recent(),weekly_report(),dashboard_summary(),score_event_causes()
db=JSONL ring buffer + compact history
tests=py_compile,sample,simulate-gap,guardian --simulate-alert,human-report,systemd start/stop/restart
scripts=systemd/user/*.service,systemd/user/*.timer,docs/KUMA.md
avoid=automatic remediation,secret tokens in repo,huge logs
ARCH:
sampler=5s loop; /proc first; vmstat/pidstat/iostat fallback cached every 60s; bounded JSONL
gap_detector=monotonic delta >30s => PROBABLE_FREEZE_OR_STALL
boot_detector=boot_id change + heartbeat wall gap >120s => UNEXPECTED_INTERRUPTION
evidence=journalctl+dmesg around gap window stored under freeze-evidence/<event_id>
guardian=separate command/timer; detects pressure; prompts only in terminal; systemd path records/telemeters
timeline=recent merges freeze gaps, unexpected interruptions, PSI/memory/I/O critical events, guardian alerts
correlation=score_event_causes ranks RAM/swap/PSI/CPU/top-process families per freeze
weekly=7d freeze count, avg/longest gap, recurring process, PSI means from compact history
dashboard_json=stable read-only JSON consumed by linux-mint-service-dashboard
kuma=push only; no Kuma remediation
FLOW:
sample=snapshot->boot_check->gap_check->critical_event_check->history_point->append_jsonl->prune/rotate->Kuma push
daemon=sample every 5s
human_report=JSONL->24h freeze count->pressure summary->heuristic causes
recent=events.jsonl+guardian-events.jsonl->reverse chronological human timeline
weekly_report=events/history->7d aggregate
guardian=pressure->candidate safe_filter->prompt_or_noninteractive_event->Kuma push
INV:
arch=forensics_before_action
data=ring buffer bounded by retention+size
ux=single-key prompt where TTY exists
backup=no automatic cleanup beyond ring rotation
migration=legacy anti-freeze removed; not reused
version=1.1.0 in CLI
security=Kuma URLs in ~/.config/mint-freeze-forensics/kuma.env only
perf=Nice=10; IOSchedulingClass=idle; observed RSS~28MB; steady CPU~2-3% after prune/proc-io optimization
BUILD:
cmd=python3 -m py_compile mint_freeze_forensics.py
env=Linux Mint; Python3; optional sysstat for pidstat/iostat
requirements=no pip deps
TEST:
unit=python3 -m py_compile mint_freeze_forensics.py
smoke=mint-freeze-forensics sample; mint-freeze-forensics status; mint-freeze-forensics recent; mint-freeze-forensics weekly-report
gap=mint-freeze-forensics simulate-gap --seconds 35; simulation=true not counted as real freeze
boot=mint-freeze-forensics simulate-interruption --seconds 180; simulation=true not counted as real freeze
guardian=mint-freeze-forensics guardian --once --non-interactive --simulate-alert
systemd=systemctl --user start/stop/restart/status mint-freeze-forensics.service
DATA:
DB=JSONL
Schema=samples.jsonl/events.jsonl/guardian-events.jsonl/history.jsonl
Paths=~/.local/state/mint-freeze-forensics
Config=~/.config/mint-freeze-forensics
Retention=samples 3600s default; events >=7d; history 8d compact points; size caps 16MB/4MB/3MB
Rotation=*.jsonl.1 when size cap exceeded
Evidence=freeze-evidence/<event_id>/{journal.txt,dmesg.txt}
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
risk=guardian TTY prompt unavailable under systemd; timer uses noninteractive alert+Kuma heartbeat
ROAD:
now=observe live freeze patterns for 24-72h; wait for >=3 real freeze events
next=run historical-validation after >=3 real freeze events; tune guardian thresholds after real freeze evidence
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
