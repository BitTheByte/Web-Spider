import SimpleHTTPServer
import SocketServer
import time
import sys
PORT = int(sys.argv[1])

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()

def do_GET(self):
	post_body = self.rfile.read(content_len)
	print(post_body)



timeout = 30
_timeout = 0
while True:
	time.sleep(1)
	do_GET()
	_timeout += 1
	if _timeout == timeout:
		exit();