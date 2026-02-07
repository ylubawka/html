import http.server
import socketserver
import webbrowser

PORT = 8000

# Этот код просто запускает твой HTML файл в браузере как сайт
Handler = http.server.SimpleHTTPRequestHandler

print(f"Пранк запущен на порту {PORT}")
webbrowser.open(f"http://localhost:{PORT}/index.html")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
