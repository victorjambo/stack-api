from flask_restplus import Resource
from flask import jsonify, request
from main import api
from api.utilities.messages import SUCCESS_MESSAGES
from api.models import User
from api.model_serializers import UserSchema


@api.route('/users')
class UserResource(Resource):
    def get(self):
        """List all users"""
        users = User.query.all()
        users_schema = UserSchema(many=True, only=("id", "username", "email"))
        return jsonify({
            "data": users_schema.dump(users).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("Users")
        })

    def post(self):
        """Register user"""
        request_data = request.get_json()

        user_schema = UserSchema(only=["id", "username", "email", "password", "created_at", "updated_at"])
        user_data = user_schema.load_object_into_schema(request_data)
        user = User(**user_data)
        user.save()

        return jsonify({
            "data": user_schema.dump(user).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["created"].format("User")
        })


@api.route('/users/<string:user_id>')
class SingleUserResource(Resource):
    def get(self, user_id):
        """get single user"""
        user = User.get_or_404(user_id)
        users_schema = UserSchema(only=("id", "username", "email", "password"))

        return jsonify({
            "data": users_schema.dump_object_into_schema(user),
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("User")
        })

    def put(self, user_id):
        """Update username or password"""
        request_data = request.get_json()

        user = User.get_or_404(user_id)

        user_schema = UserSchema(only=["username", "password"])
        user_data = user_schema.load_object_into_schema(request_data)

        user = user.update(user_data)
        user.save()

        return jsonify({
            "data": user_schema.dump(user).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["updated"].format("User")
        })

    def delete(self, user_id):
        """delete user"""

        user = User.get_or_404(user_id)
        user.delete()

        return jsonify({
            "status": "success",
            "message": SUCCESS_MESSAGES["deleted"].format("User")
        })
