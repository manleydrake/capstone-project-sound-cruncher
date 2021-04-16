from flask import Flask
from flask import render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def DCASE():
    return render_template("DCASE.html")


app.config["IMAGE UPLOADS"] = "/Users/michael/desktop/cscapstone-main/flaskapp/soundsample"


@app.route("/loading", methods=["GET", "POST"])
def loading():
    if request.method == "POST":
        print("run prediction files here")
        os.system("./write.sh")
        if request.files:
            file_one = request.files["sound"]
            file_one.save(os.path.join(app.config["IMAGE UPLOADS"], file_one.filename))
            return redirect(request.url)
    return render_template("loading.html")
 

@app.route("/results")
def results(): 
    with open('result.csv', encoding = 'ISO-8859-1') as f:
        f1 = f.readlines()
        key = []
        value = []
        html_str = '<style> table, th, td{ border :1px solid black; align-content:center; text-align:center; } body { background-color: rgb(0, 204, 153); outline: black; }caption{ font-size:24; } </style> <table style="width:100%"> <caption>Prediction</caption> <tr> <th>'
        for line in f1:
            if 'Column' in line:
                key = (line.split(','))

            else:
                value = line.split(',')

        html_str = html_str + key[0] + '</th><th>' + key[1] + '</th> <th>' + key[2] + '</th> </tr>'
        html_str = html_str + ' <tr> <td>' + value[0] + '</td> <td>' + value[1] + '</td> <td>' + value[2] + '</td> </tr> </table>'

    return html_str


# these two lines of code should always be the last in the file
if __name__ == "__main__":
    app.run(debug=True)
