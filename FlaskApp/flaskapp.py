from flask import Flask
from flask import render_template, request, redirect
import os


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def DCASE():
    return render_template("DCASE.html")


app.config["IMAGE UPLOADS"] = "/Users/michael/desktop/capstone-project-team-6-sound-cruncher/flaskapp/soundsample"


@app.route("/loading", methods=["GET", "POST"])
def loading():
    if request.method == "POST":
        
        print("run prediction files here")
        #os.system("python2 /Users/michael/desktop/capstone-project-team-6-sound-cruncher/mlprogram/predict/predict.py")

        os.system("python write_results.py")#writes to result.csv

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
            if 'Name' in line:
                key = (line.split(','))

            else:
                value = line.split(',')

        html_str = html_str + 'Name</th><th>Genus</th> <th> Species </th> <th>Accuracy</tr>'
        val = str(float(value[3]) * 100)
        html_str = html_str + ' <tr> <td>' + value[0] + '</td> <td>' + value[1] + '</td> <td>' + value[2] + '</td> <td>' + val + '</td> </tr> </table>'
        

        if value[0] == "Great Kiskadee":
            html_str = html_str + '<img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Pitangus_sulphuratus_3.jpg" width="850" height="650">'

        if value[0] == "Guianan Warbling Antbird":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/179883581/1800" width="850" height="650">'

        if value[0] == "Palm Tanager":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/41391251/1800" width="850" height="650">'

        if value[0] == "Plain Antvireo":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/238821021/900" width="850" height="650">'

        if value[0] == "Planalto Tyrannulet":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/95496391/900" width="850" height="650">'

        if value[0] == "Rufous-capped Motmot":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/79036751/1800" width="850" height="650">'

        if value[0] == "Rufous-sided Crake":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/320044501/1800" width="850" height="650">'

        if value[0] == "Striped Cuckoo":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/321337621/1800" width="850" height="650">'

        if value[0] == "White-throated toucanet":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/44419191/1800" width="850" height="650">'

        if value[0] == "Xingu Scale-backed Antbird":
            html_str = html_str + '<img src="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/182286871/1800" width="850" height="650">'


    return html_str


# these two lines of code should always be the last in the file
if __name__ == "__main__":
    app.run(debug=True)
