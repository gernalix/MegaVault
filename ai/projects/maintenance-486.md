META:
name=maintenance-486
slug=maintenance-486
path=/home/daniele/codex-workspace/projects/vm_oracle/maintenance-486
remote=none
branch=master
verified_commit=ed9de94
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Oracle VM maintenance/report workspace for prompt 486; source material is mostly reports and logs, so operational details are limited a...
STACK:
lang=Shell;fw=UNKNOWN;db=UNKNOWN;platform=UNKNOWN;tools=UNKNOWN
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=scripts/ssh_diag_486.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- UNKNOWN
FLOW:
- UNKNOWN
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 // true
arch=scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%
arch=scripts/ssh_diag_486.sh:16:timeout 35 ssh \
arch=scripts/ssh_diag_486.sh:18:-o ConnectTimeout=12 \
data=UNKNOWN
safety=dev/project.metadata.json:9:"metadata_version": 1,
safety=preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- scripts/ssh_diag_486.sh:1:#!/usr/bin/env bash
- scripts/ssh_diag_486.sh:5:key="${2:-../ssh-key-2026-02-01.key}"
- scripts/ssh_diag_486.sh:12:echo "=== raw SSH banner ==="
- scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n'
- scripts/ssh_diag_486.sh:15:echo "=== short SSH command ==="
- scripts/ssh_diag_486.sh:16:timeout 35 ssh \
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
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
BUG:
- scripts/ssh_diag_486.sh:2:set -euo pipefail
- scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 // true
- scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n'
- scripts/ssh_diag_486.sh:16:timeout 35 ssh \
- scripts/ssh_diag_486.sh:18:-o ConnectTimeout=12 \
RISK:
- UNKNOWN
ROAD:
now=scripts/ssh_diag_486.sh:2:set -euo pipefail
next=scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 // true
later=scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n'
LINK:
meta=../../../projects/vm_oracle/maintenance-486/dev/project.metadata.json
human=../../human/projects/maintenance-486/overview.md
legacy=../../../projects/vm_oracle/maintenance-486/dev/legacy
repo=../../../projects/vm_oracle/maintenance-486
OPEN:
- no tests detected by static scan
- data/storage rules absent from active code
