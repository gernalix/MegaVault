# Alert Registry

Aggiornato: 2026-07-09. Autorita' operativa: [ALERT_REGISTRY AI](../../ai/global/ALERT_REGISTRY.md).

## Fedora corrente

Nessun servizio o timer di alert specifico dei progetti MegaVault, nessun sender Kuma e nessuna sorgente Telegram risultano verificati sul nuovo host.

Sono attivi i segnali locali Fedora ABRT per crash/oops, `smartd` per salute storage e `systemd-oomd` per pressione memoria. Questi servizi non sostituiscono il monitoraggio applicativo.

## Regole

Non stampare o committare token, chat ID o push URL. Prima di dichiarare un alert attivo verificare sender, timer, consegna e destinazione; gli alert sono segnali e non autorizzano remediation automatica.
