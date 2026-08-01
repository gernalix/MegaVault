# SuperContacts Overview

Android contacts app backed by Room/SQLite; repo files and tests cover contact CRUD, tags, initiatives, photos, field descriptions, address suggestions, duplicate checks, backup/ex

## Stato e codice
- Repository: `/home/daniele/codex-workspace/SuperContacts`
- Branch/commit verificati: `codex/prompt-729604-capsule-audit` / `97441c4`
- File codice/config/test/script analizzati: 96 su 96
- Stack rilevato: Kotlin, Python, Shell, Gradle, Jetpack Compose, Android
- Capsulizzazione: 100% reale, baseline minima permanente.
- Bridge feature residui: nessuno.
- Owner capsule: `ContactHomeCapsule`, `ContactDetailCapsule`, `ContactMessagingCapsule`, `ContactHistoryCapsule`, `ContactInitiativeCapsule`, `ContactSuggestionCapsule`, `ContactDuplicateCapsule`, `ContactBackupCapsule`, `ContactOperationStatusCapsule`.
- Enforcement obbligatorio: `CapsuleArchitectureEnforcementTest` per facade zero-logic, root wiring, AppContainer, owner/contract map e boundary cross-capsule; `ContactFieldDescriptionUiTest` per descrizioni fuori dal reading mode.
- Ultimo fix smoke Pixel: v23 reintroduce in modalità edit i pulsanti `+` descrizione per tutti i campi editabili, inclusi i campi vuoti preparati al bisogno; le descrizioni inserite restano visibili sia in reading sia in edit, mentre i pulsanti descrizione restano nascosti in reading.
- Ultima chiusura UI Home: v25 sposta le ricerche salvate in una voce unica `🔖 Ricerche salvate`, aggiunge dialog dedicato con applica/copia/elimina con conferma, evita duplicazione del nome nei risultati ricerca, mantiene un solo indicatore ASC/DESC e forza scroll top a ogni cambio ordinamento o direzione.
- Ultima feature messaggistica: v26 genera localmente link WhatsApp/Telegram/Signal dai numeri internazionali salvati, aggiorna i link in modo incrementale quando il telefono cambia, preserva conferme/rifiuti manuali e non certifica la registrazione reale del numero sulle piattaforme.
- Ultima rifinitura UX: v27 elimina il rumore visivo dei link decisi; solo gli `unverified` restano in card, i confermati sono icone rapide e i rifiutati non occupano spazio nella scheda.

## Orientamento rapido
- Entrypoint: `app/src/main/AndroidManifest.xml,app/src/main/java/com/supercontacts/app/MainActivity.kt,app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt`
- Core/data: `app/src/main/assets/countries-v1.csv,app/src/main/java/com/supercontacts/app/data/local/ContactAddressSuggestionRow.kt,app/src/main/java/com/supercontacts/app/data/local/ContactEventWithContactName.kt,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/1.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/10.json,app/schemas/com.supercontacts.app.data.local.SuperContactsDatabase/2.json`
- Test: `app/src/androidTest/java/com/supercontacts/app/AddressAutocompleteRepositoryTest.kt,app/src/androidTest/java/com/supercontacts/app/AddressLocalSuggestionTest.kt,app/src/androidTest/java/com/supercontacts/app/BackupManagerInstrumentedTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactDuplicateUiTest.kt,app/src/androidTest/java/com/supercontacts/app/ContactFieldDescriptionUiTest.kt`
- Script/build: `tools/build-finalize.ps1,tools/build-finalize.sh,tools/codex_guardrails.ps1,tools/codex_guardrails.py,app/build.gradle.kts,build.gradle.kts,gradle.properties,settings.gradle.kts`

## Link
- Owner repository corrente: `UNKNOWN` dopo verifica locale dei path candidati.
- Snapshot storico più recente noto: [SuperContacts v33](../../../ai/archive/projects_legacy/supercontacts-v33.md).
- Snapshot precedente v30: [SuperContacts legacy](../../../ai/archive/projects_legacy/supercontacts.md).
- Repository: repo path (`../../../../SuperContacts`; status=UNKNOWN)
