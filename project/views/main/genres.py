from flask import request
from flask_restx import Resource, Namespace

from project.container import genre_service
from project.dao.models import GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    # @auth_required
    def get(self):
        page = request.args.get("page")
        all_genres = genre_service.get(page=page)
        return GenreSchema(many=True).dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    # @auth_required
    def get(self, gid):
        genre = genre_service.get(gid=gid)
        return GenreSchema().dump(genre), 200