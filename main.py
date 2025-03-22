from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', '2')
        self.end_headers()

        self.wfile.write(b'OK')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        data = self.rfile.read().decode()
        print(f'Received: {data}')

server = HTTPServer(('localhost', PORT), RequestHandler)

try:
    print("Server started on port " + str(PORT))
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print("Server stopped.")