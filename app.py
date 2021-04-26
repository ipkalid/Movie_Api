import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, db, Director, Movie, Actor, Casting, db_drop_and_create_all
from auth import AuthError, requires_auth
import json

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    
    # db.create_all()
    # db_drop_and_create_all()
    # Director.insertData()
    # Actor.insertData()
    # Movie.insertData()
    # Casting.insertData()

# --------------------------------------Actor--------------------------------------



    @app.route('/')
    def get_healthy():
        return 'healthy v2'

    @app.route('/data')
    @requires_auth('post:actors')
    def get_data(token):
        try:
            return jsonify({
                "success": True,
                "actors": "user data granted",
                "token": token
            }), 200
        except Exception as e:
            abort(400)

    @app.route('/actors')
    def get_actors():
        try:
            actors = Actor.query.order_by(Actor.name).all()

            actors_list = []

            for actor in actors:
                actor = actor.format()
                actors_list.append(actor)

            return jsonify({
                "success": True,
                "actors": actors_list
            }), 200
        except Exception as e:
            abort(400)

    @app.route('/actors/<int:actor_id>')
    def get_actor_detail(actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        try:
            movies = Casting.query.filter_by(movie_id=actor.id).all()
            movie_list = []

            for movie in movies:
                movie_list.append(movies.name)

            return jsonify({
                "success": True,
                "id": actor.id,
                "name": actor.name,
                "birth_date": actor.birth_date,
                "gender": actor.gender,
                "movies": movie_list
            }), 200

        except Exception as e:
            abort(401)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(token):
        body = request.get_json()

        name = body.get('name', None)
        birth_date = body.get('birth_date', None)
        gender = body.get('gender', None)

        if ((name is None) and (gender is None) and (birth_date is None)):
            abort(400)

        try:
            actor = Actor(name=name, gender=gender, birth_date=birth_date)

            Actor.insert(actor)

            new_actor = Actor.query.get(actor.id)

            return jsonify({
                "success": True,
                "actor": new_actor.format()
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        try:
            id = actor.id
            actor.delete()

            return jsonify({
                "success": True,
                "delete": id
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(token, actor_id):

        body = request.get_json()

        name = body.get('name', None)
        birth_date = body.get('birth_date', None)
        gender = body.get('gender', None)

        actor = Actor.query.get(actor_id)

        if ((name is None) and (birth_date is None) and (gender is None)):
            abort(400)

        if actor is None:
            print('d')
            abort(404)
        try:
            if name is not None:
                actor.name = name
            if birth_date is not None:
                actor.birth_date = birth_date
            if gender is not None:
                actor.gender = gender

            actor.update()

            return jsonify({
                "success": True,
                "actor": actor.format()
            }), 201

        except Exception as e:
            print(e)
            abort(401)


# --------------------------------------Movie--------------------------------------

    @app.route('/movies')
    def get_movies():
        try:
            movies = Movie.query.order_by(Movie.name).all()

            movies_list = []

            for movie in movies:
                movie = movie.format()
                movies_list.append(movie)

            return jsonify({
                "success": True,
                "movies": movies_list
            }), 200
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/movies/<int:movie_id>')
    def get_movies_detail(movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        try:
            director = Director.query.get(movie.director_id)
            casts = Casting.query.filter_by(movie_id=movie.id).all()
            cast_list = []

            for cast in casts:
                cast_list.append(cast.actor_name())

            return jsonify({
                "success": True,
                "id": movie.id,
                "name": movie.name,
                "relese_date": movie.relese_date,
                "director": director.name,
                "casts": cast_list
            }), 200

        except Exception as e:
            abort(401)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(token):
        body = request.get_json()

        name = body.get('name', None)
        relese_date = body.get('relese_date', None)
        director_id = body.get('director_id', None)

        if ((name is None) and (director_id is None) and (relese_date is None)):
            abort(400)

        try:
            movie = Movie(name=name, director_id=director_id,
                          relese_date=relese_date)

            Director.insert(movie)

            new_movie = Movie.query.get(movie.id)

            return jsonify({
                "success": True,
                "movie": new_movie.format()
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        try:
            id = movie.id
            movie.delete()

            return jsonify({
                "success": True,
                "delete": id
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(token, movie_id):

        body = request.get_json()

        name = body.get('name', None)
        relese_date = body.get('relese_date', None)
        director_id = body.get('director_id', None)

        movie = Movie.query.get(movie_id)

        if ((name is None) and (relese_date is None) and (director_id is None)):
            abort(400)

        if movie is None:
            abort(404)
        try:
            if name is not None:
                movie.name = name
            if relese_date is not None:
                movie.relese_date = relese_date
            if director_id is not None:
                movie.director_id = director_id

            movie.update()

            return jsonify({
                "success": True,
                "movie": movie.format()
            }), 201

        except Exception as e:
            print(e)
            abort(401)


# --------------------------------------Director--------------------------------------

    @app.route('/directors')
    def get_directors():
        try:
            directors = Director.query.order_by(Director.name).all()

            directors_list = []

            for director in directors:
                director = director.format()
                directors_list.append(director)

            return jsonify({
                "success": True,
                "directors": directors_list
            }), 200
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/directors/<int:director_id>')
    def get_director_detail(director_id):

        director = Director.query.get(director_id)

        if director is None:
            abort(404)

        try:
            movies = Movie.query.filter_by(director_id=director.id).all()
            movie_list = []

            for movie in movies:
                movie_list.append(movie.name)

            return jsonify({
                "success": True,
                "id": director.id,
                "name": director.name,
                "birth_date": director.birth_date,
                "gender": director.gender,
                "movies": movie_list
            }), 200

        except Exception as e:
            print(e)
            abort(401)

    @app.route('/directors', methods=['POST'])
    @requires_auth('post:directors')
    def post_directors(token):
        body = request.get_json()

        name = body.get('name', None)
        birth_date = body.get('birth_date', None)
        gender = body.get('gender', None)

        if ((name is None) and (gender is None) and (birth_date is None)):
            abort(400)

        try:
            directors = Director(name=name, gender=gender,
                                 birth_date=birth_date)

            Director.insert(directors)

            new_director = Director.query.get(directors.id)

            return jsonify({
                "success": True,
                "director": new_director.format()
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/directors/<int:director_id>', methods=['DELETE'])
    @requires_auth('delete:directors')
    def delete_director(token, director_id):

        director = Director.query.get(director_id)

        if director is None:
            abort(404)

        try:
            id = director.id
            director.delete()

            return jsonify({
                "success": True,
                "delete": id
            }), 201

        except Exception as e:
            abort(401)

    @app.route('/directors/<int:director_id>', methods=['PATCH'])
    @requires_auth('patch:directors')
    def patch_director(token, director_id):

        body = request.get_json()

        name = body.get('name', None)
        birth_date = body.get('birth_date', None)
        gender = body.get('gender', None)

        director = Director.query.get(director_id)

        if ((name is None) and (birth_date is None) and (gender is None)):
            abort(400)

        if director is None:
            print('d')
            abort(404)
        try:
            if name is not None:
                director.name = name
            if birth_date is not None:
                director.birth_date = birth_date
            if gender is not None:
                director.gender = gender

            director.update()

            return jsonify({
                "success": True,
                "director": director.format()
            }), 201

        except Exception as e:
            abort(401)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "The requested URL was not found on this server."
        }), 404

    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized."
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
