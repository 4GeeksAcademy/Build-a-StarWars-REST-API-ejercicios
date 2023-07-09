from flask import Flask, Blueprint, request, jsonify
from models import Planet



planet_routes = Blueprint("planet_routes", __name__)

@planet_routes.route('/', methods=['GET'])
def handle_planets():

    response_body = {
        "msg": "Hello, this is your GET /planets/<int:planets_id> response "

    }
    
    return jsonify(response_body), 200

@planet_routes.route('/<int:planets_id>', methods=['GET'])
def handle_planets_id(planets_id):

    response_body = {
        "msg": f"Hello, this is your GET /planets/<int:planets_id> response {planets_id}"

    }
    
    return jsonify(response_body), 200