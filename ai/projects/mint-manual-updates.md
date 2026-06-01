META:
name=mint-manual-updates
slug=mint-manual-updates
path=/home/daniele/codex-workspace/mint-manual-updates
remote=none
branch=master
verified_commit=bd9d452
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Servizio user systemd v4 per controllare e applicare aggiornamenti prudenti su Linux Mint 22.3 / Ubuntu noble
STACK:
lang=UNKNOWN
fw=UNKNOWN
db=UNKNOWN
platform=UNKNOWN
tools=UNKNOWN
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json,systemd/user/mint-extra-updater.service,systemd/user/mint-extra-updater.timer,systemd/user/mint-manual-updates.service,systemd/user/mint-manual-updates.timer
db=UNKNOWN
tests=UNKNOWN
scripts=UNKNOWN
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
arch=UNKNOWN
FLOW:
flow=systemd/user/mint-extra-updater.service:11:ExecStart=/home/daniele/codex-workspace/mint-manual-updates/bin/mint-extra-updater --run
flow=systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
flow=systemd/user/mint-extra-updater.timer:4:[Timer]
INV:
arch=UNKNOWN
data=dev/project.metadata.json:9:"metadata_version": 1,; systemd/user/mint-extra-updater.timer:11:WantedBy=timers.target
ux=UNKNOWN
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=UNKNOWN
perf=systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200; systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=systemd/user/mint-extra-updater.timer:11:WantedBy=timers.target; systemd/user/mint-manual-updates.timer:11:WantedBy=timers.target
paths=UNKNOWN
backup=UNKNOWN
restore=UNKNOWN
import=dev/project.metadata.json:9:"metadata_version": 1,
export=dev/project.metadata.json:9:"metadata_version": 1,
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=dev/project.metadata.json:9:"metadata_version": 1,
dnb=systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
dnb=systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v1
dnb=systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=UNKNOWN
RISK:
risk=UNKNOWN
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../mint-manual-updates/dev/project.metadata.json
human=../../human/projects/mint-manual-updates/overview.md
legacy=../../../mint-manual-updates/dev/legacy
repo=../../../mint-manual-updates
OPEN:
open=tests=UNKNOWN_OR_ABSENT
