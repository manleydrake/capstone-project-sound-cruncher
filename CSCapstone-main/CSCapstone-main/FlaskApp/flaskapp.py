from flask import Flask
from flask import render_template, request, redirect
import os
app = Flask(__name__)


@app.route('/DCASE', methods=["GET", "POST"])
def DCASE():

	# if request.method == "POST":
	# 	if request.files:
	# 		file_one = request.files["sound"]
	# 		file_one.save(os.path.join(app.config["IMAGE UPLOADS"], file_one.filename)) 
	# 		print("it worked")
	# 		return redirect(request.url)

	return render_template('DCASE.html')


app.config["IMAGE UPLOADS"] = "/Users/michaelscott/desktop/cs178/flaskapp/images"


@app.route('/results', methods=["GET", "POST"])
def results():
	
	if request.method == "POST":
		if request.files:
			file_one = request.files["sound"]
			file_one.save(os.path.join(app.config["IMAGE UPLOADS"], file_one.filename)) 
			print("it worked")
			return redirect(request.url)
	return 'Results'


from flask import render_template

@app.route("/hello/<username>/")
def hello_user(username):
	return render_template('layout.html', name=username)

	


# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)