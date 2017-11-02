## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request
## CREATE AN INDEX ROUTE AND A FUNCTION(PAGE) FOR ITd

comments = [{'name' : 'kumar', 'message':'hi'}]



@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/ITCareer', methods = ['GET', 'POST'])
def ITCareer():
    if request.method == 'POST':
        name1 = request.form['User']
        message1 = request.form['Thoughts']
        comments.append({'name' : name1, 'message': message1})
        print(comments)
        return render_template('/ITCareer.html', messages = comments)
    elif request.method == 'GET':
        return render_template('/ITCareer.html', messages = comments)
