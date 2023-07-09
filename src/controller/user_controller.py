from flask import Flask, request, jsonify
from models.user import User
import json
def get():
    response = 'get'
    return response

def post():
    user = json.loads(request.data)
    db.session.add(User.nickname==user.name, User.email==user.email)
    response = user
    db.session.commit()
    return response