# surface-recovery-hardening Overview

Questo progetto documenta e supporta le operazioni di recovery del Surface Linux Mint durante trasferimenti USB pesanti. Il caso operativo attuale e `rsync-transfer`: copia conservativa dal disco Seagate 4TB BitLocker al disco ext4 `Seagate6TB2`.

## Stato operativo verificato
- Verificato: 2026-06-01 14:17 CEST, prompt `#847392`.
- Repository: `/home/daniele/codex-workspace/surface-recovery-hardening`
- Commit verificato: `3f455ea`
- Transfer attivo: `rsync-transfer.service` transient user unit.
- Sorgente: `/dev/sdb2` aperta come `/dev/mapper/source_bitlocker`, montata read-only su `/media/daniele/Seagate Expansion Drive`.
- Destinazione: `/dev/sdc1`, UUID `75e5363d-6736-4a7e-84be-5242f4735a27`, ext4 rw su `/media/daniele/Seagate6TB2`.
- Destinazione dati: `/media/daniele/Seagate6TB2/vecchio disco`.

## Servizi
- `rsync-transfer.service`: transient, avviato con `systemd-run --user`, non persistente per evitare duplicati.
- `transfer-usb-io-watchdog.service`: system-wide, enabled, monitora eventi USB/I/O e mette in pausa rsync se vede errori critici.
- `rsync-uptime-kuma-push.service`: user, enabled, invia stato a Kuma usando match sul vero comando rsync.
- `transfer-vecchio-disco-adaptive-throttle.service`: user, enabled, mantiene profilo I/O conservativo.
- `media-daniele-Seagate6TB2.automount`: system-wide, enabled, monta la destinazione per UUID.

## Link
- AI doc: [AI doc](../../../ai/projects/surface-recovery-hardening.md)
- Metadata: [dev/project.metadata.json](../../../../surface-recovery-hardening/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../surface-recovery-hardening/dev/legacy)
- Repository: [repo path](../../../../surface-recovery-hardening)
