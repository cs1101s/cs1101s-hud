#!/usr/bin/env python3
"""Local preview server for cs1101s-hud (avoids file:// CORS issues with fetch()).

Usage:
    ./serve.py [port]

Then open http://127.0.0.1:<port>/ (append e.g. ?title=Midterm&start=1300&duration=5).
"""
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8811

handler = http.server.SimpleHTTPRequestHandler
handler.directory = str(Path(__file__).parent)


class QuietHandler(handler):
    def log_message(self, format, *args):
        pass


def main():
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/"
        print(f"Serving cs1101s-hud at {url}  (Ctrl+C to stop)")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
