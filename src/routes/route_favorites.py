from flask import Flask, Blueprint, request, jsonify

people_routes = Blueprint("people_routes", __name__)

@people_routes.route('/user/favorites', methods=['GET'])
def handle_user_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }

    return jsonify(response_body), 200


@people_routes.route('/favorite/planet/<int:planet_id>', methods=['POST', 'DELETE'])
def handle_favorite_planet(planet_id):

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": f"Hello, this is your POST /favorite/planet response {planet_id}",
        "data": response_data

        }
    
        print(jsonify(response_body))
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':

        print("Delete")
        return jsonify("delete"), 200


@people_routes.route('/favorite/people/<int:people_id>', methods=['POST', 'DELETE'])
def handle_favorite_people(people_id):

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": f"Hello, this is your POST /favorite/people response {people_id}",
        "data": response_data

        }
    
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':

        print("Delete")
        return jsonify("delete"), 200


