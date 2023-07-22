from models.favorites import Favorite
from models.users import User
from models.planet import Planet
from models.character import Character
from utils import db
from flask import Flask, jsnoify

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

def get_favorites(request):
    user_id = request.get('user_id')
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsnoify([favorite.serialize for favorite in favorites])