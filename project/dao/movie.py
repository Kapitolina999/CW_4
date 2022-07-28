from sqlalchemy import desc

from project.config import config
from project.dao.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, page=None, mid=None, did=None, gid=None, year=None, status=None):

        if page:

            limit = config.ITEMS_PER_PAGE
            offset = limit * (int(page) - 1)

            if did:
                return self.session.query(Movie).filter(Movie.director_id == did).limit(limit).offset(offset).all()
            if gid:
                return self.session.query(Movie).filter(Movie.genre_id == gid).limit(limit).offset(offset).all()
            if year:
                return self.session.query(Movie).filter(Movie.year == year).limit(limit).offset(offset).all()
            if status == 'new':
                return self.session.query(Movie).order_by(desc(Movie.created)).limit(limit).offset(offset).all()

            return self.session.query(Movie).limit(limit).offset(offset).all()

        else:

            if mid:
                return self.session.query(Movie).get(mid)
            if did:
                return self.session.query(Movie).filter(Movie.director_id == did).all()
            if gid:
                return self.session.query(Movie).filter(Movie.genre_id == gid).all()
            if year:
                return self.session.query(Movie).filter(Movie.year == year).all()
            if status == 'new':
                return self.session.query(Movie).order_by(desc(Movie.created)).all()

            return self.session.query(Movie).all()
