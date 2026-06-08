# SOFTWARE_INVENTORY
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=command_versions_live_2026-06-08+dpkg+flatpak+HOST_PROFILE
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/SOFTWARE_INVENTORY.md

RUNTIME_TOOLS:
tool=codex;path=/home/daniele/.npm-global/bin/codex;version=codex-cli_0.137.0;critical=yes
tool=gh;path=/usr/bin/gh;version=2.45.0;critical=yes
tool=git;path=/usr/bin/git;version=2.43.0;critical=yes
tool=python3;path=/usr/bin/python3;version=3.12.3;critical=yes
tool=sqlite3;path=/home/daniele/Android/Sdk/platform-tools/sqlite3;version=3.50.6;critical=yes;note=PATH_precedes_apt_sqlite3
tool=sqlite3_apt;package=sqlite3;version=3.45.1-1ubuntu2.5;critical=yes
tool=rg;path=/home/daniele/.npm-global/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg;critical=yes
tool=curl;path=/usr/bin/curl;critical=yes
tool=jq;path=/usr/bin/jq;critical=yes
tool=systemctl;path=/usr/bin/systemctl;critical=yes

ANDROID_TOOLS:
tool=adb;path=/home/daniele/Android/Sdk/platform-tools/adb;version=1.0.41;critical=yes
tool=sdkmanager;path=/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager;version=20.0;critical=yes
tool=java;path=/home/daniele/.local/share/jdks/jdk-17.0.19+10/bin/java;version=openjdk_17.0.19_2026-04-21;critical=yes
tool=Android_Studio;path=/home/daniele/.config/Google/AndroidStudio2026.1.1;version=UNKNOWN;critical=yes

NODE_TOOLS:
tool=node;path=/usr/bin/node;version=v24.16.0;critical=yes
tool=npm;path=/home/daniele/.npm-global/bin/npm;version=11.16.0;critical=yes

BACKUP_STORAGE_TOOLS:
tool=restic;path=/usr/bin/restic;version=0.16.4;critical=yes
tool=cryptsetup;path=/usr/sbin/cryptsetup;version=2.7.0-1ubuntu4.2;critical=yes
tool=veracrypt;path=/usr/bin/veracrypt;version=1.26.24-1~ubuntu24.04-1;critical=yes
tool=rclone;path=UNKNOWN;version=UNKNOWN;critical=no

NETWORK_REMOTE_TOOLS:
tool=tailscale;path=/usr/bin/tailscale;version=1.98.4;critical=yes
tool=x11vnc;path=/usr/bin/x11vnc;version=0.9.16-10;critical=yes
tool=docker;path=UNKNOWN_local;version=UNKNOWN;critical=Oracle_Kuma_remote_only

BROWSERS_DESKTOP:
tool=firefox;package=firefox;version=151.0.1+linuxmint1+zena;critical=yes
tool=google-chrome-stable;package=google-chrome-stable;version=149.0.7827.53-1;critical=yes
tool=Telegram_Desktop;flatpak=org.telegram.desktop;critical=yes
tool=insync;package=insync;version=3.9.10.60041-noble;critical=yes

PROJECT_RELATIONS:
project=supercontacts;tools=Android_Studio,adb,java,Gradle_UNKNOWN
project=multitimetracker;tools=Android_Studio,adb,java,Gradle_UNKNOWN
project=soldi;tools=Android_Studio,adb,java,Gradle_UNKNOWN
project=mint-cloud-backup;tools=restic,jq,curl,systemd
project=surface-recovery-hardening;tools=cryptsetup,rsync,systemctl,journalctl,lsblk,findmnt
project=mint-update-tracker;tools=python3,sqlite3,systemd
project=mint-freeze-forensics;tools=python3,systemd,journalctl,dmesg
project=codex-token-watcher;tools=codex,node,npm,python3,sqlite3
project=windowtabnotes;tools=python3,sqlite3,GTK3,rofi,wmctrl,xdotool,jq

OPEN:
open=Gradle_versions_not_refreshed_in_this_prompt
open=Android_Studio_product_info_not_refreshed_in_this_prompt
