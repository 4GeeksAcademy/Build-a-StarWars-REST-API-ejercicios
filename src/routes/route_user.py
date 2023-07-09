from flask import Flask, Blueprint, request, jsonify
from models import User

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/', methods=['GET','POST'])
def handle_hello():

    if request.method == 'GET':
        print('users')
        return 'get users'

    if request.method == 'POST':
        print('users')
        return 'post user'