from sqlalchemy import desc

from project.config import config
from project.dao.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, page=None, mid=None, did=None, gid=None, year=None, status=None):
        query = self.session.query(Movie)

        if mid:
            return query.get(mid)
        if did:
            query = query.filter(Movie.director_id == did)
        if gid:
            query = query.filter(Movie.genre_id == gid)
        if year:
            query = query.filter(Movie.year == year)
        if status == 'new':
            query = query.order_by(desc(Movie.year))
        if page:
            limit = config.ITEMS_PER_PAGE
            offset = limit * (int(page) - 1)
            query = query.limit(limit).offset(offset)

        return query.all()

