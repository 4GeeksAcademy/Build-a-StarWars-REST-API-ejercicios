import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    favorites = relationship('Favorites', backref='user', lazy=True)

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('vehicles.id'))

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    user_id = 
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    favorites = relationship('Favorites', backref='planet', lazy=True)
    planet_properties = relationship('Planet_Properties', populates="Planet" , lazy=True)

class Planet_Properties(Base):
    __tablename__ = "planet_properties"
    id = Column(Integer, primary_key=True)
    planet_id = Column(ForeignKey('planet.id'))
    name = Column(ForeignKey('planet.name'))
    climate = Column(String, nullable=False)
    created = Column(String, nullable=False)
    diameter = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    residents = Column(String, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)
    created=Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    url = Column(String, nullable=False, unique=True)
    planet = relationship('Planet', populates="Planet_Properties" , lazy=True)


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    favorites = relationship('Favorites', backref='vehicle', lazy=True) 
    vehicle_properties = relationship('Vehicle_Properties', populates="Vehicle" , lazy=True) 

class Vehicle_Properties(Base):
    __tablename__ = "vehicle_properties"
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicle.id'))
    name = Column(ForeignKey('vehicle.name'))
    cargo_capacity = Column(Integer, nullable=False)
    created = Column(String, nullable=False)
    crew = Column(Integer, nullable=False)
    length = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    model = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    passengers = Column(Integer, nullable=False)
    pilots = Column(String, nullable=False)
    films = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created=Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    vehicle_properties = relationship('Vehicle', populates="Vehicle_Properties" , lazy=True)  

class Character(Base):
    __table_name__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    favorites = relationship('Favorites', backref='character', lazy=True)
    character_properties = relationship('Character_Properties', populates='character', lazy=True)

class Character_Properties(Base):
    __table_name__ = "character_properties"
    id = Column(Integer, primary_key=True)
    character_id = Column(ForeignKey('Character.id'))
    cargo_capacity = Column(String, nullable=False)
    consumables = Column(String, nullable=False)
    crew = Column(String, nullable=False)
    cargo_manufacturercapacity = Column(String, nullable=False)
    max_atmosphering_speed = Column(String, nullable=False)
    pilots = Column(String, nullable=False)
    passengers = Column(String, nullable=False)
    films = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created = Column(DateTime)
    edited = Column(DateTime)
    character = relationship('Character', populates='character_properties', lazy=True)

## Draw from SQLAlchemy base
render_er(Base, "diagram.png")
