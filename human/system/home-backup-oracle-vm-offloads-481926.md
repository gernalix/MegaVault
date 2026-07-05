# Oracle VM offloads nei backup home #481926

Dal 2026-06-22 la cartella seguente e' inclusa nei backup rsync locali:

```bash
/media/daniele/Seagate6TB2/oracle-vm-offloads
```

Nei nuovi snapshot finira' qui:

```bash
/media/daniele/Seagate6TB2/home-backups/snapshots/<timestamp>/external/oracle-vm-offloads/
```

La configurazione live e':

```bash
/home/daniele/.config/home-backup/home-backup.env
HOME_BACKUP_EXTRA_SOURCES="/media/daniele/Seagate6TB2/oracle-vm-offloads"
```

Validazione: sorgente presente, circa `5.0G`, destinazione con circa `2.7T` liberi, dry-run extra diretto PASS con `18` file regolari e `5,292,109,458` byte. Gli exclude non filtrano `.db`, `.sqlite`, `.sqlite3`, manifest o sha256.
