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

import os

#!C:/Python27/python.exe
def processRequest(path, params):
    if path in ["/", ""]:
        path = "/index_example3.html"

        #Check the file extension required and
        #set the right mime type

    sendReply = False
    if path.endswith(".html"):
        mimetype='text/html'
        sendReply = True
    if path.endswith(".jpg"):
        mimetype='image/jpg'
        sendReply = True
    if path.endswith(".gif"):
        mimetype='image/gif'
        sendReply = True
    if path.endswith(".js"):
        mimetype='application/javascript'
        sendReply = True
    if path.endswith(".css"):
        mimetype='text/css'
        sendReply = True
    if path.endswith(".txt"):           #slouzi k testovani prace s parametry
        errorMsg = "Unsupported extension for path " + "bla"
        for i in params.values():
            errorMsg = errorMsg + "<br>" + i

    else:
        errorMsg = "Unsupported extension for path " + path

    if sendReply == True:
        f = open(os.curdir + os.sep + path)
        s = f.read()
        f.close()

        return (s, mimetype)
    else:
        return (errorMsg, "text/html")

import cgi