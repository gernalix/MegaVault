META:
name=android
slug=android
path=/home/daniele/codex-workspace/projects/android
remote=none
branch=home-git-worktree
verified_commit=none
verified_at=2026-06-05T11:50:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
PURPOSE:
purpose=Host-local Android helper project; currently owns Linux Mint user service for ADB Wi-Fi Debug auto-connect.
STACK:
lang=Python,Markdown
fw=none
db=none
platform=Linux Mint user systemd,Android platform-tools adb,Avahi mDNS
tools=adb,avahi-browse,systemctl --user,zenity,notify-send
MAP:
entry=adb-wifi-autoconnect.py
ui=none; optional zenity/terminal pairing UI disabled unless ADB_WIFI_AUTOCONNECT_AUTO_PAIR_UI=1
core=adb-wifi-autoconnect.py
db=none
scripts=adb-wifi-autoconnect.py
docs=README-adb-wifi-autoconnect.md
config=~/.config/adb-wifi-autoconnect/config.json
unit=~/.config/systemd/user/adb-wifi-autoconnect.service
installed=~/.local/bin/adb-wifi-autoconnect
state=~/.local/state/adb-wifi-autoconnect/state.json
log=~/.local/state/adb-wifi-autoconnect/adb-wifi-autoconnect.log
tests=python3 -m py_compile adb-wifi-autoconnect.py; adb-wifi-autoconnect scan-now; adb-wifi-autoconnect status
avoid=creating duplicate ADB services,adb kill-server,disconnecting existing devices,saving pairing codes
ARCH:
service=adb-wifi-autoconnect.service Type=simple Restart=always RestartSec=30
loop=run_forever -> scan_once every ADB_WIFI_AUTOCONNECT_POLL default 15s
discovery=adb mdns services + avahi-browse _adb-tls-connect._tcp + _adb-tls-pairing._tcp
connect=adb connect HOST:PORT per endpoint; retry throttled by CONNECT_RETRY_SECONDS=90
pairing=manual by default; service records pairing endpoints but does not open focus-stealing UI unless ADB_WIFI_AUTOCONNECT_AUTO_PAIR_UI=1; code never persisted
identity=config profiles match host or mDNS/ADB tokens; endpoint records include profile_id,label,service_id,hostname,mdns_name
profiles=default pixel host 192.168.1.37 tokens Pixel_8a,akita,52131JEKB01070; default tcl host 192.168.1.200 tokens 6102H,QCGADUVOSSEYFES4,Android-3.local
multi_device=allow_unknown_devices=true; each endpoint retried independently; connected host suppresses stale same-host ports without disconnecting others
FLOW:
install=./adb-wifi-autoconnect.py install -> copies script, writes user unit, creates default config, daemon-reload, enable
start=systemctl --user restart adb-wifi-autoconnect.service
status=adb-wifi-autoconnect status -> systemd,adb devices -l,mdns,profiles,endpoints,log tail
logs=journalctl --user -u adb-wifi-autoconnect.service; tail ~/.local/state/adb-wifi-autoconnect/adb-wifi-autoconnect.log
pair=Android Developer options -> Wireless debugging -> Pair device with pairing code; manual terminal pairing default
pair_manual=adb pair HOST:PORT CODE; adb connect HOST:PORT
INV:
script=adb-wifi-autoconnect.py v0.3.0
unit=~/.config/systemd/user/adb-wifi-autoconnect.service enabled
timer=none
db=none
state_json=state.json devices + profiles + pair_dialogs + last_adb_start_epoch
config_json=config.json devices[] + allow_unknown_devices
log_rotation=1MiB app log + .1
BUILD:
cmd=python3 -m py_compile /home/daniele/codex-workspace/projects/android/adb-wifi-autoconnect.py
install=cd /home/daniele/codex-workspace/projects/android && ./adb-wifi-autoconnect.py install
TEST:
syntax=python3 -m py_compile adb-wifi-autoconnect.py
systemd=systemctl --user status adb-wifi-autoconnect.service --no-pager
live=adb-wifi-autoconnect scan-now && adb-wifi-autoconnect status
device_truth=adb devices -l authoritative for connected/offline state; mDNS is only advertisement
DATA:
db=none
paths=~/.config/adb-wifi-autoconnect/config.json; ~/.local/state/adb-wifi-autoconnect/state.json; ~/.local/state/adb-wifi-autoconnect/adb-wifi-autoconnect.log
backup=not required; config is small JSON; state rebuilds from discovery
secrets=pairing codes never stored
DNB:
dnb=Do not create parallel systemd units or duplicate project slugs.
dnb=Do not run adb kill-server during service repair unless user explicitly approves; it can disrupt active Android work.
dnb=Do not claim Pixel/TCL connected from mDNS alone; verify with adb devices -l.
dnb=Do not save pairing codes in config,state,logs,docs.
BUG:
issue=pre-2026-06-05 MegaVault missing android project registration; service existed only in filesystem/.codexmeta/README and generic service reports.
issue=ADB mDNS advertisements can be stale; connect may return Connection refused or failed while service remains healthy.
issue=pre-pair TCL 6102H advertised 192.168.1.200:34719 with Avahi TXT name=6102H but adb connect failed until first-time adb pair.
issue=2026-06-05 pairing UI stole focus during manual entry; auto pairing UI disabled by default.
RISK:
risk=Wireless debugging ports change frequently; endpoint history must not be treated as current connectivity.
risk=Multiple Android devices can share network; profile matching must remain token/host based and allow unknown devices unless operator disables it.
risk=ADB server crashes can appear in journal; service keeps polling and restarts ADB server periodically instead of killing sessions.
ROAD:
now=Pixel+TCL multi-device profiles, per-device logs/state, retry/reconnect loop.
now=2026-06-05 TCL paired and connected as 192.168.1.200:34719 product=6102H_EEA model=6102H device=Cruze_Lite_S
next=Optional health alert when known device is advertised but fails connect for N consecutive attempts without pairing endpoint.
later=Optional CLI to edit config profiles without manual JSON edits.
LINK:
meta=../../../projects/android/dev/project.metadata.json
human=../../human/projects/android/overview.md
legacy=../../../projects/android/.codexmeta
repo=../../../projects/android
OPEN:
open=Pixel not connected at final check; Pixel pairing endpoint advertised, but adb devices -l only shows TCL.
