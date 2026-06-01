# maintenance-486 Troubleshooting

## Problemi e sintomi rilevati nel codice
- scripts/ssh_diag_486.sh:2:set -euo pipefail
- scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 // true
- scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true
- scripts/ssh_diag_486.sh:16:timeout 35 ssh \
- scripts/ssh_diag_486.sh:18:-o ConnectTimeout=12 \

## Comandi/verifiche utili trovati
- scripts/ssh_diag_486.sh:1:#!/usr/bin/env bash
- scripts/ssh_diag_486.sh:5:key="${2:-../ssh-key-2026-02-01.key}"
- scripts/ssh_diag_486.sh:12:echo "=== raw SSH banner ==="
- scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true
- scripts/ssh_diag_486.sh:15:echo "=== short SSH command ==="
- scripts/ssh_diag_486.sh:16:timeout 35 ssh \

## Safety prima di correggere
- dev/project.metadata.json:9:"metadata_version": 1,
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
