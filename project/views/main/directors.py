from flask import request
from flask_restx import Resource, Namespace

from project.container import director_service
from project.dao.models import DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        page = request.args.get("page")
        all_directors = director_service.get(page=page)
        return DirectorSchema(many=True).dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # @auth_required
    def get(self, did):
        director = director_service.get(did=did)
        return DirectorSchema().dump(director), 200