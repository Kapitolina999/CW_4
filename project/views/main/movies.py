from flask import request
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.models import MovieSchema
from project.setup.api.models import movie

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    # @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        page = request.args.get("page")
        did = request.args.get("director_id")
        gid = request.args.get("genre_id")
        year = request.args.get("year")
        status = request.args.get("status")
        all_movies = movie_service.get(page=page, did=did, gid=gid, year=year, status=status)
        return MovieSchema(many=True).dump(all_movies), 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    # @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self, mid):
        movie = movie_service.get(mid=mid)
        return MovieSchema().dump(movie), 200