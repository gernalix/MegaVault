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
core=snapshot(),record_sample(),daemon(),guardian(),human_report()
db=JSONL ring buffer
tests=py_compile,sample,simulate-gap,guardian --simulate-alert,human-report,systemd start/stop/restart
scripts=systemd/user/*.service,systemd/user/*.timer
avoid=automatic remediation,secret tokens in repo,huge logs
ARCH:
sampler=5s loop; /proc first; vmstat/pidstat/iostat fallback cached every 60s; bounded JSONL
gap_detector=monotonic delta >30s => PROBABLE_FREEZE_OR_STALL
evidence=journalctl+dmesg around gap window stored under freeze-evidence/<event_id>
guardian=separate command/timer; detects pressure; prompts only in terminal; systemd path records/telemeters
kuma=push only; no Kuma remediation
FLOW:
sample=snapshot->gap_check->append_jsonl->prune/rotate->Kuma push
daemon=sample every 5s
human_report=JSONL->24h freeze count->pressure summary->heuristic causes
guardian=pressure->candidate safe_filter->prompt_or_noninteractive_event->Kuma push
INV:
arch=forensics_before_action
data=ring buffer bounded by retention+size
ux=single-key prompt where TTY exists
backup=no automatic cleanup beyond ring rotation
migration=legacy anti-freeze removed; not reused
version=VERSION in CLI
security=Kuma URLs in ~/.config/mint-freeze-forensics/kuma.env only
perf=Nice=10; IOSchedulingClass=idle; observed MemoryCurrent~16MB
BUILD:
cmd=python3 -m py_compile mint_freeze_forensics.py
env=Linux Mint; Python3; optional sysstat for pidstat/iostat
requirements=no pip deps
TEST:
unit=python3 -m py_compile mint_freeze_forensics.py
smoke=mint-freeze-forensics sample; mint-freeze-forensics status
gap=mint-freeze-forensics simulate-gap --seconds 35
guardian=mint-freeze-forensics guardian --once --non-interactive --simulate-alert
systemd=systemctl --user start/stop/restart/status mint-freeze-forensics.service
DATA:
DB=JSONL
Schema=samples.jsonl/events.jsonl/guardian-events.jsonl
Paths=~/.local/state/mint-freeze-forensics
Config=~/.config/mint-freeze-forensics
Retention=samples 3600s default; events >=24h; size caps 8MB/4MB
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
RISK:
risk=pidstat/iostat/vmstat calls can stretch sample duration under pressure; timeout bounded
risk=guardian TTY prompt unavailable under systemd; timer uses noninteractive alert+Kuma heartbeat
ROAD:
now=observe live freeze patterns for 24-72h
next=tune guardian thresholds after real freeze evidence
later=optional TUI wrapper for guardian prompt
LINK:
meta=../../../mint-freeze-forensics/dev/project.metadata.json
human=../../human/projects/mint-freeze-forensics/overview.md
repo=../../../mint-freeze-forensics
kuma=oracle-uptime-kuma.md
OPEN:
open=causal percentages heuristic; validate after real freeze corpus
open=Kuma screenshots/browser not used; all config via Oracle VM DB+push
tool_interval=MFF_TOOL_SAMPLE_INTERVAL_SECONDS default 60
