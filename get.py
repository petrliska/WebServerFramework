#! c:/Python27/python
# -*- coding: utf-8 -*-

import cgi
import cgitb

print "Content-type: text/html"
print

form = cgi.FieldStorage()
jmeno = form.getvalue('jmeno')
prijmeni = form.getvalue('prijmeni')
mesto = form.getvalue('mesto')


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Pokusna stranka</title>
        <meta charset="UTF-8">

        <style>
            table
            {
                margin-left: auto;
                margin-right: auto;
                border-spacing: 0px;
            }
            td, th
            {
                border: 1px solid blue;
            }
        </style>
        
    </head>
    <body>
        <table>
            <tr><th>Jméno</th><th>Příjmení</th><th>Město</td></th>
            <tr><td>"""+jmeno+"</td><td>"+prijmeni+"</td><td>"+mesto+"""</td></tr>
        </table>
    </body>
</html>"""

print html
