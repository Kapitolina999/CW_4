from project.dao.favourite_movie import FavouriteMovieDAO
from project.dao.genre import GenreDAO
from project.dao.movie import MovieDAO
from project.dao.director import DirectorDAO
from project.dao.user import UserDAO
from project.services.auth import AuthService
from project.services.director import DirectorService
from project.services.favourite_movie import FavouriteMovieService

from project.services.genre import GenreService
from project.services.movie import MovieService
from project.services.user import UserService
from project.setup.db import db

# DAO
movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
user_dao = UserDAO(db.session)
favourite_movie_dao = FavouriteMovieDAO(db.session)

# Services
genre_service = GenreService(genre_dao)
movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)
favourite_movie_service = FavouriteMovieService(favourite_movie_dao)
