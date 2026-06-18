# Soldi

Soldi is now a local-first Android finance capsule.

- Project path: `/home/daniele/AndroidStudioProjects/Soldi`
- Package/applicationId: `com.gernalix.soldi`
- Version: `2`
- Debug APK: `/home/daniele/AndroidStudioProjects/Soldi/app/build/outputs/apk/debug/2.apk`
- Storage: internal Room SQLite database `soldi.db`
- Export/import: user-selected SAF folder with stable `soldi.db`, `soldi.db.bak`, and transient `soldi.db.tmp`
- UI: Compose screens for fast transactions, receipts/OCR confirmation, products, places, tags/chains, links, and analytics
- Guardrail: `Soldi` is a real app, not a template source for new apps.

The app tracks transactions, accounts, tags, chains, places, receipts, products, aliases, receipt items, transaction links, life events, price memory, receipt reconciliation, and wealth analytics. Wealth snapshots are reconstructed from SQLite data instead of stored as a separate source of truth.
