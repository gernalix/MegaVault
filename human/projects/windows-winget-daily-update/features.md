# Windows Winget Daily Update Features

## Funzioni
- Aggiorna le sorgenti winget.
- Elenca gli aggiornamenti disponibili.
- Esegue l'upgrade completo con accettazione accordi package/source.
- Scrive log timestampati per stdout e stderr.
- Continua anche se un comando winget termina con errore.
- Applica timeout per evitare blocchi lunghi.
- Mantiene `latest.log` come accesso rapido all'ultimo run.
- Usa PowerShell 7 se disponibile.

## Comandi utili
Avvio manuale:

```powershell
Start-ScheduledTask -TaskName 'Winget Daily Update'
```

Ultimo log:

```powershell
Get-Content 'C:\Users\seste\Documents\windows\maintenance\logs\latest.log' -Tail 200
```

Stato task:

```powershell
Get-ScheduledTask -TaskName 'Winget Daily Update'
```
