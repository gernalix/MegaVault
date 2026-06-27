# Windows Winget Daily Update Troubleshooting

## Il task non aggiorna alcuni pacchetti
Possibile causa: il task e' registrato con privilegi limitati.

Rimedio: aprire PowerShell come amministratore e ri-registrare il task con `RunLevel Highest`.

## Leggere l'ultimo log
```powershell
Get-Content 'C:\Users\seste\Documents\windows\maintenance\logs\latest.log' -Tail 200
```

## Avviare manualmente
```powershell
Start-ScheduledTask -TaskName 'Winget Daily Update'
```

## Disabilitare
```powershell
Disable-ScheduledTask -TaskName 'Winget Daily Update'
```

## Rimuovere
```powershell
Unregister-ScheduledTask -TaskName 'Winget Daily Update' -Confirm:$false
```

## Il PC era in sleep
Comportamento atteso: il task non deve svegliare il PC. Viene avviato quando Windows lo considera disponibile.
