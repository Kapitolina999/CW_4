import json
from contextlib import suppress
from sqlalchemy.exc import IntegrityError

from project.config import config
from project.dao.models import Genre, Movie, Director
from project.server import create_app
from project.setup.db import db


def load_data_db(model):
    """
    :param model: модель БД
    :return: None
    """
    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)
    if model is Movie:
        data = data.get('movies')
    elif model is Genre:
        data = data.get('genres')
    else:
        data = data.get('directors')

    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    app = create_app(config)

    with app.app_context():
        load_data_db(Movie)  # Как реализовать функцию, чтобы все модели передать в нее кортежем?
        load_data_db(Genre)
        load_data_db(Director)

        with suppress(IntegrityError):
            db.session.commit()
