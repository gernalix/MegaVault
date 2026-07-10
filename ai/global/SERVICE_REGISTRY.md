# SERVICE_REGISTRY
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=systemctl_live_2026-07-10+HOST_PROFILE+activity_638214+activity_847263
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/SERVICE_REGISTRY.md

CURRENT_FEDORA:
host=fedora
os=Fedora_Linux_44_Workstation
service_manager=systemd
system_state=running
user_state=running
project_services_verified=none
project_service_migration=not_revalidated
user_linger_daniele=yes

SYSTEM_SERVICES_RELEVANT:
service=NetworkManager.service;state=active/running;purpose=network
service=firewalld.service;state=active/running;purpose=firewall
service=dnf5daemon-server.service;state=active/running;purpose=package_management
service=fwupd.service;state=active/running;purpose=firmware_updates
service=smartd.service;state=active/running;purpose=storage_health
service=systemd-oomd.service;state=active/running;purpose=memory_pressure_control
service=udisks2.service;state=active/running;purpose=removable_storage
service=gdm.service;state=active/running;purpose=GNOME_display_manager
service=rustdesk.service;scope=system;state=enabled+active/running;purpose=RustDesk_remote_access;exec=/usr/bin/rustdesk_--service;package=rustdesk-1.4.9-0.x86_64;starts=user_server+tray_when_session_exists
service=windowtabnotes.service;state=removed/not-found;scope=system;removed_at=2026-07-10;reason=WindowTabNotes Fedora uninstall after GNOME Wayland limitation validation

USER_SERVICES_RELEVANT:
service=gnome-session-manager@gnome.service;state=active/running;purpose=GNOME_session
service=flatpak-portal.service;state=active/running;purpose=Flatpak_portal
service=pipewire.service;state=active/running;purpose=audio_video
service=wireplumber.service;state=active/running;purpose=media_session
service=xdg-desktop-portal.service;state=active/running;purpose=desktop_portal
service=adb-device-keeper.service;scope=user;state=enabled+active/running;purpose=allowlisted_Pixel_8a+TCL_6102H_ADB_WiFi_availability;exec=/home/daniele/.local/bin/adb-device-keeper_--daemon;docs=ADB_DEVICE_KEEPER.md

TIMERS_RELEVANT:
timer=dnf-makecache.timer;scope=system;state=active;purpose=package_metadata
timer=fstrim.timer;scope=system;state=active;purpose=SSD_trim
timer=logrotate.timer;scope=system;state=active;purpose=log_rotation
timer=systemd-tmpfiles-clean.timer;scope=system+user;state=active;purpose=temp_cleanup

RULES:
rule=use_systemctl_for_system_units
rule=use_systemctl_--user_for_user_units
rule=verify_unit_live_before_documenting_project_runtime
rule=do_not_assume_pre_migration_project_units_exist
rule=ADB_keeper_is_user_scoped+linger_required_for_logout_and_boot
rule=RustDesk_official_unit_is_only_autostart_mechanism;do_not_add_XDG_or_user_systemd_duplicate
rule=RustDesk_vendor_ExecStop_uses_broad_pkill_pattern;run_service_restart_in_command_without_other_RustDesk_double_dash_arguments

OPEN:
open=project_specific_services_and_timers_not_migrated_or_revalidated
open=RustDesk_permanent_password+Android_physical_test_pending_user;Wayland_GDM_pre-login_unsupported
