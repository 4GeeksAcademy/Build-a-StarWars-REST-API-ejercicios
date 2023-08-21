from models.favorites import Favorites
from models.user import User
from models.planet import Planet
from models.character import Character
from utils import db
from flask import Flask, jsonify, request

def set_favorite(request):
    user_id = request.get('user_id')
    planet_id = request.get('planet_id')
    character_id = request.get('character_id')
    if user_id is None:
        return jsnoify('you need to provide a user_id')
    if user_id is None and planet_id is None and character_id is None:
            return jsnoify('you need to provide a user_id, planet_id, or character_id')   
    favorite = Favorite()
    favorite.user_id = user_id
    favorite.planet_id = planet_id
    favorite.character_id = character_id
    db.session.add(favorite)
    db.session.commit()
    return jsnoify(favorite.serialize)

def get_favorites():
    user_id = request.data.get('user_id')
    find_user = User.query.filter_by(id=user_id).first()
    if find_user is None:
        return jsnoify('User not found')
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    if len(favorites) == 0 or favorites is None:
        return jsnoify('No favorites found')
    return jsnoify([favorite.serialize for favorite in favorites])


def delete_favorite():
    user_id = request.data.get('user_id')
    planet_id = request.data.get('planet_id')
    character_id = request.data.get('character_id')
    if user_id is None:
        return jsnoify('you need to provide a user_id')
    if user_id is None and planet_id is None and character_id is None:
            return jsnoify('you need to provide a user_id, planet_id, or character_id')   
    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id, character_id=character_id).first()
    if favorite is None:
        return jsnoify('Favorite not found')
    db.session.delete(favorite)
    db.session.commit()
    return jsnoify(favorite.serialize)