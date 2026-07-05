# Grindr Web Exporter

Tool locale per esportare chat visibili da Grindr Web usando Firefox, Playwright e SQLite.

Stato: MVP creato. I test sintetici passano, ma il profilo Firefox predefinito non contiene cookie Grindr, quindi non e' stato possibile validare `export-one` su una chat reale. Prossimo passo: login con `grindr-export --profile-mode persistent-copy --pause-for-login setup-check`, poi `export-one`.
