# Audit Telegram MegaVault

Stato: audit completato il 2026-06-13. Nessuna migrazione eseguita.

Questo audit ha cercato tutti gli usi Telegram locali e sulla VM Oracle. Lo scopo era capire cosa esiste gia, scegliere la base migliore per una futura libreria comune e preparare il CSV che dovra essere compilato manualmente con i chat_id.

## Risultato principale

La migliore base trovata e:

`/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py`

Motivi:

- non contiene token o chat_id hardcoded;
- funziona sia da CLI sia come import Python;
- supporta messaggi e file;
- ha timeout HTTP;
- gestisce errori in modo piu pulito delle copie vecchie;
- e gia usato da molti script locali.

Non e stata creata nessuna libreria nuova in questa esecuzione.

## Progetti trovati

Sono stati trovati 26 progetti o runtime che usano Telegram in modo reale o legacy:

- MultiTimeTracker
- SuperContacts
- amici-fb
- amici-fb-vm-legacy
- parcel-tracker
- disk-usage-monitor
- home-incremental-backup
- home-seed-critical-backup
- surface-recovery-hardening
- mint-manual-updates
- codex-token-watcher
- codex-usage-monitor-vm
- codex-weekly-limit-monitor-vm
- owntracks-sqlite-watcher
- owntracks-watcher
- facebook-video-archiver
- oracle-backup-service
- remote-opt-oracle-backup
- oracle-uptime-kuma
- telegram-insert-bot
- telegram-media-monitor
- telegram-bot-vm-disabled
- porno-bot-vm
- strano-anello-vm
- yt-dlp-downloader-oracle-vm
- workflowy-import-vm

Il CSV da compilare e:

`/home/daniele/codex-workspace/MegaVault/dev/ai/infrastructure/telegram_projects_chat_id.csv`

Il file contiene solo i nomi progetto. I chat_id sono vuoti apposta.

## Stato attuale

La situazione e mista:

- molti script locali usano gia il helper `amici_fb/telegram_notify.py`;
- alcune parti della VM Oracle hanno copie vecchie del helper con token/chat_id hardcoded;
- alcuni progetti inviano Telegram direttamente via Bot API invece di usare un helper comune;
- alcuni bot completi usano `python-telegram-bot` o Telethon e non vanno trattati come semplici notificatori;
- Uptime Kuma ha una notifica Telegram configurata nel suo database, da non cambiare insieme agli script Python.

## Vantaggi della centralizzazione futura

- un solo token Telegram gestito in modo coerente;
- chat_id per progetto tramite CSV/config;
- meno duplicati `telegram_notify.py`;
- meno rischio di token o chat_id hardcoded nei repo;
- stesso comportamento su Linux Mint e VM Oracle;
- test e troubleshooting piu semplici.

## Rischi principali

- VM Oracle contiene helper vecchi con segreti hardcoded;
- MultiTimeTracker e SuperContacts hanno percorsi release/finalize con chat_id o token fuori dalla futura mappa comune;
- i watchdog storage/backup sono ad alto rischio: non vanno migrati senza test controllati;
- i bot completi non sono equivalenti a semplici notifiche e richiedono trattamento separato;
- Kuma Telegram notification id 1 e condivisa da molti monitor: non va modificata senza backup DB e piano dedicato.

## Prossima esecuzione

La prossima esecuzione dovra:

1. leggere il CSV compilato;
2. creare la libreria comune;
3. installarla su Linux Mint e VM Oracle;
4. migrare prima i progetti a basso rischio;
5. migrare backup/watchdog solo con test dedicati;
6. mantenere compatibilita legacy;
7. eliminare duplicati solo dopo verifica;
8. aggiornare documentazione e registri.

Nessuno di questi passi e stato eseguito ora.
