# Topologia rete globale

Aggiornato: 2026-07-10. Autorita' operativa: [NETWORK_TOPOLOGY AI](../../ai/global/NETWORK_TOPOLOGY.md).

## Fedora corrente

- Host `fedora`, Fedora Linux 44 Workstation sul ThinkPad P14s Gen 5 AMD.
- Wi-Fi `wlp2s0` attivo con IPv4 `192.168.1.231/24`; gateway predefinito `192.168.1.1`.
- Ethernet `enp1s0f0` down; Tailscale non rilevato nel PATH.
- Loopback `127.0.0.1`.

## Android

ADB usa `/home/daniele/Android/Sdk/platform-tools/adb`. Il server utente condiviso ascolta solo su `127.0.0.1:5037`; `adb-device-keeper.service` e' abilitato e attivo e gestisce Pixel 8a e TCL 6102H senza dipendere da Android Studio.

Il Pixel Android 17 pubblica regolarmente il servizio mDNS dinamico. Il TCL Android 12 non lo ha pubblicato durante le verifiche, quindi il servizio conserva anche l'ultimo endpoint con identita' verificata. Vedere [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

Gli indirizzi di rete cambiano: verificarli live prima dell'uso. Nomi mDNS e IP in cache non provano che un device Android sia raggiungibile.
