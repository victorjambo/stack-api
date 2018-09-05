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
serialization_errors = {  #pylint: disable=C0103
    'url_syntax':
    '{0} is not a valid url',
    'email_syntax':
    '{0} is not a valid email address',
    'email_exists':
    '{0} is already registered',
    'email_length':
    'Email must be at least 6 characters',
    'field_required':
    'This field is required',
    'field_length':
    'Field must be at least {0} characters',
    'json_invalid':
    'Invalid JSON input provided',
    'string_characters':
    'Field must start and end with a letter, only contain letters, non-consecutive fullstops, hyphens, spaces and apostrophes',  #pylint: disable=C0301
    'string_length':
    'Field must be {0} characters or less',
    'input_control':
    'Incorrect input control type provided, please provide one of {input_controls}',  #pylint: disable=C0301
    'choices_required':
    'choices seperated by comma must be provided if multi choice inputs controls are selected',  #pylint: disable=C0301
    'provide_attributes':
    'Please provide at least one attribute',
    'attribute_required':
    'The attribute {} is required',
    'unrelated_attribute':
    'The attribute {} is not related to this asset category',
    'invalid_category_id':
    'This asset category id is invalid',
    'invalid_center_id':
    'This center id is invalid',
    'category_not_found':
    'This category does not exist in the database',
    'center_not_found':
    'This center does not exist in the database',
    'attribute_not_related':
    'attribute with the id of {attribute_id} is not related to the asset category of id {asset_category_id}',  #pylint: disable=C0301
    'invalid_id':
    'Invalid id in parameter',
    'key_error':
    '{} key not found',
    'choices_type':
    'Choices must be an Array',
    'invalid_field':
    'invalid field supplied',
    'invalid_query_strings':
    '{0} contains invalid parameter {1}',
    'json_type_required':
    'Content-Type should be application/json',
    'duplicate_asset':
    'Asset with the tag {} already exists',
    'asset_category_assets':
    'Assets for category {} fetched successfully',
    'exists':
    '{} already exists',
    'person_not_found':
    'Person not found',
    'last_page_returned':
    'The requested page exceeds the total pages count, however the last page was returned',
    'not_found':
    '{} not found',
    'center_not_found':
    'Center not found',
    'invalid_choice':
    'The value of attribute {} must one of these options: {}'
}
