import jwt
import os
from .base_validator import ValidationError
from functools import wraps
from flask import jsonify, request
from api.utilities.messages import jwt_errors


def token_required(f):
    """Ensures user is logged in before action
    Checks of token is provided in header
    decodes the token then returns current user info
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = request.headers['Authorization']

        if not token:
            raise ValidationError({'message': jwt_errors['NO_TOKEN_MSG']}, 401)

        try:
            public_key = os.getenv("SECRET")
            decoded_token = jwt.decode(token, public_key)
            current_user = decoded_token["id"]
        except jwt.ExpiredSignatureError:
            return jsonify({'message': jwt_errors['EXPIRED_TOKEN_MSG']}), 401
        except ValueError:
            return jsonify({'message': jwt_errors['SERVER_ERROR_MESSAGE']}), 401

        setattr(request, 'decoded_token', decoded_token)
        return f(current_user, *args, **kwargs)
    return wrap
