"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def get_all_people():
    list_people = People.get_people()
    
    return jsonify(list_people), 200

@app.route('/people/<people_id>', methods=['GET'])
def get_people_id(people_id):
    people = People.query.get(people_id)

    return jsonify(people.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    list_planets = Planet.get_planets()

    return jsonify(list_planets), 200

@app.route('/planets/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return jsonify(planet.serialize()), 200

@app.route('/users', methods=['GET'])
def get_users():
    list_users= User.get_users()

    return jsonify(list_users), 200

@app.route('/favorites/<user_id>', methods=['GET'])
def get_user_favorites(user_id):
    list_favorites = Favorites.get_favorites(user_id)

    return jsonify(list_favorites), 200

@app.route('/favorite/planet/<planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    body = request.get_json()
    new_favorite = Favorites(user_id=body["user_id"], planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify("Favorite planet added"), 201

@app.route('/favorite/people/<people_id>', methods=['POST'])
def add_favorite_people(people_id):
    body = request.get_json()
    new_favorite = Favorites(user_id=body["user_id"], people_id=people_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify("Favorite people added"), 201

@app.route('/favorite/planet/<planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    body = request.get_json()
    favorite = Favorites.query.filter(Favorites.user_id==body['user_id'], Favorites.planet_id==planet_id).first()
    if favorite is not None:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify("Favorite planet deleted"), 200

@app.route('/favorite/people/<people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    body = request.get_json()
    favorite = Favorites.query.filter(Favorites.user_id==body['user_id'], Favorites.people_id==people_id).first()
    if favorite is not None:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify("Favorite people deleted"), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
