from flask import Flask, request, render_template, current_app as app  
from sense_hat import SenseHat  
from time import sleep
import sqlite3

app = Flask(__name__)
sense = SenseHat()
messages = {}
sense.low_light = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sent', methods=['GET', 'POST'])
def success():
    if request.method == "POST":
        message = request.form.get("message")
        author = request.form.get("author")
        messages[author] = message
        sense.show_message(message)

        conn = sqlite3.connect("./static/data/messages.db")
        curs = conn.cursor()
        curs.execute("INSERT INTO messages VALUES((?),(?))", (author, message))
        conn.commit()
        conn.close()
        sense.show_message(message)                                             
    return render_template('sent.html', message = message, author = author)

@app.route('/messages')
def all_messages():
    conn = sqlite3.connect("./static/data/messages.db")
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * FROM messages")
    for row in rows:
        message = {'name':row[0], 'message':row[1]}
        messages.append(message)
    conn.close()
    return render_template('log.html', messages = messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
