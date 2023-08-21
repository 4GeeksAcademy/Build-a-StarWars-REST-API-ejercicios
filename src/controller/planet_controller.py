
from utils.db import db
import bcrypt
from models.planet import Planet
from flask import Flask, jsonify, request
import json
import datetime as DateTime

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

def set_planets():
    list_planets = request
    if(len(list_planets) == 0):
        return {"message": "No planets found."}
    
    for planet in list_planets:
        parsed_planet = json.loads(planet)
        planet_in_db = Planet.query.filter_by(name=parsed_planet.name).first()
        if planet_in_db is None:  
            new_planet = Planet()
            new_planet.name = parsed_planet.get('name')
            new_planet.climate = parsed_planet.get('climate')
            new_planet.created = DateTime.now()
            new_planet.diameter = parsed_planet.get('diameter')
            new_planet.gravity = parsed_planet.get('gravity')
            new_planet.population = parsed_planet.get('population')
            new_planet.surface_water = parsed_planet.get('surface_water')
            new_planet.terrain = parsed_planet.get('terrain')
            db.session.add(new_planet)
            db.session.commit()