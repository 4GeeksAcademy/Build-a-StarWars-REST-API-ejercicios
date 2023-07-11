from flask import Flask, jsonify, request, Blueprint
import bcrypt
from models.user import User

user_register = Blueprint('user_register', __name__)

@user_register.route('/', methods=['POST'])
def register():
    if request.method == 'POST':
        nickname = request.get('nickname')
        password = request.get('password')
        email = request.get('email')

        if User.query.filter_by(nickname=nickname).first() is not None:
            return jsonify({'message': 'Username already taken'}), 400

        if User.query.filter_by(email=email).first() is not None:
            return jsonify({'message': 'Email already taken'}), 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User()
        new_user.nickname = nickname
        new_user.password = hashed_password
        new_user.email = email
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201