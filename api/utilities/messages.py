SUCCESS_MESSAGES = {
    'created': '{} successfully created',
    'fetched': '{} fetched successfully',
    'deleted': '{} successfully deleted',
    'updated': '{} successfully updated',
    'register': '{} successfully registered',
    'reset_password': 'Reset Password Success',
    'login': 'Login Success',
}

ERROR_MESSAGES = {
    'AUTH_ERROR': 'Authentication Error. Wrong username or password'
}

jwt_errors = {
    'INVALID_TOKEN_MSG':
    "Authorization failed due to an Invalid token.",
    'EXPIRED_TOKEN_MSG':
    "Token expired. Please login to get a new token",
    'SIGNATURE_ERROR':
    "Cannot verify the signature of the token provided as\
    it was signed by a non matching private key",
    'SERVER_ERROR_MESSAGE':
    "Authorization failed. Please contact support.",
    'NO_BEARER_MSG':
    "Bad request. The token should begin with the word\
    'Bearer'.",
    'NO_TOKEN_MSG':
    "Bad request. Header does not contain an authorization\
 token."
}
