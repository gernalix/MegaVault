# Troubleshooting

```bash
ssh -i /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key ubuntu@150.230.148.128
sudo docker ps --filter name=uptime-kuma
sudo sqlite3 -header -column /opt/uptime-kuma/data/kuma.db "select id,name,type,active,parent from monitor order by id;"
```

Token:

- Non stampare e non committare gli URL `/api/push/<token>`.
- Lato Mint sono in `~/.config/mint-freeze-forensics/kuma.env`.

Backup prima di modificare Kuma:

```bash
sudo mkdir -p /opt/uptime-kuma/backups
sudo cp -a /opt/uptime-kuma/data/kuma.db /opt/uptime-kuma/backups/kuma-pre-<prompt>-$(date -u +%Y%m%dT%H%M%SZ).db
```

Prima di aggiungere o cambiare monitor:

- Verificare se esiste gia un monitor con lo stesso nome o lo stesso servizio.
- Preferire aggiornare il monitor esistente invece di crearne uno duplicato.
- Se si modifica direttamente SQLite, prima leggere `.schema` e fare backup.
- Dopo la modifica, documentare query eseguite e risultato.
- Riavviare/verificare il container solo se la modifica lo richiede.

Per collegare un servizio locale a Kuma:

- Creare o riusare un monitor push in Kuma.
- Salvare l'URL push completo solo in un env file locale fuori da Git.
- Aggiungere un pusher leggero, con timeout e messaggio esplicito.
- Eseguire un push di test e verificare HTTP 200.
- Aggiornare `SERVICE_REGISTRY.md` per il servizio/timer e `ALERT_REGISTRY.md` per il monitor.

Per ridurre alert rumorosi:

- Non spegnere notifiche reali senza diagnosi.
- Capire se il DOWN e causato da servizio fermo, token errato, rete, timer troppo lento o finestra Kuma troppo stretta.
- Correggere prima il pusher locale; poi, se serve, aumentare intervallo, timeout o retry.
- Se un monitor non serve piu, disattivarlo o marcarlo obsoleto senza cancellare storico.
