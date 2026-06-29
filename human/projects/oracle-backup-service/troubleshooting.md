# oracle-backup-service Troubleshooting

## Problemi e sintomi rilevati nel codice
- scripts/backup.sh:2:set -euo pipefail
- scripts/backup.sh:13:LAST_REMOTE_ERROR_FILE="$STATE_DIR/last_remote_error"
- scripts/backup.sh:14:LAST_REMOTE_FAILURE_EPOCH_FILE="$STATE_DIR/last_remote_failure_epoch"
- scripts/backup.sh:36:RESTIC_BACKUP_TIMEOUT_SECONDS="${RESTIC_BACKUP_TIMEOUT_SECONDS:-5400}"
- scripts/backup.sh:37:RESTIC_PRUNE_TIMEOUT_SECONDS="${RESTIC_PRUNE_TIMEOUT_SECONDS:-3600}"
- scripts/backup.sh:38:REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS="${REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS:-21600}"
- scripts/backup.sh:82:cleanup_failed_snapshot() {
- scripts/backup.sh:96:cleanup_failed_snapshot
- scripts/check_backup_health.py:20:LAST_FAILED_REPOS_FILE = STATE_DIR / "last_failed_repos"
- scripts/check_backup_health.py:22:LAST_REMOTE_ERROR_FILE = STATE_DIR / "last_remote_error"
- scripts/check_backup_health.py:37:except FileNotFoundError:
- scripts/check_backup_health.py:45:except Exception:
- scripts/check_backup_health.py:52:except ValueError:
- scripts/check_backup_health.py:69:except ValueError:
- scripts/check_backup_health.py:77:except Exception:
- scripts/check_backup_health.py:87:except Exception as exc:
- scripts/oracle-backup-healthcheck.sh:2:set -euo pipefail
- scripts/oracle-backup-healthcheck.sh:12:LAST_FAILED_REPOS_FILE="/var/lib/oracle_backup/last_failed_repos"

## Comandi/verifiche utili trovati
- scripts/check_remote_quota.py:1:#!/usr/bin/env python3
- scripts/prune.sh:1:#!/usr/bin/env bash
- scripts/prune.sh:7:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/prune.sh:51:if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock && \
- scripts/prune.sh:53:restic -r "$repo" forget \
- scripts/prune.sh:58:restic -r "$repo" prune \

## Stato 2026-06-05
- Quota remota OCI ancora critica: `oci:bucket-20260206-0730` usa `22.262 GBytes` (`23903533548` bytes), soglia critical `21 GiB`, limite assunto `22 GiB`.
- Repo remoto `rclone:oci:bucket-20260206-0730/oraclevm`: 837 snapshot `oracle-vm,autosnap-5min`, dal 2026-05-02 al 2026-05-05.
- Policy configurata: `RESTIC_KEEP_LAST=48`, `RESTIC_FORGET_GROUP_BY=host,tags`. Esistono snapshot prunabili secondo policy, ma restic standard non riesce a creare il lock perche' il backend rifiuta upload su `locks/...` con `StorageLimitExceeded`.
- Non eseguire prune distruttivo con `--no-lock` senza approvazione esplicita o temporaneo aumento quota. Prima scelta sicura: ottenere headroom quota, poi eseguire `/opt/oracle_backup/prune.sh`.
- Fallback locale valido: `/var/lib/oracle_backup/emergency_repo`, 27 snapshot, circa 9.572 GiB raw-data. Non cancellare finche' il remoto e' degradato.
- Pulizia `/` applicata senza toccare backup/DB: `apt-get clean`, `journalctl --vacuum-size=300M`, compressione `/var/log/syslog.1` in `/var/log/syslog.1.gz`; spazio passato da 6.6G liberi/86% a 7.5G liberi/84%.

## Stato 2026-06-29
- Root cause `BACKUP_BLOCKED_FALLBACK_QUOTA`: remoto OCI ancora pieno (`StorageLimitExceeded`), fallback locale usato, retention locale non forzata prima/dopo i write fallback.
- Fix live: `/opt/oracle_backup/backup.sh` forza la retention restic locale quando la quota fallback bloccherebbe un write e la forza di nuovo dopo un fallback riuscito.
- Non cancellare file in `/var/lib/oracle_backup/emergency_repo`; usare policy restic configurata (`LOCAL_FALLBACK_KEEP_LAST=11`, `LOCAL_FALLBACK_RETENTION_GROUP_BY=host,tags`).
- Healthcheck finale: `BACKUP_BLOCKED_FALLBACK_QUOTA` risolto; stato residuo `WARNING REMOTE_DEGRADED` finche' OCI resta pieno.
- `strano_anello.db`: circa `6.2G` (`6573379584` bytes), quindi un singolo stream fallback puo' consumare gran parte della riserva prewrite.

## Accesso VM
- Host: `ubuntu@150.230.148.128`.
- Hostname atteso: `instance-20260201-1126`.
- Chiave SSH primaria Windows: `C:\Users\seste\Downloads\Telegram Desktop\ssh-key-2026-02-01.key`.
- Comando: `ssh -i "C:\Users\seste\Downloads\Telegram Desktop\ssh-key-2026-02-01.key" -o IdentitiesOnly=yes ubuntu@150.230.148.128`.
- Se Windows OpenSSH rifiuta la chiave per ACL troppo aperte, usare una copia temporanea con permessi stretti o la chiave manutenzione verificata: `C:\Users\seste\Documents\windows\maintenance\ssh\oracle-uptime-kuma-reset.key`.
- Non copiare mai il contenuto della chiave nei documenti MegaVault.

## Safety prima di correggere
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- Non cancellare `/var/lib/oracle_backup/emergency_repo`, `/var/lib/oracle_backup/sqlite_snapshots`, DB SQLite, WAL/SHM o repo restic per liberare spazio senza snapshot/verifica e policy documentata.
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP_INTERVAL_SECONDS" -gt 0 ]]; then
- scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
- scripts/backup.sh:69:if ! flock -n 9; then
- scripts/backup.sh:85:rm -rf -- "$snap_run_dir"
- scripts/backup.sh:92:kill "$heartbeat_pid" 2>/dev/null // true
- scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh // true
- scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
