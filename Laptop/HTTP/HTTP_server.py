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
sys.path.append(home+'/SCR/Laptop')
import GUI_support
sys.path.append(home+'/SCR/Laptop/BT/Clock')
import Temp

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
	MyData=post_data.split("=").replace('+',' ')
	print(MyData[1]) 
	if(MyData[1]!=''):
	    GUI_support.DataRec.set(MyData[1])
	    if(MyData[1]=='in'):
	        GUI_support.SendUp(str(Temp.read('i')),'4')
   	    if(MyData[1]=='out'):
		GUI_support.SendUp(str(Temp.read('o')),'4')
        
def run(server_class=HTTPServer, handler_class=S, port=5906):
    server_address = ('192.168.0.201', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

