from marshmallow import fields
from .config.auditable_schema import AuditableBaseSchema

class UserSchema(AuditableBaseSchema):
    """there should be a comment here"""
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
