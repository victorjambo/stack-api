"""Module for validating duplicate data"""
import re

from api.middlewares.base_validator import ValidationError
from api.utilities.messages.error_messages import serialization_errors


def validate_duplicate(model, **kwargs):
    """
    Checks if model instance already exists in database

    Parameters:
         model(object): model to run validation on
         kwargs(dict): keyword arguments containing fields to filter query by
    """

    record_id = kwargs.get('id')
    kwargs.pop('id', None)  # remove id from kwargs if found or return None

    query = dict(deleted=False, **kwargs)
    if record_id:
        result = model.query.filter_by(**query).filter(
            model.id == record_id).first(
            )  # selects the first query object for model records

        if result:
            return None  # return None if query object is found

    result = model.query.filter_by(**query).first()
    if result:
        raise ValidationError({
            'message':
            serialization_errors['exists'].format(
                f'{re.sub(r"(?<=[a-z])[A-Z]+",lambda x: f" {x.group(0).lower()}" , model.__name__)}'
            )
        }, 409)
