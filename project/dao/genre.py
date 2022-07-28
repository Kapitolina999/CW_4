from project.config import config
from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, page=None, gid=None):

        if page:
            limit = config.ITEMS_PER_PAGE
            offset = limit * (int(page) - 1)
            return self.session.query(Genre).limit(limit).offset(offset).all()

        else:
            if gid:
                return self.session.query(Genre).get(gid)
            return self.session.query(Genre).all()
