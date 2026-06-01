# SuperContacts Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- gradle.properties: # For more details on how to configure your build environment visit
- gradle.properties: # http://www.gradle.org/docs/current/userguide/build_environment.html
- gradle.properties: # When configured, Gradle will run in incubating parallel mode.
- gradle.properties: # https://developer.android.com/r/tools/gradle-multi-project-decoupled-projects
- build.gradle.kts: // Top-level build file where you can add configuration options common to all sub-projects/modules.
- tools/build-finalize.sh: build/preflight/validate/finalize/send-artifacts) ;;
- tools/codex_guardrails.py: from __future__ import annotations
- tools/guardrails/engine.py: from __future__ import annotations
- tools/tests/test_guardrails_engine.py: from __future__ import annotations
- app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt: import androidx.test.platform.app.InstrumentationRegistry
- app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt: import androidx.test.platform.app.InstrumentationRegistry
- app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt: import android.database.sqlite.SQLiteDatabase
- app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt: import androidx.compose.ui.test.assertIsDisplayed
- app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt: import androidx.compose.ui.test.assertIsDisplayed

## Useful Limits And Boundaries
- dev/legacy/dev/NEODOC.md: - Branch-only work. Preserve unrelated local files and ignored artifacts.
- dev/legacy/dev/NEODOC.md: - Pixel validation uses debug/deviceTest packages only; never overwrite the personal `com.supercontacts.app` install.
- dev/legacy/dev/NEODOC.md: - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata.
- dev/legacy/dev/NEODOC.md: - Frequent paths must stay indexed or bounded; no heavy real-time UI work.
- dev/legacy/dev/NEODOC.md: - Phone normalization is centralized; phone can be searched but must not appear on Home cards.
- dev/legacy/dev/NEODOC.md: - Home cards show display name from name, nickname, email, else `Unnamed contact`; never phone.
- dev/legacy/dev/NEODOC.md: - Home search never displays photo path/filename/URI/storage internals. Photo field values are excluded from match metadata; phone matches are not rendered on Home.
- dev/legacy/dev/NEODOC.md: - UI must always show `Sorted by: <criterion> (<ASC/DESC>)`; direction toggle persists immediately.
- dev/legacy/dev/NEODOC.md: - Cold-start and already-running intents route through the same resolver. Missing/invalid contacts show a friendly message and do not crash.
- dev/legacy/dev/NEODOC.md: - Photos are app-owned files under backup/SAF root `photos/`; DB stores relative references like `photos/<file>.jpg`.
- dev/legacy/dev/NEODOC.md: - UI must never show photo filename/path, SAF URI, content URI, or raw storage internals.
- dev/legacy/dev/NEODOC.md: - New photo writes use contact-aware unique filenames. Cleanup deletes only app-owned relative photo references or legacy app file paths.

## Where The Feature Code Appears To Live
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/supercontacts/app/MainActivity.kt`
- `tools/codex_guardrails.py`
- `tools/tests/test_guardrails_engine.py`
- `gradlew`
- `tools/build-finalize.ps1`
- `tools/build-finalize.sh`
- `tools/codex_guardrails.ps1`
- `tools/codex_guardrails.sh`
- `tools/guardrails/__init__.py`
- `tools/guardrails/engine.py`
