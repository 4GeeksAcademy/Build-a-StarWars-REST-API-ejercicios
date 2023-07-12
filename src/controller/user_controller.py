from flask import Flask, request, jsonify
from models.user import User
from models.favorites import Favorites
from utils import db
import json
import bcrypt

def get():
    user = User.query.filter_by(nickname=request.args.get('nickname')).first()
    if not user:
        return {'message': 'User not found'}
    

def post():
    data = request.get_json()
    if not data or not data.get('nickname') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Please fill in all fields'})
    if User.query.filter_by(nickname=data.get('nickname')).first():
        return jsonify({'message': 'Nickname taken'})
    
    user = User()
    user.nickname = data.get('nickname')
    user.email = data.get('email')
    password = data.get('password')
    user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

def get_user_favorites(user_id):
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    if not favorites:
            return {'message': 'No favorites found'}
    return jsonify(favorites.serialize())