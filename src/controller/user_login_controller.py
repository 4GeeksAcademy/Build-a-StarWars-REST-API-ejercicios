from flask import Flask, request, jsonify
import bcrypt
from models.user import User

def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    password_hash = user.password
    if bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) == password_hash:
        return jsonify(user.serialize())
    else:
        return jsonify({'message': 'Invalid username or password'})
