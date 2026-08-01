# ACTIVITY 582941 - AUTOKEY TO ESPANSO

META:
activity_id=582941
date=2026-07-14
host=Fedora_44_Workstation_GNOME_50_Wayland
status=PASS_WITH_WARNING
scope=remove_AutoKey_install_Espanso_migrate_text_expansions_update_docs

BASELINE:
autokey_process=/usr/bin/python3_/home/daniele/.local/libexec/autokey-wayland-fedora44_active
autokey_cpu_before=0.2_percent_at_audit;known_incident_previous_peak_about_100_percent_core
autokey_memory_before=30.9MiB_service_status
logs=ENODEV_FileNotFoundError_on_/dev/input/event22_and_prior_Errno19_No_such_device
packages=autokey-common_0.97.4-0.fc44+autokey-gtk_0.97.4-0.fc44_from_dlk_autokey_COPR
service=autokey.service_user_enabled_active_at_start
backup=/home/daniele/backups/autokey/582941-20260714T222324+0200

INSTALL:
method=Terra_RPM_package_per_official_Espanso_Fedora_Wayland_docs
repo=terra_only;baseurl=https://repos.fyralabs.com/terra44;gpgcheck=yes;repo_gpgcheck=yes
repo_key_fingerprint=AE09157A4DE88B497EA1D5D300CDAB43DE226D6F
installed=terra-release_44-9+terra-gpg-keys_44-4+espanso-wayland_2.3.0-1.fc44+wxBase_3.2.9-2.fc44+wxGTK_3.2.9-2.fc44+wxGTK-i18n_3.2.9-2.fc44
binary=/usr/bin/espanso
capability=/usr/bin/espanso_cap_dac_override_ep
service=/home/daniele/.config/systemd/user/espanso.service
service_exec=/usr/bin/espanso_daemon
service_state=enabled+active/running
ports=none

MIGRATION:
source=/home/daniele/.config/autokey/data
espanso_config=/home/daniele/.config/espanso/config/default.yml
espanso_matches=/home/daniele/.config/espanso/match/base.yml
espanso_migration_report=/home/daniele/.config/espanso/migration-582941.json
backend=Clipboard
keyboard_layout=it
matches_migrated=3
triggers=adr,aktest638417x,semicolon_aktest638417
not_migrated=AutoKey_scripts_macros_hotkeys_sample_scripts+phrases_without_abbreviation
reason=user_requested_text_expansion_only;no_command_line_or_personal_content_exported

REMOVAL:
dnf_removed=autokey-gtk,autokey-common
dnf_autoremoved=gnome-extensions-app,gtksourceview3,libappindicator-gtk3,python3-magic,python3-pyasyncore,python3-pydbus,python3-xlib
repo_removed=dlk/autokey_COPR_file_deleted_after_disable
user_removed=/home/daniele/.config/autokey,/home/daniele/.local/share/autokey,/home/daniele/.local/share/applications/autokey-gtk.desktop,/home/daniele/.local/libexec/autokey-wayland-fedora44,/home/daniele/.local/bin/autokey-post-login-638417-check,/home/daniele/.local/share/gnome-shell/extensions/autokey-gnome-extension@autokey
cache_removed=/home/daniele/.cache/libdnf5/autokey-wayland-test-*+/home/daniele/.cache/libdnf5/copr:copr.fedorainfracloud.org:dlk:autokey-*

TESTS:
espanso_version=2.3.0
service_active=PASS
service_enabled=PASS
espanso_service_status=running
match_list=PASS_3_matches
GTK_temp_window_match_exec=PASS_all_3_migrated_matches_inserted;private_match_verified_by_length_hash_and_config_comparison_without_printing_content
GTK_temp_window_trigger_typing=PASS_WITH_SEPARATOR;aktest638417x_and_adr_typed_from_virtual_keyboard_already_present_before_Espanso_restart_expanded_to_expected_text_plus_word_separator
Chrome_temp_profile=attempted;DevTools_control_required_custom_WebSocket;not_used_as_pass_evidence
autokey_packages_absent=PASS
autokey_process_absent=PASS
autokey_user_unit_absent=PASS
system_failed_units=PASS_0
user_failed_units=PASS_0
listeners=PASS_no_autokey_or_espanso_ports
SELinux=unchanged

RESOURCE_AFTER:
espanso_cpu_idle=0.0_percent_for_daemon_and_worker_after_settle
espanso_memory=MemoryCurrent_about_16MiB;RSS_daemon_about_35MiB;RSS_worker_about_39MiB
temperature_snapshot=Tctl_67.2C;ThinkPad_fans_1959_RPM;not_attributed_to_Espanso
autokey_loop=eliminated_by_removal

ROLLBACK:
step1=systemctl --user disable --now espanso.service
step2=rm -f /home/daniele/.config/systemd/user/espanso.service;systemctl --user daemon-reload
step3=sudo dnf remove espanso-wayland;optionally sudo dnf remove terra-release terra-gpg-keys wxBase wxGTK wxGTK-i18n if not otherwise used
step4=sudo dnf config-manager addrepo_or_reenable_dlk_autokey_COPR_only_if_explicitly_requested
step5=sudo dnf install autokey-gtk autokey-common
step6=restore /home/daniele/backups/autokey/582941-20260714T222324+0200/config-autokey to /home/daniele/.config/autokey and restore user unit/wrapper/desktop only if returning to previous implementation
step7=systemctl --user daemon-reload;systemctl --user enable --now autokey.service
warning=rollback_reintroduces_known_ENODEV_loop_risk

LIMITATIONS:
limitation=Physical_keyboard_trigger_after_logout/login_not_automatable_without_user_typing;virtual_keyboard_trigger_and_service_restart_validated;systemd_enablement_proves_autostart_configuration
limitation=GNOME_Wayland_app_specific_matching_not_available_without_kdotool;not_needed_for global text expansion
limitation=Espanso_Wayland_support_is_upstream_experimental;current daemon uses EVDEVSource+EVDEVInjector+WaylandFallbackClipboard

DOCS:
updated=ai/global/SOFTWARE_INVENTORY.md
updated=ai/global/SERVICE_REGISTRY.md
updated=ai/global/INCIDENT_REGISTRY.md
updated=human/global/SOFTWARE_INVENTORY.md
updated=human/global/SERVICE_REGISTRY.md
updated=human/global/INCIDENT_REGISTRY.md
timeline=updated_before_final
