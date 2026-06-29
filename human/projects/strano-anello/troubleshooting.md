# Troubleshooting

- DB cresce oltre 100 MiB: eseguire `tools/strano_db_maintenance.py anomalies` e `top-tables`.
- WAL cresce: verificare che il servizio non sia in esecuzione, poi checkpoint via maintenance compact o SQLite.
- Spazio non liberato dopo replace DB: controllare `sudo lsof +L1`; Datasette puo' tenere aperto il vecchio inode, quindi `sudo systemctl restart datasette.service`.
- Timer non parte: `systemctl status strano-anello.timer strano-anello.service`.
- Run fallisce: controllare `journalctl -u strano-anello.service -n 100 --no-pager` e `data/health.json`.
