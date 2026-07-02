# ThinkPad Android Dev Optimization Report

Data: 2026-07-02  
Macchina: Lenovo ThinkPad P14s Gen 5 AMD, Ryzen 7 PRO 8840HS, 32 GB RAM nominali, SSD KIOXIA 1 TB  
Report root: `C:\Users\seste\Documents\MegaVault\ai\reports\thinkpad_android_dev_optimization_20260702_085726`

## Stato finale

**Overall iniziale: WARN**

Ambiente Android principale: **PASS**. `adb`, `emulator`, `sdkmanager`, JDK 21, Android SDK, AVD `Pixel_8a`, Gradle wrapper e verifica progetto reale funzionano.

WARN residui:

- Defender exclusions non applicate per mancanza di privilegi amministratore.
- Gradle globale non installato: winget non espone un pacchetto Gradle ufficiale su questa macchina; i wrapper dei repo sono presenti e restano la strada corretta.
- Android Studio e Git hanno update disponibili via winget, ma non sono stati aggiornati automaticamente per evitare update invasivi durante una sessione attiva.
- Connected test su `parole create` con policy `EmulatorOrTcl`: TCL passa, AVD Pixel_8a ha 1 test strumentale fallito. Questo e un problema test/app, non toolchain.

Nota device aggiornata: dopo la tua indicazione, i test devono usare solo emulatore o TCL/6102H. Il Pixel 8a fisico e stato disconnesso dalla sessione ADB corrente.

## Follow-up prioritario 2026-07-02

**Overall follow-up: PASS**

Punti richiesti e stato:

- **PASS - Pixel fisico escluso dai test.** Lo script `run_android_project_verification.ps1` ora blocca i connected test se vede un device non ammesso che non riesce a disconnettere. Il Pixel fisico wireless viene disconnesso dalla sessione ADB; un Pixel USB/non disconnettibile diventa FAIL bloccante. Ultima verifica ADB: nessun device fisico visibile durante la run `EmulatorOnly`.
- **PASS - Causa del test emulatore trovata.** Il failure originale era in `WordPulseUiInstrumentedTest.timelineDetailsAndPrefixSearchExposeCapturedWords`: `Total occurrences` esisteva nell'unmerged semantics tree ma non nel merged tree. Il report XML diceva esplicitamente: "the unmerged tree contains '1' node that matches". Fix mirato in `C:\Users\seste\Documents\parole create\app\src\androidTest\java\com\wordpulse\app\WordPulseUiInstrumentedTest.kt`: `onNodeWithText(..., useUnmergedTree = true)` per `Total occurrences` e `2`.
- **PASS - Verifica emulatore dopo fix.** Run completa solo emulatore: `qa\parole_create_20260702_094137\summary.txt`, `overall=PASS`, `connectedDebugAndroidTest=PASS`, 11 test su `Pixel_8a(AVD) - 17`, nessun Pixel fisico, nessun TCL.
- **PASS - Diagnosi diretta del singolo test.** Run diretta via `adb -s emulator-5554 shell am instrument` del solo test: `qa\emulator_direct_diagnosis_20260702_093807\summary.txt`, `instrument_exit=0`.
- **PASS - Cleanup emulatore rafforzato.** `run_android_project_verification.ps1` ora chiude in loop ogni processo `emulator`/`qemu-system` nato durante la run, includendo i processi con `Path` vuoto. Ultima run: `kill_emulator_process_fallback.log` conferma stop di `emulator` e `qemu-system-x86_64-headless` al primo tentativo e nessun residuo al secondo.

Nota: una run intermedia `qa\parole_create_20260702_093330` ha mostrato `INSTRUMENTATION_FAILED / Process crashed` con 0 test. Non si e riprodotta dopo la verifica diretta e la run completa successiva; la prova conclusiva e `qa\parole_create_20260702_094137`, PASS.

Stato ADB corrente dopo il follow-up: riconnesso solo TCL/6102H via mDNS (`192.168.1.200:39327`); Pixel fisico non e presente in `adb devices -l`.

## Stato prima

- PATH Android gia presente nella sessione, ma da rendere persistente/validato.
- `ANDROID_HOME` e `ANDROID_SDK_ROOT`: `C:\Users\seste\AppData\Local\Android\Sdk`.
- `JAVA_HOME`: Android Studio bundled JBR.
- Gradle globale assente.
- `adb`, `emulator`, `sdkmanager`, Git, PowerShell 7, Python, winget presenti.
- Device wireless iniziali: Pixel 8a e TCL/6102H visibili via ADB.
- Entrambi i device fisici risultavano bloccati da keyguard/PIN: gli script ora classificano questo caso come WARN `manual unlock required`.

## Stato dopo

Verifica finale in nuova PowerShell: `logs\final_new_shell_verification.txt`.

- `ANDROID_HOME`: `C:\Users\seste\AppData\Local\Android\Sdk`
- `ANDROID_SDK_ROOT`: `C:\Users\seste\AppData\Local\Android\Sdk`
- `JAVA_HOME`: `C:\Program Files\Android\Android Studio\jbr`
- `adb`: 37.0.0 / 1.0.41
- `emulator`: 36.6.11
- `sdkmanager`: 21.0
- `java` / `javac`: 21.0.10
- `git`: 2.54.0.windows.1
- `gradle`: non installato globalmente, wrapper-first
- AVD: `Pixel_8a`
- ADB finale: solo TCL/6102H fisico connesso

SDK installati/rilevati:

- `platform-tools` 37.0.0
- `emulator` 36.6.11
- `build-tools` 35.0.0, 36.0.0, 36.1.0, 37.0.0
- `platforms` android-35, android-36, android-36.1, android-37.0
- `system-images;android-37.0;google_apis_playstore_ps16k;x86_64`

## Modifiche applicate

- Creata struttura report con `logs`, `scripts`, `qa`, `backups`.
- Salvato backup env utente: `logs\env_backup_20260702_090510.json`.
- Impostate persistenti a livello User:
  - `ANDROID_HOME`
  - `ANDROID_SDK_ROOT`
  - `JAVA_HOME`
- PATH utente verificato senza duplicati/broken entries. Le entry Android/JDK erano gia presenti come percorsi espansi; lo script ora aggiunge le varianti `%ANDROID_HOME%`/`%JAVA_HOME%` solo se mancano davvero.
- Accettate licenze Android SDK.
- Installato `platforms;android-35`, gia presenti android-36/36.1/37 e build-tools recenti.
- Corretto duplicato SDK `cmdline-tools\latest-2`: spostato in backup in `backups\android_sdk_cmdline_tools\latest-2_20260702_090628`.
- Power AC tuning applicato:
  - sleep AC off
  - hibernate AC off
  - processor max AC 100
  - impostazioni batteria non cambiate
- ADB server riparato e device matrix salvata.
- Pixel 8a fisico disconnesso dalla sessione ADB dopo istruzione "solo emulatore o TCL".

## Script creati

- `scripts\audit_android_dev_env.ps1`
- `scripts\fix_android_dev_env.ps1`
- `scripts\start_pixel8a_emulator.ps1`
- `scripts\wait_android_device_ready.ps1`
- `scripts\run_android_project_verification.ps1`
- `scripts\repair_adb.ps1`
- `scripts\android_device_matrix.ps1`
- `scripts\clean_gradle_android_caches_safe.ps1`
- `scripts\new_android_project_sanity_check.ps1`

Tutti gli script passano parsing PowerShell.

## Benchmark e verifiche progetto

Progetto reale usato: `C:\Users\seste\Documents\parole create`.

Run wrapper/build/lint/unit:

- `assembleDebug`: PASS, 4.73 s
- `testDebugUnitTest`: PASS, 1.41 s
- `lintDebug`: PASS, 26.70 s
- summary: `qa\parole_create_20260702_091544\summary.txt`

Run con device policy `EmulatorOrTcl`:

- `assembleDebug`: PASS, 7.41 s
- `testDebugUnitTest`: PASS, 1.41 s
- `lintDebug`: PASS, 23.57 s
- `connectedDebugAndroidTest`: WARN, 87.34 s
- TCL/6102H: 10/10 test PASS
- Pixel_8a AVD: 1/10 test FAIL
- Pixel fisico: non usato
- summary: `qa\parole_create_20260702_092139\summary.txt`

Run finale solo emulatore dopo fix test/cleanup:

- `assembleDebug`: PASS, 20.11 s
- `testDebugUnitTest`: PASS, 2.45 s
- `lintDebug`: PASS, 45.40 s
- `connectedDebugAndroidTest`: PASS, 94.86 s
- Device usato: `Pixel_8a(AVD) - 17`
- Pixel fisico: non visibile/non usato
- TCL: non usato
- Cleanup: PASS, nessun `emulator/qemu` residuo
- summary: `qa\parole_create_20260702_094137\summary.txt`

## Comando quotidiano consigliato

```powershell
$ReportRoot = "C:\Users\seste\Documents\MegaVault\ai\reports\thinkpad_android_dev_optimization_20260702_085726"
& "$ReportRoot\scripts\run_android_project_verification.ps1" -ProjectPath "<repo>" -UseEmulator Pixel_8a -RunLint -RunUnitTests -RunConnectedTests -KillStartedEmulator -DevicePolicy EmulatorOrTcl
```

Solo TCL:

```powershell
& "$ReportRoot\scripts\run_android_project_verification.ps1" -ProjectPath "<repo>" -RunLint -RunUnitTests -RunConnectedTests -DevicePolicy TclOnly
```

Solo emulatore:

```powershell
& "$ReportRoot\scripts\run_android_project_verification.ps1" -ProjectPath "<repo>" -UseEmulator Pixel_8a -RunLint -RunUnitTests -RunConnectedTests -KillStartedEmulator -DevicePolicy EmulatorOnly
```

Policy assoluta corrente: non usare Pixel fisico nei test. Target ammessi: `EmulatorOnly`, `TclOnly`, oppure `EmulatorOrTcl`.

## Checklist prima di far lavorare Codex su un'app Android

1. Aprire una nuova PowerShell.
2. Confermare `adb devices -l`: al momento solo TCL o emulatore, non Pixel fisico.
3. Se serve AVD: `& "$ReportRoot\scripts\start_pixel8a_emulator.ps1" -AvdName Pixel_8a`.
4. Se serve TCL: sbloccarlo manualmente se richiede PIN.
5. Nel repo: verificare `.\gradlew.bat --version`.
6. Eseguire il comando quotidiano sopra.
7. Leggere `summary.txt` nella cartella QA generata.

## Interventi manuali rimasti

Defender exclusions richiedono PowerShell amministratore:

```powershell
Add-MpPreference -ExclusionPath "C:\Users\seste\.gradle"
Add-MpPreference -ExclusionPath "C:\Users\seste\.android"
Add-MpPreference -ExclusionPath "C:\Users\seste\AppData\Local\Android\Sdk"
Add-MpPreference -ExclusionPath "C:\Users\seste\Documents\MTT"
Add-MpPreference -ExclusionPath "C:\Users\seste\Documents\SuperContacts"
Add-MpPreference -ExclusionPath "C:\Users\seste\Documents\parole create"
```

Rischio: le esclusioni riducono la scansione antivirus. Applicarle solo a repo/cache di sviluppo, non a Downloads/Desktop.

Update disponibili ma non applicati automaticamente:

```powershell
winget upgrade --id Git.Git --exact
winget upgrade --id Google.AndroidStudio --exact
```

Gradle globale: non disponibile via winget su questa macchina. Continuare wrapper-first; se serve davvero un Gradle globale, installarlo manualmente da distribuzione ufficiale e aggiungere solo il relativo `bin` al PATH utente.

## File principali

- Audit iniziale: `logs\initial_audit_raw.txt`
- Audit post-fix: `logs\audit_android_dev_env_20260702_091311.txt`
- Fix log: `logs\fix_android_dev_env_20260702_090510.txt`
- Verifica finale nuova shell: `logs\final_new_shell_verification.txt`
- Playbook: `troubleshooting_playbook.md`
- Evidence follow-up PASS: `qa\parole_create_20260702_094137\summary.txt`
