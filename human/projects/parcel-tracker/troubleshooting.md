# parcel-tracker Troubleshooting

## Problemi e sintomi rilevati nel codice
- parcel_tracker.py:14:import urllib.error
- parcel_tracker.py:76:error TEXT
- parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:
- parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
- parcel_tracker.py:109:return resp.read().decode(charset, errors="replace")
- parcel_tracker.py:145:except json.JSONDecodeError:
- parcel_tracker.py:192:digest = hashlib.sha256(page.encode("utf-8", errors="replace")).hexdigest()
- parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
- parcel_tracker.sh:3:set -euo pipefail

## Comandi/verifiche utili trovati
- parcel_tracker.sh:2:#!/usr/bin/env bash
- parcel_tracker.sh:6:PYTHON_BIN="${PYTHON_BIN:-python3}"

## Safety prima di correggere
- dev/project.metadata.json:9:"metadata_version": 1,
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
