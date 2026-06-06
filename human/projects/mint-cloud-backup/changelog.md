# mint-cloud-backup Changelog

## Eventi MegaVault
- 2026-06-06: `#482917` riduce flapping Kuma: lock nel pusher, timer 2 minuti, monitor Kuma `cloud backup` a interval 180s/timeout 60s/retries 2 e fallback messaggi non vuoti.
- 2026-06-02T06:54:28+02:00: `#284916` registra `mint-cloud-backup` in MegaVault/neodocs senza modificare runtime live.
- 2026-06-02: `#739284` corregge monitoraggio cloud backup: falso auth da JSONL + `.gvfs` + stale lock; heartbeat Kuma torna `running/up`.
