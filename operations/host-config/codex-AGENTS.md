# Codex Operating Entrypoint

Questo file e' l'unico entrypoint operativo generale da leggere e applicare normalmente per i task di Daniele. Serve a permettere prompt futuri brevi, naturali e autosufficienti: la richiesta dell'utente definisce lo scopo, queste regole assorbono il bootstrap ripetitivo.

## Regole Universali

- Fai solo quanto richiesto e usa il minimo cambiamento necessario.
- Parti dai file, componenti, comandi o fatti direttamente pertinenti alla richiesta.
- Non fare esplorazione generale del repository o del filesystem salvo necessita' concreta.
- Riutilizza informazioni, evidenze e output gia' verificati nella sessione se lo stato non e' cambiato.
- Non fare refactor, cleanup, modernizzazioni, ottimizzazioni o fix fuori scope.
- Evita tool-call, comandi, letture, test e verifiche equivalenti o ridondanti.
- Non ripetere retry identici senza nuova evidenza o stato modificato.
- Esegui prima test/verifiche mirati; amplia solo se rischio, fallimento o requisito esplicito lo richiede.
- **Notifiche interattive sospese su richiesta utente**: non inviare notifiche Fedora o Telegram prima/dopo azioni interattive e non introdurre ritardi artificiali. `/home/daniele/.local/bin/codex-interactive-notify` è un compatibility shim silenzioso. Resta vietato usare input simulato via tastiera/PTY/GUI per controllare Codex stesso.
- Quando acceptance criteria e verifiche necessarie sono PASS, termina subito: niente audit, esplorazione o rassicurazioni extra.
- Nel report finale sii conciso: risultato, file modificati, verifica, commit/push o blocker reale.

- Grindr Web: le credenziali persistenti, quando configurate, sono nel Fedora Secret Service con riferimento canonico `/home/daniele/.config/grindr-auth/credential-ref.json`. Non stampare, loggare, copiare in repo/chat/MegaVault o mostrare i valori. Recuperale solo al momento dell'uso e passale direttamente al flusso di login. Prima di login/navigazione interattiva applica sempre il contratto Fedora+Telegram prima/dopo.

## Routing Condizionale

- Task locali ordinari: usa solo questo file e i file direttamente pertinenti al task.
- PersonalHub o suoi moduli/componenti: leggi e segui solo `/home/daniele/MegaVault/ai/personalhubdoc.md`; usa `/home/daniele/MegaVault/megavault.sqlite` solo per fatti strutturati necessari.
- Meta-infrastruttura/MegaVault/Git/monitoring: unica fonte operativa AI `/home/daniele/MegaVault/ai/META_INFRASTRUCTURE.md`; nessun protocollo C2 aggiuntivo.
- MegaVault: leggi `/home/daniele/MegaVault/ai/BOOTSTRAP.md` solo quando servono project context persistente, `project_id`, fatti/regole custoditi in MegaVault, infrastruttura, servizi, incidenti, segreti, o aggiornamenti MegaVault; apri poi solo la sezione specialistica indicata.

## Identita' e Fonti

- Se `project_id=N` e' fornito, risolvilo esclusivamente da `/home/daniele/MegaVault/megavault.sqlite`; non inferirlo da memoria, nomi, path o somiglianze.
- Non consultare MegaVault per modifiche locali banali quando la richiesta e i file pertinenti bastano.
- Non inventare fatti: verifica live cio' che serve per affermazioni correnti.
