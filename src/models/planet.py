from utils import db

class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.String(100), nullable=False)
    hair_color = db.Column(db.String(100), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    eye_color = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    favorites = db.relationship('Favorites', backref='planet', lazy=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "url": self.url,
        }
        