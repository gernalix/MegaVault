# system_watchdog Troubleshooting

## Problemi e sintomi rilevati nel codice
- systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
- systemd/system-watchdog.service:21:StandardError=journal
- watchdog.py:9:import urllib.error
- watchdog.py:38:except OSError:
- watchdog.py:50:except (ValueError, IndexError):
- watchdog.py:67:error TEXT,
- watchdog.py:100:except ValueError:
- watchdog.py:140:except OSError:
- watchdog.py:144:def push(url, timeout):
- watchdog.py:148:with urllib.request.urlopen(req, timeout=timeout) as resp:
- install.sh:2:set -euo pipefail
- logs.sh:2:set -euo pipefail
- status.sh:2:set -euo pipefail
- uninstall.sh:2:set -euo pipefail

## Comandi/verifiche utili trovati
- install.sh:1:#!/usr/bin/env bash
- install.sh:8:python3 --version >/dev/null
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- logs.sh:1:#!/usr/bin/env bash
- logs.sh:4:journalctl -u system-watchdog.service -n "${1:-100}" --no-pager
- status.sh:1:#!/usr/bin/env bash
- status.sh:5:systemctl --no-pager --full status system-watchdog.service // true
- status.sh:7:python3 "$ROOT/watchdog.py" last // true
- uninstall.sh:1:#!/usr/bin/env bash
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
- uninstall.sh:6:sudo systemctl daemon-reload

## Safety prima di correggere
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
