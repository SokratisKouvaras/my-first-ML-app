from flask import Flask, Response, render_template, request, make_response, redirect, url_for
from static import *
import os
import pickle
import sklearn
import csv

app = Flask(__name__, template_folder="templates", static_folder="static")
app.debug = False

uploaded_file = []
model1 = pickle.load(open('ml_models/model.pickle', 'rb'))



@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/index", methods=["GET"])
def home(name=None):
    return render_template("index.html", name=name)


@app.route("/model1", methods=["GET"])
def model1(name=None):
    return render_template("model1.html", name=name)


@app.route("/model1/download", methods=["GET"])
def getPredictionsCSV():
    csv = "1,2,3\n4,5,6\n"
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=predictions.csv"},
    )


@app.route("/model1/upload", methods=["GET", "POST"])
def uploadmodel1():
    try:
        user_file = request.files["file"]
        if user_file.filename != "":
            filepath = os.path.join("static/files", user_file.filename) 
            user_file.save(filepath)
            with open(filepath, encoding="utf8") as file:
                csv_file = csv.reader(file,delimiter=';')
                for row in csv_file:
                    uploaded_file.append(row)
            return redirect(url_for("model1"))

    except Exception as e:
        print(f"Exception:{e}")
        resp = make_response(render_template("error.html"), 404)
        return resp


@app.route("/model2", methods=["GET", "POST"])
def model2(name=None):
    return render_template("model2.html", name=name)
