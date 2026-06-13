# Sostanze

Sostanze is now a local-first Android app for medications, supplements, stock, prescriptions, interactions, and intake tracking.

- Project path: `/home/daniele/AndroidStudioProjects/Sostanze`
- Package/applicationId: `com.gernalix.sostanze`
- Current UI: Compose Material3 app with Home, Scorte, Prescrizioni, and Interazioni tabs.
- Build command: `./gradlew --no-daemon --console=plain testDebugUnitTest assembleDebug`
- Verified debug APK: `app/build/outputs/apk/debug/app-debug.apk`
- Database: Room SQLite `sostanze.db`

The Home screen follows the MultiTimeTracker Events pattern: compact action buttons, search, grouped sections, overflow actions, and a collapsible taken-today area.

The app applies only user-entered interaction rules. It does not contain medical advice.
