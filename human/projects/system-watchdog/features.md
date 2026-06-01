# system_watchdog Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `watchdog.py`: utc_now, utc_iso, local_iso, read_text, boot_id, uptime_seconds, connect_db, last_heartbeat

## Confini operativi
- install.sh:10:sudo install -m 0644 "$SERVICE_SRC" "$SERVICE_DST"
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
- uninstall.sh:5:sudo rm -f /etc/systemd/system/system-watchdog.service
- uninstall.sh:6:sudo systemctl daemon-reload
- dev/project.metadata.json:9:"metadata_version": 1,
- install.sh:8:python3 --version >/dev/null
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
