import bcrypt
from models.vehicle import Vehicle
from flask import Flask, request, jsonify

def get():
    vehicles = Vehicle.query.all()
    if len(vehicles) == 0:
        return "No vehicles found", 404
    return [jsonify(vehicles.serialize() for vehicle in vehicles)]

def get_vehicle(id):
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle is None:
        return "Vehicle not found", 404
    return jsonify(vehicle.serialize())