# Attivita 631904 - incidente GNOME/GDM dopo restart di systemd-logind

Data indagine: 2026-07-23 (Europe/Copenhagen)
Stato: PASS CON WARNING

## Esito

La causa dell'incidente e il comando `systemctl restart systemd-logind` eseguito
alle 16:18:28 CEST durante l'attivita 847316, non il drop-in Qulose, non il
profilo energetico balanced e non il blocco automatico GNOME. Il restart ha
temporaneamente rimosso il servizio D-Bus `org.freedesktop.login1` mentre la
sessione Wayland di GNOME deteneva i dispositivi di input/seat; GDM ha quindi
avviato un nuovo greeter su tty1. La sua interfaccia e stata scambiata per una
lock screen.

La configurazione GNOME preesistente era gia persistita e corretta:

- `org.gnome.desktop.screensaver lock-enabled=false`;
- `org.gnome.desktop.session idle-delay=uint32 0`;
- timeout AC e batteria `0`, azione `nothing`, `idle-dim=false`.

`lock-enabled` significa solo bloccare quando lo screensaver diventa attivo;
il blocco manuale resta un percorso distinto. Non risultano chiamate
`loginctl lock-session`, `org.gnome.ScreenSaver.Lock`, suspend o hibernate nel
boot dell'incidente.

## Timeline ricostruita

| Ora CEST | Evidenza | Interpretazione |
| --- | --- | --- |
| 16:18:28 | audit/sudo: `systemctl restart systemd-logind` | inizia il fattore scatenante. |
| 16:18:28 | `systemd-logind`: stop, poi nuova istanza PID 80100 | il servizio che assegna seat/VT/dispositivi viene ricreato. |
| 16:18:28 | `gnome-shell[9246]`: impossibile rilasciare/aprire `/dev/input/event*`, nome `org.freedesktop.login1` senza owner | perdita diretta del controllo dei dispositivi della sessione Wayland. |
| 16:18:28-30 | PAM `gdm-launch-environment` per `gdm-greeter`, `gnome-shell[80532]` avviato come Wayland display server | GDM crea il greeter, non uno screen shield GNOME. |
| 16:21:41 | PAM `gdm-password` per `daniele`, terminale `/dev/tty1` | la password e autenticazione GDM, non prova di auto-lock. |
| 16:21:41-43 | vecchia shell: `NotInControl`; `Unexpected non-NULL onscreen_native->next_frame` | conflitto/race di handoff tra vecchia sessione, greeter e compositor. |
| 16:22:49 | kernel: `fbcon: Taking over console`; `Console: switching to colour frame buffer device 240x75` | spiega schermo nero e caratteri testuali in alto a sinistra. |
| 16:23 circa | fine del journal precedente; `last` classifica chiusura come `crash` | il riavvio non e stato pulito; il log non prova se fu forzato dall'utente. |
| 16:24-25 | nuovo boot e nuova sessione Wayland attiva | la configurazione logind viene caricata senza restart in-sessione. |

## Schermo nero con caratteri

Il passaggio esplicito a `fbcon` rende piu probabile una console framebuffer
senza getty che un campo password GNOME rimasto senza rendering: non risultano
un nuovo prompt PAM o un agetty nel momento 16:22:49. Per questo i caratteri
potevano essere eco visuale senza prompt, shell, login o messaggi. Non ci sono
errori AMDGPU/DRM, page-flip timeout, ring fault, GPU reset, OOM killer,
systemd-oomd kill, panic, watchdog o coredump che indichino un guasto kernel o
driver indipendente.

## Correzioni applicate

1. Nessuna modifica alla configurazione GNOME: era gia persistita e non era la
   causa.
2. Nessuna modifica al drop-in
   `/etc/systemd/logind.conf.d/90-ignore-short-power-key.conf`: la politica e
   ora caricata dal boot e la proprieta D-Bus `HandlePowerKey` vale `ignore`.
3. Ripristinato, come richiesto, il profilo persistente Power Profiles/TuneD a
   `performance`/`throughput-performance`. Verificati:
   `ActiveProfile=performance`, `tuned-adm active=throughput-performance`,
   `/etc/tuned/ppd_base_profile=performance`.

## Prevenzione e rollback

Per future modifiche a `logind.conf`, non eseguire `systemctl restart
systemd-logind` nella sessione grafica attiva. Installare il drop-in e
applicarlo al prossimo riavvio pianificato; il boot appena effettuato ha gia
confermato l'applicazione sicura della policy.

Rollback del solo profilo energetico richiesto da questa attivita:

```bash
sudo busctl set-property net.hadess.PowerProfiles /net/hadess/PowerProfiles \
  net.hadess.PowerProfiles ActiveProfile s balanced
```

Non e necessario ne sicuro riavviare `systemd-logind` per il rollback del
profilo energetico.

## Recupero se ricompare

1. Premere `Ctrl+Alt+F3` per una TTY libera e accedere.
2. Raccogliere prima le prove senza riavviare:

```bash
journalctl -b -0 -o short-iso | tail -n 500
journalctl --user -b -0 -p warning..alert -o short-iso
loginctl list-sessions
ps -eo pid,ppid,stat,comm,args --forest | rg 'gnome-shell|gdm|mutter|Xwayland'
```

3. Se GDM/seat e incoerente, salvare l'output e riavviare il sistema dalla TTY
   con `sudo systemctl reboot`. Non riavviare `systemd-logind` come tentativo
   di riparazione della sessione Wayland.

Il journald e persistente (`/var/log/journal`, circa 3.7 GiB) e
`systemd-coredump.socket` e attivo; non e stato aggiunto tracing permanente.

## Limite residuo

Non e stata eseguita una riproduzione intenzionale del restart logind, per non
interrompere nuovamente la sessione grafica. La correlazione causale e tuttavia
diretta nei log; resta ignoto soltanto il gesto esatto che ha effettuato il
riavvio non pulito finale.
