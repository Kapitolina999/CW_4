
from flask import abort

from project.config import config
from project.dao.favourite_movie import FavouriteMovieDAO
from project.exceptions import ItemNotFound


class FavouriteMovieService:
    def __init__(self, dao: FavouriteMovieDAO):
        self.dao = dao

    def get_user_movie(self, uid, mid):
        if user_movie := self.dao.get_user_movie(uid, mid):
            return user_movie
        raise ItemNotFound

    def create(self, uid, mid):
        self.dao.create(uid, mid)

    def delete(self, uid, mid):
        self.dao.delete(uid, mid)



