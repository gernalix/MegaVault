META:
activity_id=638417
timestamp_utc=2026-07-13T08:21:00Z
host=fedora Fedora_Linux_44_Workstation GNOME_50.3 Wayland
result=PENDING_TEST_POST_LOGIN
scope=AutoKey desktop integration,Wayland implementation,input injection,clipboard,launcher,autostart,rollback

CAUSE:
visual=The Fedora desktop file was valid but AutoKey normally started background-only;showTrayIcon=true depended on an AppIndicator tray not present in the active GNOME extension set. The GTK scale-factor critical was reproducible but nonfatal and did not explain native input failure.
functional=Fedora autokey 0.96.0-16.fc44 selects XRecord and upstream documents the official application as X11-only. Real kernel input proved no hotkey or phrase detection in GNOME Text Editor Wayland,while XWayland hotkey detection worked.
fork_release_defect=AutoKey for Wayland 0.97.4 captured evdev input but cloned all keyboard and mouse capabilities into one uinput device. An incomplete EV_ABS set made GNOME Shell 50/libinput log missing tablet capabilities resolution and ignore the entire device. WaylandClipboard also called wl-paste synchronously without timeout and could hang when no clipboard owner existed.

IMPLEMENTATION:
name=AutoKey for Wayland
version=0.97.4-0.fc44
origin=signed Fedora COPR dlk/autokey;upstream https://github.com/dlk3/autokey-wayland
release=v0.97.4
commit=a41c8a0a145ee00ffb7e197c3b5dd26a3e946e7e
rpm_signature_key=934ab84ccb870b1c;fingerprint=ECCCE60ADF70C09F55B4E1E5934AB84CCB870B1C
install_path=/usr/bin/autokey-gtk+/usr/lib/python3.14/site-packages/autokey
compat_wrapper=/home/daniele/.local/libexec/autokey-wayland-fedora44
wrapper_behavior=Monkeypatch only process-local evdev.UInput.from_device for AutoKey named device to filter EV_ABS;preserve EV_KEY+EV_REL;bound wl-paste reads to 1s and treat absent owner as empty. No RPM file changed;rpm -V clean.
extension=/home/daniele/.local/share/gnome-shell/extensions/autokey-gnome-extension@autokey;version=0.2;shell_versions=45-50;enabled_in_gsettings=yes;live_discovery=pending_relogin
extension_static_validation=PASS;metadata JSON valid and gnome-extensions pack produced a valid archive;temporary archive removed

PACKAGES:
upgraded=autokey-common_0.96.0-16.fc44_to_0.97.4-0.fc44;autokey-gtk_0.96.0-16.fc44_to_0.97.4-0.fc44
installed=gnome-extensions-app_50.2-1.fc44;python3-magic_0.4.27-16.fc44;python3-pyasyncore_1.0.4-6.fc44;python3-pydbus_0.6.0-34.fc44
removed=python3-file-magic_5.46-3.fc44;replaced_by_python3-magic because package conflict and only old AutoKey depended on it
preexisting_required=wl-clipboard_2.2.1;python3-evdev_1.9.3;python3-pyudev_0.24.4
not_installed=xautomation_1.09;provides visgrep,png2pat,xte,xmousepos;optional X11-only image/input helpers not required by final Wayland architecture
dnf_check=PASS

FILES:
created=/home/daniele/.local/libexec/autokey-wayland-fedora44
created=/home/daniele/.local/share/applications/autokey-gtk.desktop;same desktop ID overrides system entry so Gio/GNOME sees exactly one logical AutoKey
created=/home/daniele/.config/systemd/user/autokey.service;enabled on graphical-session.target;PartOf+After graphical-session.target;Restart=on-failure 5s;KillMode=mixed
created=/home/daniele/.local/bin/autokey-post-login-638417-check
created=/home/daniele/.config/autokey/data/638417 Tests;retained proof hotkey Ctrl+Alt+Shift+F12 and phrase aliases
modified=/home/daniele/.config/autokey/autokey.json;version 0.97.4;isFirstRun=false;showTrayIcon=false;user phrases/scripts preserved
modified=org.gnome.shell enabled-extensions adds autokey-gnome-extension@autokey;existing background-logo preserved
system_state=input group includes daniele;/dev/uinput root:input 0660 after udev reload+trigger

DESKTOP:
launcher_validation=desktop-file-validate PASS;absolute Exec and TryExec point to wrapper;Terminal=false;NoDisplay=false;Icon=autokey exists
logical_menu_entries=1 by Gio AppInfo;desktop ID autokey-gtk.desktop;name AutoKey
gui=PASS;second -c activation displayed one active AT-SPI frame named AutoKey and retained one application process
tray=disabled intentionally;active GNOME session had no AppIndicator extension;launcher opens or reveals GUI without tray dependency
autostart=single systemd user unit enabled;no user or system XDG AutoKey autostart found
current_state=service enabled+inactive and no AutoKey process;next login required so user manager gains input group and GNOME Shell discovers extension

TESTS:
standard_0.96_GTK_Wayland=FAIL;real uinput typed abbreviation remained literal and hotkey marker absent
standard_0.96_Zenity_XWayland=PARTIAL;XRecord detected hotkey and phrase but clipboard injection failed;proves visual warning was not root cause
fork_0.97.4_before_wrapper=FAIL;input captured but journal GNOME Shell logged libinput missing tablet capabilities resolution and ignored virtual device
wrapper_device=PASS;/proc/bus/input/devices exposes autokey mouse and keyboard with EV_KEY+EV_REL and no EV_ABS;GNOME journal contains no ignore line
GTK_Wayland_phrase=PASS;real kernel uinput abbreviation aktest638417x became exact AutoKey Wayland test 638417 OK in GNOME Text Editor;final send mode Ctrl+V clipboard
GTK_Wayland_hotkey=PASS;real Ctrl+Alt+Shift+F12 created marker with exact AutoKey test OK and notify-send notification
Chrome_Wayland_classification=PASS;isolated Chrome command line contained --ozone-platform=wayland and had no X11 window;textarea result verified through DevTools after real kernel input
Chrome_Wayland_phrase=PASS;exact output AutoKey Wayland test 638417 OK with clipboard initially ownerless
Chrome_Wayland_hotkey=PASS;exact marker AutoKey test OK
Zenity_XWayland_classification=PASS;xwininfo found X11 window 0x1e00004 class zenity.zenity
Zenity_XWayland_phrase=PASS;exact clipboard expansion
Zenity_XWayland_hotkey=PASS;exact marker AutoKey test OK
clipboard=PASS;WaylandClipboard direct set/get and final ownerless clipboard expansion both verified;wrapper timeout prevented hang and AutoKey restored prior/empty clipboard after paste
single_instance=PASS;second configuration activation revealed GUI and process count remained one
restart_core=PASS;QA service restarted repeatedly,configuration reloaded and hotkey/phrase persisted
menu_launch_real=PENDING_POST_LOGIN;current Shell cannot discover an extension installed after Shell startup
autostart_real=PENDING_POST_LOGIN
logout_login=PENDING_POST_LOGIN;not forced because Chrome,Codex,and other user applications were open
journal=PASS_WITH_NONFATAL_WARNINGS;no coredump,traceback,or final libinput reject;libayatana deprecation and gtk_widget_get_scale_factor critical do not stop service or GUI

LAYOUT_LIMIT:
primary_layout=Italian;secondary=US
finding=Fork 0.97.4 internal abbreviation lookup assumes US punctuation,so physical Italian Shift+comma is seen internally as comma even though GNOME types semicolon.
mitigation=Retained requested ;aktest638417 plus layout-independent alias aktest638417x;all decisive tests use the alias. No global layout was changed.

BACKUP:
autokey=/home/daniele/backups/autokey/638417-20260713T094500+0200;mode=0700;contains pre-change config,post-stop config,local share log,and system desktop copy
incident_db=/home/daniele/sync_root/db/backups/incident_registry.activity-638417.pre-update.20260713T082100Z.sqlite;mode=0600
incident=AUTOKEY_FEDORA44_WAYLAND_INPUT_BLOCKED;SQLite upsert+event append+checkpoint+integrity_check ok;status MITIGATED pending post-login

CLEANUP:
removed=temporary kernel emitter,preflight stub,AT-SPI helper,isolated Chrome profile,Zenity/editor temp files,markers,wl-copy QA owner,transient units and all QA processes
final_processes=none;autokey.service inactive until next login
duplicates=no competing RPM/pip/pipx/Flatpak/source implementation;one RPM implementation+one process-local compatibility wrapper;one logical launcher;one autostart

ROLLBACK:
step1=systemctl --user disable --now autokey.service
step2=remove user unit,launcher,wrapper,post-login checker,and test folder only after optionally restoring /home/daniele/backups/autokey/638417-20260713T094500+0200/config-post-stop/autokey
step3=gnome-extensions disable autokey-gnome-extension@autokey;remove its user directory after logout;remove UUID from org.gnome.shell enabled-extensions while preserving other entries
step4=sudo dnf copr disable dlk/autokey;sudo dnf install --allowerasing autokey-gtk-0.96.0-16.fc44 autokey-common-0.96.0-16.fc44 python3-file-magic;or sudo dnf remove autokey-gtk autokey-common for complete removal
step5=sudo gpasswd -d daniele input only if no other software requires that membership;logout/login;verify /dev/uinput rule state from remaining packages
step6=restore chosen backup configuration without deleting user phrases/scripts;run dnf check and desktop-file-validate

POST_LOGIN:
command=/home/daniele/.local/bin/autokey-post-login-638417-check
expected=extension listed/enabled;autokey.service active;one wrapper process;UInputInterface and compatibility log;one GNOME logical launcher;manual menu+GTK+Chrome checks PASS
status_boundary=Do not change incident to RESOLVED or activity to PASS until this checklist succeeds in a fresh graphical login.
