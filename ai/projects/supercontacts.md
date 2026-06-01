# SuperContacts AI OPERATIONS

PROJECT
- name: SuperContacts
- slug: supercontacts
- purpose: Android contacts app backed by Room/SQLite; repo files and tests cover contact CRUD, tags, initiatives, photos, field descriptions, address suggestions, duplicate checks, backup/export, and debug-device validation.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/SuperContacts`
- remote: `https://github.com/gernalix/SuperContacts.git`
- branch: `codex/prompt-xxx`
- last_verified_commit/date: `3aa6287` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Kotlin, Python, Shell
- frameworks: Gradle, Jetpack Compose, KSP
- DB: Room/SQLite
- platform: Android
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/supercontacts/app/MainActivity.kt`
- `tools/codex_guardrails.py`
- `tools/tests/test_guardrails_engine.py`
important_folders:
- `app`
- `dev`
- `gradle`
- `local_archives`
- `output`
- `tmp`
- `tools`
important_files:
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
- `dev/README.md`
tests:
- `app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFormScrollDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoCropUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryDuplicateMatchingTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryHomeTagFilterTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryInitiativeTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryTimestampTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/InitiativeUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ManualVerificationSeedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/TestBackupSupport.kt`
- `app/src/test/java/com/supercontacts/app/ContactDuplicateNormalizerTest.kt`
- `app/src/test/java/com/supercontacts/app/ExampleUnitTest.kt`
- `tools/tests/test_guardrails_engine.py`
scripts:
- `gradlew`
- `tools/build-finalize.ps1`
- `tools/build-finalize.sh`
- `tools/codex_guardrails.ps1`
- `tools/codex_guardrails.py`
- `tools/codex_guardrails.sh`
- `tools/guardrails/__init__.py`
- `tools/guardrails/engine.py`
- `tools/tests/test_guardrails_engine.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `build`
- `.gradle`
- `output`
- `tmp`

ARCH
summary:
- dev/legacy/dev/NEODOC.md: - Branch-only work. Preserve unrelated local files and ignored artifacts.
- dev/legacy/dev/INDEX.md: # SuperContacts Neodoc Entrypoint
- dev/legacy/apps_installate_mint.txt: 7zip/noble,now 23.01+dfsg-11 amd64 [installed]
- build.gradle.kts: // Top-level build file where you can add configuration options common to all sub-projects/modules.
- settings.gradle.kts: includeGroupByRegex("com\\.android.*")
- gradle.properties: # Project-wide Gradle settings.
- tools/build-finalize.ps1: [Parameter(Mandatory = $true, Position = 0)]
- tools/build-finalize.sh: build/preflight/validate/finalize/send-artifacts) ;;
- tools/codex_guardrails.ps1: [ValidateSet("preflight", "discovery", "validate")]
- tools/codex_guardrails.py: from __future__ import annotations
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | # SuperContacts NEODOC |
| `dev/legacy/dev/NEODOC.md` | ## Ops |
| `dev/legacy/dev/NEODOC.md` | ## Architecture |
| `dev/legacy/dev/NEODOC.md` | ## Data Invariants |
| `dev/legacy/dev/NEODOC.md` | ## Home UX |
| `dev/legacy/dev/NEODOC.md` | ## Deep Links |
| `dev/legacy/dev/NEODOC.md` | ## Media Lifecycle |
| `dev/legacy/dev/NEODOC.md` | ## Privacy |
| `dev/legacy/dev/NEODOC.md` | ## Changelog |
| `dev/legacy/dev/NEODOC.md` | ## Known Limits |
| `dev/legacy/dev/NEODOC.md` | ## Testing Notes |
| `dev/legacy/dev/NEODOC.md` | ## Future Docs Rule |
| `dev/legacy/dev/INDEX.md` | # SuperContacts Neodoc Entrypoint |
| `gradle.properties` | # Project-wide Gradle settings. |
| `gradle.properties` | # IDE (e.g. Android Studio) users: |
| `gradle.properties` | # Gradle settings configured through the IDE *will override* |
| `gradle.properties` | # any settings specified in this file. |
| `gradle.properties` | # For more details on how to configure your build environment visit |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | - Branch-only work. Preserve unrelated local files and ignored artifacts. |
| `dev/legacy/dev/NEODOC.md` | - Patch runtime version source: `app/src/main/assets/patch-version.txt`. It is an integer asset, not Gradle config. |
| `dev/legacy/dev/NEODOC.md` | - Pixel validation uses debug/deviceTest packages only; never overwrite the personal `com.supercontacts.app` install. |
| `dev/legacy/dev/NEODOC.md` | - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata. |
| `dev/legacy/dev/NEODOC.md` | - Frequent paths must stay indexed or bounded; no heavy real-time UI work. |
| `dev/legacy/dev/NEODOC.md` | - New contacts get `public_id = c-<uuid>`; migration v8 backfills old rows and indexes `public_id`. |
| `dev/legacy/dev/NEODOC.md` | - Phone normalization is centralized; phone can be searched but must not appear on Home cards. |
| `dev/legacy/dev/NEODOC.md` | - Home cards show display name from name, nickname, email, else `Unnamed contact`; never phone. |
| `dev/legacy/dev/NEODOC.md` | - Home search never displays photo path/filename/URI/storage internals. Photo field values are excluded from match metadata; phone matches are not rendered on Home. |
| `dev/legacy/dev/NEODOC.md` | - UI must always show `Sorted by: <criterion> (<ASC/DESC>)`; direction toggle persists immediately. |
| `dev/legacy/dev/NEODOC.md` | - Stable external schema: `supercontacts://contact/{public_id}`. |
| `dev/legacy/dev/NEODOC.md` | - Cold-start and already-running intents route through the same resolver. Missing/invalid contacts show a friendly message and do not crash. |
| `dev/legacy/dev/NEODOC.md` | - Photos are app-owned files under backup/SAF root `photos/`; DB stores relative references like `photos/<file>.jpg`. |
| `dev/legacy/dev/NEODOC.md` | - UI must never show photo filename/path, SAF URI, content URI, or raw storage internals. |
| `dev/legacy/dev/NEODOC.md` | - New photo writes use contact-aware unique filenames. Cleanup deletes only app-owned relative photo references or legacy app file paths. |
| `dev/legacy/dev/NEODOC.md` | - Replace/remove flow: DB transaction commits first and returns the old unreferenced path; old file is deleted after commit. If DB update fails after staging a new file, the staged file is deleted as rollback cleanup. |
| `dev/legacy/dev/NEODOC.md` | - Deletion checks existence, ignores missing files, logs only minimal success/failure, and must not crash UI. |
| `dev/legacy/dev/NEODOC.md` | - Backup/import keeps `super_contacts_backup.sqlite` plus sibling `photos/` usable; relative photo references must survive restore. |
| `dev/legacy/dev/NEODOC.md` | - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ |
| `dev/legacy/dev/NEODOC.md` | - v15: Generic field descriptions with parent-bound add/edit/remove UI, localized EN/IT strings, Room v9 migration, parent-aware history events, and backup/import preservation. |
| `dev/legacy/dev/NEODOC.md` | - Distance sorting still depends on saved coordinates and current device location permission. |
| `dev/legacy/dev/NEODOC.md` | - Deep links use generated app-local `public_id`; old rows get public ids during Room migration v8 or when restored through supported migrations. |
| `dev/legacy/dev/NEODOC.md` | - Required for v18 nationality/field descriptions: `:app:compileDebugKotlin`, debug build, Pixel debug install/open, and UI evidence for visible description buttons on name/phone/email/address/nationality, add/edit/remove description, |
| `dev/legacy/dev/NEODOC.md` | - Required for v17 nationality/field descriptions: `:app:compileDebugKotlin`, debug build, repository/history instrumentation, backup/import instrumentation, Pixel debug install/open, and UI evidence for description actions on name/ph |
| `dev/legacy/dev/NEODOC.md` | - Android-safe Gradle profile: keep safety wrapper enabled, use `TasksMax>=768`, `LimitNPROC>=4096`, `--no-daemon`, and `--max-workers=1` for Kotlin/KSP-heavy tasks. |
| `dev/legacy/dev/NEODOC.md` | - Required for prior patch families: debug build, relevant instrumentation/unit tests, Pixel install/launch/search/sort/direction persistence/rotate/deep link/clipboard/photo replace-delete cleanup/cold start/app-closed deep link. |

BUILD_TEST
build_files:
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
commands_found:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | - Device smoke package for manual adb flows: `com.supercontacts.app.debug`. |
| `dev/legacy/dev/NEODOC.md` | - Final report must include version, changed files, root cause, UX, deep link schema, sort persistence, cleanup strategy, docs state, limits, commit hash, git status, Pixel evidence. |
| `dev/legacy/apps_installate_mint.txt` | bash-completion/noble,noble,now 1:2.11-8 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | bash/noble,now 5.2.21-2ubuntu4 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | flatpak/noble-updates,noble-security,now 1.14.6-1ubuntu0.1 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | gh/noble-updates,noble-security,now 2.45.0-1ubuntu0.3 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | git-man/noble-updates,noble-updates,noble-security,noble-security,now 1:2.43.0-1ubuntu7.3 all [installed,automatic] |
| `dev/legacy/apps_installate_mint.txt` | git/noble-updates,noble-security,now 1:2.43.0-1ubuntu7.3 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python-apt-common/noble-security,noble-security,now 2.7.7ubuntu5.1 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-apport/noble-updates,noble-updates,noble-security,noble-security,now 2.28.1-0ubuntu3.8 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-apt/noble-security,now 2.7.7ubuntu5.1 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-aptdaemon.gtk3widgets/noble,noble,now 1.1.1+bzr982-0ubuntu44 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-aptdaemon/noble,noble,now 1.1.1+bzr982-0ubuntu44 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-argcomplete/noble-updates,noble-updates,now 3.1.4-1ubuntu0.1 all [installed,automatic] |
| `dev/legacy/apps_installate_mint.txt` | python3-blinker/noble,noble,now 1.7.0-1 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-brlapi/noble,now 6.6-4ubuntu5 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-brotli/noble,now 1.1.0-2build2 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-bs4/noble,noble,now 4.12.3-1 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-cairo/noble,now 1.25.1-2build2 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-certifi/noble,noble,now 2023.11.17-1 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-cffi-backend/noble,now 1.16.0-2build1 amd64 [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-chardet/noble,noble,now 5.2.0+dfsg-1 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-click/noble,noble,now 8.1.6-2 all [installed] |
| `dev/legacy/apps_installate_mint.txt` | python3-colorama/noble,noble,now 0.4.6-4 all [installed] |
test_targets:
- `app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFormScrollDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoCropUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryDuplicateMatchingTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryHomeTagFilterTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryInitiativeTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryTimestampTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/InitiativeUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ManualVerificationSeedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/TestBackupSupport.kt`
- `app/src/test/java/com/supercontacts/app/ContactDuplicateNormalizerTest.kt`
- `app/src/test/java/com/supercontacts/app/ExampleUnitTest.kt`
- `tools/tests/test_guardrails_engine.py`
known_test_flakiness_or_requirements:
- dev/legacy/dev/NEODOC.md: - Final report must include version, changed files, root cause, UX, deep link schema, sort persistence, cleanup strategy, docs state, limits, commit hash, git status, Pixel evidence.
- tools/guardrails/engine.py: code="adb-ddmlib-timeout-non-blocking",
- tools/tests/test_guardrails_engine.py: "stderr_preview": "com.android.ddmlib.TimeoutException: timeout after test completion",
- tools/tests/test_guardrails_engine.py: self.assertEqual(warnings[0]["code"], "adb-ddmlib-timeout-non-blocking")
- app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt: val failure = runCatching {
- app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt: assertNotNull(failure)
- app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt: ?: error("Phone field missing")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: ?: error("Phone field missing")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: val detail = repository.getContactById(contactId).first() ?: error("Missing contact")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: val updated = repository.getContactById(contactId).first() ?: error("Missing updated contact")

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | - Branch-only work. Preserve unrelated local files and ignored artifacts. |
| `dev/legacy/dev/NEODOC.md` | - Patch runtime version source: `app/src/main/assets/patch-version.txt`. It is an integer asset, not Gradle config. |
| `dev/legacy/dev/NEODOC.md` | - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata. |
| `dev/legacy/dev/NEODOC.md` | - Home cards show display name from name, nickname, email, else `Unnamed contact`; never phone. |
| `dev/legacy/dev/NEODOC.md` | - Home search never displays photo path/filename/URI/storage internals. Photo field values are excluded from match metadata; phone matches are not rendered on Home. |
| `dev/legacy/dev/NEODOC.md` | - Photos are app-owned files under backup/SAF root `photos/`; DB stores relative references like `photos/<file>.jpg`. |
| `dev/legacy/dev/NEODOC.md` | - Replace/remove flow: DB transaction commits first and returns the old unreferenced path; old file is deleted after commit. If DB update fails after staging a new file, the staged file is deleted as rollback cleanup. |
| `dev/legacy/dev/NEODOC.md` | - Backup/import keeps `super_contacts_backup.sqlite` plus sibling `photos/` usable; relative photo references must survive restore. |
| `dev/legacy/dev/NEODOC.md` | - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ |
| `dev/legacy/dev/NEODOC.md` | - Deep links use generated app-local `public_id`; old rows get public ids during Room migration v8 or when restored through supported migrations. |
| `dev/legacy/dev/NEODOC.md` | - Final report must include version, changed files, root cause, UX, deep link schema, sort persistence, cleanup strategy, docs state, limits, commit hash, git status, Pixel evidence. |
| `dev/legacy/apps_installate_mint.txt` | lsb-release/noble,noble,now 12.0-2 all [installed] |
| `settings.gradle.kts` | id("org.gradle.toolchains.foojay-resolver-convention") version "1.0.0" |
| `tools/build-finalize.ps1` | Set-StrictMode -Version Latest |
| `tools/build-finalize.ps1` | $PatchVersionFile = Join-Path $RepoRoot "app\src\main\assets\patch-version.txt" |
| `tools/build-finalize.ps1` | [string]$Version |
| `tools/build-finalize.ps1` | if ($Version -eq "System.Object[]") { |
| `tools/build-finalize.ps1` | throw "Versione non valida: 'System.Object[]'" |
| `tools/build-finalize.ps1` | if ($Version -match "\s") { |
| `tools/build-finalize.ps1` | throw ("Versione non valida, contiene spazi o newline: '{0}'" -f $Version) |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata. |
| `dev/legacy/dev/NEODOC.md` | - New contacts get `public_id = c-<uuid>`; migration v8 backfills old rows and indexes `public_id`. |
| `dev/legacy/dev/NEODOC.md` | - Photos are app-owned files under backup/SAF root `photos/`; DB stores relative references like `photos/<file>.jpg`. |
| `dev/legacy/dev/NEODOC.md` | - New photo writes use contact-aware unique filenames. Cleanup deletes only app-owned relative photo references or legacy app file paths. |
| `dev/legacy/dev/NEODOC.md` | - Replace/remove flow: DB transaction commits first and returns the old unreferenced path; old file is deleted after commit. If DB update fails after staging a new file, the staged file is deleted as rollback cleanup. |
| `dev/legacy/dev/NEODOC.md` | - Deletion checks existence, ignores missing files, logs only minimal success/failure, and must not crash UI. |
| `dev/legacy/dev/NEODOC.md` | - Backup/import keeps `super_contacts_backup.sqlite` plus sibling `photos/` usable; relative photo references must survive restore. |
| `dev/legacy/dev/NEODOC.md` | - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ |
| `dev/legacy/dev/NEODOC.md` | - v15: Generic field descriptions with parent-bound add/edit/remove UI, localized EN/IT strings, Room v9 migration, parent-aware history events, and backup/import preservation. |
| `dev/legacy/dev/NEODOC.md` | - Deep links use generated app-local `public_id`; old rows get public ids during Room migration v8 or when restored through supported migrations. |
| `dev/legacy/dev/NEODOC.md` | - Required for v17 nationality/field descriptions: `:app:compileDebugKotlin`, debug build, repository/history instrumentation, backup/import instrumentation, Pixel debug install/open, and UI evidence for description actions on name/ph |
| `dev/legacy/dev/NEODOC.md` | - Required for prior patch families: debug build, relevant instrumentation/unit tests, Pixel install/launch/search/sort/direction persistence/rotate/deep link/clipboard/photo replace-delete cleanup/cold start/app-closed deep link. |
| `dev/legacy/dev/NEODOC.md` | - Device smoke package for manual adb flows: `com.supercontacts.app.debug`. |
| `dev/legacy/dev/NEODOC.md` | - Final report must include version, changed files, root cause, UX, deep link schema, sort persistence, cleanup strategy, docs state, limits, commit hash, git status, Pixel evidence. |
| `dev/legacy/apps_installate_mint.txt` | geoip-database/noble,noble,now 20240403-1ubuntu1 all [installed] |
| `tools/build-finalize.ps1` | Write-Log ("TELEGRAM {0}: Telegram non disponibile (telegram_notify.py mancante)" -f $ArtifactType) |
| `tools/build-finalize.ps1` | Write-Log ("TELEGRAM {0}: Telegram non disponibile (Python non disponibile)" -f $ArtifactType) |
| `tools/build-finalize.ps1` | $result = New-FinalizeState -Version $Version |
| `tools/build-finalize.ps1` | if (($state.PSObject.Properties.Name -contains "version") -and $state.version -eq $Version) { |
| `tools/build-finalize.ps1` | Write-Log ("Finalize state ignorato perché non leggibile: {0}" -f $_.Exception.Message) |
| `tools/build-finalize.ps1` | return $State.commit -and |
| `tools/build-finalize.ps1` | $State.push -in @("pushed", "already-pushed") -and |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | - Cold-start and already-running intents route through the same resolver. Missing/invalid contacts show a friendly message and do not crash. |
| `dev/legacy/dev/NEODOC.md` | - Deletion checks existence, ignores missing files, logs only minimal success/failure, and must not crash UI. |
| `dev/legacy/dev/NEODOC.md` | ## Known Limits |
| `dev/legacy/dev/NEODOC.md` | - Final report must include version, changed files, root cause, UX, deep link schema, sort persistence, cleanup strategy, docs state, limits, commit hash, git status, Pixel evidence. |
| `tools/build-finalize.ps1` | Write-Log ("FAIL: exit code {0}" -f $exitCode) |
| `tools/build-finalize.ps1` | Write-Log ("TELEGRAM {0}: FAIL exit code {1}" -f $ArtifactType, $exitCode) |
| `tools/build-finalize.ps1` | Write-Log ("TELEGRAM {0}: FAIL {1}" -f $ArtifactType, $_.Exception.Message) |
| `tools/build-finalize.ps1` | Write-Log ("ESITO: FAIL ({0}) - {1}" -f $Command, $_.Exception.Message) |
| `tools/build-finalize.sh` | log "FAIL: exit code $status" |
| `tools/build-finalize.sh` | log "TELEGRAM $label: FAIL" |
| `tools/build-finalize.sh` | if [[ -e "$repo_root/$path" ]] && ! is_generated_path "$path" && ! git -C "$repo_root" ls-files --error-unmatch "$path" >/dev/null 2>&1; then |
| `tools/codex_guardrails.ps1` | Write-Error $_ |
| `tools/guardrails/engine.py` | except Exception as exc: # pragma: no cover - failure path |
| `tools/guardrails/engine.py` | code="adb-ddmlib-timeout-non-blocking", |
| `tools/tests/test_guardrails_engine.py` | "stderr_preview": "com.android.ddmlib.TimeoutException: timeout after test completion", |
| `tools/tests/test_guardrails_engine.py` | self.assertEqual(warnings[0]["code"], "adb-ddmlib-timeout-non-blocking") |
| `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt` | val failure = runCatching { |
| `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt` | assertNotNull(failure) |
| `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt` | ?: error("Phone field missing") |
| `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt` | ?: error("Phone field missing") |
| `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt` | val detail = repository.getContactById(contactId).first() ?: error("Missing contact") |
| `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt` | val updated = repository.getContactById(contactId).first() ?: error("Missing updated contact") |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/dev/NEODOC.md: - Branch-only work. Preserve unrelated local files and ignored artifacts.
- dev/legacy/dev/NEODOC.md: - Patch runtime version source: `app/src/main/assets/patch-version.txt`. It is an integer asset, not Gradle config.
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
- dev/legacy/dev/NEODOC.md: - Deletion checks existence, ignores missing files, logs only minimal success/failure, and must not crash UI.
- dev/legacy/dev/NEODOC.md: - Backup/import keeps `super_contacts_backup.sqlite` plus sibling `photos/` usable; relative photo references must survive restore.
- dev/legacy/dev/NEODOC.md: - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ
- dev/legacy/dev/NEODOC.md: - v15: Generic field descriptions with parent-bound add/edit/remove UI, localized EN/IT strings, Room v9 migration, parent-aware history events, and backup/import preservation.

RECENT_DECISIONS
| source | fact |
|---|---|
| `tools/build-finalize.sh` | local current next |
| `tools/build-finalize.sh` | next=$((current + 1)) |
| `tools/build-finalize.sh` | printf '%s' "$next" > "$version_file" |
| `tools/build-finalize.sh` | log "Versione patch aggiornata: $next" |
| `tools/build-finalize.sh` | printf '%s\n' "$next" |
| `tools/guardrails/engine.py` | database_file = next( |
| `tools/guardrails/engine.py` | state_index = next((index for index, token in enumerate(columns[1:], start=1) if token in ADB_DEVICE_STATES), None) |
| `tools/tests/test_guardrails_engine.py` | device_test = next( |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | ## Future Docs Rule |
| `dev/legacy/dev/NEODOC.md` | - No duplicate AI/human doc trees. No stale roadmap copies. Keep this file token-efficient. |
| `dev/legacy/dev/INDEX.md` | - Append future notes under the matching section in `dev/NEODOC.md`. |
| `tools/build-finalize.ps1` | push = "pending" |
| `tools/build-finalize.ps1` | telegram_apk = "pending" |
| `tools/build-finalize.ps1` | telegram_zip = "pending" |
| `tools/build-finalize.sh` | local current next |
| `tools/build-finalize.sh` | next=$((current + 1)) |
| `tools/build-finalize.sh` | printf '%s' "$next" > "$version_file" |
| `tools/build-finalize.sh` | log "Versione patch aggiornata: $next" |
| `tools/build-finalize.sh` | printf '%s\n' "$next" |
| `tools/guardrails/engine.py` | database_file = next( |
| `tools/guardrails/engine.py` | state_index = next((index for index, token in enumerate(columns[1:], start=1) if token in ADB_DEVICE_STATES), None) |
| `tools/tests/test_guardrails_engine.py` | device_test = next( |

LEGACY_SUMMARY
- legacy_docs_read_count: 36
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/dev/NEODOC.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/apps_installate_mint.txt`
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
- `tools/build-finalize.ps1`
- `tools/build-finalize.sh`
- `tools/codex_guardrails.ps1`
- `tools/codex_guardrails.py`
- `tools/codex_guardrails.sh`
- `tools/guardrails/__init__.py`
- `tools/guardrails/engine.py`
- `tools/tests/test_guardrails_engine.py`
- `app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactFormScrollDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoCropUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactPhotoDeviceTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryDuplicateMatchingTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryHomeTagFilterTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryInitiativeTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryTimestampTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/InitiativeUiTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/ManualVerificationSeedTest.kt`
- `app/src/androidTest/java/com/supercontacts/app/TestBackupSupport.kt`
- `app/src/test/java/com/supercontacts/app/ContactDuplicateNormalizerTest.kt`
- `app/src/test/java/com/supercontacts/app/ExampleUnitTest.kt`
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/supercontacts/app/MainActivity.kt`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../SuperContacts/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/supercontacts/overview.md)
- human_folder: [human folder](../../human/projects/supercontacts)
- legacy_docs: [dev/legacy](../../../SuperContacts/dev/legacy)
- repo_path: [repo](../../../SuperContacts)

OPEN_QUESTIONS
- dev/legacy/dev/NEODOC.md: - Cold-start and already-running intents route through the same resolver. Missing/invalid contacts show a friendly message and do not crash.
- dev/legacy/dev/NEODOC.md: - Deletion checks existence, ignores missing files, logs only minimal success/failure, and must not crash UI.
- app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt: ?: error("Phone field missing")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: ?: error("Phone field missing")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: val detail = repository.getContactById(contactId).first() ?: error("Missing contact")
- app/src/androidTest/java/com/supercontacts/app/ContactsRepositoryEventTest.kt: val updated = repository.getContactById(contactId).first() ?: error("Missing updated contact")
