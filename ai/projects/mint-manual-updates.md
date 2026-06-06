META:
name=mint-manual-updates
slug=mint-manual-updates
path=/home/daniele/codex-workspace/mint-manual-updates
remote=none
branch=master
verified_at=2026-06-04T00:00:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
prompt=482917
PURPOSE:
purpose=User-systemd Linux Mint extra/manual updater with safe local Python venv maintenance
scope_primary=bin/mint-manual-updates
scope_extra=bin/mint-extra-updater remains consolidated Android/extra updater surface
STACK:
lang=Bash
db=SQLite optional via sqlite3 CLI for Android SDK history
platform=Linux Mint/Ubuntu user session
tools=systemd-user,flatpak,fwupdmgr,yt-dlp,pipx,rustup,npm,gem,cargo,curl,tar,sha256sum,sdkmanager,avdmanager,timeout,flock
MAP:
entry_extra=bin/mint-extra-updater
entry_manual=bin/mint-manual-updates
systemd_extra=systemd/user/mint-extra-updater.service,systemd/user/mint-extra-updater.timer
systemd_manual=systemd/user/mint-manual-updates.service,systemd/user/mint-manual-updates.timer
state_extra=~/.local/state/mint-extra-updater
state_manual=~/.local/state/mint-manual-updates
docs=dev/README.md,dev/TEST_PLAN.md,dev/CHANGELOG.md
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
extra_script=single Bash script with sections for flatpak,fwupd,yt-dlp,pipx,rustup,npm,report-only gem/cargo,Android Studio,Android SDK
manual_script=Bash service updater with apt/flatpak/snap/fwupd/global-pip-report/AppImage/Docker-report/local-venv-report and explicit venv upgrade modes
android_sdk=integrated in bin/mint-extra-updater; no dependency on retired android-sdk-auto-update project
global_command=bin/mint-extra-updater --run
no_android_only_mode=true
FLOW:
run=bin/mint-extra-updater --run
report=bin/mint-extra-updater --report
systemd=ExecStart=/home/daniele/codex-workspace/mint-manual-updates/bin/mint-extra-updater --run
manual_run=bin/mint-manual-updates --run
manual_venv_report=bin/mint-manual-updates --upgrade-venvs-report-only
manual_venv_upgrade=bin/mint-manual-updates --upgrade-venvs
android_flow=find SDK root from ANDROID_SDK_ROOT,ANDROID_HOME,~/Android/Sdk,/opt/android-sdk,~/android-sdk -> find sdkmanager -> sdkmanager --list -> history -> licenses -> sdkmanager --update
npm_flow=if npm exists -> npm outdated -g for log -> npm update -g during --run
android_studio_flow=find local tar install -> fetch https://developer.android.com/studio -> parse Linux archive URL and SHA -> download -> sha256sum verify -> extract -> compare product-info buildNumber -> backup old install -> replace install
venv_flow=discover under /home/daniele/codex-workspace patterns */venv/bin/python,*/.venv/bin/python,*/env/bin/python; prune .git,node_modules,build,dist,.gradle,.cache,__pycache__; normal mode report-only; --upgrade-venvs mutates only each venv via its python -m pip
INV:
no_duplicate_projects=android-sdk-auto-update is redundant after prompt 739204 consolidation
no_external_delegate=Android SDK updates must not call /home/daniele/codex-workspace/android-sdk-auto-update/android_sdk_auto_update.sh
android_update_scope=sdkmanager-managed installed packages only: tools/platform-tools/build-tools/platforms/cmdline-tools/emulator/extras/system-images when reported by sdkmanager
android_not_scope=Gradle/AGP/Kotlin project files, AVD deletion, SDK root deletion, PATH rewrites, secrets
npm_update_scope=npm global packages via npm update -g
android_studio_update_scope=local tar install, not flatpak/snap/apt package
global_pip_scope=report-only pip3 list --outdated; never sudo pip/global pip/global pip3 updates
venv_default_scope=/home/daniele/codex-workspace only; external roots require explicit --venvs-root PATH
venv_update_scope=only --upgrade-venvs; per-venv python -m pip only; guardrails before mutation; report-only stays non-mutating; continue on individual venv failures
guardrails_removed=Android license-presence precheck and external-wrapper requirement removed
minimum_checks=command/path availability, timeout, flock lock, sdkmanager exit codes
BUILD:
cmd=bash -n bin/mint-extra-updater
cmd_manual=bash -n bin/mint-manual-updates
install=bin/mint-extra-updater --install
TEST:
static=bash -n bin/mint-extra-updater
static_manual=bash -n bin/mint-manual-updates; shellcheck bin/mint-manual-updates if installed
systemd=systemd-analyze --user verify systemd/user/mint-extra-updater.service systemd/user/mint-extra-updater.timer
systemd_manual=systemd-analyze --user verify systemd/user/mint-manual-updates.service systemd/user/mint-manual-updates.timer
run=bin/mint-extra-updater --run
manual_smoke=bin/mint-manual-updates --help; bin/mint-manual-updates --dry-run; bin/mint-manual-updates --upgrade-venvs-report-only
DATA:
extra_logs=~/.local/state/mint-extra-updater/logs
extra_reports=~/.local/state/mint-extra-updater/reports,~/.local/state/mint-extra-updater/last-report.txt,~/.local/state/mint-extra-updater/last-run.json
manual_logs=~/.local/state/mint-manual-updates/mint-manual-updates.log
manual_reports=~/.local/state/mint-manual-updates/last-report.txt,~/.local/state/mint-manual-updates/last-run.json
venv_logs=~/.local/state/mint-manual-updates/venv-logs
android_history_csv=~/.local/state/mint-extra-updater/android-sdk-history/android_updates_history.csv
android_history_sqlite=~/.local/state/mint-extra-updater/android-sdk-history/android_updates_history.sqlite
android_history_table=android_update_history
android_history_fields=timestamp_utc,package,previous_version,new_version,operation,size_bytes,size_mb,exit_status,duration_seconds,hostname,username,sdk_path
android_studio_state=~/.local/state/mint-extra-updater/android-studio
android_studio_backups=~/.local/state/mint-extra-updater/android-studio/backups
migration=preserve old android-sdk-auto-update/logs before deleting redundant project
retention=state dir persists outside git
DNB:
dnb=do not create another updater project for Android SDK
dnb=do not call retired Android project after consolidation
dnb=do not add Android-only mode; all update work runs through bin/mint-extra-updater --run
dnb=do not remove AVDs, system-images, SDK cache, SDK root, Gradle/Kotlin project files
dnb=do not install Android Studio from unofficial package sources; use official Android Developers Linux archive and SHA
dnb=do not embed Telegram tokens or package secrets
dnb=do not keep npm report-only; update npm globals in --run
dnb=do not auto-update gem/cargo globals; keep report-only unless user changes project objective
dnb=do not use sudo pip, pip global, pip3 global, --break-system-packages for system Python updates
dnb=do not auto-upgrade venvs in normal --run/--dry-run; only --upgrade-venvs mutates venvs
dnb=do not scan/update venvs outside /home/daniele/codex-workspace unless --venvs-root PATH is explicit
BUG:
issue=fwupdmgr get-updates can return non-zero for no updatable devices; classify known no-update text as current
issue=sdkmanager license acceptance is noninteractive via yes pipe; rely on sdkmanager rc not yes SIGPIPE
RISK:
risk=sdkmanager --update can update platform-tools/cmdline-tools/build-tools/platforms and may run long; timeouts configurable via ANDROID_SDK_AUTO_UPDATE_* env
risk=Android Studio archive is large; preserve backup before replacing local tar install
risk=deleting redundant Android project can remove prior history; migrate logs first
risk=systemd PATH must include Android cmdline-tools path for timer runs
risk=venv package upgrades can break projects; default report-only, explicit upgrade only, per-venv logs and failure continuation
ROAD:
now=prompt482917 local venv support added to manual updater v5
next=keep AI doc current when updater scope changes
later=only add gem/cargo mutation if project objective explicitly expands
LINK:
meta=../../../mint-manual-updates/dev/project.metadata.json
human=../../human/projects/mint-manual-updates/overview.md
legacy=../../../mint-manual-updates/dev/legacy
repo=../../../mint-manual-updates
OPEN:
open=none_known_after_static_and_run_validation
