from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE-URI'] = 'mysql+pymysql://build-a-blog:Miami2020@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/')
@app.route('/blog', methods=['POST', 'GET'])
def blog():

    if request.method == 'POST':
        blog = request.form['blog']
        blogs.append(blog)

    return render_template('blog.html', blogs=blogs)

@app.route('/newpost')
def newpost():
    return render_template('newpost.html')

if __name__== '__main__':
    app.run()