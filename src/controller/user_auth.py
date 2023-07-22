from flask import Flask, request, jsonify
import bcrypt
from models.user import User


def register(request, *args, **kwargs):
    username = request.get('username')
    password = request.get('password')
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already taken'})
    user = User(username=username, password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

def login(request, *args, **kwargs):
    username = request.get('username')
    password = request.get('password')
    user = User.query.filter_by(username=username).first()
    if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password):
        return jsonify(user.serialize())
    else:
        return jsonify({'message': 'Invalid username or password'})
    
