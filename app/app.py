from flask import Flask,Response,render_template,request
from static import *
import os
app = Flask(__name__, template_folder="templates",static_folder="static")
app.debug = False

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def home(name=None):
    return render_template('index.html', name=name)

@app.route('/model1', methods=['GET'])
def model1(name=None):
    return render_template('model1.html', name=name)


@app.route('/model2', methods=['GET','POST'])
def model2(name=None):
    return render_template('model2.html', name=name)

@app.route('/test', methods=['GET'])
def test(name=None):
    return render_template('test.html', name=name)

@app.route("/test/download", methods=['POST'])
def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})

@app.route('/test', methods=['POST'])
def uploadmodel1():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        filepath = os.path.join('static/files',uploaded_file.filename)
        uploaded_file.save(filepath)
        print('FILE SAVED')
        return()