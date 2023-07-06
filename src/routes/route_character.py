from flask import Flask, Blueprint, request, jsonify

people_routes = Blueprint("people_routes", __name__)

@people_routes.route('/people', methods=['GET'])
def handle_people():

    response_body = {
        "msg": "Hello, this is your GET /people response "
    }

    return jsonify(response_body), 200


@people_routes.route('/people/<int:people_id>', methods=['GET'])
def handle_people_id(people_id):

    response_body = {
        "msg": f"Hello, this is your GET /people/<int:people_id> response {people_id}"

    }
    
    return jsonify(response_body), 200


