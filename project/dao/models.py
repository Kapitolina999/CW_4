from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, func, Table
from sqlalchemy.orm import relationship

from project.setup.db import db


class Genre(db.Model):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(db.Model):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)


# Создаем таблицу для реализации отношения многие-ко-многим для сохранения избранных фильмов пользователей
# users_movies = db.Table('users_movies',
#                         db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#                         db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
#                         extend_existing=True)

# Создаем таблицу для реализации отношения многие-ко-многим для сохранения избранных фильмов пользователей
class UsersMovies(db.Model):
    __tablename__ = 'users_movies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    director = relationship('Director')
    users = relationship('User', secondary='users_movies', backref='movie')


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    favourite_genre = relationship('Genre')
    favourite_movie = relationship('Movie', secondary='users_movies', backref='user')


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre = fields.Pluck(GenreSchema, 'name')
    director = fields.Pluck(DirectorSchema, 'name')


class UserSchema(Schema):
    name = fields.Str()
    surname = fields.Str()
    email = fields.Str()
    favourite_genre = fields.Pluck(GenreSchema, 'name')
    favourite_movie = fields.Pluck(MovieSchema, 'title', many=True)

