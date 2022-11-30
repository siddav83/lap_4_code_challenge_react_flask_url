from flask import Blueprint,request,jsonify
from ..database.urls import urls
from werkzeug import exceptions
from ..helper_function.main import short_url_creator
from ..database.db import db
from ..models.main import Url

main_routes = Blueprint("main",__name__)

@main_routes.route('/home', methods=['GET','POST'])
def get_and_create():
    if  request.method == "GET":
        db = Url.query.all()
        return jsonify(db), 200
    
    elif request.method == "POST":
        new_request = request.json['long_url']
        new_url = short_url_creator()
        obj = {
            "long_url": new_request,
            "short_url": new_url
            }
        urls.append(obj)
        return obj,201
