# Activity 487361 GNOME Window Title

ID=487361
DATE=2026-07-13
STATUS=PASS
CATEGORY=feature
IMPORTANCE=P2
HOST=fedora
USER=daniele

ENVIRONMENT:
- os=Fedora_Linux_44_Workstation
- gnome_shell=50.3
- session=GNOME_Wayland
- gnome_extensions_cli=/usr/bin/gnome-extensions
- gnome_extensions_app=50.2-1.fc44

COMPATIBILITY:
- requested=Window_title_is_back;uuid=window-title-is-back@fthx;latest=38;shell_versions=46,47,48,49;GNOME_50=unsupported
- requested_extension_forced=NO
- upstream_replacement=Tasks_in_panel;uuid=tasks-in-panel@fthx;version=72;shell_version=50;source=extensions.gnome.org_extension_8642
- replacement_reason=requested_extension_is_superseded_and_has_no_GNOME_50_release

INSTALL:
- extension_manager=com.mattjakeman.ExtensionManager;version=0.6.5;origin=Flathub;scope=system
- extension_package=official_extensions.gnome.org_zip;version_tag=72551
- extension_path=/home/daniele/.local/share/gnome-shell/extensions/tasks-in-panel@fthx
- restart_or_logout=not_required

CONFIGURATION:
- show_focused_window=true
- show_window_icon=true
- show_window_app=true
- show_window_title=true
- group_windows=false
- accessory_taskbar_features=disabled
- GNOME_activities_button=shown

VERIFY:
- gnome_extensions_info=Enabled_Yes+State_ACTIVE+Version_72
- global_disable_user_extensions=false
- gnome_shell_errors=none
- AT_SPI_top_bar_title=ChatGPT_-_Fedora_-_Google_Chrome
- AT_SPI_top_bar_application=Google_Chrome
- result=PASS_title_and_application_visible_in_top_bar

EXECUTION_INSIGHTS:
- blocker=InstallRemoteExtension_DBus_returned_NoReply_after_install
- root_cause=GNOME_Shell_extension_registration_disconnected_the_remote_call_during_live_reload
- impact=command_exit_did_not_represent_final_extension_state
- workaround=verify_gnome-extensions_list+info+AT-SPI_instead_of_trusting_call_exit
- resolution=extension_registered_enabled_ACTIVE_and_visually_verified
- status=RESOLVED

ROLLBACK:
- disable=gnome-extensions_disable_tasks-in-panel@fthx
- uninstall=gnome-extensions_uninstall_tasks-in-panel@fthx
- extension_manager_optional_remove=flatpak_uninstall_com.mattjakeman.ExtensionManager

