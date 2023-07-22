from flask import Blueprint

from .route_character import people_routes
from .route_favorites import favorites_routes
from .route_planet import planet_routes
from .route_user import user_routes

from .route_user_auth import user_auth
from .route_user_register import user_register

api = Blueprint('api', __name__)

api.register_blueprint(people_routes, url_prefix='/people')
api.register_blueprint(favorites_routes, url_prefix='/favorites')
api.register_blueprint(planet_routes, url_prefix='/planet')
api.register_blueprint(user_routes, url_prefix='/user')
api.register_blueprint(user_auth, url_prefix='/auth')
api.register_blueprint(user_register, url_prefix='/register')
