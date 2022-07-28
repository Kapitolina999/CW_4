from project.dao.genre import GenreDAO
from project.exceptions import ItemNotFound


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get(self, page=None, gid=None):
        if genre := self.dao.get(page, gid):
            return genre
        raise ItemNotFound(f'Genre with id={gid} not exists.')
