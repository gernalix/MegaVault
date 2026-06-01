# facebook-video-archiver Roadmap

## Segnali dal codice
- no tests detected by static scan

## Debito/rischi da considerare
- facebook_archive_dashboard.py:38:except OSError:
- facebook_archive_dashboard.py:47:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
- facebook_archive_dashboard.py:62:lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
- facebook_archive_dashboard.py:69:except subprocess.CalledProcessError:
- facebook_archive_dashboard.py:89:except OSError:
- facebook_archive_dashboard.py:96:except OSError:
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
- facebook_archive_dashboard.py:162:"ultimi warning/errori:",
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
- facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
- facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
- facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
