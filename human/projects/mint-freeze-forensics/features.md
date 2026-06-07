# Features

- Campionamento 5s: uptime, loadavg, memoria, swap, PSI cpu/memory/io, top RSS/CPU/I/O, process groups browser/java/gradle/Android Studio/codex/rsync, docker fallback, temperatura.
- Campionamento storage: root mount/source/fstype, swap path/backing device, `/sys/block` essenziale, `lsblk` compatto e flag USB/Samsung/T7.
- Delta I/O per processo: read/write/cancelled-write da `/proc/<pid>/io` e major page faults da `/proc/<pid>/stat`, con rate limit e skip sotto PSI estrema.
- Fallback `vmstat/pidstat/iostat` cacheato ogni 60s per ridurre overhead.
- Ring buffer persistente con retention e size cap.
- Gap detector: `PROBABLE_FREEZE_OR_STALL` quando il delta fra campioni supera 30s.
- Evidence bundle per gap: `journal.txt` e `dmesg.txt`.
- Evidence bundle esteso: `kernel-storage-keywords.txt` e `io-storage-snapshot.json`.
- Human report con freeze 24h, PSI, processi dominanti e cause euristiche.
- `io-report` con freeze reali 24h, top processi I/O, root/swap su T7, errori kernel storage/USB e probabilità browser/swap/T7/filesystem/kernel/altro.
- Guardian separato, whitelist persistente, nessuna azione automatica.
- Push Kuma per storico/grafici/alerting.
