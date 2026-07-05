# Topologia rete globale

Aggiornato: 2026-07-05. Autorita' operativa: [NETWORK_TOPOLOGY AI](../../ai/global/NETWORK_TOPOLOGY.md).

## Host corrente

- Host primario: `DANIELE_PC`, Windows 11 Pro su ThinkPad P14s Gen 5 AMD.
- IP LAN/Tailscale correnti: non verificati in questo passaggio.
- Non usare il vecchio IP Surface `192.168.1.97` come stato corrente senza `ipconfig`/verifica live.

## Oracle VM/Kuma

- Nodo remoto: `ubuntu@150.230.148.128`.
- Ruoli: Uptime Kuma, backup Oracle, monitoraggio remoto.
- DB Kuma: `/opt/uptime-kuma/data/kuma.db` sul runtime remoto Linux.
- Path chiave SSH Windows: unknown; vecchio path Linux solo storico.

## Android

- ADB Windows: `C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe`.
- Pixel 8a/TCL: indirizzi correnti unknown; verificare con `adb devices -l`.

## Storico

Surface/Linux Mint, Tailscale `100.68.141.10`, servizi push Mint e monitor Kuma Mint sono snapshot storici o specifici di progetto.
