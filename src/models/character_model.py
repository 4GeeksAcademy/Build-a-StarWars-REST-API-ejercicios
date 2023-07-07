from utils.db import db

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cargo_capacity = db.Column(db.String, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    crew = db.Column(db.String, nullable=False)
    cargo_manufacturercapacity = db.Column(db.String, nullable=False)
    max_atmosphering_speed = db.Column(db.String, nullable=False)
    pilots = db.Column(db.String, nullable=False)
    passengers = db.Column(db.String, nullable=False)
    films = db.Column(db.String, nullable=False)
    vehicle_class = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    favorites = db.relationship('Favorites', backref='character', lazy=True)