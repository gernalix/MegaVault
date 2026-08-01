# ACTIVITY_593814_LOGSEQ_FEDORA_APPIMAGE
DATE=2026-07-26T20:09:12+02:00
STATUS=PASS
PROTOCOL=../MEGAVAULT_PROTOCOL.md
SCOPE=Fedora_44_user_AppImage+GNOME_integration+live_validation

INPUT:
requested=/home/daniele/Downloads/logseq-linux-x64-builds/Logseq-linux-x86_64-2.0.1.AppImage
exists_before=yes
version=2.0.1;source=embedded_logseq.desktop_X-AppImage-Version+launch_log
arch=x86_64;format=ELF_64_bit_static_pie_AppImage_type2
bytes=182798636
sha256=43515fdd0a9e7a26349998d0e5eae063f6cf7649a932dfca78b1d83d31a9359a

PRESTATE:
existing_install=user_AppImage_2.0.1;sha256=49de367078b37670febdb987e562b75dee1e1ae96c28bfb8738779c42297dd0c;bytes=182773866
comparison=same_version+same_ELF_BuildID_a87aaf5da1bf2ef30becedd1aa58e217818fb503+different_bytes+different_sha256
duplicates=RPM_none+Flatpak_none+one_installed_AppImage
data_preservation=no_config_graph_or_user_data_deleted_or_reconfigured

CHANGES:
binary=/home/daniele/.local/opt/logseq/2.0.1/Logseq-linux-x86_64-2.0.1.AppImage;mode=0755;owner=daniele:daniele;action=atomic_replace_with_requested_file
downloads=requested_AppImage_moved_out;remaining_Logseq_AppImages=0
launcher=/home/daniele/.local/bin/logseq;type=symlink;target=/home/daniele/.local/opt/logseq/2.0.1/Logseq-linux-x86_64-2.0.1.AppImage
desktop=/home/daniele/.local/share/applications/logseq.desktop;Name=Logseq;Exec=/home/daniele/.local/bin/logseq;Categories=Office
icon=/home/daniele/.local/share/icons/hicolor/512x512/apps/logseq.png;source=AppImage_usr/share/icons/hicolor/512x512/apps/logseq.png;sha256=e3801c054138a9cc5eb555c0cea985620716ddf621421369213da82b9fff557a
desktop_database=/home/daniele/.local/share/applications/mimeinfo.cache;logseq_scheme_registered=yes
dependencies_installed=none
dependency_runtime=fuse-libs-2.9.9-25.fc44+fuse-2.9.9-25.fc44;preexisting=yes;libfuse.so.2=present

LAUNCH:
manual=/home/daniele/.local/bin/logseq
menu=gtk-launch_logseq
isolated_test=temporary_HOME+XDG_dirs;duration=15s_until_controlled_timeout;version_log=Logseq_App_2.0.1_Starting;relevant_errors=none;residual_processes=none
GNOME_test=gtk-launch_exit_0;process_alive_after_10s=yes;runtime_config=/home/daniele/.config/Logseq;relevant_errors=none
runtime_note=Electron_fs.W_OK_deprecation_warning_nonfatal
coredumps_since_test=none

TESTS:
test=installed_file_regular+executable+owner+sha256;result=PASS
test=single_installation_RPM+Flatpak+AppImage+Downloads;result=PASS;count=1
test=desktop-file-validate;result=PASS;exit=0
test=GNOME_desktop_database+gtk-launch;result=PASS
test=isolated_real_runtime_no_immediate_exit;result=PASS
test=normal_profile_process_alive_after_10s;result=PASS
test=launch_log_error_filter+journal+coredump;result=PASS

UPDATE:
method=obtain_future_x86_64_AppImage+verify_version_arch_sha256;create_/home/daniele/.local/opt/logseq/VERSION;chmod_0755;retarget_/home/daniele/.local/bin/logseq;extract_and_refresh_icon+desktop;run_desktop-file-validate+update-desktop-database+isolated_launch;remove_old_binary_only_after_PASS
preserve=/home/daniele/.config/Logseq+all_graph_paths+user_data

EXECUTION_INSIGHTS:
problem=preexisting_2.0.1_install_was_not_byte_identical_to_requested_2.0.1_file
cause=different_AppImage_payload_for_same_version;exact_provenance_of_user_supplied_file_not_inferred
resolution=requested_file_replaced_prior_binary_atomically_after_live_hash+format+version_checks
blocker=initial_safe_replacement_command_rejected_before_execution_due_temporary_rm_pattern;impact=none;resolution=single_same_filesystem_atomic_mv;status=RESOLVED
