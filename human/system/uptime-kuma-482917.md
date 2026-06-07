# Uptime Kuma cleanup prompt 482917

Aggiornato: 2026-06-06.

## Cosa e stato fatto

- Inventariati i monitor push dell'istanza Kuma `http://150.230.148.128:3001`.
- Salvato backup DB Kuma prima delle modifiche: `/opt/uptime-kuma/backups/kuma-pre-482917-20260606T181225Z.db`.
- Allargate le finestre dei monitor rumorosi per evitare DOWN quando un job arriva pochi secondi o minuti in ritardo.
- Disattivati i monitor obsoleti: `mint heartbeat`, `rsync-transfer`, `codex-token-watcher`.
- Conservate le notifiche Telegram sui monitor attivi: gli alert reali non sono stati silenziati.
- Aggiunti tag `482917-reviewed`, `push-monitor` e, dove opportuno, `obsolete-disabled`.
- Rimosso `os-observer` dagli indici e dalle schede vive MegaVault come richiesto.

## Monitor dopo la correzione

| Monitor | Stato operativo | Note |
|---|---|---|
| cloud backup | attivo/up | interval 180s, timeout 60s, retries 2; pusher con lock e messaggi non vuoti |
| mint-home-backup | attivo/up warning | follow-up `#618903`: `rsync_exit=137` era abort controllato dal runtime guard (`ABORTED_SAFE`) classificato male; heartbeat resta warning, non successo |
| amici_fb | attivo/up | invariato salvo tag MegaVault/Kuma |
| disk-usage-monitor | attivo/up | interval 420s, timeout 60s, retries 2; heartbeat RUNNING iniziale |
| parcel-tracker | attivo/up | interval 2400s, timeout 60s |
| mint-home-backup-retention | attivo/up | separato dal fallimento del backup principale |
| software audit mint | attivo/up | SQLite busy temporaneo diventa UP `DB_BUSY retrying` |
| mint heartbeat | disattivato | heartbeat generico obsoleto |
| rsync-transfer | disattivato | nessun transfer live verificato da monitorare |
| codex-token-watcher | disattivato | nessun runner/servizio live trovato |

## Documentazione trasversale

Questa pagina copre i cambiamenti che attraversano piu progetti o script live fuori da un singolo repository. I dettagli specifici sono stati riportati anche nelle schede MegaVault dei progetti interessati:

- `mint-cloud-backup`
- `mint-update-tracker`
- `surface-recovery-hardening`
- `oracle-uptime-kuma`
- `mint-freeze-forensics`

## Problemi aperti

- `mint-home-backup`: follow-up `#618903` completato. Il caso 2026-06-06 e `ABORTED_SAFE` per load alto; `rsync_exit=137` resta DOWN se non esiste un motivo `WHY_ABORTED` persistito dal guard.
- I report storici generati da vecchie migrazioni MegaVault possono ancora contenere riferimenti a `os-observer`; non sono stati riscritti per evitare churn su artefatti storici.
