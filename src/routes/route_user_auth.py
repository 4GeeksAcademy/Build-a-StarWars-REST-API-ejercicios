from flask import Flask, request, Blueprint, jsonify
from models.user import User
import bcrypt
from controller.user_auth import login, register
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

user_auth = Blueprint('user_login', __name__)

@user_auth.route('/login', methods=['POST'])
def user_login():
    return login()
   

@user_auth.route('/register', methods=['POST'])
def user_register():
    return register()