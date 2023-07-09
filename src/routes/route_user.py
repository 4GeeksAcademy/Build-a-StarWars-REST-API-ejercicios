from flask import Flask, Blueprint, request, jsonify
from models import User
from controller.user_controller import get
user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/', methods=['GET','POST'])
def handle_hello():

    if request.method == 'GET':
        response = get()
        return response

    if request.method == 'POST':
        print('users')
        return 'post user'

@user_routes.route('/<int:user_id>/favorites', methods=['GET'])
def handle_user_favorites(user_id):
    return f'get favorites for user {user_id}'

