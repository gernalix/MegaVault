# Disk Usage Monitor Troubleshooting

## T7/root cresce di oltre 100 GiB in poche ore

Caso verificato: prompt `731584`, 2026-06-13.

Sintomo: Disk Usage Monitor segnala `/dev/sda2` montato `/` in crescita di circa +157 GiB in 24h.

Causa trovata: `/home/daniele/.codex/logs_2.sqlite-wal` era circa 152.44 GiB. Il DB SQLite era integro e in WAL mode. Codex tiene DB/WAL/SHM aperti durante la sessione; molte scritture di log possono lasciare un WAL enorme allocato finche' un checkpoint SQLite `TRUNCATE` riesce.

Verifica rapida:

```bash
du -sh ~/.codex
find ~/.codex -xdev -type f -size +1G -printf '%s\t%TY-%Tm-%Td %TH:%TM:%TS\t%p\n' | sort -nr
lsof ~/.codex/logs_2.sqlite ~/.codex/logs_2.sqlite-wal ~/.codex/logs_2.sqlite-shm
sqlite3 -readonly ~/.codex/logs_2.sqlite 'PRAGMA journal_mode; PRAGMA wal_autocheckpoint; PRAGMA synchronous; PRAGMA page_size; PRAGMA page_count; PRAGMA freelist_count; PRAGMA quick_check;'
sqlite3 ~/.codex/logs_2.sqlite 'PRAGMA wal_checkpoint(PASSIVE);'
/home/daniele/.local/bin/codex-sqlite-wal-maintenance --dry-run
systemctl --user status codex-sqlite-wal-maintenance.timer codex-sqlite-wal-maintenance.service --no-pager
```

Fix locale installato: `codex-sqlite-wal-maintenance.timer`. Il timer gira ogni 30 minuti. Soglie: soft warning `1 GiB`, hard maintenance `5 GiB`, critical notification `20 GiB`. Lo script fa `quick_check`, registra holder `lsof`, tenta solo `PRAGMA wal_checkpoint(TRUNCATE)`, mostra dimensioni before/after e non cancella file a mano.

Per controllare recidive, il WAL deve restare piccolo o crescere lentamente:

```bash
for i in 1 2 3 4 5; do date -u +%Y-%m-%dT%H:%M:%SZ; stat -c '%n %s bytes' ~/.codex/logs_2.sqlite*; sleep 30; done
df -h /
```

Non fare:
- `rm ~/.codex/logs_2.sqlite-wal` o `rm ~/.codex/logs_2.sqlite-shm` mentre Codex e' aperto.
- `pkill codex` o `killall codex` generico.
- Cancellare `~/.codex/sessions`, config, credential o transcript recenti.
