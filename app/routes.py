from app import app
from flask import render_template

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'mango']
    return render_template('index.html', name = 'Shira', fruits = fruits)

@app.route('/posts')
def posts():
    return render_template('posts.html')