from marshmallow import fields
from .config.auditable_schema import AuditableBaseSchema

class UserSchema(AuditableBaseSchema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
