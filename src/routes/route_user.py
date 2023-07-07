from flask import Flask, Blueprint, request, jsonify
from models import User

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/user', methods=['GET','POST'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200