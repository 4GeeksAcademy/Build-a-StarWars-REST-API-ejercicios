from flask import Flask, request, Blueprint, jsonify
from models.user import User
import bcrypt
from controller.user_login_controller import login

user_login = Blueprint('user_login', __name__)

@user_login.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'Post':
        return login()


