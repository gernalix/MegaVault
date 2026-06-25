# amici_fb Overview

`amici_fb` e' ora migrato su Windows 11.

## Stato corrente

- Repository Git valido: `C:\codex_clean_repos\amici_fb`
- Export Linux conservato: `C:\codex\amici_fb`
- Remote ufficiale: `https://github.com/gernalix/amici_fb`
- Data migrazione: `2026-06-25`
- Scheduler attivo previsto: Windows Task Scheduler, task `amici_fb Daily Snapshot 0900`
- Modalita' registrata: `Interactive`; il tentativo `S4U` e' stato negato da Windows.
- Ultimo test Task Scheduler: `2026-06-25 16:43:35`, risultato `0`, stato finale `Ready`.

## Cosa fa

Il progetto apre Facebook con Playwright, usa la sessione salvata in
`fb_storage_state.json`, estrae la lista amici, salva snapshot CSV, aggiorna
SQLite e produce un CSV di diff rispetto allo snapshot precedente.

Se Facebook chiede di nuovo login, 2FA o mostra il profilo salvato senza entrare,
rigenerare la sessione Playwright con:

```powershell
cd C:\codex_clean_repos\amici_fb
python -u .\amici_fb_task_runner.py --login --login-wait-seconds 600
```

## Runtime Windows

- Python globale: `C:\Users\seste\AppData\Local\Programs\Python\Python314\python.exe`
- Dipendenze: `playwright`, `requests`
- Browser Playwright: `C:\Users\seste\AppData\Local\ms-playwright\chromium-1223`
- Nessun ambiente Python locale e' supportato.

## Output verificato

- Snapshot: `C:\codex_clean_repos\amici_fb\data\amici_2026-06-25T144337Z.csv`
- Diff: `C:\codex_clean_repos\amici_fb\data\diff_2026-06-25T144228Z_vs_2026-06-25T144337Z.csv`
- Log: `C:\codex_clean_repos\amici_fb\data\scheduler_logs\amici_fb_daily_2026-06-25T164336.log`
- Righe snapshot: `185`
- Righe diff: `0`
