# Network Topology

Topologia di rete leggibile derivata da [NETWORK_TOPOLOGY AI](../../ai/global/NETWORK_TOPOLOGY.md). La fonte operativa e' il file AI; questo documento non va usato come sorgente per Codex.

## Host corrente Windows

- Host corrente: ThinkPad P14s Gen 5 AMD.
- OS: Windows 11 Pro.
- Hostname, interfaccia principale, IP LAN, gateway, Wi-Fi, Tailscale e IP attuali dei telefoni sono `UNKNOWN`.
- Non assumere per il ThinkPad l'IP LAN, Tailscale o gli IP ADB storici del Surface.

## Host locale legacy

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
- Kuma admin: solo tunnel SSH verso `127.0.0.1:3002`, poi browser locale `http://127.0.0.1:3001`.
- Kuma pubblico: `http://150.230.148.128:3001` e' solo proxy `/api/push/...`; root/dashboard pubbliche devono rispondere `403`.
- SSH live: `UNKNOWN`, timeout durante questa discovery.

Vista sintetica:

- ThinkPad: workstation principale corrente, LAN e Tailscale `UNKNOWN`.
- Surface: workstation legacy, LAN `192.168.1.97`, Tailscale `100.68.141.10`.
- Oracle VM: Kuma e backup remoti.
- Kuma: alerting/storico/visualizzazione, non remediation.
- Pixel 8a e TCL 6102H: target ADB Wi-Fi, da verificare live prima dell'uso.

## Vincoli

- Kuma e' storico, alerting e visualizzazione: un DOWN e' un segnale, non una prova conclusiva.
- Per ADB Wi-Fi usare una verifica live del device/plugin; `adb devices -l` o equivalente del workflow Windows, mDNS/Avahi non basta.
- Non stampare URL push Kuma o token.
