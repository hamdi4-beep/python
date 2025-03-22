from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', '2')
        self.end_headers()

        self.wfile.write(b'OK')

server = HTTPServer(('localhost', PORT), RequestHandler)

try:
    print("Server started on port " + str(PORT))
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print("Server stopped.")