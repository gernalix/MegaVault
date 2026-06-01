# system_watchdog Roadmap

## Segnali dal codice
- no tests detected by static scan

## Debito/rischi da considerare
- systemd/system-watchdog.service:15:Environment=WATCHDOG_TIMEOUT=20
- systemd/system-watchdog.service:21:StandardError=journal
- watchdog.py:9:import urllib.error
- watchdog.py:38:except OSError:
- watchdog.py:50:except (ValueError, IndexError):
- watchdog.py:67:error TEXT,
- watchdog.py:100:except ValueError:
- watchdog.py:140:except OSError:
- install.sh:10:sudo install -m 0644 "$SERVICE_SRC" "$SERVICE_DST"
- install.sh:11:sudo systemctl daemon-reload
- install.sh:12:sudo systemctl enable --now system-watchdog.service
- install.sh:13:sudo systemctl --no-pager --full status system-watchdog.service // true
- uninstall.sh:4:sudo systemctl disable --now system-watchdog.service // true
- uninstall.sh:5:sudo rm -f /etc/systemd/system/system-watchdog.service
