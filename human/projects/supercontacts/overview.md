# SuperContacts Overview

Android contacts app backed by Room/SQLite; repo files and tests cover contact CRUD, tags, initiatives, photos, field descriptions, address suggestions, duplicate checks, backup/ex

## Stato e codice
- Repository: `/home/daniele/codex-workspace/SuperContacts`
- Branch/commit verificati: `codex/prompt-184926-capsules` / `fbe61e2`
- File codice/config/test/script analizzati: 96 su 96
- Stack rilevato: Kotlin, Python, Shell, Gradle, Jetpack Compose, Android
- Capsulizzazione: 100% reale, baseline minima permanente.
- Bridge feature residui: nessuno.
- Owner capsule: `ContactHomeCapsule`, `ContactDetailCapsule`, `ContactHistoryCapsule`, `ContactInitiativeCapsule`, `ContactSuggestionCapsule`, `ContactDuplicateCapsule`, `ContactBackupCapsule`, `ContactOperationStatusCapsule`.
- Enforcement obbligatorio: `CapsuleArchitectureEnforcementTest` per architettura e `ContactFieldDescriptionUiTest` per descrizioni fuori dal reading mode.

## Orientamento rapido
- Entrypoint: `app/src/main/AndroidManifest.xml,app/src/main/java/com/supercontacts/app/MainActivity.kt,app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt`
- Core/data: `app/src/main/assets/countries-v1.csv,app/src/main/java/com/supercontacts/app/data/local/ContactAddressSuggestionRow.kt,app/src/main/java/com/supercontacts/app/data/local/ContactEventWithContactName.kt,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/2.json`
- Test: `app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt,app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt,app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt`
- Script/build: `tools/build-finalize.ps1,tools/build-finalize.sh,tools/codex_guardrails.ps1,tools/codex_guardrails.py,app/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts`

## Link
- AI doc: [AI doc](../../../ai/projects/supercontacts.md)
- Metadata: [dev/project.metadata.json](../../../../SuperContacts/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../SuperContacts/dev/legacy)
- Repository: [repo path](../../../../SuperContacts)
