from flask import Flask, render_template, request, current_app as app
from sense_hat import SenseHat
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/petpeeve', methods=['GET', 'POST']) 
def petpeeve():
    if request.method == "POST":
        message = request.form.get("message")
        sense.show_message(message)
    return render_template('index.html', message = message)

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')