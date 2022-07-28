import base64
import hashlib
import hmac
import calendar
import datetime

import jwt
from flask_restx import abort

from project.config import config
from project.constants import JWT_SECRET, JWT_ALGO
from project.services.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generation_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        #Аутентификация
        if user is None:
            raise abort(404)

        # Если создание новых токенов, то проходим проверку
        if not is_refresh:
            #Аутентификация пароля
            if not self.user_service.compare_passwords(password, user.password):
                abort(400)

        data = {'email': user.email}

        #Задаем время жизни access_token
        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=config.TOKEN_EXPIRE_MINUTES)
        data['exp'] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=config.TOKEN_EXPIRE_DAYS)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALGO])
        email = data['email']
        # т.к. это refresh, то пароль уже не требуем, потому что авторизация уже пройдена
        return self.generation_tokens(email, None, is_refresh=True)
