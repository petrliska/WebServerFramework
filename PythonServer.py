#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Liska_P
#
# Created:     13.08.2013
# Copyright:   (c) Liska_P 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!C:/Python27/python.exe
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import cgi
import HTTPHandler
import logging
import SocketServer
import SimpleHTTPServer
import sys
import urlparse

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
##        if os.environ.get('REQUEST_METHOD','').lower()=='get' :
##        form = os.environ.get('QUERY_STRING', '')
##        if os.environ['QUERY_STRING']:
##            form = cgi.FieldStorage()
##        else:
##            form = None
##        cgi.print_environ()
##        fp=self.rfile
##        headers=self.headers
##        env = environ.get('REQUEST_METHOD':'GET','QUERY_STRING', None)
##        'CONTENT_TYPE':self.headers['Content-Type'],}
##        form = cgi.FieldStorage(fp,headers,env)
##        form = cgi.FieldStorage()                   #ani jedna verze nefunguje
##        s = HTTPHandler.processRequest(self.path, form)

        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed_path.query)    #nacteni parametru do dictionary
        try:
            params = dict([p.split('=') for p in parsed_path[4].split('&')])
        except:
            params = {}

        s = HTTPHandler.processRequest(parsed_path[2], params)
        if (s[1] != None):
            try:
                #Open the static file requested and send it
                self.send_response(200)
                self.send_header('Content-type',s[1])
                self.end_headers()
                self.wfile.write(s[0])
                return
            except IOError:
                self.send_error(404,'File Not Found: %s' % self.path)


    #Handler for the POST requests
    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})

        names=[]
        values=[]
        for i in form.list:
            names.append(i.name)
            values.append(i.value)
        dictionary = dict(zip(names, values))   #prevod parametru do dictionary

        s = HTTPHandler.processRequest(self.path, dictionary)
        if (s[1] != None):
            try:
                self.send_response(200)
                self.send_header('Content-type',s[1])
                self.end_headers()
                self.wfile.write(s[0])
                return
            except IOError:
                self.send_error(404,'File Not Found: %s' % self.path)


try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()