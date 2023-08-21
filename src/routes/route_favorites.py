from flask import Flask, Blueprint, request, jsonify
from models import Favorites
from controller.favorites_controller import get_favorites, set_favorite, delete_favorite

favorites_routes = Blueprint("favorites_routes", __name__)


@favorites_routes.route('/', methods=['GET'])
def handle_favorites():

    response_body = {
        "msg": "Hello, this is your GET favorites response ",
        "data": get_favorites()
    }

    return jsonify(response_body), 200


@favorites_routes.route('/planet', methods=['POST', 'DELETE'])
def handle_favorite_planet(planet_id):
    if request.method == 'POST':
        response_body = {
        "msg": "Hello, add new favorite planet",
        "data": set_favorite()

        }
    
        print(jsonify(response_body))
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':
        delete_favorite()
        response_body = {
            'msg': f'delete planet'
        }
        return jsonify("delete"), 200


@favorites_routes.route('/people', methods=['POST', 'DELETE'])
def handle_favorite_people(people_id):

    if request.method == 'POST':
        
        response_body = {
        "msg": f"Hello, add people {people_id}",
        "data": set_favorite()
        }
    
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':
        delete_favorite()
        response_body = {
            'msg': f'delete peopele'
        }
        return jsonify("delete"), 200


