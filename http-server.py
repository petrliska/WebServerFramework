#-------------------------------------------------------------------------------
# Name:        http-server
# Purpose:
#
# Author:      Liska_P
#
# Created:     08.08.2013
# Copyright:   (c) Liska_P 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!C:/Python27/python.exe

import os
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

#import os
#import BaseHTTPServer, CGIHTTPServer

serverAddr = ("", 8080)

os.chdir("C:\Program Files\Apache Software Foundation\Apache2.2\www")

serv = BaseHTTPServer.HTTPServer(serverAddr, CGIHTTPServer.CGIHTTPRequestHandler)

serv.serve_forever()