import jwt
from flask import request, abort

from project.constants import JWT_SECRET, JWT_ALGO
from project.container import user_service


def access_user(func):
    """
    определяет доступ пользователя к профилю (возвращает uid по токену)
    """
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            print('JWT decode Exception', e)
            abort(401)

        email = data['email']
        user = user_service.get_by_email(email)
        uid = user.id

        return func(uid=uid, *args, **kwargs)
    return wrapper
