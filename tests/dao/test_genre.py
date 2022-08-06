import pytest

from project.dao.genre import GenreDAO
from project.dao.models import Genre


class TestGenreDAO:

    @pytest.fixture
    def genre_dao(self, db):
        return GenreDAO(db.session)

    @pytest.fixture
    def genre_1(self, db):
        genre = Genre(id=1, name="Ужас")
        db.session.add(genre)
        db.session.commit()
        return genre

    @pytest.fixture
    def genre_2(self, db):
        genre = Genre(id=2, name="Кошмар")
        db.session.add(genre)
        db.session.commit()
        return genre

    @pytest.fixture
    def genre_3(self, db):
        genre = Genre(id=3, name="Комедия")
        db.session.add(genre)
        db.session.commit()
        return genre

    def test_get_genre_by_id(self, genre_1, genre_dao):
        assert genre_dao.get(genre_1.id) == [genre_1]

    def test_get_genre_by_id_not_found(self, genre_dao):
        assert not genre_dao.get(2)

    def test_get_all_genres(self, genre_dao, genre_1, genre_2, genre_3):
        assert genre_dao.get() == [genre_1, genre_2, genre_3]

    def test_get_genres_by_page(self, app, genre_dao, genre_1, genre_2, genre_3):
        assert genre_dao.get(page=1) == [genre_1]
        assert genre_dao.get(page=2) == [genre_2]
        assert genre_dao.get(page=3) == [genre_3]
        assert genre_dao.get(page=4) == []