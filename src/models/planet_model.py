from utils.db import db

class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    climate = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    diameter = db.Column(db.String, nullable=False)
    films = db.Column(db.String, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    residents = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String, nullable=False, unique=True)
    favorites = db.relationship('Favorites', backref='planet', lazy=True)