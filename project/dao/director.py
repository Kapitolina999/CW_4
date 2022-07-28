from project.config import config
from project.dao.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, page=None, did=None):

        if page:
            limit = config.ITEMS_PER_PAGE
            offset = limit * (int(page) - 1)
            return self.session.query(Director).limit(limit).offset(offset).all()
        else:
            if did:
                return self.session.query(Director).get(did)
            return self.session.query(Director).all()


