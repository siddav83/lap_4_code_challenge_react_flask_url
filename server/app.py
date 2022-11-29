
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to Flask!'

@app.route('/home', methods=['POST'])
def create():
    if request.method == 'GET':
        return jsonify(urls), 200
    elif request.method == 'POST':
        new_pokemon = request.json
        last_id = pokemons[-1]['id']
        new_pokemon['id'] = last_id + 1
        pokemons.append(new_pokemon)
        return new_pokemon, 201
