from project.config import config
from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, page=None, gid=None):
        query = self.session.query(Genre)
        if gid:
            return query.get(gid)
        if page:
            limit = config.ITEMS_PER_PAGE
            offset = limit * (int(page) - 1)
            query = query.limit(limit).offset(offset)
        return query.all()
