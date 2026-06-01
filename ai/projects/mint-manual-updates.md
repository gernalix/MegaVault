META:
name=mint-manual-updates
slug=mint-manual-updates
path=/home/daniele/codex-workspace/mint-manual-updates
remote=none
branch=master
verified_commit=bd9d452
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Servizio user systemd v4 per controllare e applicare aggiornamenti prudenti su Linux Mint 22.3 / Ubuntu noble.
STACK:
lang=UNKNOWN;fw=UNKNOWN;db=UNKNOWN;platform=UNKNOWN;tools=UNKNOWN
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
core=systemd/user/mint-extra-updater.service
core=systemd/user/mint-extra-updater.timer
core=systemd/user/mint-manual-updates.service
core=systemd/user/mint-manual-updates.timer
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=UNKNOWN
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- systemd/user/mint-extra-updater.service:11:ExecStart=~/cw/mint-manual-updates/bin/mint-extra-updater --run
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-extra-updater.timer:4:[Timer]
- systemd/user/mint-extra-updater.timer:11:WantedBy=timers.target
- systemd/user/mint-manual-updates.service:11:ExecStart=~/cw/mint-manual-updates/bin/mint-manual-updates --run
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
FLOW:
- systemd/user/mint-extra-updater.service:11:ExecStart=~/cw/mint-manual-updates/bin/mint-extra-updater --run
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-extra-updater.timer:4:[Timer]
- systemd/user/mint-extra-updater.timer:11:WantedBy=timers.target
- systemd/user/mint-manual-updates.service:11:ExecStart=~/cw/mint-manual-updates/bin/mint-manual-updates --run
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.timer:4:[Timer]
- systemd/user/mint-manual-updates.timer:11:WantedBy=timers.target
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
arch=systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v1
arch=systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
arch=systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v1
data=UNKNOWN
safety=dev/project.metadata.json:9:"metadata_version": 1,
safety=systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v1
safety=systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v1
safety=preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- UNKNOWN
TEST:
- UNKNOWN
DATA:
db=UNKNOWN
backup=UNKNOWN
import=UNKNOWN
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- dev/project.metadata.json:9:"metadata_version": 1,
- systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v1
- systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v1
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
BUG:
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
RISK:
- UNKNOWN
ROAD:
now=systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
next=systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
later=UNKNOWN
LINK:
meta=../../../mint-manual-updates/dev/project.metadata.json
human=../../human/projects/mint-manual-updates/overview.md
legacy=../../../mint-manual-updates/dev/legacy
repo=../../../mint-manual-updates
OPEN:
- no tests detected by static scan
- data/storage rules absent from active code
