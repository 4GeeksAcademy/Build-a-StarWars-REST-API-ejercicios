from flask import Flask, Blueprint, request, jsonify
from  models import Character
from controller.people_controller import get, get_people, set_chartacter
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
    return  get_people(people_id)


@people_routes.route('/setpeople', methods=['POST'])
def handle_set_people():
    return set_chartacter()