from flask import Flask, request, render_template, current_app as app  
from sense_hat import SenseHat  
from time import sleep
from flask_apscheduler import APScheduler
import sqlite3

sense = SenseHat

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('add', methods=['POST'])
def add():
    task = request.form['task']
    deadline = request.form['deadline']
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks (task, date) VALUES((?), (?), (?))", (task, deadline))
    conn.commit()
    conn.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



