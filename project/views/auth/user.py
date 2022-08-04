from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.dao.models import UserSchema
from project.helpers.decorators import access_user

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @access_user
    def get(self, uid):
        user = user_service.get(uid)
        return UserSchema().dump(user), 200

    @access_user
    def patch(self, uid):
        data = request.json
        data['id'] = uid
        user_service.partial_update(data)
        return '', 204


@user_ns.route('/password')
class UserPasswordView(Resource):
    @access_user
    def put(self, uid):
        data = request.json
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')
        data['id'] = uid

        # Проверяем, что передан старый пароль password_1 и новый password_2
        if None in (password_1, password_2):
            return 'Не все поля заполнены', 400

        user_service.password_update(uid, password_1, password_2)
        return '', 204
