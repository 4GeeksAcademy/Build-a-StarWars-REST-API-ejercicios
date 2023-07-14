"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, render_template, send_from_directory
from flask_migrate import Migrate


from utils import db
from routes.api import api
#from models import Person


public_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public')
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///star_wars.db"


MIGRATE = Migrate(app, db)
db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(api, url_prefix = '/api')

@app.route('/')
def index():
    print(public_folder)
    return 'working'

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
