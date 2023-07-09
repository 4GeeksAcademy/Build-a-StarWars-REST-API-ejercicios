from flask import Flask, Blueprint, request, jsonify
from models import Favorites


favorites_routes = Blueprint("favorites_routes", __name__)
favorites_people_routes = Blueprint("favorites_people_routes", __name__)
favorites_planet_routes = Blueprint("favorites_planet_routes", __name__)
favorites_vehicle_routes = Blueprint("favorites_vehicle_routes", __name__)

@favorites_routes.route('/', methods=['GET'])
def handle_favorites():

    response_body = {
        "msg": "Hello, this is your GET favorites response "
    }

    return jsonify(response_body), 200


@favorites_planet_routes.route('/planet/<int:planet_id>', methods=['POST', 'DELETE'])
def handle_favorite_planet(planet_id):


    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": f"Hello, add new favorite {planet_id}",
        "data": response_data

        }
    
        print(jsonify(response_body))
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':

        response_body = {
            'msg': f'delete planet id: {planet_id}'
        }
        return jsonify("delete"), 200


@favorites_people_routes.route('/people/<int:people_id>', methods=['POST', 'DELETE'])
def handle_favorite_people(people_id):

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": f"Hello, add people {people_id}",
        "data": response_data

        }
    
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':

        response_body = {
            'msg': f'delete peopele {people_id}'
        }
        return jsonify("delete"), 200


@favorites_vehicle_routes.route('/vehicle/<int:vehicle_id>', methods=['POST', 'DELETE'])
def handle_favorite_vehicles(vehicles_id):

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": f"Hello, add vehicle {vehicles_id}",
        "data": response_data

        }
    
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':

        response_body = {
            'msg' : f'delete vehicle {vehicles_id}'
        }
        return jsonify("delete"), 200