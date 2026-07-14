# SERVICE_REGISTRY
VERSION=14
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=systemctl_live_2026-07-14+HOST_PROFILE+activity_638214+activity_847263+activity_593184+activity_471852+activity_471853+activity_583921+activity_684219+activity_638417+activity_846219+activity_826417+activity_582941
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/SERVICE_REGISTRY.md

CURRENT_FEDORA:
host=fedora
os=Fedora_Linux_44_Workstation
service_manager=systemd
system_state=running
user_state=running
project_services_verified=fedora-system-monitor+fedora-t7-backup+fedora-diagnostics
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
service=fedora-system-monitor-events.service;state=enabled+active/running;purpose=event_driven_journal_capture;processes=python+journalctl;activity=593184
service=fedora-system-monitor-lifecycle.service;state=enabled+active/exited;purpose=boot+clean_shutdown_tracking;activity=593184
service=fedora-system-monitor-collect@.service;state=static_template;purpose=isolated_periodic_collectors;activity=593184
service=fedora-system-monitor-device-add@.service;state=static_template;purpose=udev_device_add;activity=593184
service=fedora-system-monitor-device-change@.service;state=static_template;purpose=udev_device_change;activity=593184
service=fedora-system-monitor-device-remove@.service;state=static_template;purpose=udev_device_remove;activity=593184
service=fedora-system-monitor-prometheus.service;state=active_as_prometheus_dependency+disabled_direct_enablement;purpose=readonly_localhost_9109_metrics_endpoint;runtime_dependency=stdlib_only;live_test=PASS;activity=471852+826417
service=prometheus.service;state=enabled+active/running;package=prometheus-3.13.0-1.fc44;bind=127.0.0.1:9090;retention=30d_or_5GB;scrape=15s;restart=on-failure_5s;targets=prometheus+node+fedora-system-monitor;activity=826417
service=prometheus-node-exporter.service;aliases=node_exporter.service_same_unit;state=enabled+active/running;package=node-exporter-1.11.1-1.fc44;bind=127.0.0.1:9100;restart=on-failure_5s;privilege=prometheus_user+no_capabilities;activity=826417
command=fedora-diagnostics;service=none;timer=none;mode=manual_on_demand;path=/usr/local/bin/fedora-diagnostics;activity=826417
service=t7-restic-backup.service;scope=system;state=static_oneshot+tested_success;purpose=udev_connect_mount+encrypted_incremental_backup+conditional_maintenance+sync+unmount+notify;runtime=/usr/local/libexec/t7-restic-lifecycle;activity=684219
service=t7-restic-reminder.service;scope=system;state=static_oneshot+tested_success;purpose=single_disconnect_reminder_if_serial_still_present;activity=684219
service=fedora-external-updater-root.service;scope=system;state=installed+timer_enabled+manual_PASS;purpose=complementary_safe_external_updates_root_scope;activity=846219
udev=90-t7-name.rules;match=USB_disk_add+serial_S6YGNS0Y903440H;action=TAG_systemd+SYSTEMD_WANTS_t7-restic-backup.service;duplicate_events=flock_ignored;activity=684219
audit=fedora-system-monitor_1.1.1;watchers=minute+five_minute+fifteen_minute_real_ok;tests=93_PASS;selftest=18_PASS;udev=verify_PASS;hardening=systemd_analyze_verify_PASS;capabilities_base=DAC_READ_SEARCH+SETGID+SETUID;capabilities_daily=base+SYS_ADMIN;capabilities_daemon_device_lifecycle=none;SYS_RAWIO=absent;activity=471853

USER_SERVICES_RELEVANT:
service=gnome-session-manager@gnome.service;state=active/running;purpose=GNOME_session
service=flatpak-portal.service;state=active/running;purpose=Flatpak_portal
service=pipewire.service;state=active/running;purpose=audio_video
service=wireplumber.service;state=active/running;purpose=media_session
service=xdg-desktop-portal.service;state=active/running;purpose=desktop_portal
service=adb-device-keeper.service;scope=user;state=enabled+active/running;purpose=allowlisted_Pixel_8a+TCL_6102H_ADB_WiFi_availability;exec=/home/daniele/.local/bin/adb-device-keeper_--daemon;docs=ADB_DEVICE_KEEPER.md
service=autokey.service;scope=user;state=removed/not-found;purpose=removed_after_ENODEV_uinput_loop_and_replaced_by_Espanso;backup=/home/daniele/backups/autokey/582941-20260714T222324+0200;activity=582941
service=espanso.service;scope=user;state=enabled+active/running;purpose=Espanso_Wayland_text_expansion;exec=/usr/bin/espanso_daemon;wanted_by=default.target;restart=on-failure_3s;config=/home/daniele/.config/espanso;backend=Clipboard;keyboard_layout=it;ports=none;activity=582941
service=activitywatch.service;scope=user;state=enabled+active/running;purpose=ActivityWatch_official_aw-qt_server_only;exec=/home/daniele/.local/opt/activitywatch/aw-qt_--no-gui_--autostart-modules_aw-server;wanted_by=graphical-session.target;restart=on-failure_5s;port=127.0.0.1:5600;extra_layers=none;activity=284617
service=activitywatch-wayland-watcher.service;scope=user;state=enabled+inactive_until_next_graphical_login;purpose=ActivityWatch_GNOME_Wayland_AFK+active_window_via_aw-awatcher;exec=/usr/bin/aw-awatcher;wanted_by=graphical-session.target;requires=activitywatch.service;restart=always_5s;port_extra=none;extension=focused-window-dbus@flexagoon.com_v11;activity=735804
service=fedora-external-updater-user.service;scope=user;state=installed+timer_enabled+manual_PASS;purpose=complementary_safe_external_updates_user_scope;activity=846219

TIMERS_RELEVANT:
timer=dnf-makecache.timer;scope=system;state=active;purpose=package_metadata
timer=fstrim.timer;scope=system;state=active;purpose=SSD_trim
timer=logrotate.timer;scope=system;state=active;purpose=log_rotation
timer=systemd-tmpfiles-clean.timer;scope=system+user;state=active;purpose=temp_cleanup
timer=fedora-system-monitor-fast.timer;scope=system;state=enabled+active;calendar=every_minute;purpose=minute+overdue_5m+15m_collectors
timer=fedora-system-monitor-hourly.timer;scope=system;state=enabled+active;calendar=hourly;purpose=software+update+health_snapshot
timer=fedora-system-monitor-daily.timer;scope=system;state=enabled+active;calendar=03:15;purpose=inventory+backup+retention+summary
timer=fedora-system-monitor-weekly.timer;scope=system;state=enabled+active;calendar=Sunday_04:15;purpose=full_validation
timer=t7-restic-reminder.timer;scope=system;state=static_one_shot_after_success;delay=30min;purpose=notify_once_only_if_T7_serial_still_present_and_unmounted;activity=684219
timer=fedora-external-updater-root.timer;scope=system;state=enabled+active;calendar=daily+persistent+randomized_12min;purpose=complementary_external_update_root_scope;activity=846219
timer=fedora-external-updater-user.timer;scope=user;state=enabled+active;calendar=daily+persistent+randomized_18min;purpose=complementary_external_update_user_scope;activity=846219
removed_timers=t7-restic-backup.timer+t7-restic-check.timer+t7-restic-maintenance.timer;reason=T7_normally_disconnected+backup_on_connect;activity=684219
path=fedora-system-monitor-software.path;scope=system;state=enabled+active;purpose=event_driven_software_metadata_changes

RULES:
rule=use_systemctl_for_system_units
rule=use_systemctl_--user_for_user_units
rule=verify_unit_live_before_documenting_project_runtime
rule=do_not_assume_pre_migration_project_units_exist
rule=ADB_keeper_is_user_scoped+linger_required_for_logout_and_boot
rule=RustDesk_official_unit_is_only_autostart_mechanism;do_not_add_XDG_or_user_systemd_duplicate
rule=RustDesk_vendor_ExecStop_uses_broad_pkill_pattern;run_service_restart_in_command_without_other_RustDesk_double_dash_arguments
rule=AutoKey_removed_do_not_reenable_without_explicit_rollback;Espanso_is_user_session_scoped;use_only_espanso.service_with_ExecStart_espanso_daemon_on_GNOME_Wayland;do_not_add_duplicate_XDG_autostart

OPEN:
open=project_specific_services_and_timers_not_migrated_or_revalidated
open=RustDesk_permanent_password+Android_physical_test_pending_user;Wayland_GDM_pre-login_unsupported
