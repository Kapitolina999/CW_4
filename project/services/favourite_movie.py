from project.dao.favourite_movie import FavouriteMovieDAO


class FavouriteMovieService:
    def __init__(self, dao: FavouriteMovieDAO):
        self.dao = dao

    def create(self, uid, mid):
        self.dao.create(uid, mid)

    def delete(self, uid, mid):
        self.dao.delete(uid, mid)
