# ACTIVITY_948315_SECURE_BOOT_EVIDENCE
STATUS=PASS_CON_WARNING
MANUAL_STATUS=PASS WITH WARNING
DATE=2026-07-30
SCOPE=Fedora_44+Secure_Boot_forensic_capture+no_reboot
RESULT=capture_environment_ready+incident_remains_OPEN
OWNER_REPORT=/home/daniele/projects/fedora-diagnostics/docs/ai/AUDIT_948315.md
RUNTIME=/usr/local/sbin/fedora-secureboot-forensics-capture
UNIT=fedora-secureboot-forensics-capture.service_enabled+inactive+never_started
OUTPUT=/var/log/fedora-secureboot-forensics
PROTECTED=LUKS+partitions+Secure_Boot+keys+kernel+initramfs+original_BLS+GRUB+grubenv_unchanged
BOUNDARY=normal_pre-root_dracut_timeout_requires_console_photo_or_video
