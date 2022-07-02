from flask import Flask,render_template
from static import *
app = Flask(__name__, template_folder="templates",static_folder="static")
app.debug = False

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello(name=None):
    return render_template('index.html', name=name)