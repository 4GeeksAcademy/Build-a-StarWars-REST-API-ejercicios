from utils import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password,
        }
        
    def __repr__(self):
        return '<User %r>' % self.id