import requests
from utils import db
from models import Character, Planet

def setupCharacters ():
    if db.session.query(Character).count() == 0:
        for i in range(1, 11):
            response = requests.get(f'https://swapi.tech/api/people/{i}')
            json = response.json()
            content = json["result"]
            properties = json["result"]["properties"]

            person_info = {
                "id": content["uid"],
                "name": properties["name"],
                "height": properties["height"],
                "mass": properties["mass"],
                "hair_color": properties["hair_color"],
                "skin_color": properties["skin_color"],
                "eye_color": properties["eye_color"],
                "gender": properties["gender"],
                "birth_year": properties["birth_year"],
                "url": content["uid"],         
            }

            character = Character(
                id=person_info["id"],
                name=person_info["name"],
                height=person_info["height"],
                mass=person_info["mass"],
                hair_color=person_info["hair_color"],
                skin_color=person_info["skin_color"],
                eye_color=person_info["eye_color"],
                gender=person_info["gender"],
                birth_year=person_info["birth_year"],
                url=person_info["url"]
            )

            db.session.add(character)

        db.session.commit()
        print("Data added to the Character table.")
    else:
        print("The Character table is not empty.")


def setupPlanets():
    if db.session.query(Planet).count() == 0:
        for i in range(1, 11):
            response = requests.get(f'https://swapi.tech/api/planets/{i}')
            json = response.json()
            content = json["result"]
            properties = json["result"]["properties"]

            planet_info = {
                "id": content["uid"],
                "name": properties["name"],
                "climate": properties["climate"],
                "diameter": properties["diameter"],
                "gravity": properties["gravity"],
                "orbital_period": properties["orbital_period"],
                "population": properties["population"],
                "rotation_period": properties["rotation_period"],
                "surface_water": properties["surface_water"],
                "url": content["uid"],         
            }

            planet = Planet(
                id=planet_info["id"],
                name=planet_info["name"],
                climate=planet_info["climate"],
                diameter=planet_info["diameter"],
                gravity=planet_info["gravity"],
                orbital_period=planet_info["orbital_period"],
                population=planet_info["population"],
                rotation_period=planet_info["rotation_period"],
                surface_water=planet_info["surface_water"],
                url=planet_info["url"]
            )

            db.session.add(planet)

        db.session.commit()
        print("Data added to the Planet table.")
    else:
        print("The Planet table is not empty.")


