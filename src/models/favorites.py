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

    def serializer():
        return{
            'id': fields.Integer,
            'user_id': fields.Integer,
            'planet_id': fields.Integer,
            'character_id': fields.Integer,
        }