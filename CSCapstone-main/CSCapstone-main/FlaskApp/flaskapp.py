from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello from Flask!</h1>'

@app.route('/about')
def about():
	return '<h2>An about page!</h2>'

@app.route('/DCASE')
def DCASE():
	return '<header> <img src="dcase2021_challenge.png" alt="DCASE 2021 Challenge" id="logoImage" class="center" /> </header> <body> <p>Click on the "Choose File" button to upload a file:</p> <p>This is a test!</p> <form action="test.html" method="post"> <input type="file" id="myFile" name="filename" color="green" value="user-file"> <input type="submit" value="Upload"> </form> </body>'

@app.route('/results')
def results():
	return 'Results'


from flask import render_template

@app.route("/hello/<username>/")
def hello_user(username):
	return render_template('layout.html', name=username)


# these two lines of code should always be the last in the file
if __name__ == '__main__':
	app.run(debug=True)