from http.server import BaseHTTPRequestHandler, HTTPServer

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

try:
    httpd = HTTPServer(('', 3000), Request)
    httpd.serve_forever()
except Exception as e:
    print('Something went wrong!', e)