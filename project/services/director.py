from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get(self, page=None, did=None):
        if director := self.dao.get(page, did):
            return director
        raise ItemNotFound(f'Director with id={did} not exists.')