"""Serve the exams locally and open the browser:  python serve.py"""
import http.server, socketserver, webbrowser, os
PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as s:
    url = f"http://127.0.0.1:{PORT}/index.html"
    print("Serving", url, "(Ctrl+C to stop)")
    webbrowser.open(url)
    s.serve_forever()
