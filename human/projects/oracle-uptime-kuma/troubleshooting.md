# Troubleshooting

Connessione:

```bash
ssh oracle-vm
cd /opt/uptime-kuma
sudo docker ps --filter name=uptime-kuma
curl -sS -I --max-time 10 http://127.0.0.1:3002/dashboard
sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db 'PRAGMA integrity_check;'
```

Accesso amministrativo:

```bash
ssh -L 3001:127.0.0.1:3002 oracle-vm
```

Aprire `http://150.230.148.128:3001/dashboard`. In alternativa, aprire `http://127.0.0.1:3001` dopo aver avviato il tunnel SSH.

Inventario sicuro:

```bash
sudo sqlite3 -readonly -header -column /opt/uptime-kuma/data/kuma.db \
  'select id,name,type,active,parent,"interval",timeout,retry_interval,maxretries from monitor order by id;'
sudo sqlite3 -readonly -header -column /opt/uptime-kuma/data/kuma.db \
  'select monitor_id,notification_id from monitor_notification order by monitor_id,notification_id;'
```

Backup prima di modificare:

```bash
sudo mkdir -p /opt/uptime-kuma/backups
sudo cp -a /opt/uptime-kuma/data/kuma.db /opt/uptime-kuma/backups/kuma-pre-<prompt>-$(date -u +%Y%m%dT%H%M%SZ).db
```

Per un monitor rosso:

- Verificare prima il servizio sorgente, il timer, lo script e il file env locale.
- Per i push, controllare che il pusher abbia mandato HTTP 200 e che l'heartbeat sia fresco.
- Per i backup, leggere lo stato locale del backup: Kuma non e' la verita' finale.
- Per freeze analysis, leggere `mint-freeze-forensics` prima di cambiare soglie Kuma.
- Non stampare mai URL `/api/push/<token>`, token Telegram o chat id.

Errore `OCI runtime exec failed`:

```bash
df -hT /run /tmp / /var/lib/docker
sudo du -xh -d 2 /run | sort -h | tail -n 30
sudo journalctl -u docker -u containerd -b --no-pager | grep -Ei 'OCI|runc|no space|copy stream'
sudo docker exec uptime-kuma true
```

Caso risolto `#672184`: `/run` era pieno al 100% per journal runtime in `/run/log/journal`, anche se `/` e `/tmp` erano utilizzabili. Il fix e' il limite journald in `/etc/systemd/journald.conf.d/90-runtime-run-limit.conf`; rollback in `/home/ubuntu/maintenance-672184/before/journald-20260612T195948Z`. Non fare prune Docker o modifiche Kuma se `nsenter` funziona e fallisce solo il percorso runc/containerd.

Verifica hardening pubblico:

```bash
curl -i --max-time 10 http://150.230.148.128:3001/
curl -i --max-time 10 http://150.230.148.128:3001/dashboard
```

La root deve redirigere a `/dashboard` e `/dashboard` deve restituire `200 OK`. Un URL `/api/push/...` valido deve continuare a restituire HTTP 200 dal proxy.

Per ridurre rumore:

- Non spegnere Telegram su guasti reali.
- Correggere prima pusher, lock, timeout curl e classificazione stato.
- Allargare intervallo/timeout/retry solo dopo aver capito la cadenza reale.
- Disattivare o marcare obsoleto solo se il monitor non ha piu una sorgente valida.
