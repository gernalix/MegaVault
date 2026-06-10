META:
name=mint-freeze-forensics
slug=mint-freeze-forensics
path=/home/daniele/codex-workspace/mint-freeze-forensics
repo=/home/daniele/codex-workspace/mint-freeze-forensics
branch=main
prompt=847261
latest_prompt=746182
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
core=snapshot(),record_sample(),daemon(),guardian(),human_report(),io_report(),freeze_root_cause(),recent(),weekly_report(),dashboard_summary(),score_event_causes(),adaptive_capture
db=JSONL ring buffer + compact history
tests=py_compile,sample,io-report,freeze-root-cause,recent,dashboard-json,simulate-gap,guardian --simulate-alert,human-report,systemd start/stop/restart
scripts=systemd/user/*.service,systemd/user/*.timer,docs/KUMA.md
avoid=automatic remediation,secret tokens in repo,huge logs
ARCH:
sampler=5s loop; /proc first; vmstat/pidstat/iostat fallback cached; bounded JSONL
gap_detector=monotonic delta >30s => PROBABLE_FREEZE_OR_STALL
boot_detector=boot_id change + heartbeat wall gap >120s => UNEXPECTED_INTERRUPTION
evidence=journalctl+dmesg around gap window stored under freeze-evidence/<event_id>
storage=root/swap mount + backing block + USB/Samsung/T7 markers + compact lsblk cache
advanced_telemetry=/proc/meminfo expanded fields; PSI memory/io/cpu avg10/avg60/avg300/total; /proc/vmstat swap/pagefault/reclaim deltas
proc_io_delta=/proc/<pid>/io read/write/cancelled-write deltas + /proc/<pid>/stat major fault deltas; normal rate-limited to 5s; forced during adaptive capture
focus=Firefox and Codex process families include RSS,VMS,page faults,major faults,open files,I/O deltas,CPU percent,threads,context switches
pre_freeze_capture=triggered by PSI memory/io>=25, swap storms, page-fault storms, low MemAvailable, reclaim activity; JSON snapshots under pre-freeze-capture/
adaptive_capture=normal 5s unchanged; trigger PSI memory/io avg10>=90 or freeze gap; capture interval 1s; max window 120s; kernel storage keyword sampling rate-limited
guardian=separate command/timer; detects pressure; prompts only in terminal; systemd path records/telemeters
timeline=recent merges freeze gaps, unexpected interruptions, PSI/memory/I/O critical events, guardian alerts
correlation=score_event_causes ranks RAM/swap/PSI/CPU/top-process families per freeze
weekly=7d freeze count, avg/longest gap, recurring process, PSI means from compact history
dashboard_json=stable read-only JSON consumed by linux-mint-service-dashboard
io_report=24h freeze I/O/storage report; root/swap T7 detection; kernel keyword evidence; PSI IO correlation; probabilistic causes
freeze_root_cause=recent freeze timeline; nearest pre-freeze snapshot; PSI/RAM/swap/process evidence; candidate probabilities A-G
kuma=push only; no Kuma remediation; telemetry counts stay status=up; red means heartbeat failure/expiry
FLOW:
sample=snapshot->pre_freeze_check->capture_trigger_check->boot_check->gap_check->critical_event_check->history_point->append_jsonl->prune/rotate->Kuma push
daemon=sample every 5s normal; 1s only while capture.active and active_until_epoch not expired
human_report=JSONL->24h freeze count->pressure summary->heuristic causes
io_report=events+evidence+live storage snapshot->top read/write/fault deltas where available->fallback cumulative I/O marked as historical
freeze_root_cause=events+nearest pre-freeze capture+process focus+storage topology->candidate score normalization->human report
recent=events.jsonl+guardian-events.jsonl->reverse chronological human timeline
weekly_report=events/history->7d aggregate
guardian=pressure->candidate safe_filter->prompt_or_noninteractive_event->Kuma push
INV:
arch=forensics_before_action
data=ring buffer bounded by retention+size
ux=single-key prompt where TTY exists
backup=no automatic cleanup beyond ring rotation
migration=legacy anti-freeze removed; not reused
version=1.4.0 in CLI
security=Kuma URLs in ~/.config/mint-freeze-forensics/kuma.env only
perf=Nice=10; IOSchedulingClass=idle; v1.4 normal sample keeps 5s daemon interval; push interval 30s; proc I/O sampling 5s with pressure skip >=98 PSI avg10
BUILD:
cmd=python3 -m py_compile mint_freeze_forensics.py
env=Linux Mint; Python3; optional sysstat for pidstat/iostat
requirements=no pip deps
TEST:
unit=python3 -m py_compile mint_freeze_forensics.py
smoke=mint-freeze-forensics sample; mint-freeze-forensics io-report; mint-freeze-forensics freeze-root-cause --hours 24 --limit 3; mint-freeze-forensics recent; mint-freeze-forensics dashboard-json; mint-freeze-forensics status
gap=mint-freeze-forensics simulate-gap --seconds 35; simulation=true not counted as real freeze
boot=mint-freeze-forensics simulate-interruption --seconds 180; simulation=true not counted as real freeze
guardian=mint-freeze-forensics guardian --once --non-interactive --simulate-alert
systemd=systemctl --user start/stop/restart/status mint-freeze-forensics.service
DATA:
DB=JSONL
Schema=samples.jsonl/events.jsonl/guardian-events.jsonl/history.jsonl/advanced-telemetry-state.json/pre-freeze-capture-state.json; samples include storage + proc I/O deltas from v1.2.0 and expanded freeze telemetry from v1.4.0
Paths=~/.local/state/mint-freeze-forensics
Config=~/.config/mint-freeze-forensics
Retention=samples 3600s default; events >=7d; history 8d compact points; size caps 16MB/4MB/3MB
Rotation=*.jsonl.1 when size cap exceeded
Evidence=freeze-evidence/<event_id>/{journal.txt,dmesg.txt,kernel-storage-keywords.txt,io-storage-snapshot.json}; pre-freeze-capture/prefreeze-*.json
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
risk=pidstat/iostat/vmstat/proc-io calls can stretch sample duration under pressure; tool/Kuma/prune rate-limited; proc-io skips at PSI avg10>=98
risk=events before v1.2.0 do not contain read/write deltas or major fault deltas; io-report marks cumulative-only evidence explicitly
risk=adaptive capture intentionally raises sampling only during <=120s windows; do not make capture default/continuous
risk=guardian TTY prompt unavailable under systemd; timer uses noninteractive alert+Kuma heartbeat
RCA:
prompt_746182=Kuma red root cause was telemetry counters sent with down status for nonzero freeze/guardian counts, plus 60s local push interval equal to Kuma interval
fix_746182=v1.4.0 sends freeze/guardian telemetry as up heartbeat, keeps incident evidence in msg/ping, default push interval 30s
verify_746182=2026-06-10 remote Kuma DB monitor 13-17 latest status=1 after installed launcher sample --force-kuma
ROAD:
now=observe live freeze patterns for 24-72h with v1.4 advanced telemetry and pre-freeze capture
next=compare freeze-root-cause output after next real Firefox/Codex freeze against pre-freeze capture evidence
later=optional TUI wrapper for guardian prompt; optional richer sysstat parsing when sysstat exists
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
proc_io_interval=MFF_PROC_IO_INTERVAL_SECONDS default 5
kuma_push_interval=MFF_KUMA_PUSH_INTERVAL_SECONDS default 30
status_page=http://150.230.148.128:3001/status/mint-freeze-analysis
