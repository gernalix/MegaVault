META:
name=owntracks-watcher
slug=owntracks-watcher
path=/home/daniele/codex-workspace/owntracks-watcher
remote=none
branch=codex/prompt-384917
verified_commit=eaac5bc
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- UNKNOWN: source docs do not state a clear purpose.
STACK:
lang=UNKNOWN;fw=UNKNOWN;db=UNKNOWN;platform=UNKNOWN;tools=UNKNOWN
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=UNKNOWN
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- UNKNOWN
FLOW:
- UNKNOWN
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
data=UNKNOWN
safety=dev/project.metadata.json:9:"metadata_version": 1,
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
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
BUG:
- UNKNOWN
RISK:
- UNKNOWN
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../owntracks-watcher/dev/project.metadata.json
human=../../human/projects/owntracks-watcher/overview.md
legacy=../../../owntracks-watcher/dev/legacy
repo=../../../owntracks-watcher
OPEN:
- thin active code corpus; verify repo purpose manually
- no tests detected by static scan
- data/storage rules absent from active code
