from unittest.mock import patch

import pytest

from project.dao.models import Genre
from project.exceptions import ItemNotFound
from project.services.genre import GenreService


class TestGenresService:

    @pytest.fixture()
    # Заменяем GenreDAO на мок
    @patch('project.dao.genre.GenreDAO')
    def genre_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get.return_value = [
            Genre(id=1, name='genre_1'),
            Genre(id=2, name='genre_2'),
        ]
        return dao

    @pytest.fixture()
    def genre_service(self, genre_dao_mock):
        return GenreService(dao=genre_dao_mock)

    def test_get_genre(self, genre_service):
        assert genre_service.get(1)

    def test_genre_not_found(self, genre_dao_mock, genre_service):
        genre_dao_mock.get.return_value = None

        with pytest.raises(ItemNotFound):
            genre_service.get(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_genres(self, genre_dao_mock, genre_service, page):
        genres = genre_service.get(page=page)
        assert len(genres) == 2
        assert genres == genre_dao_mock.get.return_value
