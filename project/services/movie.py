from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get(self, page=None, mid=None, did=None, gid=None, year=None, status=None):
        return self.dao.get(page, mid, did, gid, year, status)
