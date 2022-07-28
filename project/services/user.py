import base64
import hashlib
import hmac

from flask import abort

from project.config import config
from project.dao.user import UserDAO
from project.exceptions import ItemNotFound


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get(self, uid):
        if user := self.dao.get(uid):
            return user
        raise ItemNotFound(f'User with id={uid} not exists.')

    def get_by_email(self, email):
        if user := self.dao.get_by_email(email):
            return user
        raise ItemNotFound

    def create(self, data):
        data['password'] = self._get_hash(data['password'])
        return self.dao.create(data)

    def partial_update(self, data):
        uid = data['id']
        user = self.get(uid)

        if 'name' in data.keys():
            user.name = data['name']
        if 'surname' in data.keys():
            user.surname = data['surname']
        if 'favourite_genre_id' in data.keys():
            user.favourite_genre_id = data['favourite_genre_id']  # Как передать жанр, а не id жанра?

        self.dao.update(user)

    def password_update(self, uid, password_1, password_2):
        user = self.get(uid)
        #  Сравниваем старый пароль password_1 с паролем пользователя в БД
        if not self.compare_passwords(password_1, user.password):
            abort(401)
        user.password = self._get_hash(password_2)
        return self.dao.update(user)

    def _get_hash(self, password):
        """
        Хэш-функция
        :param password: пароль пользователя
        :return: хэш-пароль
        """
        return base64.b64encode(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), config.PWD_HASH_SALT,
                                                    config.PWD_HASH_ITERATIONS))

    def compare_passwords(self, password, password_hash):
        """
           сравнение паролей
           :param password: проверяемый пароль
           :param password_hash: хэш-пароль
           :return: bool
        """
        # compare_digest сравнивает значения a и b возвращает True
        return hmac.compare_digest(base64.b64decode(password_hash), base64.b64decode(self._get_hash(password)))
