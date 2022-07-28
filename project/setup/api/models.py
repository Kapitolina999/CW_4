from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Никита Михалков'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Утомленные солнцем'),
    'description': fields.String(required=True, max_length=255, example='О тех, кто утомился'),
    'trailer': fields.String(required=True, max_length=100, example='www.ссылка'),
    'year': fields.Integer(required=True, example=2022),
    'genre': fields.String(required=True, max_length=100, example='Комедийная драма'),
    'rating': fields.Integer(required=True, example=9.9),
    'director': fields.String(required=True, max_length=100, example='Сам себе режиссер'),
})