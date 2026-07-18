# Alert Registry

Aggiornato: 2026-07-18. Autorita' operativa: [ALERT_REGISTRY AI](../../ai/global/ALERT_REGISTRY.md).

## Fedora corrente

Fedora System Monitor 1.2.0 e' verificato come sender Kuma sul nuovo host. Usa cinque monitor: Fedora Host (ID 39), Storage (40), Network (41), Services (42) e Software (43). L’occupazione zram è ora informativa: Host è verde perché MemAvailable è 68,752%, PSI e pressione composta sono zero e non risultano OOM. Storage resta correttamente rosso per Seagate al 2,8% libero e per lo storico di rimozione non sicura; Network, Services e Software sono verdi.

Gli endpoint sono root-only e non compaiono nel repository o nei log. L'istanza Kuma esistente usa ancora HTTP: il funzionamento e' verificato, ma HTTPS resta necessario per la confidenzialita' del trasporto.

Sono attivi i segnali locali Fedora ABRT per crash/oops, `smartd` per salute storage e `systemd-oomd` per pressione memoria. Questi servizi non sostituiscono il monitoraggio applicativo.

## Regole

Non stampare o committare token, chat ID o push URL. Prima di dichiarare un alert attivo verificare sender, timer, consegna e destinazione; gli alert sono segnali e non autorizzano remediation automatica.
