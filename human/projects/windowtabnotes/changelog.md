# WindowTabNotes Changelog

## Eventi MegaVault
- 2026-06-10: `#428673` rafforza e verifica il test Firefox end-to-end. Lo script `system/scripts/test-firefox-extension.sh` ora usa URL univoci per run, carica `windowtabnotes@local` come add-on temporaneo in Firefox reale via Selenium, apre tre tab, verifica overlay GTK su tre contesti, salva tre testi passando dal service worker Firefox a Native Messaging e SQLite, riavvia `windowtabnotes.service`, riapre Firefox e verifica persistenza DB + overlay su tre contesti. Esito verificato: `ok=true` su Firefox 151.0.4. Limite rimasto: il profilo reale standard `/home/daniele/.config/mozilla/firefox/50b1zmic.default-release` non carica permanentemente l'estensione locale unsigned; `firefox-status --json` lo segnala come `extension_not_loaded_in_active_profile`.
- 2026-06-10: `#594271` fixa il flusso Firefox end-to-end. Il servizio era attivo, ma il daemon riconosceva solo Chrome come contesto browser-tab; quindi le tab Firefox potevano arrivare al native host senza far comparire la nota giusta. In piu Firefox riusava id tab piccoli e poteva scontrarsi con vecchi contesti DB. Ora Firefox usa id interni separati, il daemon mostra note per tab Firefox, `firefox-status` riconosce i profili temporanei di test e `system/scripts/test-firefox-extension.sh` apre Firefox con add-on temporaneo, tre tab e verifica tre finestrelle note distinte.
- 2026-06-07: `#618739` fixa Firefox locale: `browser-extension-firefox/` passa da symlink a directory self-contained, `native-debug` verifica `allowed_extensions`, aggiunti `firefox-status --json` e `system/scripts/test-firefox-extension.sh`; profilo attivo verificato `/home/daniele/.config/mozilla/firefox/50b1zmic.default-release`, native messaging ok, standard Firefox resta limitato a temporary add-on non firmato.
- 2026-06-07: `#739284` verifica e rende operativo `windowtabnotes.service` come systemd --user 24/7: `enabled`, `active`, `Linger=yes`, `Restart=always`, restart manuale ok, kill `MainPID` ok con auto-restart, dashboard/search/overlay probe ok; `check --json` reso robusto ai lock SQLite live separando `window_sync`.
- 2026-06-06: `#482916` aggiunge estensione Firefox MV3 con codice comune Chrome, manifest Gecko `windowtabnotes@local`, install wrapper `system/scripts/install-firefox.sh` e diagnostica native host Chrome/Firefox separata.
- 2026-06-01T18:25:43+02:00: `#482719` follow-up ha portato a `v22`: il daemon ora crea e mostra la nota per il contesto attivo quando manca; verificato `overlay_count=1`.
- 2026-06-01T18:16:12+02:00: `#482719` ha portato WindowTabNotes a `v21`, hardenato `windowtabnotes.service`, aggiunto `windowtabnotes-status` e migrato lo schema SQLite a v5 con snapshot del contesto nota.
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.

## Evidenza audit
- File codice/config/test/script analizzati: 32 / 32.
- Invarianti estratte: 90; data/storage facts: 80; rischi: 57; bug markers: 70.
