import base64
import os
from pathlib import Path
from typing import Type

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent  # Что это значит? О каком файле речь?


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess') #
    JSON_AS_ASCII = False  # Flask не будет кодировать в ASCII, а выводимые строки будут как есть,
    # то есть в виде строк в формате unicode
    # Отключаем сортирвку по алфавиту
    JSON_SORT_KEYS = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130


    # PWD_HASH_SALT = base64.b64decode("salt")
    # PWD_HASH_ITERATIONS = 100_000
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000

    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('project.db').as_posix()


class ProductionConfig(BaseConfig):
    DEBUG = False
    # TODO: дополнить конфиг


class ConfigFactory:
    dotenv.load_dotenv(override=True)
    flask_env = os.getenv('FLASK_ENV')  # то же самое, что и os.environ.get()?

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:  # Что такое cls?
        if cls.flask_env == 'development':
            return DevelopmentConfig
        elif cls.flask_env == 'production':
            return ProductionConfig
        elif cls.flask_env == 'testing':
            return TestingConfig
        raise NotImplementedError  # Исключение, возникающее в случаях, когда наследник класса не переопределил метод,
        # который должен был


config = ConfigFactory.get_config()
