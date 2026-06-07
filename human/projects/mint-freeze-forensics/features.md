# Features

- Campionamento 5s: uptime, loadavg, memoria, swap, PSI cpu/memory/io, top RSS/CPU/I/O, process groups browser/java/gradle/Android Studio/codex/rsync, docker fallback, temperatura.
- Ring buffer persistente con retention e size cap.
- Gap detector: `PROBABLE_FREEZE_OR_STALL` quando il delta fra campioni supera 30s.
- Evidence bundle per gap: `journal.txt` e `dmesg.txt`.
- Human report con freeze 24h, PSI, processi dominanti e cause euristiche.
- Guardian separato, whitelist persistente, nessuna azione automatica.
- Push Kuma per storico/grafici/alerting.
