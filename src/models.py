from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

    def get_users():
        users = db.session.query(User)
        list_users = []
        for user in users:
            list_users.append(user.serialize())
        return list_users

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(120))
    height = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    eye_color = db.Column(db.String(120))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
        }

    def get_people():
        people = People.query.all()
        list_people = []
        for character in people:
            list_people.append(character.serialize())
        return list_people

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120))
    population = db.Column(db.String(120))
    orbital_period = db.Column(db.String(120))
    rotation_period = db.Column(db.String(120))
    diameter = db.Column(db.String(120))

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
        }
    
    def get_planets():
        planets = Planet.query.all()
        list_planets = []
        for planet in planets:
            list_planets.append(planet.serialize())
        return list_planets

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    user = db.relationship(User)
    people = db.relationship(People)
    planet = db.relationship(Planet)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
        }

    def get_favorites(user_id):
        favorites = db.session.query(Favorites).filter(Favorites.user_id == user_id)
        list_favorites = []
        for favorite in favorites:
            list_favorites.append(favorite.serialize())
        return list_favorites

    

