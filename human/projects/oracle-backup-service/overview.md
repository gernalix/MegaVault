# Oracle backup service

La documentazione operativa è stata migrata nel repository proprietario:

- overview (`../../../projects/oracle-backup-service/docs/human/overview.md`; status=owner_repo_verified_local_2026-08-01)
- operations (`../../../projects/oracle-backup-service/docs/ai/OPERATIONS.md`; status=owner_repo_verified_local_2026-08-01)
- incidenti (`../../../projects/oracle-backup-service/docs/ai/INCIDENT_REGISTRY.md`; status=owner_repo_verified_local_2026-08-01)

Stato verificato il 26 luglio 2026:

- repository: `/home/daniele/MegaVault/projects/oracle-backup-service`;
- ramo: `codex/731904-oracle-remote-recovery`;
- VM: `ubuntu@150.230.148.128`;
- backup remoto OCI: OK, snapshot `685d4861`;
- `restic check`: OK;
- restore test `/etc/hostname`: OK;
- healthcheck: tutti i controlli OK;
- `REMOTE_DEGRADED`: assente.

Accesso:

```bash
ssh -i /home/daniele/MegaVault/secrets/oracle-cloud/oracle-vm-rsa \
  -o IdentitiesOnly=yes \
  ubuntu@150.230.148.128
```

Il contenuto della chiave non deve mai essere copiato in MegaVault o Git.
