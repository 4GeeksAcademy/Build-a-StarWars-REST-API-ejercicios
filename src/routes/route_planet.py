from flask import Flask, Blueprint, request, jsonify
from models import Planet
from controller.planet_controller import get, get_planet


planet_routes = Blueprint("planet_routes", __name__)

@planet_routes.route('/', methods=['GET'])
def handle_planets():

    response_body = {
        "msg": "get list planet ",
        'data': get()
    }
    
    return jsonify(response_body), 200

@planet_routes.route('/<int:planets_id>', methods=['GET'])
def handle_planets_id(planets_id):

    response_body = {
        "msg": f"get planet {planets_id}",
        'data': get_planet(planets_id)

    }
    
    return jsonify(response_body), 200