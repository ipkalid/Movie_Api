from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
import json
import os

database_path = os.environ['DATABASE_URL']

#print(database_path)

#database_path = 'postgres://postgres:1234@localhost:5432/ctest'
#export DATABASE_URL='postgres://postgres:1234@localhost:5432/testv'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    movies = db.relationship('Movie', backref='directors')

    def format(self):
        return {
            'id': self.id,
            'name': self.name}

    def __repr__(self):
        return f'<Director: {self.id}, name: {self.name}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insertData():
        for x in range(10):
            director = Director(name='name_{}'.format(
                x), birth_date='2020/12/{}'.format(x + 1), gender='male')
            db.session.add(director)
            db.session.commit()


class Actor(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    cast = db.relationship('Casting', backref='actor')

    def __repr__(self):
        return f'<Actor: {self.id}, name: {self.name}>'

    def format(self):
        return {
            'id': self.id,
            'name': self.name}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insertData():
        for x in range(10):
            actor = Actor(name='name_{}'.format(
                x), birth_date='2020/12/{}'.format(x + 1), gender='male')
            db.session.add(actor)
            db.session.commit()


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    relese_date = db.Column(db.String, nullable=False)

    director_id = db.Column(
        db.Integer,
        db.ForeignKey('director.id'),
        nullable=False)

    casts = db.relationship('Casting', backref='movie')

    def __repr__(self):
        return f'<Venue: {self.id}, name: {self.name}>'

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'relese_date': self.relese_date}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insertData():
        for x in range(10):
            movie = Movie(name='name_{}'.format(x),
                          relese_date='2020/12/{}'.format(x + 1),
                          director_id= 1 )
            db.session.add(movie)
            db.session.commit()


# -------------------------------------------------------


class Casting(db.Model):
    __tablename__ = 'casting'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)

    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __repr__(self):
        return f'<Venue: {self.id}, name: {self.name}>'

    def actor_name(self):
        return {
            'movie_name': self.name,
            'actor_name': Actor.query.get(self.actor_id).name}

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'relese_date': self.relese_date}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insertData():
        for x in range(10):
            cast = Casting(
                name='name_{}'.format(x),
                actor_id=x + 1,
                movie_id=2)
            db.session.add(cast)
            db.session.commit()
