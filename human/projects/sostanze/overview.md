# Sostanze

Sostanze is now a local-first Android app for medications, supplements, stock, prescriptions, interactions, and intake tracking.

- Project path: `/home/daniele/projects/Sostanze`
- Package/applicationId: `com.gernalix.sostanze`
- Current UI: Compose Material3 app with Home, Scorte, Prescrizioni, and Interazioni tabs.
- Build command: `./gradlew --no-daemon --console=plain testDebugUnitTest assembleDebug`
- Verified debug APK: `output/4.apk`
- Database: Room SQLite `sostanze.db`
- ImportExport: live SAF SQLite export/import with fixed `sostanze.db` filename.

The Home screen follows the MultiTimeTracker Events pattern: compact action buttons, search, grouped sections, overflow actions, and a collapsible taken-today area.

The app applies only user-entered interaction rules. It does not contain medical advice.
