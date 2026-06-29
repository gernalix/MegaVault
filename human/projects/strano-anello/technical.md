# Technical

Comandi:

```bash
cd /home/ubuntu/bots/strano_anello
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/strano_db_maintenance.py analyze --exact-counts
.venv/bin/python tools/strano_db_maintenance.py duplicates
.venv/bin/python tools/strano_db_maintenance.py anomalies --max-db-bytes 104857600 --max-wal-bytes 67108864 --max-diagnostic-rows 200000
```

Compaction sicura:

```bash
sudo systemctl stop strano-anello.timer
sudo systemctl stop strano-anello.service
.venv/bin/python tools/strano_db_maintenance.py compact --apply --replace
sudo systemctl restart datasette.service
sudo systemctl start strano-anello.timer
```
