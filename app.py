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

    <a href="sessions"> <u>sessions</u> <a>
    </center>

    </body>
    </html>
    """.format(COLOR, my_uuid,)

@app.route('/agenda')
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


@app.route('/sessions')
def sessions():
    start_page = "<html><head>\"Sessions\"</head><br><body>"
    end_page = "</body></html>"
    mid_page = ""
    with open("sessions.txt", 'r') as f:
        lines = csv.reader(f)
        for row in lines:
            mid_page = mid_page + "  " + str(row[1]) + "  " + str(row[2]) +"  "+ str(row[3])+ "  " + str(row[4])+ "<br>"
    f.close()
    mid_page =mid_page + "<a href=\"/\"> <u>Return</u> <a> </center>"
    return start_page + mid_page + end_page


if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
