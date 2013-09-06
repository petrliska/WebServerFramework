#!C:/Python27/python.exe
# -*- coding: utf-8 -*-

import web
import WebHandler

render = web.template.render('templates/')

urls = (
    '/favicon.ico', 'favicon',
##    '/post/.*', 'post_params',
    '/(.*)', 'handler')

##app = web.application(urls, globals())

##web.config.debug=False

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('192.168.1.130', port))

class favicon:
    def GET(self):
        pass

class handler:
    def GET(self, page):
        vstup = web.input(_unicode=False)
        web.header("Content-Type", 'text/html') # Set the Header
        s=WebHandler.ProcessRequest(page, vstup)

        return s

    def POST(self, page):
        vstup = web.input(_unicode=False)
        web.header("Content-Type", 'text/html') # Set the Header
        s=WebHandler.ProcessRequest(page, vstup)

        return s

##class post_params:
##    def GET(self):
##        s=params()
##        return s
##        s = web.ctx.query
##        l = s[1:].split('&')
##        seznam = []
##        for item in l:
##            key, val = item.split('=')
##            seznam.append(key+' '+val)
##        j = '\n'.join(seznam)
##        return j
##        return render.index(i.jmeno)
##    def POST(self):
##        s=WebHandler.params()
##        return s


if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8080)