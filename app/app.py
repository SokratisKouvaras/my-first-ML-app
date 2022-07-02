from flask import Flask,render_template
from static import *
app = Flask(__name__, template_folder="templates",static_folder="static")
app.debug = False

@app.route('/')
@app.route('/home')
@app.route('/index')
def home(name=None):
    return render_template('index.html', name=name)

@app.route('/model1')
def model1(name=None):
    return render_template('model1.html', name=name)

@app.route('/model2')
def model2(name=None):
    return render_template('model2.html', name=name)