from marshmallow import fields
from .config.auditable_schema import AuditableBaseSchema
from .users import UserSchema


class AnswerSchema(AuditableBaseSchema):
    title = fields.Str()
    answerer = fields.Nested(UserSchema, only=["id", "username", "email"])

