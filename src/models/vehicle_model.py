from utils.db import db

class Vehicle(db.Model):
    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    created = db.Column(db.String, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    length = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    model = db.Column(db.String, nullable=False)
    vehicle_class = db.Column(db.String, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    pilots = db.Column(db.String, nullable=False)
    films = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    favorites = db.relationship('Favorites', backref='vehicle', lazy=True)