## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request
## CREATE AN INDEX ROUTE AND A FUNCTION(PAGE) FOR IT

comments = [{input() :input()}]



@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/ITCareer', methods = ['GET', 'POST'])
def ITCareer():
	if request.method == 'POST':
		name1 = request.form['User']
		message1 = request.form['THoughts']
		comments.append({'name' : name1, 'message': message1)

		print(comments)
		return render_template('/ITCareer.html', messages = comments)
