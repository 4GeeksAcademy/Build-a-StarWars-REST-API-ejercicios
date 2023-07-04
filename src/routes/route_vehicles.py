

@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def handle_vehicles_id(vehicles_id):

    response_body = {
        "msg": f"Hello, this is your GET /vehicles/<int:vehicles_id> response {vehicles_id}"

    }
    
    return jsonify(response_body), 200