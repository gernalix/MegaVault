# Custom Services Status

Aggiornamento operativo: 2026-06-07 07:40 CEST.

Prompt: `#847261`.

## Anti-Freeze Legacy Rimossi

Eliminati da systemd/disko e rimossi dal routing MegaVault vivo:

- `freeze-reboot-monitor.service`
- `freeze-zram-swap.service`
- `screen-watchdog.service`
- `system-watchdog.service`
- `/home/daniele/freeze_reboot_monitor`
- `/home/daniele/codex-workspace/mint_freeze_diag`
- `/home/daniele/codex-workspace/system_watchdog`
- `/home/daniele/bin/kuma-auto-healer`
- `/home/daniele/.config/kuma-auto-healer`
- `/etc/sysctl.d/99-codex-mint-freeze.conf`
- `/etc/sysctl.d/99-z-freeze-anti-freeze.conf`

Verifica:

```bash
systemctl list-unit-files --no-pager | rg -i 'freeze-reboot|freeze-zram|screen-watchdog|system-watchdog'
systemctl --user list-unit-files --no-pager | rg -i 'freeze|autofix|os-observer|system-watchdog|screen-watchdog'
```

Risultato 2026-06-07: nessuna unità legacy trovata.

## Nuovi Servizi Osservativi

| Nome | Scope | Stato atteso | Script | Note |
|---|---|---|---|---|
| `mint-freeze-forensics.service` | user | enabled/running | `~/.local/bin/mint-freeze-forensics daemon` | sampler 5s; no remediation |
| `mint-resource-guardian.timer` | user | enabled/running | `mint-resource-guardian.service` | early warning; cooldown; no kill automatico |
| `mint-resource-guardian.service` | user | oneshot | `mint-freeze-forensics guardian --once --non-interactive` | CLI manuale supporta prompt `[K] [I] [W] [D]` |

## Servizi Lasciati Fuori Dalla Rimozione

- `transfer-usb-io-watchdog.service`: non è anti-freeze generico; guardrail dati per transfer rsync.
- `rsync-uptime-kuma-push.service`: pusher Kuma specifico transfer.
- `home-backup-kuma-push*`, `mint-cloud-backup-kuma-push*`, `mint-update-tracker*`: monitor/pusher specifici, non remediation freeze.

## Kuma

- Kuma runtime: Oracle VM `150.230.148.128`, container `uptime-kuma`.
- Nuovo gruppo: `Mint Freeze Analysis`, id `12`.
- Monitor: `Freeze Gaps` id `13`, `PSI Memory` id `14`, `PSI IO` id `15`, `Guardian Alerts` id `16`, `Forensics Alive` id `17`.

## Fonti

- `systemctl list-unit-files`
- `systemctl --user list-unit-files`
- `systemctl --user status mint-freeze-forensics.service`
- `ssh ubuntu@150.230.148.128 sudo sqlite3 /opt/uptime-kuma/data/kuma.db`
