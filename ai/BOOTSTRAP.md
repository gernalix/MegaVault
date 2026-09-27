# MEGAVAULT_BOOTSTRAP

authority_checkout=/home/daniele/MegaVault
authority_db=/home/daniele/MegaVault/megavault.sqlite
authority_branch=master

- Applica prima `/home/daniele/.codex/AGENTS.md`.
- Leggi solo i fatti DB e la sezione di `MEGAVAULT_PROTOCOL.md` necessari al task; per PersonalHub usa solo `personalhubdoc.md`.
- Risolvi `project_id` esclusivamente dal DB canonico. Non duplicare inventari o protocolli.
- Scrivi tramite CLI/helper canonici. Non editare SQLite direttamente.
- Lavora in task worktree; integra tramite single writer. Il checkout canonico non e' un workspace agente.
- Aggiorna il canonico solo con `python3 tools/megavault_update.py`: dirty state, branch errato o operazione Git pendente bloccano senza stash, commit automatici, reset o rebase.
- Valida con `PYTHONDONTWRITEBYTECODE=1 python3 megavault.py validate` e SQLite integrity/FK.
- Recovery Phase A 853479: checkpoint verificato in `/home/daniele/.local/state/megavault-phase-a/853479`; la copia `/home/daniele/projects/MegaVault` non e' autorevole.
