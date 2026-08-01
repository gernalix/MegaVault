# Audit Telegram Notify

Aggiornato: 2026-08-01. Autorità: [audit AI](../../ai/infrastructure/telegram_notify_audit.md).

Il helper condiviso corrente proviene da `projects/amici_fb/telegram_notify` ed è installato in `/usr/local/lib/python3.14/site-packages/telegram_notify`. I quattro moduli installati hanno hash identici alla sorgente; `_shared/telegram_notify.py` è soltanto il wrapper di compatibilità.

Le API supportano testo, messaggi con titolo, file e notifiche compatibili. Il destinatario opzionale `chat_id` è keyword-only; senza valore viene usato il destinatario privato configurato. Errori HTTP e di trasporto sono sanitizzati e il token non viene riportato.

La configurazione utente è in `~/.config/telegram-notify/telegram-notify.env`, directory `0700`, file `0600`. Il controllo configurazione è passato senza stampare valori e non è stato inviato alcun messaggio reale.

La scansione Python del repository `amici_fb` non ha trovato implementazioni Bot API duplicate fuori dal helper canonico e dai test mock. Lo stato degli altri repository è `UNKNOWN` perché non sono stati inclusi nella revalidazione live.

La versione precedente è preservata in `../archive/infrastructure/telegram_notify_audit_legacy.md`.
