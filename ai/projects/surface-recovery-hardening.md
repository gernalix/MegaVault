PROJECT: surface-recovery-hardening
SLUG: surface-recovery-hardening
PATH: /home/daniele/codex-workspace/surface-recovery-hardening
REMOTE: git@github.com:gernalix/surface-recovery-hardening.git
BRANCH: main

STACK:
- unknown/local-tooling

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 21
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- not declared

TEST:
- not detected

VERSIONING:
- git_branch: main
- git_remote: git@github.com:gernalix/surface-recovery-hardening.git
- preexisting_status_count: 10

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118
- ?? reports/prompt418_recovery_restart_20260510_224929/
- ?? reports/prompt684_did_error_20260514_070407.zip
- ?? reports/prompt734_post_crash_20260510_222255/

KNOWN_BUGS:
- dev/legacy/docs/TROUBLESHOOTING.md

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- CHANGELOG.md -> dev/legacy/CHANGELOG.md
- README.md -> dev/legacy/README.md
- docs/ARCHITECTURE.md -> dev/legacy/docs/ARCHITECTURE.md
- docs/OPERATIONS.md -> dev/legacy/docs/OPERATIONS.md
- docs/TROUBLESHOOTING.md -> dev/legacy/docs/TROUBLESHOOTING.md
- reports/REPORT_v1.md -> dev/legacy/reports/REPORT_v1.md
- reports/REPORT_v2_display_theme_scaling.md -> dev/legacy/reports/REPORT_v2_display_theme_scaling.md
- reports/REPORT_v4_usb_io_hardening.md -> dev/legacy/reports/REPORT_v4_usb_io_hardening.md
- reports/REPORT_v5_source_cleanup_analyzer.md -> dev/legacy/reports/REPORT_v5_source_cleanup_analyzer.md
- reports/display_theme_scaling_report_v2.txt -> dev/legacy/reports/display_theme_scaling_report_v2.txt
- reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_af_rsync_required.txt -> dev/legacy/reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_af_rsync_required.txt
- reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_x_rsync_required.txt -> dev/legacy/reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_x_rsync_required.txt
- reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open.txt -> dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open.txt
- reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open_sudo.txt -> dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open_sudo.txt
- reports/prompt418_recovery_restart_20260510_224929/source_mapper_lsblk_after_open.txt -> dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_mapper_lsblk_after_open.txt
- reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md -> dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md
- reports/prompt684_did_error_20260514_070407/user_services_status.txt -> dev/legacy/reports/prompt684_did_error_20260514_070407/user_services_status.txt
- reports/prompt734_post_crash_20260510_222255/dmesg_filtered_usb_io_before_quirk.txt -> dev/legacy/reports/prompt734_post_crash_20260510_222255/dmesg_filtered_usb_io_before_quirk.txt
- reports/prompt734_post_crash_20260510_222255/pre_second_reboot_pgrep.txt -> dev/legacy/reports/prompt734_post_crash_20260510_222255/pre_second_reboot_pgrep.txt
- reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt -> dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt
- reports/xfce_layout_guard_systemd_path_selftest_v2.txt -> dev/legacy/reports/xfce_layout_guard_systemd_path_selftest_v2.txt

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
