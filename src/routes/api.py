from flask import Blueprint
from .route_character import people_routes
# from .route_favorites import route_favorite
from .route_planet import planet_routes
from .route_user import user_routes
from .route_vehicles import vehicles_routes

api = Blueprint('api', __name__)

api.register_blueprint(people_routes, url_prefix="/character")
# api.register_blueprint(route_favorite, url_prefix="/favorite")
api.register_blueprint(planet_routes, url_prefix="/planet")
api.register_blueprint(user_routes, url_prefix="/user")
api.register_blueprint(vehicles_routes, url_prefix="/vehicles")





