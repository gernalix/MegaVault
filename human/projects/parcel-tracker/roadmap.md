# parcel-tracker Roadmap

## Segnali dal codice
- parcel_tracker.py:2:from __future__ import annotations
- parcel_tracker.py:137:next_data = re.search(r"<script[^>]+id=[\"']__NEXT_DATA__[\"'][^>]*>(.*?)</script>", page, re.I / re.S)
- parcel_tracker.py:138:if next_data:
- parcel_tracker.py:139:scripts.append(next_data.group(1))
- parcel_tracker.py:155:status = clean_text(next((x for x in text_fields if clean_text(x)), ""))

## Debito/rischi da considerare
- parcel_tracker.py:14:import urllib.error
- parcel_tracker.py:76:error TEXT
- parcel_tracker.py:98:def fetch_url(url: str, timeout: int = 30) -> str:
- parcel_tracker.py:107:with urllib.request.urlopen(req, timeout=timeout) as resp:
- parcel_tracker.py:109:return resp.read().decode(charset, errors="replace")
- parcel_tracker.py:145:except json.JSONDecodeError:
- parcel_tracker.py:192:digest = hashlib.sha256(page.encode("utf-8", errors="replace")).hexdigest()
- parcel_tracker.py:201:raise RuntimeError(f"Telegram helper missing: {TELEGRAM_HELPER}")
