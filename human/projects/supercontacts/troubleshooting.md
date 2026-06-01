# SuperContacts Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
- dev/legacy/dev/NEODOC.md: - Patch runtime version source: `app/src/main/assets/patch-version.txt`. It is an integer asset, not Gradle config.
- dev/legacy/dev/NEODOC.md: - Pixel validation uses debug/deviceTest packages only; never overwrite the personal `com.supercontacts.app` install.
- dev/legacy/dev/NEODOC.md: - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata.
- dev/legacy/dev/NEODOC.md: - Home cards show display name from name, nickname, email, else `Unnamed contact`; never phone.
- dev/legacy/dev/NEODOC.md: - Home search never displays photo path/filename/URI/storage internals. Photo field values are excluded from match metadata; phone matches are not rendered on Home.
- dev/legacy/dev/NEODOC.md: - Cold-start and already-running intents route through the same resolver. Missing/invalid contacts show a friendly message and do not crash.
- dev/legacy/dev/NEODOC.md: - Photos are app-owned files under backup/SAF root `photos/`; DB stores relative references like `photos/<file>.jpg`.
- dev/legacy/dev/NEODOC.md: - UI must never show photo filename/path, SAF URI, content URI, or raw storage internals.
- dev/legacy/dev/NEODOC.md: - Replace/remove flow: DB transaction commits first and returns the old unreferenced path; old file is deleted after commit. If DB update fails after staging a new file, the staged file is deleted as rollback cleanup.
- dev/legacy/dev/NEODOC.md: - Backup/import keeps `super_contacts_backup.sqlite` plus sibling `photos/` usable; relative photo references must survive restore.
- dev/legacy/dev/NEODOC.md: - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ
- dev/legacy/dev/NEODOC.md: - v15: Generic field descriptions with parent-bound add/edit/remove UI, localized EN/IT strings, Room v9 migration, parent-aware history events, and backup/import preservation.
- dev/legacy/dev/NEODOC.md: - Distance sorting still depends on saved coordinates and current device location permission.
- dev/legacy/dev/NEODOC.md: - Required for v17 nationality/field descriptions: `:app:compileDebugKotlin`, debug build, repository/history instrumentation, backup/import instrumentation, Pixel debug install/open, and UI evidence for description actions on name/ph
