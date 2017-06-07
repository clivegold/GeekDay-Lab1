import os
import uuid
import csv
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#777799"
GREEN = "#99CC99"

COLOR = GREEN


@app.route('/')
def mainmenu():

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>

    <a href="agenda"> <u>Agenda</u> <a>
    </center>

    <a href="agenda_over"> <u>Agenda_over</u> <a>
    </center>

    <a href="map"> <u>Map</u> <a>
    </center>

    <a href="sessions"> <u>sessions</u> <a>
    </center>

    </body>
    </html>
    """.format(COLOR,my_uuid,)

@app.route('agenda')
def agenda():
    return """
    <HTML>
<title>Agenda</title>
<header>This is My Agenda</header>

<body>

<b>This is the schedule for today</b>
<table border=2 cellspacing=10 cellpadding=10
<tr>
	<td> This is cell 1
	<td> This is cell 2
<tr>
	<td> This is cell 3
	<td> This is cell 4
</table>

<a href="/"> <u>Return</u> <a>
</center>
</body>

""".format(COLOR)

@app.route('/map')
def map():
    return """
    <HTML>
<title>Agenda</title>
<header>This is My Agenda</header>

<body>

<a href="/"> <u>Return</u> <a>
</center>
</body>

""".format(COLOR)

@app.route('sessions')
def sessions(file_name):
    with open(file_name, 'r') as f:
        lines =csv.reader(f)
##        for row in lines:
##            print "session ", row[1],"time ", row[2],"presenter ",row[3],"title ",row[4]
    return """
    <HTML>
    <body>
     <center><h1><font color="white">Sessions:<br/>
        {}</br> 
    <a href="/"> <u>Return</u> <a>
    </center>
    </body>
    </html>
""".format(lines, COLOR)


@app.route("/agenda_over")
def agenda_over():
    return """
<html>
<head>
    <style type="text/css">
    .OverLay { position: absolute; z-index: 3; opacity: 0.5; filter: alpha(opacity = 50); top: 0; bottom: 0; left: 0; right: 0; width: 100%; height: 100%; background-color: Black; color: White;}
    body { height: 100%; }
    html { height: 100%; }
    </style>
</head>

<body>
    <div style="height: 100%; width: 100%; position: relative;">
        <div style="height: 100px; width: 300px; background-color: Red;">
        </div>
        <div style="height: 230px; width: 9000px; background-color: Green;">
        </div>
        <div style="height: 900px; width: 200px; background-color: Blue;"></div>
        <div class="OverLay">TestTest!</div>
    </div>


    </body>
</html> 
""".format()

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
