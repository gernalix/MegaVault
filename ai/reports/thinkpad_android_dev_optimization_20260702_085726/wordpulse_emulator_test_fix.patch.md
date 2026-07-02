# WordPulse Emulator Test Fix

File modificato localmente:

`C:\Users\seste\Documents\parole create\app\src\androidTest\java\com\wordpulse\app\WordPulseUiInstrumentedTest.kt`

Motivo:

Su `Pixel_8a(AVD) - 17`, il report AndroidTest indicava che il testo `Total occurrences` esisteva nell'unmerged semantics tree ma non nel merged tree. Il TCL/6102H passava, quindi il problema era una fragilita del matcher Compose, non dati mancanti.

Patch applicata:

```diff
-            composeRule.onNodeWithText("Total occurrences").assertExists()
-            composeRule.onNodeWithText("2").assertExists()
+            composeRule.onNodeWithText("Total occurrences", useUnmergedTree = true).assertExists()
+            composeRule.onNodeWithText("2", useUnmergedTree = true).assertExists()
```

Conferma:

- Direct single-test instrumentation on emulator: `qa\emulator_direct_diagnosis_20260702_093807\summary.txt`, `instrument_exit=0`.
- Full Gradle `EmulatorOnly` verification: `qa\parole_create_20260702_094137\summary.txt`, `overall=PASS`.
