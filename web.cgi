#! C:/Python27/python.exe
# -*- coding: utf-8 -*-

import web
import os
import WebHandler
import cgi
import cgitb
cgitb.enable()

##vstup = web.input()
##path = web.ctx.homepath

form = cgi.FieldStorage()

names=[]
values=[]
for i in form.list:
    names.append(i.name)
    values.append(i.value)
dictionary = dict(zip(names, values))

htmlData = WebHandler.ProcessRequest(os.environ.get('PATH_INFO', '')[1:], dictionary)

##htmlData = WebHandler.ProcessRequest(path, None)

print "Content-Type: text/html"
print

print htmlData