import bcrypt
from models.character import Character
from flask import Flask, request, jsonify

def get():
    peoples = Character.query.all()
    if len(peoples) == 0:
        return jsonify({"message": "No people found"})
    return [jsonify(peoples.serialize() for peoples in peoples)]

def get_people(id):
    people = Character.query.filter_by(id=id).first()
    if not people:
        return jsonify({"message": "No people found"})
    return jsonify(people.serialize())