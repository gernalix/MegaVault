# Topologia rete globale

Aggiornato: 2026-07-14. Autorita' operativa: [NETWORK_TOPOLOGY AI](../../ai/global/NETWORK_TOPOLOGY.md).

## Fedora corrente

- Host `fedora`, Fedora Linux 44 Workstation sul ThinkPad P14s Gen 5 AMD.
- Wi-Fi `wlp2s0` attivo con IPv4 `192.168.1.231/24`; gateway predefinito `192.168.1.1`.
- Ethernet `enp1s0f0` down; Tailscale non rilevato nel PATH.
- Loopback `127.0.0.1`.

Fedora System Monitor invia esclusivamente heartbeat e stati sintetici all'istanza Uptime Kuma esistente su `150.230.148.128:3001`, senza modifiche firewall. Gli endpoint sono root-only e i messaggi non contengono dati sensibili. Il readback operativo e' stato verificato via SQLite remoto sulla VM Oracle. Il collegamento attuale e' HTTP e va migrato a HTTPS per proteggere il trasporto.

## Android

ADB usa `/home/daniele/Android/Sdk/platform-tools/adb`. Il server utente condiviso ascolta solo su `127.0.0.1:5037`; `adb-device-keeper.service` e' abilitato e attivo e gestisce Pixel 8a e TCL 6102H senza dipendere da Android Studio.

Il Pixel Android 17 pubblica regolarmente il servizio mDNS dinamico. Il TCL Android 12 non lo ha pubblicato durante le verifiche, quindi il servizio conserva anche l'ultimo endpoint con identita' verificata. Vedere [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

Gli indirizzi di rete cambiano: verificarli live prima dell'uso. Nomi mDNS e IP in cache non provano che un device Android sia raggiungibile.
