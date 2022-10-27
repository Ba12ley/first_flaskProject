import requests

from program import app
from flask import render_template
from datetime import datetime

time_now = str(datetime.today())
title = 'title'


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', time_now=time_now)

@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)

@app.route('/about')
def about():
    return 'About'


@app.route('/anything')
def anything():
    return 'Anything'


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']
