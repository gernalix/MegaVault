# Windows Winget Daily Update Overview

Automazione locale per aggiornare ogni giorno le sorgenti winget e installare gli aggiornamenti disponibili quando il PC e' acceso/disponibile.

## Stato
- Task Scheduler: `Winget Daily Update`
- Script: `C:\Users\seste\Documents\windows\maintenance\winget_daily_update.ps1`
- Log: `C:\Users\seste\Documents\windows\maintenance\logs`
- Pianificazione: ogni giorno alle `03:00`, con recupero quando disponibile
- Sleep: il task non sveglia il PC
- Privilegi: registrato non elevato; la registrazione elevata ha ricevuto `Access is denied`

## Comandi eseguiti
- `winget source update`
- `winget upgrade`
- `winget upgrade --all --accept-package-agreements --accept-source-agreements`

## Link
- AI doc: [AI doc](../../../ai/projects/windows-winget-daily-update.md)
- Metadata: assente
- Legacy docs: assenti
- Repository/cartella: [maintenance](../../../../windows/maintenance)
- Script: [winget_daily_update.ps1](../../../../windows/maintenance/winget_daily_update.ps1)
