from flask import Blueprint,request,jsonify
from ..database.urls import urls
from werkzeug import exceptions
from ..helper_function.main import short_url_creator


main_routes = Blueprint("main",__name__)

@main_routes.route('/home', methods=['GET','POST'])
def get_and_create():
    if request.method == "POST":
        print((request.json['long_url']))
        new_url = short_url_creator()
        obj = {
            "long_url": request.json['long_url'],
            "short_url": new_url
        }

        return obj
        # urls.append(jsonify(obj))
        # print(urls)
        # return urls
    
    if request.method =="GET":
        return jsonify(urls)
        
        return obj,201
    elif request.method == "GET":
        return jsonify(urls), 200