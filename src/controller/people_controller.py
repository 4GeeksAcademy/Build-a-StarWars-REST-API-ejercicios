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

def set_chartacter(request):
    list_characters = request
    for character in list_characters:
        parsed_character = json.loads(chatracter)
        character_in_db = Character.query.filter_by(name=parsed_character.name).first()
        if planet_in_db is None:  
            new_character = Character()
            new_character.name = parsed_character.get('name')
            new_character.birth_year = parsed_character.get('birth_year')
            new_character.gender = parsed_character.get('gender')
            new_character.height = parsed_character.get('height')
            new_character.skin_color = parsed_character.get('skin_color')
            new_character.eye_color = parsed_character.get('eye_color')
            new_character.url = parsed_character.get('url')
            db.session.add(new_character)
            db.session.commit()