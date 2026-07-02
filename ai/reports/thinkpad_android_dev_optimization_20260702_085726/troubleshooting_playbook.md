# Troubleshooting Playbook Android Dev

Report root: `C:\Users\seste\Documents\MegaVault\ai\reports\thinkpad_android_dev_optimization_20260702_085726`

## adb non trovato

Verifica:

```powershell
echo $env:ANDROID_HOME
Get-Command adb
adb --version
```

Fix:

```powershell
& "$ReportRoot\scripts\fix_android_dev_env.ps1"
```

Il PATH utente deve contenere `%ANDROID_HOME%\platform-tools`.

## emulator non trovato

Verifica:

```powershell
Get-Command emulator
emulator -version
emulator -list-avds
```

Fix: assicurare `%ANDROID_HOME%\emulator` nel PATH e installare il package SDK `emulator`.

## sdkmanager non trovato

Verifica:

```powershell
Get-Command sdkmanager
sdkmanager --version
```

Fix: installare Android SDK Command-line Tools latest da Android Studio SDK Manager o rilanciare `fix_android_dev_env.ps1`.

## JAVA_HOME sbagliato

Per Android Studio 2026.1.1 su questa macchina il JDK corretto e:

```text
C:\Program Files\Android\Android Studio\jbr
```

Verifica:

```powershell
echo $env:JAVA_HOME
java -version
javac -version
```

## Gradle daemon lento o bloccato

Usa sempre il wrapper del progetto:

```powershell
.\gradlew.bat --stop
.\gradlew.bat --status
.\gradlew.bat :app:assembleDebug --console=plain --stacktrace
```

Pulizia sicura, prima dry-run:

```powershell
& "$ReportRoot\scripts\clean_gradle_android_caches_safe.ps1" -ProjectPath "<repo>" -StopGradleDaemons -CleanProjectBuildDirs
```

Applicazione:

```powershell
& "$ReportRoot\scripts\clean_gradle_android_caches_safe.ps1" -ProjectPath "<repo>" -StopGradleDaemons -CleanProjectBuildDirs -Apply
```

## emulator non boota

Verifica accelerazione:

```powershell
emulator -accel-check
emulator -list-avds
```

Avvio standard headless:

```powershell
& "$ReportRoot\scripts\start_pixel8a_emulator.ps1" -AvdName Pixel_8a
```

Log: `logs\emulator_Pixel_8a_*`.

## device wireless ADB sparito

Riparazione:

```powershell
& "$ReportRoot\scripts\repair_adb.ps1"
adb mdns services
adb devices -l
```

Se non torna, riaprire Wireless debugging sul device e riconnettere.

## device unauthorized

Sbloccare il telefono, accettare il fingerprint RSA, poi:

```powershell
adb kill-server
adb start-server
adb devices -l
```

## device offline

```powershell
adb reconnect
adb kill-server
adb start-server
adb devices -l
```

Se e wireless: disattivare/riattivare Wireless debugging.

## device bloccato su keyguard

Check:

```powershell
& "$ReportRoot\scripts\wait_android_device_ready.ps1" -Serial "<serial>"
```

Lo script tenta wake/dismiss non distruttivi. Se serve PIN, restituisce WARN `manual unlock required`.

## connectedAndroidTest fallisce per device non pronto

Usa il comando unico con policy device:

```powershell
& "$ReportRoot\scripts\run_android_project_verification.ps1" -ProjectPath "<repo>" -UseEmulator Pixel_8a -RunLint -RunUnitTests -RunConnectedTests -KillStartedEmulator -DevicePolicy EmulatorOrTcl
```

Al momento i target consentiti sono solo emulatore e TCL/6102H. Il Pixel fisico viene disconnesso/ignorato.

Se il Pixel fisico resta collegato via USB o in una forma non disconnettibile, la verifica deve fermarsi in FAIL prima dei connected test.

## Compose test passa su TCL ma fallisce su emulatore

Caso osservato: `WordPulseUiInstrumentedTest.timelineDetailsAndPrefixSearchExposeCapturedWords` falliva su AVD cercando `Total occurrences`.

Causa: il nodo esisteva nell'unmerged semantics tree, ma il test lo cercava nel merged tree. Fix mirato:

```kotlin
composeRule.onNodeWithText("Total occurrences", useUnmergedTree = true).assertExists()
```

Conferma: run finale `EmulatorOnly` PASS in `qa\parole_create_20260702_094137`.

## Cleanup emulatore dopo run

La verifica con `-KillStartedEmulator` deve lasciare zero processi:

```powershell
Get-Process | Where-Object { $_.ProcessName -match 'emulator|qemu' }
```

Il cleanup ora considera anche processi `qemu-system-*` con `Path` vuoto, purche nati durante la run.

## lint advisory warning vs errore reale

Apri il log `lintDebug.log` nella cartella QA. Se `lintDebug` e WARN ma `assembleDebug` e `testDebugUnitTest` sono PASS, distinguere advisory SDK/AGP da errori bloccanti. Non disabilitare lint globalmente.

## AGP/Kotlin/Gradle mismatch

Controlla:

```powershell
.\gradlew.bat --version
Get-Content .\gradle\libs.versions.toml
Get-Content .\gradle\wrapper\gradle-wrapper.properties
```

Usare wrapper del repo. Evitare Gradle globale per build riproducibili.

## local.properties mancante

Fix nel repo:

```powershell
"sdk.dir=$($env:ANDROID_HOME.Replace('\','\\'))" | Set-Content .\local.properties -Encoding ASCII
```

Oppure:

```powershell
& "$ReportRoot\scripts\run_android_project_verification.ps1" -ProjectPath "<repo>" -FixLocalProperties
```

## Android Studio usa JDK diverso dalla shell

Shell attesa:

```text
JAVA_HOME=C:\Program Files\Android\Android Studio\jbr
```

In Android Studio: Settings > Build, Execution, Deployment > Build Tools > Gradle > Gradle JDK, selezionare il bundled JBR/JDK 21.

## Compose test import/deprecation drift

Eseguire:

```powershell
.\gradlew.bat :app:lintDebug :app:testDebugUnitTest --console=plain
```

Se fallisce solo lint, leggere report HTML sotto `app\build\reports\lint-results-debug.html`.

## Room schema export mancante

Se il progetto usa Room, verificare `room.schemaLocation` o `exportSchema`. Il sanity check lo segnala:

```powershell
& "$ReportRoot\scripts\new_android_project_sanity_check.ps1" -ProjectPath "<repo>"
```

## build tools/platform API non installati

Verifica:

```powershell
sdkmanager --list_installed
```

Installa:

```powershell
sdkmanager "platforms;android-36" "platforms;android-35" "build-tools;36.0.0"
```
