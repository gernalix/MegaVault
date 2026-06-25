# amici_fb Changelog

## 2026-06-25

### Stabilizzazione Task Scheduler 16:44

- Diagnosticato il task segnalato come `Running`: al momento dell'ispezione era
  gia' `Ready`, con `LastTaskResult=1`; il log locale mostrava fallimento su
  Facebook, non un processo zombie.
- Causa reale: sessione Playwright non piu' accettata da Facebook. `/me/friends`
  veniva reindirizzato alla pagina profilo salvato/device login; il vecchio
  detector la classificava erroneamente come consenso cookie per via del footer
  `Cookies`.
- Aggiunto riconoscimento `profile_chooser`, rimossi marker cookie troppo
  generici e aggiunto un retry bounded sul pulsante Continua.
- Aggiunto `--login-wait-seconds` per rigenerare la sessione Facebook/2FA senza
  input da console; usato con successo per salvare un nuovo
  `fb_storage_state.json`.
- Ridotto il limite massimo del task a `45` minuti.
- Rimossi dall'indice Git, senza cancellarli dal disco, `fb_storage_state.json`
  e i file runtime gia' tracciati in `data\`.
- Test diretto headless: exit `0`, durata `37.812s`, 185 amici estratti.
- Test Task Scheduler: `LastTaskResult=0`, durata `47.424s`, stato finale
  `Ready`, nessun processo figlio residuo.
- Output verificato: `C:\codex_clean_repos\amici_fb\data\amici_2026-06-25T144337Z.csv`.

### Migrazione Windows iniziale

- Clonato il repository ufficiale in `C:\codex_clean_repos\amici_fb`.
- Confrontato l'export Linux `C:\codex\amici_fb` senza usare la sua `.git`.
- Recuperati dal vecchio export: `.env` locale ignorato, database
  `amici_fb.sqlite3`, storico `data\` come runtime state locale.
- Rimossi gli artefatti operativi Linux dal progetto Windows.
- Aggiunti `README.md` e `install_windows_task.ps1`.
- Aggiornato `amici_fb_daily.cmd` per usare solo Python globale.
- Aggiornato `amici_fb_task_runner.py` per usare `requests` invece di `curl`.
- Corretto uso UTC per Python 3.14.
- Installate/verificate dipendenze globali: `requests 2.34.2`,
  `playwright 1.60.0`, Chromium Playwright.
- Eseguiti due run end-to-end: ultimo exit `0`, 184 amici estratti, snapshot e
  diff prodotti.
- Creato task Windows `amici_fb Daily Snapshot 0900`: trigger giornaliero 09:00,
  `StartWhenAvailable=true`, working directory corretta, logon `Interactive`
  dopo rifiuto di `S4U` da parte di Windows.

## Eventi precedenti MegaVault

- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
