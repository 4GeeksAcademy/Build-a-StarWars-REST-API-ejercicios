from flask import Blueprint

from tools import db
from models import Character, Planet, Vehicle
from controller.add_data_to_db import setupCharacters, setupPlanets, setupVehicles

setup_routes = Blueprint('setup_routs', __name__)

@setup_routes.route('/', methods=["GET"])
def setup():
    try:
        with db.session.no_autoflush:
            if db.session.query(Character).count() == 0:
                setupCharacters()
                return "Data setup completed for Characters."
            
            if db.session.query(Planet).count() == 0:
                setupPlanets()
                return "Data setup completed for Planets."
            
            
            return "All tables already have rows. Data setup skipped."
    except Exception as e:
        return f"An error occurred during data setup: {str(e)}"