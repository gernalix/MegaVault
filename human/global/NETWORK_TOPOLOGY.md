# Topologia rete globale

Aggiornato: 2026-07-09. Autorita' operativa: [NETWORK_TOPOLOGY AI](../../ai/global/NETWORK_TOPOLOGY.md).

## Fedora corrente

- Host `fedora`, Fedora Linux 44 Workstation sul ThinkPad P14s Gen 5 AMD.
- Wi-Fi `wlp2s0` attivo con IPv4 `192.168.1.231/24`; gateway predefinito `192.168.1.1`.
- Ethernet `enp1s0f0` down; Tailscale non rilevato nel PATH.
- Loopback `127.0.0.1`.

## Android

ADB usa `/home/daniele/Android/Sdk/platform-tools/adb`. Il daemon e' stato avviato, ma `adb devices -l` non mostra device connessi.

Gli indirizzi di rete cambiano: verificarli live prima dell'uso. Nomi mDNS e IP in cache non provano che un device Android sia raggiungibile.
