# mint-manual-updates Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| UNKNOWN | No explicit roadmap found. |

## Deferred Or Risky Work
- dev/TEST_PLAN.md: - `fwupdmgr get-updates` with `No updatable devices` is not treated as a critical error.
- dev/legacy/README.md: `--relaxed` è solo manuale: alza solo load a `CPU * 3.00` e PSI CPU a `35`. Non rilassa RAM, swap, processi pesanti, freeze emergency, apt/dpkg o batteria critica.
- dev/legacy/README.md: `--force` è solo manuale e richiede un TTY con conferma esatta `FORCE_UPDATE`. Non bypassa apt/dpkg attivi, freeze emergency o batteria critica. Il timer non usa mai `--relaxed` o `--force`.
- dev/legacy/dev/INDEX.md: - Manuale `--force`: richiede TTY e conferma `FORCE_UPDATE`; non bypassa apt/dpkg, freeze emergency o batteria critica.
- dev/legacy/README.md: - `fwupd`: esegue refresh e `get-updates`; applica solo update che non dichiarano reboot/interazione manuale e passa comunque dai safety check di `fwupdmgr`. Gli altri sono solo segnalati.
- dev/legacy/README.md: - diagnosi `fwupd` con `--version`, `get-devices`, `get-updates --verbose` e journal; riavvia `fwupd` e forza refresh solo se il fallimento sembra servizio/cache;
- dev/legacy/README.md: Se `sudo -n` non e disponibile, le sezioni apt falliscono pulite e il report mostra il comando manuale necessario.
- dev/legacy/dev/INDEX.md: - `--maintenance-fixups` e solo manuale e non deve essere aggiunto al timer.
- dev/legacy/dev/AGENT_RULES.md: - Nei fixup manuali non usare `sudo pip` o `--break-system-packages`; preservare pacchetti apt-managed.
- dev/legacy/dev/AGENT_RULES.md: - Firmware su Surface delicato: applicare solo update che non dichiarano reboot/interazione manuale e senza disabilitare i safety check di `fwupdmgr`; altrimenti segnalare soltanto.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
