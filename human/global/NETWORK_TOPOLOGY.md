# Network Topology

Topologia di rete verificata dal vivo il 2026-06-08 e integrata con `HOST_PROFILE`. Il file AI autorevole e' [NETWORK_TOPOLOGY.md](../../ai/global/NETWORK_TOPOLOGY.md).

## Host locale

- Host: `daniele-Surface-Pro`.
- Interfaccia principale: `wlp1s0`, IP `192.168.1.97/24`, gateway `192.168.1.1`.
- Wi-Fi: `Alaska_5G`, 5.22 GHz, bitrate rilevato `468 Mb/s`, power management off.
- Tailscale: `tailscale0`, IP `100.68.141.10/32`.

## Endpoint locali

- Dashboard servizi: `http://127.0.0.1:8788`.
- Dashboard backup cloud: `http://127.0.0.1:8765`.

## Nodo remoto

- Oracle VM: `ubuntu@150.230.148.128`.
- Ruoli documentati: Uptime Kuma, backup Oracle e monitor remoti.
- Kuma: `http://150.230.148.128:3001`.
- SSH live: `UNKNOWN`, timeout durante questa discovery.

## Vincoli

- Kuma e' storico, alerting e visualizzazione: un DOWN e' un segnale, non una prova conclusiva.
- Per ADB Wi-Fi usare `adb devices -l`; mDNS/Avahi non basta.
- Non stampare URL push Kuma o token.
