# SOFTWARE_INVENTORY
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
DOC_CLASS=inventory
LIFECYCLE=ACTIVE
AUTHORITY_LEVEL=L2
SOURCE_OF_TRUTH=yes
SOURCE=tool_versions_live_2026-07-05+HOST_PROFILE
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/SOFTWARE_INVENTORY.md

WINDOWS_RUNTIME:
tool=pwsh;path=C:\Program Files\PowerShell\7\pwsh.exe;version=7.6.3;critical=yes
tool=git;path=C:\Program Files\Git\cmd\git.exe;version=2.55.0.windows.2;critical=yes;note=not_in_current_PowerShell_PATH_use_full_path
tool=PowerShell_Desktop;path=system;version=Windows_PowerShell_or_PowerShell_host;critical=yes
tool=rg;path=PATH_or_Codex_bundle;version=UNKNOWN;critical=yes
tool=GitHub_Desktop;path=UNKNOWN;version=UNKNOWN;critical=no;fallback=use_git_cli

ANDROID_TOOLS:
tool=Android_Studio;path=C:\Program Files\Android\Android Studio\bin\studio64.exe;version=261.23567.138.0-AI;critical=yes
tool=Android_SDK;path=C:\Users\seste\AppData\Local\Android\Sdk;critical=yes
tool=adb;path=C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe;version=1.0.41/37.0.0-14910828;critical=yes
tool=sdkmanager;path=C:\Users\seste\AppData\Local\Android\Sdk\cmdline-tools\latest\bin\sdkmanager.bat;version=UNKNOWN;critical=yes
tool=java;path=UNKNOWN;version=UNKNOWN;critical=yes

BACKUP_STORAGE_TOOLS:
tool=Veeam_Agent;service=VeeamEndpointBackupSvc;state=running;startup=automatic;critical=yes
tool=Backblaze_Windows_Client;path=not_detected_default_scan;version=UNKNOWN;critical=UNKNOWN
tool=restic;path=UNKNOWN_on_Windows;version=UNKNOWN;critical=legacy_or_remote

PROJECT_RELATIONS:
android_projects=Android_Studio,Android_SDK,adb,java_UNKNOWN,Gradle_wrapper_preferred
windows_ops=pwsh,git,rg,Get-CimInstance,Get-Disk,Get-Volume
backup_ops=Veeam_current,Backblaze_UNKNOWN,T7_VERIFY_MOUNT
remote_oracle=ssh_tooling_UNKNOWN;remote_Linux_tools_not_local_Windows_truth

LEGACY_2026-06_SURFACE_MINT:
status=historical_not_primary
tools=/usr/bin/git_2.43,/usr/bin/gh_2.45,/usr/bin/python3_3.12,/home/daniele/Android/Sdk/platform-tools/adb,systemctl,restic_0.16.4
rule=Linux_paths_and_systemd_tools_apply_only_to_legacy_Surface_or_remote_VM_context

OPEN:
open=java_path_version_not_refreshed
open=Gradle_versions_not_refreshed
open=GitHub_Desktop_install_state_UNKNOWN
