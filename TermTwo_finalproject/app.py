from flask import Flask, render_template, current_app as app
from sense_hat import SenseHat
from time import sleep

app = Flask(__name__)
sense = SenseHat()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        sense.show_message(message)
    return render_template('index.html')


app = Flask('__name__'
    app.run(debug=True, host='0.0.0.0')