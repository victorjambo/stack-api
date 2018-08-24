from flask_restplus import Resource
from flask import jsonify, request
from main import api
from api.utilities.messages import SUCCESS_MESSAGES
from api.models import User
from api.model_serializers import UserSchema
from api.utilities.generate_token import generate_token
from passlib.hash import sha256_crypt
from api.middlewares.token_required import token_required


@api.route('/auth/register')
class AuthRegisterResource(Resource):
    def post(self):
        """Register user"""
        request_data = request.get_json()

        user_schema = UserSchema(
            only=["id", "username", "email", "password", "created_at", "updated_at"])
        user_data = user_schema.load_object_into_schema(request_data)
        user_data["password"] = sha256_crypt.encrypt(str(user_data["password"]))
        user = User(**user_data)
        user.save()

        return jsonify({
            "data": user_schema.dump(user).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["created"].format("User")
        })


@api.route('/auth/login')
class AuthLoginResource(Resource):
    def post(self):
        """Login user"""
        request_data = request.authorization

        user_schema = UserSchema(only=["username", "password"])
        user_data = user_schema.load_object_into_schema(request_data)

        user = User.query_(user_data)

        token = generate_token(user, user_data)

        return jsonify({
            "token": token,
            "status": "success",
            "message": SUCCESS_MESSAGES["login"]
        })


@api.route('/auth/update')
class AuthUpdateResource(Resource):
    @token_required
    def put(self, args):
        """Update username or password"""
        request_data = request.get_json()

        user = User.get_or_404(self)

        user_schema = UserSchema(only=["username", "password"])
        user_data = user_schema.load_object_into_schema(request_data)
        user_data["password"] = sha256_crypt.encrypt(str(user_data["password"]))

        user = user.update(user_data)
        user.save()

        return jsonify({
            "data": user_schema.dump(user).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["updated"].format("User")
        })
