# Troubleshooting

```bash
mint-freeze-forensics status
mint-freeze-forensics human-report
mint-freeze-forensics io-report
journalctl --user -u mint-freeze-forensics.service -n 100 --no-pager
find ~/.local/state/mint-freeze-forensics -maxdepth 3 -type f -printf '%p %s bytes\n'
```

Note:

- `journal.txt` vuoto in un event folder significa che non c'erano righe journal nella finestra del gap.
- `io-report` mostra `cumulative_io_mb` per i freeze storici prima della v1.2.0; i delta read/write veri arrivano solo dai sample raccolti dopo l'aggiornamento.
- `mint-freeze-forensics status` mostra `capture.active`; se resta `true` oltre 120s è un bug.
- La capture usa più campioni solo durante la finestra: non va trasformata in modalità permanente.
- Se il daemon era già in esecuzione prima dell'aggiornamento CLI, continuerà a scrivere vecchi sample finché non verrà riavviato manualmente.
- I test manuali `stop/restart/simulate-gap` possono creare eventi gap intenzionali.
- `~/.config/mint-freeze-forensics/kuma.env` contiene URL push e non va committato.
