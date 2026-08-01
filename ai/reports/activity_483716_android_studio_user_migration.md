# Activity 483716 Android Studio User Migration
ID=483716
DATE=2026-07-15T11:33:35+02:00
HOST=fedora;os=Fedora_44_Workstation;user=daniele
SCOPE=migrate_Android_Studio_from_Flatpak_/app/extra_to_user_writable_official_Google_archive
PREVIOUS=Flatpak_com.google.AndroidStudio;version=2026.1.1.10;real_exec=/var/lib/flatpak/app/com.google.AndroidStudio/current/active/files/extra/bin/studio.sh;app_extra_owner=root:root;reason=IDE_updater_cannot_write_/app/extra
NEW=Android_Studio_Quail_2_2026.1.2;build=AI-261.25134.95.2612.15822958;path=/home/daniele/.local/opt/android-studio;owner=daniele:daniele;writable_by_daniele=yes
SOURCE=https://edgedl.me.gvt1.com/android/studio/ide-zips/2026.1.2.10/android-studio-quail2-linux.tar.gz;official_page=https://developer.android.com/studio;sha256=64445a54092e7056c6eb7f1a89ad116d0feec2ef5f965b8e594d62abdb58590f;verified=yes
LAUNCHER=desktop=/home/daniele/.local/share/applications/com.google.AndroidStudio.desktop;exec=/home/daniele/.local/bin/android-studio;icon=/home/daniele/.local/opt/android-studio/bin/studio.svg;flatpak_launcher_removed=yes;visible_entries=1
PRESERVED=config=/home/daniele/.config/Google/AndroidStudio2026.1.2_migrated_from_Flatpak_config;flatpak_user_data=/home/daniele/.var/app/com.google.AndroidStudio_preserved;SDK=/home/daniele/Android/Sdk;AVD=/home/daniele/.android/avd;projects=preserved;credentials=preserved
BACKUP=/home/daniele/MegaVault/backups/android-studio-483716-20260715T112725+0200;contents=essential_config_only_no_cache_no_SDK_no_AVD
VALIDATION=studio_sh_--version_PASS;writable_tree_PASS;MultiTimeTracker_opened_PASS;SDK_detected_PASS;AVD_dirs_preserved_PASS;launcher_single_user_desktop_PASS;root_launch_NEVER;project_file_changes_NONE_BY_TASK
UPDATER=UpdateCheckerService_started_release_channel;ExternalUpdateManager_logged;write_access_error_count=0;no_/app/extra_error_in_idea_log;no_update_installed
CLEANUP=temp_archive_removed=yes;old_Flatpak_installation_removed=yes;flatpak_data_not_deleted=yes
WARN=IDE_was_terminated_by_timeout_after_startup_validation_causing_nonfatal_shutdown_warnings;MultiTimeTracker_repo_had_preexisting_dirty_status
DOCS=ai/global/HOST_PROFILE.md+ai/global/SOFTWARE_INVENTORY.md+ai/MEGAVAULT_PROTOCOL.md+ai/ANDROID_PROTOCOL.md+this_report+global_timeline
STATUS=PASS_WITH_WARNING
