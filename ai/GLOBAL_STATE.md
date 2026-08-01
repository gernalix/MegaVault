# GLOBAL_STATE
VERSION=1
STATUS=AUTHORITATIVE_VERIFIED_RELATION_SUBSET
FORMAT=ultracompressed
UPDATED=2026-07-26
SOURCE=HOST_PROFILE+live_revalidations_through_2026-07-26

CURRENT:
host=fedora;os=Fedora_Linux_44_Workstation;home=/home/daniele;megavault=/home/daniele/MegaVault
project=MegaVault;repo=/home/daniele/MegaVault;timeline_db=/home/daniele/MegaVault/codex_global_timeline.sqlite;builder=/home/daniele/MegaVault/build_codex_global_timeline.py
project=fedora-system-monitor;repo=/home/daniele/MegaVault/projects/fedora-system-monitor;runtime=/usr/local/libexec/fedora-system-monitor;config=/etc/fedora-system-monitor;data=/var/lib/fedora-system-monitor;status=installed+enabled+tested;version=1.3.1;activity=482731
project=fedora-diagnostics;repo=/home/daniele/projects/fedora-diagnostics;runtime=/usr/local/lib/fedora-diagnostics;cli=/usr/local/bin/fedora-diagnostics;status=installed+enabled+functional+fault_tested+fan_analysis+telemetry;version=1.2.0;activity=826417+614283+948315
project=fedora-t7-backup;repo=/home/daniele/MegaVault/projects/fedora-t7-backup;runtime=/usr/local/libexec/t7-restic-lifecycle;repository=/mnt/T7_BACKUP/restic-fedora;status=installed+backup+maintenance+restore+failsafe_tested;commit=1495f135a81e9457e1efcb12a5db6689983b3c79;activity=684219
project=oracle-backup-service;repo=/home/daniele/projects/oracle-backup-service;runtime=ubuntu@150.230.148.128:/opt/oracle_backup;repository=rclone:oci:bucket-20260206-0730/oraclevm;status=remote_backup+check+restore+healthcheck_PASS;version=2026.08.01.1;commit=3479d69;activity=731904
project=vm_oracle;repo=/home/daniele/MegaVault/projects/vm_oracle;runtime=ubuntu@150.230.148.128;status=PASS_CON_WARNING+apt_0+snap_0+venv_0+pip_check_PASS+services_PASS+reboot_complete+ssh_command_documented;version=2026.07.26.1;commit=f93ec92;activity=731842
project=WindowTabNotes;local=removed;remote=https://github.com/gernalix/WindowTabNotes;branch=fedora-current-session-window-detection-927514;commit=40421981911c6d92111e9062eb20c506003d4d97;data_backup=/home/daniele/WindowTabNotes-backup-351806
runtime=Espanso;package=espanso-wayland-2.3.0-1.fc44.x86_64;service=espanso.service;startup=graphical-session.target;status=PASS_WITH_WARNING;activity=573814

OPEN:
open=all_other_project_runtime_relations_UNKNOWN_until_Fedora_revalidation
open=project-specific docs retained_here_are_migration_debt;move only after owner_repo+metadata+Git+local_docs verification
open=remote paths remain bound to named remote hosts;never reinterpret as Fedora-local
