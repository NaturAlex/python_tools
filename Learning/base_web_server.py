''' 
    python base_web_server.py
    #去除socketserver写法
'''
import http.server
import socketserver

class MyHttpServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('success'.encode())

def main():
    host = "localhost"
    port = 8080
    # with socketserver.TCPServer((host, port), MyHttpServer) as httpd:
        # httpd.serve_forever()
    base_info = (host, port)
    httpd = http.server.HTTPServer(base_info, MyHttpServer)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
    