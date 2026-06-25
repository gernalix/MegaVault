# amici_fb Troubleshooting

## Controlli base Windows

```powershell
cd C:\codex_clean_repos\amici_fb
python --version
python -m pip show playwright requests
python -m playwright --version
python -m py_compile .\amici_fb.py .\amici_fb_task_runner.py .\telegram_notify.py .\_shared\telegram_notify.py
```

## Esecuzione manuale

```powershell
cd C:\codex_clean_repos\amici_fb
python -u -X faulthandler .\amici_fb_task_runner.py --headless
```

## Sessione Facebook scaduta

Se il run headless segnala login richiesto, 2FA, selettore profilo o loop sul
pulsante Continua:

```powershell
cd C:\codex_clean_repos\amici_fb
python -u .\amici_fb_task_runner.py --login --login-wait-seconds 600
```

Nella finestra Chromium aperta da Playwright completare login e 2FA. Lo script
salva automaticamente `fb_storage_state.json` solo quando `/me/friends` risulta
accessibile.

## Browser Playwright mancante

```powershell
python -m playwright install chromium
```

## Task Scheduler

```powershell
Get-ScheduledTask -TaskName "amici_fb Daily Snapshot 0900"
Get-ScheduledTaskInfo -TaskName "amici_fb Daily Snapshot 0900"
```

Per registrare di nuovo:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install_windows_task.ps1
```

Il task deve avere:

- Stato finale `Ready`
- `LastTaskResult=0`
- Working directory `C:\codex_clean_repos\amici_fb`
- Azione `cmd.exe /d /c ""C:\codex_clean_repos\amici_fb\amici_fb_daily.cmd""`
- `StartWhenAvailable=true`
- limite massimo `45` minuti

## Output e log

- Log scheduler: `C:\codex_clean_repos\amici_fb\data\scheduler_logs\`
- Diagnostica browser: `C:\codex_clean_repos\amici_fb\data\browser_diag_<timestamp>\`
- Snapshot CSV: `C:\codex_clean_repos\amici_fb\data\amici_<timestamp>.csv`
- Diff CSV: `C:\codex_clean_repos\amici_fb\data\diff_<precedente>_vs_<corrente>.csv`

## Note sicurezza

`.env` e `fb_storage_state.json` contengono o possono contenere dati sensibili.
Non incollare valori reali nei log condivisi.

`data\`, `fb_storage_state.json`, database SQLite e log sono runtime locali:
devono restare fuori dai commit anche se presenti sul disco.
