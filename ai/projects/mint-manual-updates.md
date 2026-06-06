META:
name=mint-manual-updates
slug=mint-manual-updates
path=/home/daniele/codex-workspace/mint-manual-updates
remote=none
branch=master
verified_at=2026-06-06T00:00:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
prompt=927384
PURPOSE:
purpose=Single user-systemd Linux Mint updater for system packages, local Python venvs, dev tools, Android Studio, and Android SDK
official_command=bin/mint-manual-updates --run
STACK:
lang=Bash
db=SQLite optional via sqlite3 CLI for Android SDK history
platform=Linux Mint/Ubuntu user session
tools=systemd-user,apt,flatpak,fwupdmgr,snap,python3,pip,yt-dlp,pipx,rustup,npm,gem,cargo,curl,tar,sha256sum,sdkmanager,avdmanager,timeout,flock
MAP:
entry=bin/mint-manual-updates
systemd=systemd/user/mint-manual-updates.service,systemd/user/mint-manual-updates.timer
state=~/.local/state/mint-manual-updates
venv_logs=~/.local/state/mint-manual-updates/venv-logs
android_history=~/.local/state/mint-manual-updates/android-sdk-history
docs=dev/README.md,dev/TEST_PLAN.md,dev/CHANGELOG.md
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
single_command=true
removed=duplicate updater script,duplicate updater service,duplicate updater timer
manual_script=Bash guarded updater with sections for apt,fwupd,flatpak,snap,global-pip-report,venv-upgrade,yt-dlp,pipx,rustup,npm,gem-report,cargo-report,Android Studio,Android SDK,AppImage-report,Docker-report
android_sdk=in bin/mint-manual-updates; no external delegate; sdkmanager only
FLOW:
run=bin/mint-manual-updates --run
dry_run=bin/mint-manual-updates --dry-run for validation/report only
systemd=ExecStart=/home/daniele/codex-workspace/mint-manual-updates/bin/mint-manual-updates --run
guardrails=load,RAM,swap,PSI,heavy_processes,freeze,apt_dpkg,battery before updates
venv_flow=discover /home/daniele/codex-workspace patterns */venv/bin/python,*/.venv/bin/python,*/env/bin/python; prune .git,node_modules,build,dist,.gradle,.cache,__pycache__; --run reports outdated then upgrades pip/setuptools/wheel and outdated packages inside each venv; continue on failure
android_flow=find SDK root from ANDROID_SDK_ROOT,ANDROID_HOME,~/Android/Sdk,/opt/android-sdk,~/android-sdk -> find sdkmanager -> sdkmanager --list -> history -> licenses -> sdkmanager --update
android_studio_flow=find local tar install -> read product-info build/release -> fetch https://developer.android.com/studio metadata page only -> parse Linux URL/SHA/release/build-if-present -> skip if installed release/build current -> skip safe if remote build unknown -> log URL/dest/size before needed download -> sha256sum verify -> extract -> compare product-info buildNumber -> backup old install -> replace install
INV:
no_duplicate_updater=do not recreate duplicate updater script, wrapper, alias, service, timer, docs, or command
official_command_only=bin/mint-manual-updates --run
global_pip_scope=report-only pip3 list --outdated; never sudo pip/global pip/global pip3 updates
venv_default_scope=/home/daniele/codex-workspace only
venv_update_scope=normal --run mutates only venvs via each venv python -m pip after guardrails
android_update_scope=sdkmanager-managed installed packages only: tools/platform-tools/build-tools/platforms/cmdline-tools/emulator/extras/system-images when reported by sdkmanager
android_not_scope=Gradle/AGP/Kotlin project files, AVD deletion, SDK root deletion, PATH rewrites, secrets
npm_update_scope=npm global packages via npm update -g
gem_cargo_scope=report-only unless project objective explicitly changes
android_studio_update_scope=local tar install, not flatpak/snap/apt package
android_studio_download_guard=never download 1GB+ archive just to confirm same version; >500MB allowed only after metadata proves update needed
BUILD:
cmd=bash -n bin/mint-manual-updates
install=bin/mint-manual-updates --install
TEST:
static=bash -n bin/mint-manual-updates; shellcheck bin/mint-manual-updates if installed
systemd=systemd-analyze --user verify systemd/user/mint-manual-updates.service systemd/user/mint-manual-updates.timer
smoke=bin/mint-manual-updates --help; bin/mint-manual-updates --dry-run
dedupe=find bin/systemd for extra updater leftovers; service_count=1; timer_count=1
DATA:
logs=~/.local/state/mint-manual-updates/mint-manual-updates.log
reports=~/.local/state/mint-manual-updates/last-report.txt,~/.local/state/mint-manual-updates/last-run.json
venv_logs=~/.local/state/mint-manual-updates/venv-logs
android_history_csv=~/.local/state/mint-manual-updates/android-sdk-history/android_updates_history.csv
android_history_sqlite=~/.local/state/mint-manual-updates/android-sdk-history/android_updates_history.sqlite
android_history_table=android_update_history
android_history_fields=timestamp_utc,package,previous_version,new_version,operation,size_bytes,size_mb,exit_status,duration_seconds,hostname,username,sdk_path
android_studio_state=~/.local/state/mint-manual-updates/android-studio
android_studio_backups=~/.local/state/mint-manual-updates/android-studio/backups
retention=state dir persists outside git
DNB:
dnb=do not recreate duplicate updater or any second updater service/timer
dnb=do not use sudo pip, pip global, pip3 global, --break-system-packages for system Python updates
dnb=do not bypass guardrails for venv, dev-tool, or Android updates
dnb=do not remove AVDs, system-images, SDK cache, SDK root, Gradle/Kotlin project files
dnb=do not install Android Studio from unofficial package sources; use official Android Developers Linux archive and SHA
dnb=do not download Android Studio archive when installed build/release is current or remote build is unknown
dnb=do not embed Telegram tokens or package secrets
dnb=do not auto-update gem/cargo globals; keep report-only unless user changes project objective
BUG:
issue=fwupdmgr get-updates can return non-zero for no updatable devices; classify known no-update text as current
issue=sdkmanager license acceptance is noninteractive via yes pipe; rely on sdkmanager rc not yes SIGPIPE
RISK:
risk=sdkmanager --update can update platform-tools/cmdline-tools/build-tools/platforms and may run long; timeouts configurable via ANDROID_SDK_AUTO_UPDATE_* env
risk=Android Studio archive is large; precheck metadata and skip unknown/current remote build before download; preserve backup before replacing local tar install
risk=venv package upgrades can break projects; guardrails, per-venv logs, and failure continuation required
ROAD:
now=prompt927384 Android Studio large-download guard added
next=keep single-command invariant and docs current when updater scope changes
later=only add gem/cargo mutation if project objective explicitly expands
LINK:
meta=../../../mint-manual-updates/dev/project.metadata.json
human=../../human/projects/mint-manual-updates/overview.md
legacy=../../../mint-manual-updates/dev/legacy
repo=../../../mint-manual-updates
OPEN:
open=none_known_after_consolidation
