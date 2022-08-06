from flask_restx import Resource, Namespace

from project.container import favourite_movie_service
from project.helpers.decorators import access_user

favourites_movies_ns = Namespace('favourites')


@favourites_movies_ns.route('/movies/<int:mid>')
class FavouriteMovieView(Resource):
    @access_user
    def post(self, uid, mid):
        favourite_movie_service.create(uid, mid)
        return '', 204

    @access_user
    def delete(self, uid, mid):
        favourite_movie_service.delete(uid, mid)
        return '', 204
