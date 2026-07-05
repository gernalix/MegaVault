# owntracks-watcher Troubleshooting

## Config persa dopo reinstallazione Android
- Modalita' corretta: HTTP.
- URL corretto: `https://owntracks.danielegalati.com/owntracks`.
- Tracker ID per continuita' storico: `ta`.
- Device ID sul Pixel puo' restare `akita`: la continuita' DB usa `tid=ta`.
- Permessi richiesti: posizione precisa, posizione in background, notifiche; aggiungere OwnTracks alla whitelist battery/device-idle quando possibile.
- Non usare MQTT: non e' presente un broker nel percorso live verificato.
- Non usare `http://150.230.148.128:8083`: la porta diretta non e' il percorso pubblico supportato.

## Errore Android "java.io.IOException: Failed to parse JSON"
- Causa verificata prompt `#482917`: OwnTracks Android 2.5.9 parsea anche il body HTTP 2xx come messaggio OwnTracks; `{"status":"ok"}` non e' valido perche' manca `_type`.
- Fix server live: `POST /owntracks` con payload valido deve rispondere `HTTP 200` con body `[]`.
- Backup pre-fix VM: `/home/ubuntu/bots/owntracks_http_server/owntracks_http_server.py.bak.20260613T033922Z.prompt482917`.
- Verifica app: logcat deve mostrare `HTTP response body: []`, `Message sent successfully`, endpoint `IDLE`.
- Verifica DB: `positions` deve avere righe `device=ta` con `quando` UTC/Z, `lat`, `lon`, `acc`, `batt`.

## Recovery ADB post-reinstallazione
- Import config: creare `.otrc` con `_type=configuration`, `mode=3`, `url=https://owntracks.danielegalati.com/owntracks`, `auth=false`, `tid=ta`, `monitoring=3`, `locatorInterval=900`, `locatorDisplacement=150`; aprire `owntracks:///config?inline=<base64>` e salvare.
- Permessi: `adb shell pm grant org.owntracks.android android.permission.ACCESS_BACKGROUND_LOCATION`; `adb shell cmd deviceidle whitelist +org.owntracks.android`.
- Smoke: `adb shell am start-foreground-service -n org.owntracks.android/.services.BackgroundService -a org.owntracks.android.SEND_LOCATION_USER`.
- Restore batteria: dopo smoke usare `adb shell am start-foreground-service -n org.owntracks.android/.services.BackgroundService -a org.owntracks.android.CHANGE_MONITORING --ei monitoring 3`.

## Verifiche VM
- Stato servizio: `systemctl status owntracks-http-server.service --no-pager -l`.
- Log recenti: `journalctl -u owntracks-http-server.service --since '5 minutes ago' --no-pager -n 50`.
- Tunnel: `systemctl status cloudflared.service --no-pager -l`.
- DB ultimo punto: `sqlite3 -header -column /home/ubuntu/sync_root/db/owntracks.db "select id,quando,device,lat,lon,acc,batt from positions order by id desc limit 5;"`.
- Integrita' DB: `sqlite3 /home/ubuntu/sync_root/db/owntracks.db "pragma quick_check;"`.
- Test esterno valido: `TS=$(date -u +%s); curl -sS -i https://owntracks.danielegalati.com/owntracks -H 'Content-Type: application/json' -d "{\"_type\":\"location\",\"tid\":\"CD\",\"tst\":$TS,\"lat\":55.676123,\"lon\":12.568321,\"acc\":12,\"batt\":88}"`.
- Risposta attesa test esterno: `HTTP 200` e body `[]`.

## Safety prima di correggere
- Non stampare contenuti di `/root/.cloudflared/*.json`, token Cloudflare, segreti Datasette, Telegram o Kuma.
- Non aprire firewall/porta `8083` senza decisione esplicita: Cloudflare Tunnel e' il percorso pubblico.
- Non ruotare segreti per semplice reinstallazione app.
- Un `GET /` a `owntracks.danielegalati.com` ritorna `404`; non e' un guasto. Il receiver accetta `POST /owntracks`.
