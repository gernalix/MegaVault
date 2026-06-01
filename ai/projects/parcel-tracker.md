META:
name=parcel-tracker
slug=parcel-tracker
path=/home/daniele/codex-workspace/parcel-tracker
remote=none
branch=master
verified_commit=0fea1eb
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Servizio leggero user-level per monitorare la spedizione `XT329499807TS`
STACK:
lang=Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=Uptime Kuma
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json,parcel-tracker.service,parcel-tracker.timer,parcel_tracker.py
db=UNKNOWN
tests=UNKNOWN
scripts=parcel_tracker.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
core=parcel_tracker.py:TrackingSnapshot,utc_now,log,db,get_state,set_state
FLOW:
flow=script->parcel_tracker.sh=>dev/project.metadata.json
flow=parcel-tracker.service:9:ExecStart=/usr/bin/env bash /home/daniele/codex-workspace/parcel-tracker/parcel_tracker.sh --run
flow=parcel-tracker.timer:4:[Timer]
flow=parcel-tracker.timer:12:WantedBy=timers.target
INV:
arch=parcel_tracker.py:TrackingSnapshot,utc_now,log,db,get_state
data=dev/project.metadata.json:9:"metadata_version": 1,; parcel_tracker.py:223:subprocess.run([sys.executable, str(TELEGRAM_HELPER), "--check"], check=True, timeout=20)
ux=UNKNOWN
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=parcel_tracker.py:84:def get_state(conn: sqlite3.Connection, key: str) -> str | None:; parcel_tracker.py:89:def set_state(conn: sqlite3.Connection, key: str, value: str) -> None:
perf=parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:; parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=parcel-tracker.timer:12:WantedBy=timers.target; parcel_tracker.py:22:STATE_DB = BASE_DIR / "parcel_tracker.sqlite3"
paths=parcel_tracker.py:22:STATE_DB = BASE_DIR / "parcel_tracker.sqlite3"
backup=UNKNOWN
restore=UNKNOWN
import=dev/project.metadata.json:9:"metadata_version": 1,; parcel_tracker.py:234:urllib.request.urlopen(KUMA_PUSH_URL, timeout=20).read()
export=dev/project.metadata.json:9:"metadata_version": 1,
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=dev/project.metadata.json:9:"metadata_version": 1,
dnb=parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:
dnb=parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
dnb=parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
RISK:
risk=UNKNOWN
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../parcel-tracker/dev/project.metadata.json
human=../../human/projects/parcel-tracker/overview.md
legacy=../../../parcel-tracker/dev/legacy
repo=../../../parcel-tracker
OPEN:
open=tests=UNKNOWN_OR_ABSENT
