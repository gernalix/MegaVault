META:
name=WindowTabNotes
slug=windowtabnotes
path=/home/daniele/codex-workspace/WindowTabNotes
remote=git@github.com:gernalix/WindowTabNotes.git
branch=codex/prompt-581472
verified_commit=19979db
verified_at=2026-06-10T23:43:52+02:00
megavault_branch=codex/prompt-731845-kuma-operational-runbook
protocol=MEGAVAULT_PROTOCOL.md:v8

PURPOSE:
purpose=Linux/X11 + Chrome/Firefox tab note overlay; stores notes in local SQLite and binds each note to a normal window, browser tab, or workspace context.

STACK:
lang=Python,JavaScript,Shell
ui=GTK via PyGObject,Chrome MV3 extension,Firefox MV3 extension,rofi
db=SQLite WAL
service=systemd --user windowtabnotes.service
platform=Linux Mint/XFCE/X11,Chrome/Chromium Native Messaging,Firefox Native Messaging

MAP:
entry=system/bin/windowtabnotes -> python3 -m windowtabnotes.cli
status=system/bin/windowtabnotes-status -> windowtabnotes status
daemon=system/windowtabnotes/daemon.py,system/windowtabnotes/active_watch.py
db=system/windowtabnotes/db.py
native=system/bin/windowtabnotes-native-host,system/windowtabnotes/native_host.py,system/windowtabnotes/api.py
chrome=browser-extension/manifest.json,browser-extension/service_worker.js,browser-extension/content_script.js,browser-extension/popup.js
firefox=browser-extension-firefox/manifest.json + copied shared assets from browser-extension/; installer keeps Firefox copy synced because symlink packaging fails
firefox_status=system/bin/windowtabnotes firefox-status --json and firefox-proof --json -> active PID/profile lock, expected profile mismatch, extensions.json registration, persistent app-profile vs temporary/runtime false positive, real Gecko id, native manifests, native ping, standard-Firefox permanent-install limit
ui=system/windowtabnotes/gtk_ui.py,browser-extension/dashboard.html,browser-extension/dashboard.js
search=system/windowtabnotes/rofi.py
shortcuts=system/windowtabnotes/shortcuts.py
systemd=system/systemd/windowtabnotes.service.in,~/.config/systemd/user/windowtabnotes.service
install=system/scripts/install.sh
install_firefox=system/scripts/install-firefox.sh syncs self-contained browser-extension-firefox assets from browser-extension before native manifest/status checks
install_firefox_dev=system/scripts/install-firefox-developer-edition.sh installs/verifies user-local Firefox Developer Edition and uses the real dev-edition-default profile for persistent unsigned add-on use
test_firefox=system/scripts/test-firefox-extension.sh -> Selenium real Firefox E2E using temporary add-on by default or persistent Developer Edition add-on with WTN_FIREFOX_ADDON_TEMPORARY=0; verifies three unique tabs, service worker SAVE_NOTE_TEXT through Native Messaging, native metrics delta, DB text/context probe, service restart, browser reopen, and overlay visibility probe
tests=tests/test_context_persistence.py
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated,__pycache__

ARCH:
cli=argparse commands version/init-db/daemon/status/check/native-debug/search/overlay/shortcuts
daemon=active window watcher: xprop -spy _NET_ACTIVE_WINDOW + conservative fallback poll + browser active-tab metadata
windows=wmctrl lists normal windows; xprop/xdotool read active id,title,class,pid,geometry
overlay=GTK note process launched per note; overlay_runtime tracks visible note in DB metadata and cleans stale overlay windows
db=single local SQLite DB; note rows keep relational context_id plus v5 denormalized context snapshot
native_host=Chrome starts stdio host per native message; wrapper and Python metrics throttle reconnect storms
browser_bridge=shared service_worker.js syncs open tabs/active tab to native host; backend stores browser_tabs and active_browser_tab metadata
search=rofi/global search reads DB search index and queues Chrome focus requests through DB metadata

FLOW:
normal_window=daemon active_window -> upsert_window_context -> ensure/create note -> notes.context_* snapshot -> GTK overlay
browser_tab=Chrome/Firefox service_worker snapshotTab -> native UPSERT_TAB/SYNC_OPEN_TABS -> upsert_browser_tab -> note_for_browser_tab -> notes.context_url/title/tab/window snapshot -> GTK overlay when requested
chrome_focus=search queues chrome_focus_request metadata -> service_worker GET_FOCUS_REQUEST poll -> chrome.tabs/window focus or close
save_text=content/GTK -> native SAVE_NOTE_TEXT or local UI -> db.update_note_text -> refresh context snapshot -> notes.updated_at
service=~/.config/systemd/user/windowtabnotes.service -> system/bin/windowtabnotes daemon -> Restart=always
service_prompt_739284=enabled+active; MainPID restarts after SIGTERM; linger=yes; ExecStart=/home/daniele/codex-workspace/WindowTabNotes/system/bin/windowtabnotes daemon; WorkingDirectory=/home/daniele/codex-workspace/WindowTabNotes

INV:
data=do_not_delete_real_notes_during_tests_or_repair
data=DB path default ~/.local/share/windowtabnotes/windowtabnotes.sqlite3; override WTN_DB
data=notes table owns text, created_at, updated_at, context_type, context_id, geometry, visibility, context_app, context_title, context_window_id, context_workspace, context_url, context_browser_tab_id, context_browser_window_id, context_key
data=window_contexts owns window_id,app_class,title,workspace,pid,wm_name,last_seen_at
data=browser_tabs owns browser_tab_id,browser_window_id,url,title,fav_icon_url,active,incognito,index,profile_key,normalized_url,note_key,last_seen_at
data=browser note identity prefers normalized_url+profile note_key; Chrome keeps raw positive browser tab/window ids; Firefox sends scoped negative ids with profile_key=firefox:default to avoid collisions with Chrome/old rows
service=user unit must stay enabled and active; linger currently yes on host
service=daemon must log and skip transient sqlite locked/xdotool timeout rather than exiting
service=human_status=systemctl --user status windowtabnotes.service --no-pager; logs=journalctl --user -u windowtabnotes.service -n 80 --no-pager; restart=systemctl --user restart windowtabnotes.service
chrome=Native Messaging host name com.windowtabnotes.host; installed manifests under Chrome/Chromium NativeMessagingHosts
firefox=Native Messaging host name com.windowtabnotes.host; add-on id windowtabnotes@local; manifest under ~/.mozilla/native-messaging-hosts/
firefox=profile_current=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release; standard Firefox 151 cannot permanently install unsigned local add-on; temp load is required unless signed/dev-edition path is used
firefox_dev=browser=/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes; install_dir=/home/daniele/.local/opt/firefox-developer-edition; version=Mozilla Firefox 152.0b10; real_profile=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default; persistent_addon=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default/extensions/windowtabnotes@local.xpi; xpinstall.signatures.required=false; launcher uses -no-remote -profile real_profile
firefox_dev=about_addons_proof=/tmp/windowtabnotes-firefox-addons-proof.png shows WindowTabNotes visible and enabled in real Firefox Developer Edition; unsigned warning expected
firefox=browser-extension-firefox must be self-contained; symlinks make web-ext/Firefox packaging report missing background/content/icon files
firefox=Prompt #594271 fixed runtime path: standard Firefox profile still cannot permanently load unsigned add-on, but Selenium temporary install verifies add-on id windowtabnotes@local, native messaging, DB contexts, and visible overlays end-to-end
ux=do not break overlay/search behavior while changing persistence/service code
version=monotonic integer in system/windowtabnotes/version.py,browser-extension/manifest.json,browser-extension-firefox/manifest.json

BUILD:
cmd=none
run=system/bin/windowtabnotes <command>
install_chrome=system/scripts/install.sh --extension-id <chrome_extension_id>
install_firefox=system/scripts/install-firefox.sh [windowtabnotes@local]
install_firefox_dev=system/scripts/install-firefox-developer-edition.sh
deps=python3,python3-gi,GTK3,sqlite3,rofi,wmctrl,xdotool,xprop,jq optional,pipx optional for Selenium Firefox E2E

TEST:
compile=python3 -m compileall -q system/windowtabnotes tests
unit=PYTHONPATH=system python3 -m unittest tests/test_context_persistence.py
service=systemctl --user is-active windowtabnotes.service; systemctl --user is-enabled windowtabnotes.service; journalctl --user -u windowtabnotes.service --since '2 minutes ago'
status=system/bin/windowtabnotes-status --json
prompt_739284=daemon-reload+enable --now; is-enabled=enabled; is-active=active; status active running; journal readable; restart active; SIGTERM MainPID -> NRestarts=1 active; dashboard-debug ok; search-debug ok; overlay-debug ok; check --json db ok with window_sync skipped on live DB lock
native_chrome=system/bin/windowtabnotes native-debug --extension-id <chrome_extension_id> --json
native_firefox=system/bin/windowtabnotes native-debug --browser firefox --firefox-extension-id windowtabnotes@local --json
firefox_status=system/bin/windowtabnotes firefox-status --json
firefox_proof=WTN_FIREFOX_BINARY=/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes WTN_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default system/bin/windowtabnotes firefox-proof --json
firefox_lint=npx --yes web-ext@10.3.0 lint --source-dir browser-extension-firefox --self-hosted
firefox_smoke=WTN_FIREFOX_TEST_SECONDS=75 system/scripts/test-firefox-extension.sh; expected ok true, addon_id=windowtabnotes@local, firefox_status.ok=true for temp profile, native metrics total_messages+UPSERT_TAB increase, three DB note ids, three saved note texts, service_restart.ok=true, first+second session overlay context count=3
firefox_dev_persistent=WTN_FIREFOX_BINARY=/home/daniele/.local/opt/firefox-developer-edition/firefox WTN_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default WTN_FIREFOX_ADDON_TEMPORARY=0 WTN_FIREFOX_TEST_SECONDS=120 system/scripts/test-firefox-extension.sh; expected ok true, addon temporary false, third session addon_install.attempted false, app-profile extension active, first/second/third overlay context count=3, three saved note texts

DATA:
DB=SQLite
Schema=5
Path=~/.local/share/windowtabnotes/windowtabnotes.sqlite3
Override=WTN_DB
Log=~/.cache/windowtabnotes/windowtabnotes.log
NativeMetrics=~/.cache/windowtabnotes/native_host_metrics.json
Settings=~/.config/windowtabnotes/settings.json
Migration=v5 adds note context snapshot columns and backfills from extant window_contexts/browser_tabs/workspaces
Backup=manual copy DB before destructive recovery; WAL active
Restore=UNKNOWN
Import=UNKNOWN
Export=UNKNOWN
Retention=logs rotate; native metrics overwrite JSON

DNB:
* real_user_notes
* browser-extension/service_worker.js tab sync/focus request polling
* browser-extension-firefox/manifest.json must use background.scripts; Firefox does not support background.service_worker
* system/windowtabnotes/rofi.py search launcher free-text behavior
* overlay_runtime cleanup state and manual overlay suppression
* Native Messaging host manifest path/id
* MegaVault metadata+AI/Human links; legacy docs are historical only

BUG:
issue=Old journal showed daemon crashes from sqlite3.OperationalError database is locked and subprocess.TimeoutExpired xdotool getactivewindow.
fix=v21 active_watch skips/logs transient DB lock and xdotool timeout; service Restart=always.
issue=381 legacy browser_tab notes on live DB had no reconstructable tab row at v5 migration time.
impact=URL/title snapshot cannot be invented for those orphan historical notes; future writes and notes with extant context are snapshotted.
issue=Native host metrics show high GET_FOCUS_REQUEST starts/rate-limited starts.
impact=Chrome bridge works but polling can be noisy; monitor via windowtabnotes-status/native-host-status.
issue=v21 daemon stayed active but showed no overlay for windows without pre-existing notes.
fix=v22 handle_active_window uses create_if_missing=True for the active context; verified overlay_count=1/open_notes=1.
issue=Prompt #739284 live `check --json` failed on transient SQLite lock while daemon was active.
fix=check_status retries DB init and reports window_sync separately; DB ok returns exit 0 even when live sync is skipped due daemon-held lock.
issue=Prompt #618739 Firefox current profile did not work.
cause=active profile had stale `windowtabnotes@local` UUID/toolbar/tmpExtDir prefs but no loaded add-on in extensions.json; Firefox source dir was symlink-based and web-ext lint showed missing service_worker/content/icons.
fix=browser-extension-firefox self-contained; installer resyncs assets, writes both Firefox native manifest locations, and `firefox-status` exposes active profile/add-on/native truth.
test=web-ext real Firefox smoke loaded temp add-on and increased native metrics total_messages/UPSERT_TAB/SYNC_OPEN_TABS/GET_FOCUS_REQUEST.
issue=Prompt #594271 Firefox tabs reached native host but overlays did not follow Firefox tabs.
cause=daemon only treated Chrome windows as browser-tab overlay contexts; Firefox temp runs also reused small raw tab ids against DB UNIQUE(browser_tab_id), so Firefox rows could overwrite old/Chrome contexts and inherit hidden notes.
fix=v23 active_watch treats Firefox as browser window, exposes active_browser_tab debug, Firefox service_worker sends scoped negative tab/window ids with profile_key=firefox:default, firefox-status detects temporary WebDriver/web-ext runtimes, native ping retries transient SQLite locks, Selenium E2E test installs temporary add-on and verifies three tab overlays.
test=2026-06-10T17:03:22+02:00 `system/scripts/test-firefox-extension.sh` ok true; URLs example.com/mozilla.org/example.org; addon_id windowtabnotes@local; firefox_status ok true; native total_messages 59209->59232 and UPSERT_TAB 19709->19720; distinct_note_ids=3; distinct_overlay_contexts=3.
issue=Prompt #428673 Firefox real-profile equivalence needed stronger proof.
cause=Real standard Firefox profile had native manifests and stale toolbar/tmpExtDir state but did not load unsigned `windowtabnotes@local`; earlier smoke did not prove text persistence through Firefox service_worker.
fix=`system/scripts/test-firefox-extension.sh` now uses query-marker URLs to avoid stale domain notes, starts Firefox temporary add-on with `-remote-allow-system-access`, verifies service_worker `SAVE_NOTE_TEXT` via a `moz-extension://...` page, checks DB text after every save, restarts `windowtabnotes.service`, then opens a second Firefox session and verifies persisted notes plus overlay contexts again.
test=2026-06-10T22:28:34+02:00 `WTN_FIREFOX_TEST_SECONDS=75 system/scripts/test-firefox-extension.sh` ok true; Firefox 151.0.4; addon_id windowtabnotes@local; native total_messages 60541->60606 and UPSERT_TAB 19972->20002; three note ids/texts saved; service_restart MainPID changed 1232202->1242983 active; first and second session distinct overlay context count=3.
limit=Real `/home/daniele/.config/mozilla/firefox/50b1zmic.default-release` on standard Firefox still cannot permanently load unsigned local extension; `firefox-status --json` reports `extension_not_loaded_in_active_profile`. Use temporary load for tests, Mozilla-signed package, or Developer/Nightly/ESR with `xpinstall.signatures.required=false`.
issue=Prompt #739516 required real persistent Firefox install equivalent to Chrome.
fix=Installed user-local Firefox Developer Edition at `/home/daniele/.local/opt/firefox-developer-edition`, wrapper `/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes`, dedicated profile `/home/daniele/.config/windowtabnotes/firefox-developer-profile`, and persistent unsigned `windowtabnotes@local` with `xpinstall.signatures.required=false`; `firefox-status` now accepts explicit WTN_FIREFOX_BINARY/WTN_FIREFOX_PROFILE and checks actual `.parentlock` holders instead of file existence.
test=2026-06-10T23:04:06+02:00 `WTN_FIREFOX_BINARY=/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes WTN_FIREFOX_PROFILE=/home/daniele/.config/windowtabnotes/firefox-developer-profile WTN_FIREFOX_ADDON_TEMPORARY=0 WTN_FIREFOX_TEST_SECONDS=120 system/scripts/test-firefox-extension.sh` ok true; Developer Edition 152.0b10; add-on location app-profile; temporarily_installed null; third session did not call install_addon; DB backup `/home/daniele/.cache/windowtabnotes/db-backups/20260610-230406`; report `/home/daniele/.cache/windowtabnotes/firefox-e2e/firefox-dev-persistent-e2e-final-20260610.json`; three tabs example.com/example.net/example.org, three notes/texts, service_restart ok, first/second/third overlay context count=3.
issue=Prompt #184902 found the previous persistent Firefox report was not verified against the visible Developer Edition `about:addons`.
cause=The XPI was installed in `/home/daniele/.config/windowtabnotes/firefox-developer-profile`, while the real Firefox Developer Edition window used `/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default`; `firefox-status` could also prefer the wrong locked Firefox profile when standard Firefox and Developer Edition were both running.
fix=Installed `windowtabnotes@local` persistently into the real dev-edition-default profile, rewrote the launcher to use `-no-remote -profile /home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default`, and added `firefox-proof`/status fields for active PID, profile lock PIDs, profile mismatch, extensions.json registration, install_kind, visible_in_about_addons_expected, and temporary false positives.
test=2026-06-10T23:37:38+02:00 `WTN_FIREFOX_BINARY=/home/daniele/.local/opt/firefox-developer-edition/firefox WTN_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default WTN_FIREFOX_ADDON_TEMPORARY=0 WTN_FIREFOX_TEST_SECONDS=120 system/scripts/test-firefox-extension.sh` ok true; third session addon_install.attempted false; first/second/third overlay context count=3; three notes persisted after service restart; Chrome native-debug ok; visual proof `/tmp/windowtabnotes-firefox-addons-proof.png` shows WindowTabNotes enabled in real Developer Edition about:addons.

RISK:
risk=SQLite lock contention from daemon + many Chrome native-host invocations.
risk=Chrome unpacked extension may keep stale service_worker until reloaded in chrome://extensions.
risk=xdotool/xprop can timeout or fail under X11/session transitions.
risk=Killing native-host or Chrome processes can interrupt active browser bridge; avoid unless user approves.
risk=Deleting orphan browser notes would destroy user data; do not clean automatically.
risk=`journalctl -n 80` can include older Jun 01 crash traces; current status command uses recent error scan and reports last_service_error empty after Jun 07 restart/kill tests.
risk=Firefox standard release blocks permanent unsigned local extensions; real default-release can show stale UUID/tmpExtDir without loaded add-on. Persistent local success currently belongs to Firefox Developer Edition real profile `/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default`; do not claim standard Firefox permanent support unless a signed package is installed there.

ROAD:
now=v23 Firefox tab overlays pass temporary-add-on E2E and persistent Firefox Developer Edition E2E on the real dev-edition-default profile; daemon polls less aggressively; status/native diagnostics tolerate transient DB locks
next=reduce Native Messaging GET_FOCUS_REQUEST process churn if Chrome/Firefox bridge remains noisy
later=explicit backup/export/restore commands

LINK:
meta=../../../WindowTabNotes/dev/project.metadata.json
human=../../human/projects/windowtabnotes/overview.md
changelog=../../human/projects/windowtabnotes/changelog.md
legacy=../../../WindowTabNotes/dev/legacy
repo=../../../WindowTabNotes

OPEN:
open=No safe CLI command exists to create/read/delete a real test note transactionally; current tests use temp DB.
open=381 historical Chrome notes lack recoverable URL because referenced browser_tabs rows were absent during v5 migration.
open=Build/package process remains undefined beyond scripts/install.sh.
