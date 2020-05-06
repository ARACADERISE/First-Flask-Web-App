""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from flask import (
	Flask,
	render_template,
	url_for,
	request
)

app = Flask(__name__)
username_ = []

@app.route('/Submitted')
def Submit():
	return render_template('homePage.html', username=username_)

"""
	Home Page is the page where user will enter credentials
"""
@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	if request.method == 'POST':
		username_.append(request.form['Username'])
		return render_template('submit.html', username=username_)
	else:
		return render_template("userSetup.html")

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True)