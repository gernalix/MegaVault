# Troubleshooting

```bash
mint-freeze-forensics status
mint-freeze-forensics human-report
journalctl --user -u mint-freeze-forensics.service -n 100 --no-pager
find ~/.local/state/mint-freeze-forensics -maxdepth 3 -type f -printf '%p %s bytes\n'
```

Note:

- `journal.txt` vuoto in un event folder significa che non c'erano righe journal nella finestra del gap.
- I test manuali `stop/restart/simulate-gap` possono creare eventi gap intenzionali.
- `~/.config/mint-freeze-forensics/kuma.env` contiene URL push e non va committato.
