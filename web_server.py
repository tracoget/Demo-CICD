from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Set the response content
        response_content = b"Hello, World!"

        # Send the response content
        self.wfile.write(response_content)

# Create an HTTP server with the request handler
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print('Server running on port 8000...')
httpd.serve_forever()