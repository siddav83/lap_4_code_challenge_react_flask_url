
from flask import Flask, request, jsonify
# from flask_cors import CORS
from werkzeug import exceptions
import random

app = Flask(__name__)
# CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to Flask!'

@app.route('/home', methods=['GET','POST'])
def get_and_create():
    if request.method == "POST":
        res = request.json
        new_url = short_url_creator()
        print(f"new_url{new_url}")
        obj = {
            "long_url": request.json,
            "short_url": new_url
        }
        
        return obj,201
    elif request.method == "GET":
        return jsonify(urls), 200



def short_url_creator():
    random_index = ""
    array = [1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"] 
    for num in range(0,6):
        random_index += str(random.choice(array))
    return random_index  

if __name__ == "__main__":
    app.run(debug=True)
