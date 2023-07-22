from flask import Flask, request, Blueprint, jsonify
from models.user import User
import bcrypt
from controller.user_auth import login, register

user_auth = Blueprint('user_login', __name__)

@user_auth.route('/login', methods=['POST'])
def user_login():
    return login(request)
   

@user_auth.route('/register', methods=['POST'])
def user_register():
    return register(request)