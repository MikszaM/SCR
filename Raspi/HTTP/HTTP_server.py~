#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append(home+'/SCR/Raspi')
import GUI_support
sys.path.append(home+'/SCR/Raspi/RF')
import RF_client

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length) 
        self._set_headers()
	MyData=post_data.split("=")
	print(MyData[1])
	data = MyData[1] 
	if(str(data)!=''):
	    GUI_support.DataRec.set(data)
	    RF_client.execute(data,'4')
            print >>sys.stderr, 'received "%s"' % data
        
def run(server_class=HTTPServer, handler_class=S, port=5906):
    server_address = ('192.168.0.200', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
