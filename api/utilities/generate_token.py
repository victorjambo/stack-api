import jwt
import os
import datetime
from .constants import CHARSET
from passlib.hash import sha256_crypt
from api.middlewares.base_validator import ValidationError
from .messages import ERROR_MESSAGES


def generate_token(user, user_data):
    password = user.password
    candidate_password = user_data['password']

    if sha256_crypt.verify(candidate_password, password):
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token = jwt.encode(
            {
                'id': user.id,
                'username': user.username,
                'exp': exp_time
            }, os.getenv("SECRET")
        )
        return token.decode(CHARSET)
    else:
      error = ValidationError({'message': ERROR_MESSAGES['AUTH_ERROR']}, 401)
      return error.to_dict()
