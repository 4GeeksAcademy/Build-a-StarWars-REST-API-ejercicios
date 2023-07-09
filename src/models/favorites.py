from utils import db

class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __rep__(self):
        return f'id{self.id}'

    def serialize(self):
        return{
            'id': self.id,
            'user': self.user_id,
            'planet': self.planet_id,
            'character' : self.character_id,
            'vehicle' : self.vehicle_id
        }