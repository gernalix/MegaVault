# Soldi Changelog

## 2026-06-18

- Implemented prompt `#739204` as a capped local-first Android finance app.
- Added Room/SQLite schema for accounts, transactions, tags, chains, places, receipts, products, aliases, receipt items, links, life events, transaction events, settings, and price memory.
- Added Compose UI for fast entry, searchable/sortable transactions, receipt OCR confirmation, products, places, tags/chains, links, and analytics.
- Added SQLite vault export/import modeled after the MultiTimeTracker stable-file policy: `soldi.db`, `soldi.db.bak`, `soldi.db.tmp`.
- Added version source `version.txt`, footer `v2`, and debug APK `2.apk`.
- Verified local unit tests, debug build, and androidTest APK build.
- TCL device validation is pending wireless-debugging pairing; Pixel validation is intentionally ignored for this prompt.

## 2026-06-13

- Clarified `Soldi`/template guardrail: `Soldi` is a real app, not a live template or future generation source.
- Audited the previous `Soldi` folder as an Android Studio starter app with no domain logic.
- Preserved the original folder in `_backups`.
- Regenerated `Soldi` from the reusable Android template.
- Set package/applicationId to `com.gernalix.soldi`.
- Verified `./gradlew assembleDebug` and physical debug APK.
- Added local project metadata and updated MegaVault docs.

## 2026-06-05

- Initialized the original Android Studio starter project.
- Verified debug build and local Git repository.
