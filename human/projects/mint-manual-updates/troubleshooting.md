# mint-manual-updates Troubleshooting

## Problemi e sintomi rilevati nel codice
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200

## Comandi/verifiche utili trovati
- UNKNOWN: nessun comando rilevato in build/script/CI.

## Safety prima di correggere
- dev/project.metadata.json:9:"metadata_version": 1,
- systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v1
- systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v1
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
