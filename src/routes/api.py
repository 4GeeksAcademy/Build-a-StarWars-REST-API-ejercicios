from flask import Blueprint

from route_character import people_routes
from route_favorites import favorites_routes
from route_planet import planet_routes
from route_user import user_routes
from route_vehicles import vehicles_routes

api = Blueprint('api', __name__)



