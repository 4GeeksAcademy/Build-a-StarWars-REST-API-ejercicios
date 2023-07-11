from flask import Blueprint

from .route_character import people_routes
from .route_favorites import favorites_routes
from .route_planet import planet_routes
from .route_user import user_routes
from .route_vehicles import vehicles_routes
from .route_user_login import user_login
from .route_user_register import user_register

api = Blueprint('api', __name__)

api.register_blueprint(people_routes, url_prefix='/people')
api.register_blueprint(favorites_routes, url_prefix='/favorites')
api.register_blueprint(planet_routes, url_prefix='/planet')
api.register_blueprint(user_routes, url_prefix='/user')
api.register_blueprint(vehicles_routes, url_prefix='/vehicles')
api.register_blueprint(user_login, url_prefix='/login')
api.register_blueprint(user_register, url_prefix='/register')
