from flask import Flask, Blueprint, request, jsonify

vehicles_routes = Blueprint("people_routes", __name__)

@vehicles_routes.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def handle_vehicles_id(vehicles_id):

    response_body = {
        "msg": f"Hello, this is your GET /vehicles/<int:vehicles_id> response {vehicles_id}"

    }
    
    return jsonify(response_body), 200