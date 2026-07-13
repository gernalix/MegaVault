ID ATTIVITA: 684271

ESITO:
PASS CON WARNING

TIMESTAMP=2026-07-13T21:00:00+02:00
HOST=Fedora_Linux_44_Workstation;x86_64;kernel=7.1.3-200.fc44.x86_64
SOURCE_REF=activity_684271
CATEGORY=bugfix
IMPORTANCE=P1

CAUSA RADICE

L'unico VLC installato era il Flatpak Fedora `org.videolan.vlc` 3.0.23, non un RPM. Il runtime `org.fedoraproject.KDE5Platform/x86_64/f44` forniva `ffmpeg-free` con decoder H.264 nativo disabilitato e il pacchetto `noopenh264-2.6.0-4.fc44`, descritto dal pacchetto stesso come implementazione OpenH264 fittizia. Il plugin VLC `avcodec` esisteva e tutte le librerie erano linkate, ma `libopenh264` non poteva creare il decoder. Le librerie OpenH264 reali installate sull'host non erano visibili/utilizzabili come sostituzione nel sandbox.

SPIEGAZIONE TECNICA

PRE_FIX_INSTALL=Flatpak_system;app_id=org.videolan.vlc;origin=fedora;version=3.0.23;commit=4b3ce1a2145389c120f4a3ed6537a2355e7904a14a4536af53af9e628b4f09ac
PRE_FIX_FFMPEG=8.1.2;configuration_contains=--disable-decoder=h264;available_wrapper=libopenh264
PRE_FIX_RUNTIME_OPENH264=noopenh264_2.6.0-4.fc44;summary=Fake_implementation_of_the_OpenH264_library;library_size_about_11KiB
PRE_FIX_VLC_LOG=Unable_to_create_decoder;cannot_start_codec_libopenh264;no_suitable_decoder_found;Codec_h264_is_not_supported
SANDBOX_RULE=host_RPM_openh264_does_not_repair_a_Flatpak_runtime_codec
REAL_PROVIDER=for_the_previous_Fedora_stack_the_only_advertised_H264_decoder_was_FFmpeg_libopenh264_but_its_runtime_library_was_fake;the_Flathub_VLC_fix_supplies_a_full_native_FFmpeg_avcodec_H264_decoder_in_/app/lib

PACCHETTI MODIFICATI

REMOVED=Flatpak_system_org.videolan.vlc_3.0.23_origin_fedora
INSTALLED=Flatpak_system_org.videolan.VLC_3.0.23_origin_flathub_commit_3cad91eaf629cfc8afb5085613ba4569ccf674ac62ae650583aac34aeaec0038
INSTALLED_RUNTIME=org.kde.Platform/x86_64/5.15-25.08;org.kde.Platform.Locale;org.kde.KStyle.Adwaita;org.videolan.VLC.Locale
REMOTE_CHANGE=system_flathub_filter_removed_to_access_full_Flathub_catalog
RPM_CHANGES=none
CONFIG_DATA=/home/daniele/.var/app/org.videolan.vlc_preserved_5.3MiB;no_delete_data

VERIFICHE ESEGUITE

FEDORA_RELEASE=Fedora_release_44
INSTALL_INVENTORY=which_vlc_absent;rpm_vlc_absent;one_Flatpak_VLC_present
VLC_VERSION=3.0.23_Vetinari
PLUGIN_DIR=/app/lib/vlc/plugins
DECODER_MODULE=/app/lib/vlc/plugins/codec/libavcodec_plugin.so
LINKAGE=VLC_binary+avcodec_plugin_no_missing_libraries
HOST_LIBS=libavcodec_62+libavformat_62+libavutil_60+libswscale_9+libswresample_6_present;libpostproc_absent_nonrequired
HOST_CODEC_PACKAGES=ffmpeg-free+libavcodec-free+openh264+mozilla-openh264+gstreamer1-plugin-openh264_present;ffmpeg+libavcodec-freeworld+x264-libs_absent
CONFLICTS=dnf_check_PASS;dnf_repoquery_duplicates_empty;no_RPM_overwrites;one_VLC_app_ref
RPMFUSION=full_free_and_nonfree_release_repositories_not_configured;only_Fedora_third_party_nonfree_nvidia_driver_and_steam_subsets_enabled_for_Fedora_44;not_used_by_Flatpak_VLC_fix
TEST_FILE=/home/daniele/Videos/activity-684271-h264-test.mp4;generated_controlled_sample
FFPROBE=container_mov_mp4_m4a_3gp_3g2_mj2;video_h264_Baseline_640x360_yuv420p;audio_AAC_LC_48000Hz_mono;duration_3s
FFMPEG_TEST=decode_to_null_PASS
FFPLAY_TEST=video_window_exit_0_PASS
MPV_TEST=NOT_RUN_mpv_not_installed
VLC_PRE_FIX=exact_user_error_reproduced_with_full_345_line_vvv_log
VLC_POST_FIX=headless_decode_exit_0+avcodec_first_picture+no_H264_decoder_error_PASS
VLC_REAL_OUTPUT=video_output_exit_0+avcodec_first_picture_PASS
FLATPAK_REPAIR=sudo_flatpak_repair_system_dry_run_PASS_53_objects
MIME=GNOME_Showtime_defaults_unchanged;new_VLC_desktop_export_present;no_stale_VLC_default
INCIDENT_REGISTRY=AI+human+SQLite_RESOLVED;sqlite_integrity_ok;backup=/home/daniele/sync_root/db/backups/incident_registry.activity-684271.pre-update.20260713T190200Z.sqlite
GLOBAL_TIMELINE=updated;sqlite_integrity_ok;duplicate_ids_0;duplicate_equivalent_events_0;invalid_labels_0;invalid_categories_0;invalid_importance_0;generated_secret_hits_0

EVENTUALI WARNING

WARNING=Il file originale che ha generato la segnalazione non e' stato indicato; la diagnosi e' stata riprodotta e validata su un campione H.264 Baseline controllato.
WARNING=`mpv` non e' installato; non e' stato aggiunto perche' non e' parte del fix VLC e installarlo soltanto per un test violerebbe il requisito di modifica minima.
WARNING=`libpostproc` non e' presente sull'host; non e' richiesta per la decodifica H.264 e VLC e' compilato con postproc disabilitato.
WARNING=I repository RPM Fusion free/nonfree completi non sono configurati. I due repository speciali NVIDIA/Steam sono coerenti con Fedora 44, ma sono estranei al VLC Flatpak e non sono stati estesi senza necessita'.
WARNING=Il test VLC con autodetect hardware e output dummy tenta VDPAU NVIDIA e ripiega sul software; con `--avcodec-hw=none` non vi sono errori decoder. Il test video reale software ha ricevuto il primo frame ed e' terminato con codice 0.

STATO FINALE DEL SISTEMA

VLC_FINAL=one_system_Flatpak;org.videolan.VLC;origin_flathub;version_3.0.23
H264_FINAL=FFmpeg_avcodec_native_decoder_working
HOST_FFMPEG_FINAL=unchanged_and_working_with_real_OpenH264
RPM_FINAL=unchanged;dnf_check_PASS;duplicates_none
FLATPAK_FINAL=integrity_dry_run_PASS;old_app_ref_absent;desktop_export_present
RESULT_BOUNDARY=PASS_CON_WARNING_due_to_original_file_not_supplied+mpv_absent+nonblocking_libpostproc/RPMFusion_notes

EXECUTION_INSIGHTS

BLOCKER=Flathub_filter_initially_hid_VLC;root_cause=Fedora_system_Flathub_remote_was_filtered;resolution=removed_filter_after_diagnosis;status=resolved
BLOCKER=Fedora_and_Flathub_use_different_case_sensitive_App_IDs;impact=no_in_place_rebase;resolution=remove_lowercase_Fedora_ref_then_install_uppercase_Flathub_ref_without_delete_data;status=resolved
BLOCKER=flatpak_uninstall_has_no_assumeno_option;impact=unused_runtime_simulation_command_failed_without_changes;resolution=used_app/runtime_inventory_and_flatpak_repair_dry_run;status=resolved
BLOCKER=incident_registry_has_no_updater_tool_in_MegaVault_or_user_bin;impact=protocol_requires_SQLite_sync;resolution=idempotent_transaction_after_SQLite_backup;status=resolved_for_activity
DOCS=ai/global/SOFTWARE_INVENTORY.md+human/global/SOFTWARE_INVENTORY.md+ai/global/INCIDENT_REGISTRY.md+human/global/INCIDENT_REGISTRY.md+this_report
