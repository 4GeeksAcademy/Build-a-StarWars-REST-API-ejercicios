from flask import Flask, Blueprint, request, jsonify
from  models import Character
from controller.people_controller import get, get_people
people_routes = Blueprint("people_routes", __name__)

@people_routes.route('/', methods=['GET'])
def handle_people():
    peoples = get()
    response_body = {
        'msg': 'get people',
        'data': peoples
    }

    return jsonify(response_body), 200


@people_routes.route('/<int:people_id>', methods=['GET'])
def handle_people_id(people_id):

    response_body = {
        "msg": f"Hello, this is your GET /people/<int:people_id> response {people_id}",
        'data' : get(people_id)
    }
    
    return jsonify(response_body), 200


