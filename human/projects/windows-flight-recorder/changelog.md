# Windows Flight Recorder Changelog

2026-06-27T12:40:00Z=Added MegaVault metadata/AI/human documentation placeholders for production audit.
2026-06-27T13:22:30Z=Completed hardening: watch, taillog, doctor, audit, timestamp migration v2, admin task repair script, manual guide, extended tests.
2026-06-27T14:02:30Z=Fixed runtime bugs: task detection no longer reports false missing on access denied; watch header/debug/all; fast USB/session polling; probe commands; local dashboard/API/export; dashboard/probe tests.
2026-06-27T14:07:45Z=Fixed crash-recovery test interference with resident watchdog via watchdog.pause_until_utc; final runtime has one logger and one watchdog.
