from flask import Flask, Blueprint, request, jsonify
from models import Vehicle

vehicles_routes = Blueprint("vehicles_routes", __name__)

@vehicles_routes.route('/', methods=['GET'])
def handle_vehicles():

    response_body = {
        "msg": "get list vehicles"

    }
    
    return jsonify(response_body), 200

@vehicles_routes.route('/<int:vehicles>', methods=['GET'])
def handle_vehicles_id(vehicles):

    response_body = {
        "msg": f"get vehicle {vehicles}"

    }
    
    return jsonify(response_body), 200