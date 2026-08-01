# ADB Device Keeper

Aggiornato: 2026-07-10. Autorita' operativa: [ADB_DEVICE_KEEPER AI](../../ai/global/ADB_DEVICE_KEEPER.md).

`adb-device-keeper.service` mantiene disponibile il server ADB dell'utente e riconnette esclusivamente il Google Pixel 8a e il TCL 6102H gia' associati. Non esegue pairing, non modifica i telefoni e non dipende da Android Studio.

Il servizio e' abilitato e attivo anche fuori dalla sessione grafica grazie al linger dell'utente `daniele`. Controlla ogni 60 secondi quando entrambi i telefoni sono presenti e ogni 25 secondi quando ne manca almeno uno; i tentativi falliti hanno backoff fino a 5 minuti.

## Comandi essenziali

- Stato: `systemctl --user status adb-device-keeper.service`
- Riavvio: `systemctl --user restart adb-device-keeper.service`
- Log recenti: `journalctl --user -u adb-device-keeper.service -n 100 --no-pager`
- Log live: `journalctl --user -u adb-device-keeper.service -f`
- Dispositivi: `/home/daniele/Android/Sdk/platform-tools/adb devices -l`
- Ciclo manuale: `/home/daniele/.local/bin/adb-device-keeper --once`

## Limite TCL

Il TCL usa Android 12 e durante i test non ha pubblicato stabilmente il record mDNS di connessione. Finche' l'ultimo IP e porta restano validi, la cache verificata consente il recupero. Se cambiano senza che il telefono pubblichi mDNS, controllare che sia sulla stessa Wi-Fi e che “Debug wireless” sia attivo; se necessario disattivarlo e riattivarlo sul telefono, poi eseguire il ciclo manuale. Non rifare il pairing salvo revoca effettiva dell'associazione.

Percorsi, test, sicurezza, verifica post-riavvio e rollback completo sono nel documento AI autorevole collegato sopra.
