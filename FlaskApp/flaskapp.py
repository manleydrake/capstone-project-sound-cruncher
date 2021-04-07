from flask import Flask
from flask import render_template, request, redirect
import os
import tablib

app = Flask(__name__)


@app.route("/DCASE", methods=["GET", "POST"])
def DCASE():

    return render_template("DCASE.html")


app.config["IMAGE UPLOADS"] = "/Users/michael/desktop/cscapstone-main/flaskapp/soundsample"


@app.route("/loading", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        print("run prediction files here")
        os.system("./write.sh")
        if request.files:
            file_one = request.files["sound"]
            file_one.save(os.path.join(app.config["IMAGE UPLOADS"], file_one.filename))
            return redirect(request.url)
    return render_template("loading.html")

#User snippsat on python-forum.io
#https://python-forum.io/Thread-show-csv-file-in-flask-template-html

#pip install tablib
#pip install "tablib[html]" 

dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'result.csv')) as f:
    dataset.csv = f.read()
 
@app.route("/results")
def index():    
    return dataset.html


# these two lines of code should always be the last in the file
if __name__ == "__main__":
    app.run(debug=True)
