from flask import request
from flask_restx import Namespace, Resource
from sqlalchemy import exc
from sqlalchemy.exc import NoResultFound

from project.container import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):

    def post(self):
        """
        Принимает email и пароль из Body запроса в виде JSON, создает пользователя
        """
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            return 'Не все поля заполнены', 400

        try:
            user_service.get_by_email(email)
        except exc.NoResultFound:
            user_service.create(data)
            return "", 201
        else:
            return f'Пользователь с email {email} уже зарегистрирован', 400  # Какой код здесь вернуть?


@auth_ns.route('/login')
class AuthView(Resource):

    def post(self):
        """
        Принимает email и пароль из Body запроса в виде JSON, проверяет соответствие с данными в БД
        (есть ли такой пользователь, такой ли у него пароль) -> генерирует токены access_token и refresh_token
        и отдает их в виде JSON.
        """
        data = request.json
        email = data['email']
        password = data['password']

        # проверяем, что все поля заполнены
        if None in [email, password]:
            return 'Не все поля заполнены', 400

        # генерируем токены access_token и refresh_token
        tokens = auth_service.generation_tokens(email, password)
        return tokens, 201

    def put(self):
        """
        Принимает refresh_token из Body запроса в виде JSON, проверяет refresh_token,
        если токен не истек и валиден — генерирует токены access_token и refresh_token
        и отдает их в виде JSON"""

        data = request.json
        refresh_token = data['refresh_token']
        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


