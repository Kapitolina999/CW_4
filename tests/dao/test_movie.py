import pytest

from project.dao.movie import MovieDAO
from project.dao.models import Movie


class TestMovieDAO:

    @pytest.fixture
    def movie_dao(self, db):
        return MovieDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        movie = Movie(title='Фильм_1', description='Описание_1', trailer='www.trailer_1', year=2000,
                      rating=10, genre_id=1, director_id=1)
        db.session.add(movie)
        db.session.commit()
        return movie

    @pytest.fixture
    def movie_2(self, db):
        movie = Movie(title='Фильм_2', description='Описание_2', trailer='www.trailer_2', year=2022,
                      rating=9, genre_id=2, director_id=2)
        db.session.add(movie)
        db.session.commit()
        return movie

    def test_get_movie_by_mid(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(mid=movie_1.id) == movie_1

    def test_get_movie_by_did(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(did=movie_1.director_id) == [movie_1]

    def test_get_movie_by_year(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(year=movie_1.year) == [movie_1]

    def test_get_movie_by_gid(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(gid=movie_1.genre_id) == [movie_1]

    def test_get_movie_by_did_gid(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(did=movie_1.director_id, gid=movie_1.genre_id) == [movie_1]

    def test_get_movie_by_status(self, movie_1, movie_2, movie_dao):
        assert movie_dao.get(status='new') == [movie_2, movie_1]

    def test_get_movie_by_id_not_found(self, movie_dao):
        assert not movie_dao.get(2)

    def test_get_all_movies(self, movie_dao, movie_1, movie_2):
        assert movie_dao.get() == [movie_1, movie_2]

    def test_get_movies_by_page(self, app, movie_dao, movie_1, movie_2):
        assert movie_dao.get(page=1) == [movie_1]
        assert movie_dao.get(page=2) == [movie_2]
        assert movie_dao.get(page=3) == []
        assert movie_dao.get(page=4) == []
