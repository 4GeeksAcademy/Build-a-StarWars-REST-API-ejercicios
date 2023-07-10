import bcrypt
from models.planet import Planet
from flask import Flask, jsonify, request

def get():
    Planets = Planet.query.all()
    if len(Planets) == 0:
        return {"message": "No Planets found."}
    return [planet.serialize() for planet in Planets]

def get_planet(id):
    planet = Planet.query.filter_by(id=id).first()
    if not planet:
        return {"message": "Planet not found."}
    return  jsonify(planet.serialize())

