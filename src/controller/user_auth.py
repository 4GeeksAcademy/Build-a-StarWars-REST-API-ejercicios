from flask import Flask, request, jsonify

from models.user import User
from utils.db import db
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import json
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
def register():
    
    data = json.loads(request.data)
    print(data)
    username = data.get('nickname')
    password = data.get('password')
    email = data.get('email')
    pw_hash = bcrypt.generate_password_hash(password)
    if User.query.filter_by(nickname=username).first() is not None:
        return jsonify({'message': 'Username already taken'})
    user = User()
    user.nickname = username
    user.password = pw_hash
    user.email = email
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=user.serialize())
    return jsonify({'user' : user.serialize(), 'token': token}), 200

def login():
    data = json.loads(request.data)
    print(data)
    username = data.get('nickname')
    password = data.get('password')
    user = User.query.filter_by(nickname=username).first()
    if user is not None and bcrypt.check_password_hash(user.password, password):
         token = create_access_token(identity=user.serialize())
         return jsonify({'user' : user.serialize(), 'token': token})
    else:
        return jsonify({'message': 'Invalid username or password'})
    
