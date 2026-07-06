META:
name=maintenance-486
slug=maintenance-486
path=/home/daniele/codex-workspace/projects/vm_oracle/maintenance-486
remote=none
branch=master
verified_commit=ed9de94
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Oracle VM maintenance/report workspace for prompt 486; source material is mostly reports and logs, so operational details are limited and should be verified before remote changes
STACK:
lang=Shell
fw=UNKNOWN
db=UNKNOWN
platform=UNKNOWN
tools=UNKNOWN
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json
db=UNKNOWN
tests=UNKNOWN
scripts=scripts/ssh_diag_486.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
arch=UNKNOWN
FLOW:
flow=script->scripts/ssh_diag_486.sh=>dev/project.metadata.json
INV:
arch=UNKNOWN
data=dev/project.metadata.json:9:"metadata_version": 1,
ux=UNKNOWN
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 || true; scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" || true
perf=scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 || true; scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" || true
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=DB=UNKNOWN
paths=UNKNOWN
backup=UNKNOWN
restore=UNKNOWN
import=dev/project.metadata.json:9:"metadata_version": 1,; scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" || true
export=dev/project.metadata.json:9:"metadata_version": 1,
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=dev/project.metadata.json:9:"metadata_version": 1,
dnb=scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 || true
dnb=scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" || true
dnb=scripts/ssh_diag_486.sh:16:timeout 35 ssh \
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
meta=../../../projects/vm_oracle/maintenance-486/dev/project.metadata.json
human=../../human/projects/maintenance-486/overview.md
legacy=../../../projects/vm_oracle/maintenance-486/dev/legacy
repo=../../../projects/vm_oracle/maintenance-486
OPEN:
open=tests=UNKNOWN_OR_ABSENT
