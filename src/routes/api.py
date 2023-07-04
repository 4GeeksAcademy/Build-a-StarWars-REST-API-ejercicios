from flask import Blueprint

from .route_character import route_character
from .route_favorites import route_favorite
from .route_planet import route_planet
from .route_user import route_user
from .route_vehicles import route_vehicles

api = Blueprint('api', __name__)



