#!/usr/bin/env python3
"""Local preview server for docs/.

Identical to `python3 -m http.server` except that it tells the browser never to
cache anything. Plain http.server sends no Cache-Control, so Chrome guesses a
freshness window and will happily keep serving an old styles.css for a whole
review session — which looks exactly like "the change didn't work".

    python3 serve.py            # http://localhost:8000
    python3 serve.py 8001       # other port
"""
import functools
import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoCacheHandler, directory=ROOT)
    with http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler) as httpd:
        print(f"Serving {ROOT} on http://0.0.0.0:{PORT}  (no-cache)")
        httpd.serve_forever()
