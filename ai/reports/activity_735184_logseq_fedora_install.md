# Activity 735184 Logseq Fedora Install

ID=735184
DATE=2026-07-13
STATUS=PASS_WITH_WARNING
CATEGORY=release
IMPORTANCE=P1
HOST=fedora
USER=daniele

SOURCE:
- repository=https://github.com/logseq/logseq
- workflow_path=.github/workflows/build-desktop-release.yml
- workflow_name=Build-Desktop-Release
- workflow_id=5397555
- workflow_state=active
- artifact_required=logseq-linux-x64-builds
- rule_compliance=official_repo_only,no_mirror,no_darwin,no_wine,no_emulator,no_local_compile,no_remote_workflow_start,no_rpm,no_flatpak,no_sudo

ENVIRONMENT:
- os=Fedora Linux 44 Workstation Edition
- arch=uname_m_x86_64
- user=daniele
- tools_present=gh,curl,jq,unzip,file,sha256sum,sha512sum,desktop-file-validate,update-desktop-database
- gh_auth=authenticated_as_gernalix

SELECTION:
- algorithm=fetched_workflow_runs_newest_first_then_checked_completed_success_official_repo_and_exact_artifact_nonexpired_positive_size_download_url
- preference_applied=master_first
- runs_fetched=222
- skipped_conclusion=9
- skipped_unusable_artifact=198
- selected_reason=most_recent_valid_master_run_with_exact_linux_x64_artifact

RUN:
- run_id=29228358932
- run_number=2284
- run_attempt=1
- status=completed
- conclusion=success
- event=workflow_dispatch
- branch=master
- commit_sha=b09316abd7bde39d25c6c5694d01b2d4e874fe01
- created_at=2026-07-13T06:13:43Z
- updated_at=2026-07-13T06:35:29Z
- html_url=https://github.com/logseq/logseq/actions/runs/29228358932
- actor=tiensonqin
- triggering_actor=tiensonqin
- repository=logseq/logseq
- head_repository=logseq/logseq
- build_target_job=build-linux-x64
- build_target_job_id=86748897351
- build_target_job_status=completed_success
- build_target_job_started_at=2026-07-13T06:25:59Z
- build_target_job_completed_at=2026-07-13T06:28:05Z
- nightly_release_job=skipped

ARTIFACT:
- artifact_id=8270822046
- artifact_name=logseq-linux-x64-builds
- artifact_size=353844309
- artifact_created_at=2026-07-13T06:28:02Z
- artifact_updated_at=2026-07-13T06:28:02Z
- artifact_expires_at=2026-08-02T06:13:44Z
- download_method=gh_run_download_29228358932_repo_logseq/logseq_name_logseq-linux-x64-builds
- downloaded_files=VERSION,latest-linux.yml,Logseq-linux-x86_64-2.0.1.AppImage,Logseq-linux-x86_64-2.0.1.zip

VERIFY:
- version=2.0.1
- version_sources=VERSION+latest-linux.yml+AppImage_filename
- appimage_count=1
- appimage_name=Logseq-linux-x86_64-2.0.1.AppImage
- appimage_size=182773866
- appimage_file=ELF_64_bit_LSB_pie_executable_x86-64_static-pie
- appimage_readelf_machine=Advanced_Micro_Devices_X86-64
- appimage_first_bytes=7f454c46020101004149020000000000
- not_html_json_corrupt=yes
- no_mach_o_pe_arm_main_file=yes
- latest_linux_yml_path_match=yes
- latest_linux_yml_size_match=yes
- sha256=49de367078b37670febdb987e562b75dee1e1ae96c28bfb8738779c42297dd0c
- sha512_hex=40431e5306e55c920404241ce40876011c5fb7774e50ec8d672ed31105b5a1f6c3efa0abfc30f8d6992fe7c7f743ab11f353ea552cd652f8f543a564ecc6785c
- sha512_base64=QEMeUwblXJIEBCQc5Ah2ARxft3dOUOyNZy7TEQW1ofbD76Cr/DD41pkv58f3Q6sR81PqVSzWUvj1Q6Vk7MZ4XA==
- sha512_manifest_match=PASS
- appimage_extract=PASS
- startup_wm_class=Logseq_from_official_embedded_desktop_file
- icon_source=squashfs-root/usr/share/icons/hicolor/512x512/apps/logseq.png

INSTALL:
- install_dir=/home/daniele/.local/opt/logseq/2.0.1
- appimage=/home/daniele/.local/opt/logseq/2.0.1/Logseq-linux-x86_64-2.0.1.AppImage
- appimage_owner=daniele:daniele
- appimage_mode=0755
- symlink=/home/daniele/.local/bin/logseq
- symlink_target=/home/daniele/.local/opt/logseq/2.0.1/Logseq-linux-x86_64-2.0.1.AppImage
- desktop=/home/daniele/.local/share/applications/logseq.desktop
- icon=/home/daniele/.local/share/icons/hicolor/512x512/apps/logseq.png
- desktop_exec=/home/daniele/.local/bin/logseq
- desktop_validate=PASS_WITH_HINT_categories_Office_Utility_multiple_main_categories
- desktop_cache_update=PASS
- icon_cache_update=WARNING_no_index_theme_nonfatal_absolute_icon_used

TEST:
- readlink=PASS_target_/home/daniele/.local/opt/logseq/2.0.1/Logseq-linux-x86_64-2.0.1.AppImage
- file=PASS_ELF64_x86-64
- executable=PASS
- direct_launch=PASS_process_active_after_18s
- direct_launch_profile=temp_XDG
- desktop_launch=PASS_gtk-launch_with_temp_HOME_XDG
- crash_immediate=NO
- fuse_failure=NO
- sudo_used=NO
- no_sandbox_flag_added_to_launcher=NO
- app_internal_process_note=Electron_spawned_renderer_with_internal_no-sandbox_arg_but_launcher_does_not_pass_no-sandbox
- journal_user=Started_app-logseq_scope
- process_cleanup=PASS_no_pgrep_x_logseq_remaining
- user_home_graph_cleanup=PASS_/home/daniele/logseq_absent_after_tests

WARNINGS:
- Logseq first launch auto-created a Demo graph under HOME/logseq during direct test even with XDG temp paths; generated files were moved out of /home/daniele/logseq and then treated as temporary diagnostic data.
- For desktop launch verification, HOME and XDG paths were redirected to a temporary directory so no graph was left under /home/daniele.
- Logseq auto-updater logged a nonfatal 404 for https://github.com/logseq/logseq/releases/download/0.10.15/latest-linux.yml.
- desktop-file-validate returned exit 0 with a hint that Office and Utility are both main categories; kept because the task required Categories=Office;Utility;.
- gtk-update-icon-cache returned no-index-theme for the user hicolor directory; desktop file uses an absolute icon path, so this is nonfatal.

ROLLBACK:
- previous_active_logseq_install=none_found
- rollback_remove=/home/daniele/.local/bin/logseq
- rollback_remove=/home/daniele/.local/share/applications/logseq.desktop
- rollback_remove=/home/daniele/.local/opt/logseq/2.0.1
- rollback_optional_remove_icon=/home/daniele/.local/share/icons/hicolor/512x512/apps/logseq.png

FUTURE_UPDATE:
- repeat_source=official_logseq/logseq_workflow_.github/workflows/build-desktop-release.yml
- repeat_artifact=logseq-linux-x64-builds
- select_completed_success_official_master_or_official_workflow_dispatch_with_nonexpired_positive_size_artifact
- verify_VERSION_latest-linux_yml_sha512_base64_and_ELF64_x86-64_before_switching_symlink
- preserve_previous_version_until_new_launch_test_passes

CLEANUP:
- temporary_download_directory=removed_after_report_and_timeline
- macos_darwin_files_in_Downloads=preserved_untouched
- heavy_binaries_in_MegaVault=none
