# Alert Registry

Aggiornato: 2026-07-26. Autorita' operativa: [ALERT_REGISTRY AI](../../ai/global/ALERT_REGISTRY.md).

## Fedora corrente

Fedora System Monitor 1.3.1 e' verificato come sender Kuma sul nuovo host. Usa cinque monitor: Fedora Host (ID 39), Storage (40), Network (41), Services (42) e Software (43). L'occupazione zram e' informativa: la pressione usa MemAvailable, PSI, swap rate, reclaim e OOM. Storage conserva gli alert reali; i falsi `smart_check_failed` sono risolti senza sopprimere SMART o Btrfs.

Fedora System Monitor 1.3.0 usa inoltre il helper condiviso
`telegram_notify.py` per notificare aumenti o diminuzioni cumulative di almeno
1 GiB dello spazio libero. Riusa il file privato esistente, mantiene lo stato nel
database del monitor e non aggiunge servizi o timer. Primo avvio e delta sotto
soglia sono silenziosi; una notifica reale marcata TEST è stata consegnata
nell'attività 418732.

Gli endpoint sono root-only e non compaiono nel repository o nei log. L'istanza Kuma esistente usa ancora HTTP: il funzionamento e' verificato, ma HTTPS resta necessario per la confidenzialita' del trasporto.

Sono attivi i segnali locali Fedora ABRT per crash/oops, `smartd` per salute storage e `systemd-oomd` per pressione memoria. Questi servizi non sostituiscono il monitoraggio applicativo.

## Regole

Non stampare o committare token, chat ID o push URL. Prima di dichiarare un alert attivo verificare sender, timer, consegna e destinazione; gli alert sono segnali e non autorizzano remediation automatica.
