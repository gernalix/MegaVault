# HOST_PROFILE
VERSION=12
STATUS=MANDATORY_GLOBAL_CONTEXT
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=hardware_constraints
UPDATED=2026-07-14T20:05:00+02:00
SOURCE=Fedora_live_hostnamectl+uname+findmnt+lsblk+tool_versions+environment+user_context+activity_847263+activity_593184+activity_846271+activity_583921+activity_684219+activity_826417

META:
host=fedora
user=daniele
primary_machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
model=LENOVO_21ME003SFR
role=primary_Fedora_workstation_for_Codex,Android,development,monitoring,automation
path_root=/home/daniele
workspace_current=/home/daniele/MegaVault
read_after=ai/MEGAVAULT_PROTOCOL.md
human=../../human/global/HOST_PROFILE.md
protocol=../MEGAVAULT_PROTOCOL.md
centralization=host/system/storage/Android_tooling_constraints_authoritative_here

HOST_SYSTEM_CURRENT:
os=Fedora_Linux_44_Workstation
kernel=7.1.3-200.fc44.x86_64
arch=x86_64
hostname=fedora
user_home=/home/daniele
megavault_root=/home/daniele/MegaVault
shell=/bin/bash version=5.3.9
package_manager=/usr/bin/dnf
path_style=/home/daniele/...
local_rule=use_bash+Fedora_paths+dnf;verify_live_state_before_system_or_storage_changes

HARDWARE:
cpu=AMD_Ryzen_7_PRO_8840HS_w_Radeon_780M_Graphics
cpu_topology=8c/16t
ram=27.7GiB
bios=R2LET40W_1.21
gpu=Radeon_780M_integrated
constraints=laptop_power/thermal_profile,verify_sudo_requirement,use_Fedora_commands_and_mounts

STORAGE_CURRENT_FEDORA:
root=/dev/mapper/luks-0c261c5f-02dd-484f-b266-13ff4ee02abb btrfs encrypted size=951.3GiB available=844GiB mounts=/,/home
nvme=KXG8AZNV1T02_LA_KIOXIA size=953.9GiB
external_seagate=/run/media/daniele/Seagate Expansion Drive ntfs size=3.5TiB source=udisks_encrypted_volume_mapping
external_ntfs=/run/media/daniele/09FA16D309FA16D3 size=155.9GiB role=UNKNOWN
t7=name=T7 normal_state=physically_disconnected_or_USB_present_unmounted job_mount=/mnt/T7_BACKUP ext4 label=T7_BACKUP uuid=4c75ac03-4c73-43f8-afd9-f90db49a74fc model=Samsung_PSSD_T7_Shield serial=S6YGNS0Y903440H size=931.5GiB free_about=761GiB persistent_fstab=yes udisks_hint=T7 restic=/mnt/T7_BACKUP/restic-fedora connect_trigger=udev+systemd verified=2026-07-12 activity=684219
recovery_media=historical_distinct_vfat label=VEEAMRE uuid=16B8-BC99 size=14.6GiB last_seen=2026-07-12T01:09:47+02:00
storage_rule=verify_findmnt+lsblk+df_before_backup_or_large_IO;removable_mounts_can_drift

TOOLING_CURRENT_FEDORA:
git=/usr/bin/git version=2.55.0
gh=/usr/bin/gh version=2.94.0
codex=/usr/local/bin/codex version=0.144.1
python=/usr/bin/python3 version=3.14.6
pip=/usr/bin/pip version=26.0.1
pipx=/usr/bin/pipx version=1.15.0
uv=/usr/bin/uv version=0.11.26
java=/usr/bin/java OpenJDK=25.0.3
JAVA_HOME=/usr/lib/jvm/java-25-openjdk
rg=Codex_bundle version=15.1.0
ssh=/usr/bin/ssh version=OpenSSH_10.2p1
ssh_dir=~/.ssh resolved=/home/daniele/.ssh status=absent
docker=not_installed service=absent
podman=/usr/bin/podman version=5.8.4 role=optional_container_runtime

ANDROID_CURRENT_FEDORA:
android_studio=Flatpak_com.google.AndroidStudio version=2026.1.1.10 launch="flatpak run com.google.AndroidStudio"
android_sdk=/home/daniele/Android/Sdk
ANDROID_HOME=/home/daniele/Android/Sdk
ANDROID_SDK_ROOT=/home/daniele/Android/Sdk
adb=/home/daniele/Android/Sdk/platform-tools/adb version=1.0.41/37.0.0-14910828
sdkmanager=/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
adb_os=Linux_7.1.3-200.fc44.x86_64
adb_rule=verify_with_adb_devices_-l;device_IPs_and_pairing_drift

CODEX_CURRENT_FEDORA:
working_root=/home/daniele
megavault=/home/daniele/MegaVault
interactive_launcher=/usr/local/bin/codex;resolution=npm_official_launcher;native_binary=vendor_x86_64_unknown_linux_musl;pty=Ptyxis_native;tmux=no;wrapper=no;automatic_capture=no
shell_commands=bash
package_commands=dnf
service_commands=systemctl+systemctl_--user
service_manager=systemd version=259
storage_commands=findmnt+lsblk+df
path_rule=current_local_paths_must_resolve_under_Fedora_mounts
project_rule=project_or_remote_paths_never_override_HOST_SYSTEM_CURRENT

MONITORING_CURRENT:
prometheus=/usr/bin/prometheus;version=3.13.0;service=enabled+active;bind=127.0.0.1:9090;retention=30d_or_5GB;activity=826417
node_exporter=/usr/bin/node_exporter;version=1.11.1;service=prometheus-node-exporter.enabled+active;bind=127.0.0.1:9100;activity=826417
diagnostics=/usr/local/bin/fedora-diagnostics;version=1.0.0;default=7d;archive=single_sanitized_0600_ZIP;activity=826417
relationship=Prometheus_historical_metrics;Uptime_Kuma_synthetic_UP_DOWN_unchanged;fedora-system-monitor_readonly_target=127.0.0.1:9109

REMOTE_ACCESS_CURRENT:
client=RustDesk;version=1.4.9;install=official_x86_64_RPM_via_DNF;path=/usr/bin/rustdesk
runtime=rustdesk.service;scope=system;state=enabled+active;session=GNOME_Wayland;docs=SOFTWARE_INVENTORY.md+SERVICE_REGISTRY.md+../reports/prompt_847263_rustdesk_fedora.md
constraint=Wayland_control_experimental;Wayland_GDM_pre-login_unsupported;permanent_password+Android_physical_test_pending_user

DNB:
dnb=do_not_treat_non_Fedora_snapshots_as_current_host
dnb=do_not_treat_remote_paths_as_local_Fedora_paths
dnb=do_not_treat_mDNS_as_Android_device_proof
dnb=do_not_run_destructive_storage/backup/remediation_commands_without_explicit_user_intent
dnb=do_not_use_human_docs_as_operational_authority_when_AI_doc/protocol/profile_disagree

OPEN:
open=external_password_manager_escrow_pending_for_T7_Restic
open=project_specific_services_and_data_paths_require_live_revalidation_on_Fedora
