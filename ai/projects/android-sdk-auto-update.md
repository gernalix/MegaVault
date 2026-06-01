META:
name=android-sdk-auto-update
slug=android-sdk-auto-update
path=/home/daniele/codex-workspace/android-sdk-auto-update
remote=none
branch=master
verified_commit=7d6a23b
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Servizio giornaliero per aggiornare i pacchetti Android SDK gestiti da `sdkmanager` su Linux Mint/Ubuntu
STACK:
lang=Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=UNKNOWN
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json
db=UNKNOWN
tests=UNKNOWN
scripts=android_sdk_auto_update.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
script=android_sdk_auto_update.sh:usage,info,warn,error,utc_now,epoch_now
FLOW:
flow=script->android_sdk_auto_update.sh=>dev/project.metadata.json
flow=android_sdk_auto_update.sh:49:--run Backward-compatible alias for "--install --yes" used by the user timer.
flow=android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
flow=android_sdk_auto_update.sh:114:export "$key=$value"
INV:
arch=android_sdk_auto_update.sh:usage,info,warn,error,utc_now
data=dev/project.metadata.json:9:"metadata_version": 1,; android_sdk_auto_update.sh:10:CSV_FILE="$HISTORY_DIR/android_updates_history.csv"
ux=android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.; android_sdk_auto_update.sh:48:--yes Required for real install/remove operations and license acceptance.
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,; android_sdk_auto_update.sh:138:printf '%s\n' 'timestamp_utc,package,previous_version,new_version,operation,size_bytes,size_mb,exit_status,duration_seconds,hostname,username,sdk_path' >"...
i18n=UNKNOWN
security=android_sdk_auto_update.sh:114:export "$key=$value"; android_sdk_auto_update.sh:51:--test-telegram Send a Telegram test notification using configured credentials.
perf=android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"; android_sdk_auto_update.sh:16:RUN_TIMEOUT_SECONDS="${ANDROID_SDK_AUTO_UPDATE_TIMEOUT_SECONDS:-3600}"
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=android_sdk_auto_update.sh:11:SQLITE_FILE="$HISTORY_DIR/android_updates_history.sqlite"; android_sdk_auto_update.sh:64:SQLite: logs/android_updates_history.sqlite
paths=android_sdk_auto_update.sh:11:SQLITE_FILE="$HISTORY_DIR/android_updates_history.sqlite"; android_sdk_auto_update.sh:64:SQLite: logs/android_updates_history.sqlite
backup=UNKNOWN
restore=UNKNOWN
import=android_sdk_auto_update.sh:10:CSV_FILE="$HISTORY_DIR/android_updates_history.csv"; android_sdk_auto_update.sh:65:CSV: logs/android_updates_history.csv
export=android_sdk_auto_update.sh:10:CSV_FILE="$HISTORY_DIR/android_updates_history.csv"; android_sdk_auto_update.sh:65:CSV: logs/android_updates_history.csv
migration=UNKNOWN
retention=android_sdk_auto_update.sh:10:CSV_FILE="$HISTORY_DIR/android_updates_history.csv"; android_sdk_auto_update.sh:11:SQLITE_FILE="$HISTORY_DIR/android_updates_history.sqlite"
DNB:
dnb=android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
dnb=android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
dnb=android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
dnb=android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets.
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=android_sdk_auto_update.sh:224:warn "Telegram helper failed, trying curl fallback"
issue=android_sdk_auto_update.sh:246:warn "Telegram curl fallback failed"
RISK:
risk=android_sdk_auto_update.sh:12:LOCK_FILE="${XDG_RUNTIME_DIR:-/tmp}/${APP_NAME}.lock"
risk=android_sdk_auto_update.sh:46:This never deletes AVDs, system images, SDK cache, or the SDK root.
risk=android_sdk_auto_update.sh:60:It does not upgrade apt/system packages, delete AVDs, delete system images,
risk=android_sdk_auto_update.sh:61:delete caches, change global PATH, update app Gradle/AGP/Kotlin files, or save secrets.
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../android-sdk-auto-update/dev/project.metadata.json
human=../../human/projects/android-sdk-auto-update/overview.md
legacy=../../../android-sdk-auto-update/dev/legacy
repo=../../../android-sdk-auto-update
OPEN:
open=tests=UNKNOWN_OR_ABSENT
