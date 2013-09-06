#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Liska_P
#
# Created:     05.09.2013
# Copyright:   (c) Liska_P 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#! C:/Python27/python.exe
# -*- coding: utf-8 -*-

# radeckova modifikace
def ahoj():
    pass
# end of radeckova modifikace

import web

def params(vstup):
    s=''
    for key, val in vstup.iteritems():
        s=s+key+' '+val+'\n'
    return s


def ProcessRequest(page, inpt):
    if page in ["/", ""]:
            page = "index.html"
    if inpt:
        p = params(inpt)
        if p:
            return p
    f = open(page)
    s = f.read()
    f.close()
    return s
