# mint-manual-updates Troubleshooting

## Sintomi

- `status=skipped_guardrail`: il run e stato bloccato da load/RAM/swap/PSI/freeze/apt/batteria critica. `rsync` da solo non blocca piu il run.
- `rsync detected: allowed/non-blocking`: trasferimento `rsync` rilevato e consentito; lo script resta gentile tramite priorita systemd basse.
- Un venv fallisce: controllare il file dedicato in `~/.local/state/mint-manual-updates/venv-logs/`; gli altri venv continuano.
- Android SDK fallisce: controllare `~/.local/state/mint-manual-updates/android-sdk-history/available-updates-*.txt` e `last-report.txt`.
- Android Studio segnala `remote build unknown`: download automatico saltato per evitare archivio 1+ GB inutile; seguire il comando manuale nel report solo se serve.

## Comandi utili

```bash
bin/mint-manual-updates --run
bin/mint-manual-updates --status
tail -n 220 ~/.local/state/mint-manual-updates/mint-manual-updates.log
bin/mint-manual-updates --explain-guardrails
systemctl --user status mint-manual-updates.service --no-pager
systemctl --user status mint-manual-updates.timer --no-pager
```

## Safety prima di correggere

- Non usare `sudo pip`, `pip` globale o `pip3` globale per aggiornamenti Python di sistema.
- Non ricreare updater duplicati.
- Non aggiungere service/timer paralleli.
- Non rimuovere AVD, SDK root, system-images o file Gradle/Kotlin di progetto.
- Non scaricare archivi Android Studio grandi solo per verificare che la build installata sia identica.
