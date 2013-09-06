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

names=[]
values=[]
for i in form.list:
    names.append(i.name)
    values.append(i.value)
dictionary = dict(zip(names, values))

htmlData = HTTPHandler.processRequest(os.environ.get('PATH_INFO', ''), dictionary)

print "Content-type: " + htmlData[1]
print
print htmlData[0]