#! C:/Python27/python.exe
# -*- coding: utf-8 -*-
import datetime
import qrcode

print "Content-type: text/html"
print

t=datetime.datetime.now()
s= 'Právě je '+ str(t.hour)+' hodin, '+ str(t.minute)+' minut a '+ str(t.second)+' vteřin'

qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=9,border=5)
qr.add_data(s)
qr.make(fit=True)
img = qr.make_image()

#image_file = open("qr.png",'w+')
img.save("C:\Program Files\Apache Software Foundation\Apache2.2\www\qr.png")
#image_file.close()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Pokusna stranka</title>
        <meta charset="UTF-8">
        
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">
        </script>

        <script> 
            $(document).ready(function(){
            $("#lista").hover(function(){
            $("#panel1").slideToggle("slow");
          });
});
$(document).ready(function(){
  $("#lista").hover(function(){
    $("#qr").slideToggle("slow");
  });
});
</script>
        
        <style type="text/css">
            body
            {
                background-color:#b0c4de;
            }
            #qr
            {
                width: 1000px ;
                margin-left: auto ;
                margin-right: auto ;
                display:none;
            }
            #lista
            {
                width: 450px ;
                margin-left: auto ;
                margin-right: auto ;
            }
            #qr-odkaz
            {
                float:left;
            }
            #qr-python
            {
                float:right;
            }
            p
            {
                text-align: center;
                color:red;
                font-size:20pt;
                font-style: italic;
            }
            @media (max-width: 1000px)
            {
                #qr
                {
                    width: 400px ;
                }
                #qr-odkaz
                {
                    float: none;
                }
                #qr-python
                {
                    float: none;
                }
            }
            @media (max-width: 350px)
            {
                img
                {
                    max-width: 75%;
                    height: auto;
                }
            }
        </style>
    </head>
    <body>
        <br />
        <div id="lista">
            <p>"""+s+"""</p>
        </div>
        <div id="qr">
            <div id="qr-odkaz">
                <img src="http://chart.apis.google.com/chart?cht=qr&chs=350x350&chld=L&choe=UTF-8&chl="""+s+"""" alt="qr kod vygenerovany generatorem http://zxing.appspot.com/generator" />
            </div>
            <div id="qr-python">
                <img src="qr.png" alt="qr kod vygenerovany v pythonu">
            </div>
        </div>
    </body>
</html>"""

print html
