from utils import db

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String)
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String)
    eye_color = db.Column(db.String)
    url = db.Column(db.String)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    favorites = db.relationship('Favorites', backref='character', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'height': self.height,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'url': self.url
        }