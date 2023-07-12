from flask import Flask, Blueprint, request, jsonify
from models import User
from controller.user_controller import get, post, get_user_favorites
user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/', methods=['GET','POST'])
def handle_hello():

    if request.method == 'GET':
        return get()
        
    if request.method == 'POST':
        post()

@user_routes.route('/<int:user_id>/favorites', methods=['GET'])
def handle_user_favorites(user_id):
    return get_user_favorites(user_id), 200 