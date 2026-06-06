META:
name=system_watchdog
slug=system-watchdog
path=/home/daniele/codex-workspace/system_watchdog
remote=none
branch=master
verified_commit=d93002d
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Persistent heartbeat sender for a Uptime Kuma push monitor
status=DISABLED_OPERATIONALLY_PROMPT_584731
status_ts=2026-06-05T07:48:36+02:00
status_reason=anti-freeze/watchdog residual removal; Kuma reliability now delegated to service-specific pushers/monitors
status_kuma_482917=Kuma monitor id=1 `mint heartbeat` disabled on 2026-06-06 as obsolete generic heartbeat; tags=482917-reviewed,push-monitor,obsolete-disabled
STACK:
lang=Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=Uptime Kuma,systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json,systemd/system-watchdog.service,watchdog.py
db=UNKNOWN
tests=UNKNOWN
scripts=install.sh,logs.sh,status.sh,uninstall.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
core=watchdog.py:utc_now,utc_iso,local_iso,read_text,boot_id,uptime_seconds
FLOW:
flow=script->install.sh=>dev/project.metadata.json
flow=systemd/system-watchdog.service:5:StartLimitIntervalSec=0
flow=systemd/system-watchdog.service:17:ExecStart=/usr/bin/python3 /home/daniele/codex-workspace/system_watchdog/watchdog.py run
flow=systemd/system-watchdog.service:18:Restart=always
INV:
arch=watchdog.py:utc_now,utc_iso,local_iso,read_text,boot_id
data=dev/project.metadata.json:9:"metadata_version": 1,; systemd/system-watchdog.service:12:Environment=WATCHDOG_DB=/home/daniele/codex-workspace/system_watchdog/watchdog.sqlite
ux=UNKNOWN
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,; install.sh:8:python3 --version >/dev/null
i18n=UNKNOWN
security=UNKNOWN
perf=systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20; watchdog.py:144:def push(url, timeout):
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=systemd/system-watchdog.service:12:Environment=WATCHDOG_DB=/home/daniele/codex-workspace/system_watchdog/watchdog.sqlite; uninstall.sh:7:echo "Database and logs left in place: watchdog.sqlite watchdog.log"
paths=systemd/system-watchdog.service:12:Environment=WATCHDOG_DB=/home/daniele/codex-workspace/system_watchdog/watchdog.sqlite; uninstall.sh:7:echo "Database and logs left in place: watchdog.sqlite watchdog.log"
backup=UNKNOWN
restore=watchdog.py:11:from datetime import datetime, timezone
import=watchdog.py:11:from datetime import datetime, timezone; dev/project.metadata.json:9:"metadata_version": 1,
export=dev/project.metadata.json:9:"metadata_version": 1,
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=dev/project.metadata.json:9:"metadata_version": 1,
dnb=systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
dnb=watchdog.py:144:def push(url, timeout):
dnb=watchdog.py:148:with urllib.request.urlopen(req, timeout=timeout) as resp:
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=UNKNOWN
RISK:
risk=UNKNOWN
ROAD:
now=disabled: systemctl status system-watchdog.service => inactive/dead, unit disabled; Kuma `mint heartbeat` disabled in #482917
next=keep disabled unless operator explicitly restores generic host heartbeat
later=UNKNOWN
LINK:
meta=../../../system_watchdog/dev/project.metadata.json
human=../../human/projects/system-watchdog/overview.md
legacy=../../../system_watchdog/dev/legacy
repo=../../../system_watchdog
OPEN:
open=tests=UNKNOWN_OR_ABSENT
