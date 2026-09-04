# cs1101s-hud

Live countdown / announcement HUD for CS1101S assessments, served via GitHub Pages
at https://cs1101s.github.io/cs1101s-hud/

Shows a start/end time, a live clock, a countdown timer, live clarifications
(polled from `clarifications.md`), and an optional password reveal near the
end of the assessment (from `password.json`).

## Using it for an assessment

1. Edit **clarifications.md** with the real instructions for this assessment
   (it currently holds a generic placeholder).
2. If you want a password revealed near the end, set it in **password.json**:
   ```json
   {
     "password": "",
     "showWhenRemainingMinutes": 15
   }
   ```
   Leave `"password"` blank to keep the reveal disabled.
3. Commit and push — GitHub Pages picks up changes automatically.
4. Share the link with a `title`, `start` time (24hr, e.g. `1300`), and
   `duration` (minutes) query string, e.g.:
   ```
   https://cs1101s.github.io/cs1101s-hud/?title=Midterm&start=1300&duration=100
   ```
   `title` defaults to "CS1101S Assessment" if omitted.

You can also update `clarifications.md` and `password.json` mid-assessment
(and push) — the page polls both files every 10 seconds, no reload needed.

## Local preview

`index.html` fetches `clarifications.md` and `password.json` at runtime, which
doesn't work over `file://` (CORS). Use the bundled server instead:

```bash
./serve.py        # serves at http://127.0.0.1:8811/ and opens your browser
./serve.py 8000    # or pick a different port
```

Test query params locally too, e.g.
`http://127.0.0.1:8811/?title=Midterm&start=1300&duration=5`.
