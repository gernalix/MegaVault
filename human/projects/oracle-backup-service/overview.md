# Oracle backup service

La documentazione operativa è stata migrata nel repository proprietario:

- overview (`../../../../projects/oracle-backup-service/docs/human/overview.md`; status=owner_repo_verified_local_2026-08-01)
- operations (`../../../../projects/oracle-backup-service/docs/ai/OPERATIONS.md`; status=owner_repo_verified_local_2026-08-01)
- incidenti (`../../../../projects/oracle-backup-service/docs/ai/INCIDENT_REGISTRY.md`; status=owner_repo_verified_local_2026-08-01)

Stato verificato il 26 luglio 2026:

- repository: `/home/daniele/projects/oracle-backup-service`;
- ramo: `main`;
- VM: `ubuntu@150.230.148.128`;
- backup remoto OCI: OK, snapshot `685d4861`;
- `restic check`: OK;
- restore test `/etc/hostname`: OK;
- healthcheck: tutti i controlli OK;
- `REMOTE_DEGRADED`: assente.

Accesso:

```bash
oracle_env=/home/daniele/.config/codex/secrets/oracle.env
test -r "$oracle_env" || exit 1
set -a; . "$oracle_env"; set +a
test -r "$ORACLE_KEY_FILE" || exit 1
ssh -i "$ORACLE_KEY_FILE" -p "$ORACLE_PORT" \
  -o BatchMode=yes -o IdentitiesOnly=yes \
  "$ORACLE_USER@$ORACLE_HOST"
```

`oracle.env` e la chiave privata separata restano fuori dai repository, entrambi `0600`; contenuti e valori non devono mai entrare in MegaVault o Git.
