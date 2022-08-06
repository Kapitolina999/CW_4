from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api

from project.exceptions import BaseServiceError
from project.setup.db import db
from project.views.auth.auth import auth_ns
from project.views.auth.user import user_ns
from project.views.main.directors import director_ns
from project.views.main.favourites_movies import favourites_movies_ns
from project.views.main.genres import genre_ns
from project.views.main.movies import movie_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    CORS(app=app)  # Для чего?
    db.init_app(app)
    api = Api(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(favourites_movies_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
