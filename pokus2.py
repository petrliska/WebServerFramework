#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Liska_P
#
# Created:     15.08.2013
# Copyright:   (c) Liska_P 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#! C:/Python27/python.exe
# -*- coding: utf-8 -*-
import datetime
import qrcode
import HTTPHandler
import cgi
import cgitb
cgitb.enable()
import os

form = cgi.FieldStorage()
for i in form.keys():
            s = s + form[i].value + "\n"

##htmlData = HTTPHandler.processRequest(os.environ.get('PATH_INFO', ''), cgi.FieldStorage())

print "Content-type: text/html"
print
html = """
<html>
<head><title>titulek</title></head>
<body>""" + s + """
</body>
</html>
"""