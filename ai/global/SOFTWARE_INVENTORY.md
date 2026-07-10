# SOFTWARE_INVENTORY
VERSION=5
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
UPDATED=2026-07-10T05:25:49+02:00
SOURCE=tool_versions_live_2026-07-09+HOST_PROFILE+flatpak+task_481726_live_install_validation
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/SOFTWARE_INVENTORY.md

FEDORA_RUNTIME_CURRENT:
tool=bash;path=/usr/bin/bash;version=5.3.9;critical=yes
tool=dnf;path=/usr/bin/dnf;version=5.4.2.1;critical=yes
tool=systemd;path=/usr/bin/systemctl;version=259;critical=yes
tool=git;path=/usr/bin/git;version=2.55.0;critical=yes
tool=gh;path=/usr/bin/gh;version=2.94.0;critical=yes
tool=Codex_CLI;path=/usr/local/bin/codex;version=0.144.0;critical=yes
tool=python;path=/usr/bin/python3;version=3.14.6;critical=yes
tool=pip;path=/usr/bin/pip;version=26.0.1;critical=yes
tool=pipx;path=/usr/bin/pipx;version=1.15.0;critical=yes
tool=uv;path=/usr/bin/uv;version=0.11.26;critical=yes
tool=java;path=/usr/bin/java;JAVA_HOME=/usr/lib/jvm/java-25-openjdk;version=OpenJDK_25.0.3;critical=yes
tool=rg;path=Codex_bundle;version=15.1.0;critical=yes
tool=flatpak;path=PATH;critical=yes_for_Android_Studio
tool=OpenSSH;path=/usr/bin/ssh;version=10.2p1;config_dir=/home/daniele/.ssh;config_dir_status=absent;critical=yes
tool=Docker;path=missing;service=absent;version=not_installed;critical=no
tool=Podman;path=/usr/bin/podman;version=5.8.4;critical=no;role=optional_container_runtime

DESKTOP_APPS_CURRENT:
app=Obsidian;version=1.12.7;install=user_AppImage;path=/home/daniele/.local/opt/obsidian/Obsidian.AppImage;desktop=/home/daniele/.local/share/applications/obsidian.desktop;icon=/home/daniele/.local/share/icons/hicolor/512x512/apps/obsidian.png;arch=x86_64;launch=verified;gnome_applications=visible
dependency=fuse-libs.x86_64;version=2.9.9-25.fc44;reason=AppImage_libfuse.so.2
event_date=2026-07-10;summary=Obsidian_1.12.7_user_AppImage_installed_and_validated;status=completed;source_ref=task_481726

ANDROID_TOOLS_CURRENT:
tool=Android_Studio;install=Flatpak_com.google.AndroidStudio;version=2026.1.1.10;launch=flatpak_run_com.google.AndroidStudio;critical=yes
tool=Android_SDK;path=/home/daniele/Android/Sdk;ANDROID_HOME=/home/daniele/Android/Sdk;ANDROID_SDK_ROOT=/home/daniele/Android/Sdk;critical=yes
tool=adb;path=/home/daniele/Android/Sdk/platform-tools/adb;version=1.0.41/37.0.0-14910828;critical=yes
tool=sdkmanager;path=/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager;critical=yes
tool=Gradle;path=project_wrapper_preferred;version=project_specific;critical=yes

FEDORA_OPERATIONS:
package_ops=dnf
service_ops=systemctl+systemctl_--user
storage_ops=findmnt,lsblk,df
shell_ops=bash
android_ops=flatpak,adb,sdkmanager,java,project_Gradle_wrapper

OPEN:
open=current_backup_client_and_restic_state_not_refreshed_on_Fedora
open=project_Gradle_versions_are_project_specific
