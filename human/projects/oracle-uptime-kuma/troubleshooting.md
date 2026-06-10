# Troubleshooting

Connessione:

```bash
ssh -i /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key ubuntu@150.230.148.128
cd /opt/uptime-kuma
sudo docker ps --filter name=uptime-kuma
sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db 'PRAGMA integrity_check;'
```

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

Per ridurre rumore:

- Non spegnere Telegram su guasti reali.
- Correggere prima pusher, lock, timeout curl e classificazione stato.
- Allargare intervallo/timeout/retry solo dopo aver capito la cadenza reale.
- Disattivare o marcare obsoleto solo se il monitor non ha piu una sorgente valida.
