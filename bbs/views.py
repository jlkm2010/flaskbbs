from bbs import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",
                           title='Home',
                           user=user)


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/reg')
def reg():
    return render_template("register.html")

@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/detail')
def detail():
    return render_template("detail.html")

@app.route('/myposts')
def my_Posts():
    return render_template("my-posts.html")