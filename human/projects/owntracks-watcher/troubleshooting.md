# owntracks-watcher Troubleshooting

## Config persa dopo reinstallazione Android
- Modalita' corretta: HTTP.
- URL corretto: `https://owntracks.danielegalati.com/owntracks`.
- Tracker ID per continuita' storico: `ta`.
- Non usare MQTT: non e' presente un broker nel percorso live verificato.
- Non usare `http://150.230.148.128:8083`: la porta diretta non e' il percorso pubblico supportato.

## Verifiche VM
- Stato servizio: `systemctl status owntracks-http-server.service --no-pager -l`.
- Log recenti: `journalctl -u owntracks-http-server.service --since '5 minutes ago' --no-pager -n 50`.
- Tunnel: `systemctl status cloudflared.service --no-pager -l`.
- DB ultimo punto: `sqlite3 -header -column /home/ubuntu/sync_root/db/owntracks.db "select id,quando,device,lat,lon,acc,batt from positions order by id desc limit 5;"`.
- Integrita' DB: `sqlite3 /home/ubuntu/sync_root/db/owntracks.db "pragma quick_check;"`.
- Test esterno valido: `TS=$(date -u +%s); curl -sS -i https://owntracks.danielegalati.com/owntracks -H 'Content-Type: application/json' -d "{\"_type\":\"location\",\"tid\":\"CD\",\"tst\":$TS,\"lat\":55.676123,\"lon\":12.568321,\"acc\":12,\"batt\":88}"`.

## Safety prima di correggere
- Non stampare contenuti di `/root/.cloudflared/*.json`, token Cloudflare, segreti Datasette, Telegram o Kuma.
- Non aprire firewall/porta `8083` senza decisione esplicita: Cloudflare Tunnel e' il percorso pubblico.
- Non ruotare segreti per semplice reinstallazione app.
- Un `GET /` a `owntracks.danielegalati.com` ritorna `404`; non e' un guasto. Il receiver accetta `POST /owntracks`.
