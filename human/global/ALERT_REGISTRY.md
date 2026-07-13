# Alert Registry

Aggiornato: 2026-07-13. Autorita' operativa: [ALERT_REGISTRY AI](../../ai/global/ALERT_REGISTRY.md).

## Fedora corrente

Fedora System Monitor 1.1.0 e' verificato come sender Kuma sul nuovo host. Usa cinque monitor: Fedora Host (ID 39), Storage (40), Network (41), Services (42) e Software (43). Tutti gli endpoint hanno accettato heartbeat reali. Host, Network, Services e Software sono sani; Storage resta correttamente rosso per Seagate al 3,6754% libero e unsafe removal senza recovery. Le correzioni 471852 coprono recovery, identità Wi-Fi, filesystem, replay, I/O e race DNF senza modificare timeout o frequenze. Il readback amministrativo Kuma è pendente perché il JWT Chrome è stato rifiutato.

Gli endpoint sono root-only e non compaiono nel repository o nei log. L'istanza Kuma esistente usa ancora HTTP: il funzionamento e' verificato, ma HTTPS resta necessario per la confidenzialita' del trasporto.

Sono attivi i segnali locali Fedora ABRT per crash/oops, `smartd` per salute storage e `systemd-oomd` per pressione memoria. Questi servizi non sostituiscono il monitoraggio applicativo.

## Regole

Non stampare o committare token, chat ID o push URL. Prima di dichiarare un alert attivo verificare sender, timer, consegna e destinazione; gli alert sono segnali e non autorizzano remediation automatica.
