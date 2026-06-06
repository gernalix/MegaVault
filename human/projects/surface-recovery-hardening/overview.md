# surface-recovery-hardening Overview

Questo progetto documenta e supporta le operazioni di recovery del Surface Linux Mint durante trasferimenti USB pesanti. Il caso operativo attuale e `rsync-transfer`: copia conservativa dal disco Seagate 4TB BitLocker al disco ext4 `Seagate6TB2`.

## Stato operativo verificato
- Verificato: 2026-06-03 01:37 CEST, prompt `#847392`.
- Repository: `/home/daniele/codex-workspace/surface-recovery-hardening`
- Commit verificato: `a7d791d`
- Transfer attivo: `rsync-transfer.service` transient user unit, ripreso sullo stesso albero rsync dopo `SIGCONT`.
- Sorgente: `/dev/sdb2` aperta come `/dev/mapper/source_bitlocker`, montata read-only su `/media/daniele/Seagate Expansion Drive`.
- Destinazione: `/dev/sdc1`, UUID `75e5363d-6736-4a7e-84be-5242f4735a27`, ext4 rw su `/media/daniele/Seagate6TB2`.
- Destinazione dati: `/media/daniele/Seagate6TB2/vecchio disco`.

## Servizi
- `rsync-transfer.service`: transient, avviato con `systemd-run --user`, non persistente per evitare duplicati.
- `transfer-usb-io-watchdog.service`: system-wide, enabled, monitora eventi USB/I/O storage del transfer e mette in pausa rsync solo su eventi critici rilevanti.
- `rsync-uptime-kuma-push.service`: user, disabilitato in `#482917` perche non risultava un transfer live sicuro da monitorare; riabilitarlo solo insieme a un nuovo `rsync-transfer` verificato.
- `transfer-vecchio-disco-adaptive-throttle.service`: user, enabled, mantiene profilo I/O conservativo.
- `media-daniele-Seagate6TB2.automount`: system-wide, enabled, monta la destinazione per UUID.

## Kuma #482917
- Monitor Kuma `rsync-transfer` disattivato come obsoleto/no live runner.
- Non usare il rosso storico di Kuma come evidenza di transfer fallito; verificare sempre processi, mount e log live prima di riattivare il pusher.

## Link
- AI doc: [AI doc](../../../ai/projects/surface-recovery-hardening.md)
- Metadata: [dev/project.metadata.json](../../../../surface-recovery-hardening/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../surface-recovery-hardening/dev/legacy)
- Repository: [repo path](../../../../surface-recovery-hardening)
