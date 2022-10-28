from pprint import pprint

import requests

from program import app
from flask import render_template, request
from datetime import datetime

# time_now = str(datetime.today())
title = 'title'


@app.route('/')
@app.route('/index.html')
def index():
    time_now = str(datetime.today())
    return render_template('index.html', time_now=time_now)


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)


@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    pokemon_returned = []
    if request.method == 'POST' and 'pokecolour' in request.form:
        color = request.form.get('pokecolour')
        pokemon_returned = get_poke_color(color)

    return render_template('pokemon.html', pokemon_returned=pokemon_returned)


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


def get_poke_color(color):
    pokemon_returned = []
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon-color/{color}')
    data = r.json()
    pprint(data)
    for pokename in data['pokemon_species']:
        pokemon_returned.append(pokename['name'])
    # for name in pokemon_returned:
    #     print(name)
    return pokemon_returned
