import sys

import http.server
import socketserver
import importlib


def load_modules(module_name):
    if module_name in sys.modules:
        mod = importlib.reload(sys.modules[module_name])
    else:
        mod = importlib.import_module(module_name)
    return mod.html


def get_content(module_name='def_list'):
    mod_name = f"markdown_extensions_examples.{module_name}"
    ctt = load_modules(mod_name)
    content = ctt.encode('utf-8')
    return content


def home():
    examples = [
        "abbr",
        "extra",
        "attr_list",
        "def_list",
        "fenced_code",
        "footnotes",
        "md_in_html",
        "tables",
        "admonition",
        "codehilite",
        "legacy_attrs",
        "legacy_em",
        "meta",
        "nl2br",
        "sane_lists",
        "smarty",
        "toc",
        "wikilinks",
    ]
    content = f"""
    <html>
    <head>
    <title>Markdown 扩展示例</title>
    </head>
    <body>
    <h1>Markdown 扩展示例</h1>
    <ul>
    {''.join(f"<li><a href='/{example}'>{example}</a></li>" for example in examples)}
    </ul>
    </body>
    </html>
    """
    return content.encode('utf-8')


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(home())
        elif self.path == '/favicon.ico':
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'')  # 空响应体
        else:
            print(self.path[1:])
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(get_content(self.path[1:]))


try:
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
