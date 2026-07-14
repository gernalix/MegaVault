# Alert Registry

Aggiornato: 2026-07-14. Autorita' operativa: [ALERT_REGISTRY AI](../../ai/global/ALERT_REGISTRY.md).

## Fedora corrente

Fedora System Monitor 1.1.1 e' verificato come sender Kuma sul nuovo host. Usa cinque monitor: Fedora Host (ID 39), Storage (40), Network (41), Services (42) e Software (43). Tutti gli endpoint hanno accettato heartbeat reali. Host resta correttamente rosso per swap warning circa 39%; Storage resta correttamente rosso per Seagate al 5,2273% libero, ancora sotto recovery. Network, Services e Software sono verdi. L'unsafe removal stale e' stata chiusa automaticamente; il readback Kuma remoto via SQLite e' riuscito.

Gli endpoint sono root-only e non compaiono nel repository o nei log. L'istanza Kuma esistente usa ancora HTTP: il funzionamento e' verificato, ma HTTPS resta necessario per la confidenzialita' del trasporto.

Sono attivi i segnali locali Fedora ABRT per crash/oops, `smartd` per salute storage e `systemd-oomd` per pressione memoria. Questi servizi non sostituiscono il monitoraggio applicativo.

## Regole

Non stampare o committare token, chat ID o push URL. Prima di dichiarare un alert attivo verificare sender, timer, consegna e destinazione; gli alert sono segnali e non autorizzano remediation automatica.
