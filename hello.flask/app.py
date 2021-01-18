 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hiii')
def about():
    return 'hiii'

if __name__ == '__main__':
    app.run(debug=True,  host='127.0.0.1')


