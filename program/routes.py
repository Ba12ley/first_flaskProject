from program import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/anything')
def anything():
    return 'Anything'