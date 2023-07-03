"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/favorites', methods=['GET'])
def handle_user_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def handle_people():

    response_body = {
        "msg": "Hello, this is your GET /people response "
    }

    return jsonify(response_body), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def handle_people_id(people_id):

    response_body = {
        "msg": f"Hello, this is your GET /people/<int:people_id> response {people_id}"

    }
    
    return jsonify(response_body), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def handle_planets_id(planets_id):

    response_body = {
        "msg": f"Hello, this is your GET /planets/<int:planets_id> response {planets_id}"

    }
    
    return jsonify(response_body), 200

@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def handle_vehicles_id(vehicles_id):

    response_body = {
        "msg": f"Hello, this is your GET /vehicles/<int:vehicles_id> response {vehicles_id}"

    }
    
    return jsonify(response_body), 200

@app.route('/favorite/planet', methods=['POST'])
def handle_favorite_planet():

    response_data = request.data
    response_body = {
        "msg": "Hello, this is your POST /favorite/planet response",
        "data": response_data

    }
    
    print(jsonify(response_body))
    return jsonify(response_body), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
