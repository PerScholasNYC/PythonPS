## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request
## CREATE AN INDEX ROUTE AND A FUNCTION(PAGE) FOR ITd

comments = [{'name' : 'Kumar', 'message':'Cool'}]



@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/Naruto', methods = ['GET', 'POST'])
def Naruto():
        if request.method == 'POST':
            name1 = request.form['User']
            message1 = request.form['Thoughts']
            comments.append({'name' : name1, 'message': message1})
            print(comments)
            return render_template('/Comments''.html', messages = comments)
        elif request.method == 'GET':
            return render_template('/Naruto.html', messages = comments)
        return render_template('/Naruto.html')

@app.route('/Luffy', methods = ['GET', 'POST'])
def Luffy():
        if request.method == 'POST':
            name1 = request.form['User']
            message1 = request.form['Thoughts']
            comments.append({'name' : name1, 'message': message1})
            print(comments)
            return render_template('/Comments.html', messages = comments)
        elif request.method == 'GET':
            return render_template('/Luffy.html', messages = comments)
        return render_template('/Luffy.html')

@app.route('/Ichigo', methods = ['GET', 'POST'])
def Ichigo():
        if request.method == 'POST':
            name1 = request.form['User']
            message1 = request.form['Thoughts']
            comments.append({'name' : name1, 'message': message1})
            print(comments)
            return render_template('/Comments.html', messages = comments)
        elif request.method == 'GET':
            return render_template('/Ichigo.html', messages = comments)
        return render_template('/Ichigo.html')

@app.route('/Comments', methods = ['GET', 'POST'])
def Comments():
        return render_template('/Comments.html')
