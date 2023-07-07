from flask import Flask, Blueprint, request, jsonify
from models import Vehicle

vehicles_routes = Blueprint("vehicles_routes", __name__)

@vehicles_routes.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def handle_vehicles_id(vehicles_id):

    response_body = {
        "msg": f"Hello, this is your GET /vehicles/<int:vehicles_id> response {vehicles_id}"

    }
    
    return jsonify(response_body), 200