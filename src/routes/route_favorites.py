

@app.route('/user/favorites', methods=['GET'])
def handle_user_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }

    return jsonify(response_body), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['POST', 'DELETE'])
def handle_favorite_planet():

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": "Hello, this is your POST /favorite/planet response",
        "data": response_data

        }
    
        print(jsonify(response_body))
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':
        response_data = request.data
        response_body = {
        "msg": "Hello, this is your DELETE /favorite/planet response",
        "data": response_data

        }
    
        return jsonify(response_body), 200


@app.route('/favorite/people/<int:people_id>', methods=['POST', 'DELETE'])
def handle_favorite_people():

    if request.method == 'POST':
        response_data = request.data
        response_body = {
        "msg": "Hello, this is your POST /favorite/people response",
        "data": response_data

        }
    
        return jsonify(response_body), 200
    
    if request.method == 'DELETE':
        response_data = request.data
        response_body = {
        "msg": "Hello, this is your DELETE /favorite/people response",
        "data": response_data

        }
    
        return jsonify(response_body), 200


