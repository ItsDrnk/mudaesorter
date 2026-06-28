#!/usr/bin/env python3
"""Simple CORS proxy for mudae.net — run with: python mudae_proxy.py"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request

class ProxyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def do_GET(self):
        # Strip leading slash to get the target URL
        target = self.path.lstrip('/')
        if not target.startswith('http'):
            self.send_error(400, 'Pass a full URL as the path')
            return
        try:
            req = urllib.request.Request(target, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
            self.send_response(200)
            self.send_header('Content-Type', resp.headers.get('Content-Type', 'text/html'))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_error(502, str(e))

    def log_message(self, fmt, *args):
        print(f"[proxy] {fmt % args}")

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), ProxyHandler)
    print("Mudae proxy running at http://localhost:8000")
    print("Usage: fetch('http://localhost:8000/https://mudae.net/character/...')")
    print("Press Ctrl+C to stop.")
    server.serve_forever()
