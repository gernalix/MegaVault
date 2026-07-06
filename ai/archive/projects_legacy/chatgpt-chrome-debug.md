META:
name=chatgpt-chrome-debug
slug=chatgpt-chrome-debug
path=/home/daniele/codex-workspace/chatgpt-chrome-debug
remote=none
branch=master
verified_commit=fdd3773
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=ChatGPT Chrome Redirect Debug Toolkit
STACK:
lang=JS/TS,Python,Shell
fw=Playwright
db=UNKNOWN
platform=UNKNOWN
tools=Chrome,systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json,package-lock.json
db=scripts/snapshot_environment.sh
tests=UNKNOWN
scripts=START_DEBUGGING.sh,scripts/common.sh,scripts/dashboard.sh,scripts/install_user_services.sh,scripts/live_chrome_logger.sh
build=package.json
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
script=scripts/common.sh:ts,safe_name,mkdirs,chrome_bin,log_line
script=scripts/live_chrome_logger.sh:is_running,start_logger,run_foreground,stop_logger,status_logger
script=scripts/monitor_chatgpt_tab.js:arg,ts,mkdirp,appendJSONL,isChatGPTHome,isConversation
script=scripts/run_differential_tests.sh:run_case
build=package.json:no_symbols
FLOW:
flow=script->START_DEBUGGING.sh=>scripts/snapshot_environment.sh
flow=data->scripts/snapshot_environment.sh
flow=START_DEBUGGING.sh:13:./scripts/live_chrome_logger.sh start
flow=scripts/install_user_services.sh:18:ExecStart=$ROOT_DIR/scripts/live_chrome_logger.sh run
flow=scripts/install_user_services.sh:19:Restart=always
INV:
arch=scripts/common.sh:ts,safe_name,mkdirs,chrome_bin,log_line; scripts/live_chrome_logger.sh:is_running,start_logger,run_foreground,stop_logger,status_logger; scripts/monitor_chatgpt_tab.js:arg,ts,mkdirp,appendJSONL,isChatGPTHome; scripts/ru...
data=dev/project.metadata.json:9:"metadata_version": 1,; package-lock.json:3:"version": "0.1.0",
ux=scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 || true; scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
backup=scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 || true; scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
migration=UNKNOWN
version=scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 || true; scripts/snapshot_environment.sh:60:echo "== chrome://version via isolated headless profile =="
i18n=UNKNOWN
security=scripts/snapshot_environment.sh:99:((.value.granted_permissions.api // []) | join(",")),; scripts/snapshot_environment.sh:100:((.value.granted_permissions.explicit_host // []) | join(",")),
perf=package-lock.json:3:"version": "0.1.0",; package-lock.json:4:"lockfileVersion": 3,
BUILD:
files=package.json
cmd_hint=npm_script[monitor]=node scripts/monitor_chatgpt_tab.js
cmd_hint=npm_script[snapshot]=bash scripts/snapshot_environment.sh
cmd_hint=npm_script[live]=bash scripts/live_chrome_logger.sh start
cmd_hint=npm_script[differential]=bash scripts/run_differential_tests.sh
TEST:
files=UNKNOWN
cmd_hint=npm_script[differential]=bash scripts/run_differential_tests.sh
DATA:
db=scripts/monitor_chatgpt_tab.js:88:indexedDBDatabases: await safeEvaluate(page, async () => indexedDB.databases ? indexedDB.databases() : [], []),
paths=scripts/monitor_chatgpt_tab.js:88:indexedDBDatabases: await safeEvaluate(page, async () => indexedDB.databases ? indexedDB.databases() : [], []),; scripts/monitor_chatgpt_tab.js:234:appendJSONL(liveFile, { event: 'monitor-start', url, pr...
backup=scripts/snapshot_environment.sh:83:} > "$OUT/chrome_flags.json"; scripts/snapshot_environment.sh:58:"$CHROME" --version > "$OUT/chrome_version.txt" 2>&1 || true
restore=scripts/monitor_chatgpt_tab.js:56:async function safeEvaluate(page, expression, fallback) {
import=scripts/snapshot_environment.sh:83:} > "$OUT/chrome_flags.json"; scripts/dashboard.sh:18:if [[ -r "$DIAG_DIR/live/monitor_events.jsonl" ]]; then
export=scripts/snapshot_environment.sh:83:} > "$OUT/chrome_flags.json"; scripts/dashboard.sh:18:if [[ -r "$DIAG_DIR/live/monitor_events.jsonl" ]]; then
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // [])) | tostring) | test("tabs|webRequest|webNavigation|scripting|storage|cookies"))
dnb=scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") | ascii_downcase) | test("chatgpt|refresh|tab|cookie|script|style|monitor|ghostery|ublock"))
dnb=package-lock.json:4:"lockfileVersion": 3,
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=dev/project.metadata.json:2:"project_name": "chatgpt-chrome-debug",
issue=dev/project.metadata.json:3:"project_slug": "chatgpt-chrome-debug",
issue=dev/project.metadata.json:4:"project_root": "/home/daniele/codex-workspace/chatgpt-chrome-debug",
issue=dev/project.metadata.json:6:"ai_doc": "/home/daniele/codex-workspace/MegaVault/ai/archive/projects_legacy/chatgpt-chrome-debug.md",
issue=dev/project.metadata.json:7:"human_doc": "/home/daniele/codex-workspace/MegaVault/human/projects/chatgpt-chrome-debug",
RISK:
risk=scripts/snapshot_environment.sh:117:((((.value.granted_permissions.api // []) + (.value.manifest.permissions // [])) | tostring) | test("tabs|webRequest|webNavigation|scripting|storage|cookies"))
risk=scripts/snapshot_environment.sh:119:or (((.value.manifest.name // "") | ascii_downcase) | test("chatgpt|refresh|tab|cookie|script|style|monitor|ghostery|ublock"))
risk=package-lock.json:4:"lockfileVersion": 3,
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../chatgpt-chrome-debug/dev/project.metadata.json
human=../../human/projects/chatgpt-chrome-debug/overview.md
legacy=../../../chatgpt-chrome-debug/dev/legacy
repo=../../../chatgpt-chrome-debug
OPEN:
open=tests=UNKNOWN_OR_ABSENT
