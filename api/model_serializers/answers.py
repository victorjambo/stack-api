from marshmallow import fields
from .config.auditable_schema import AuditableBaseSchema
from .users import UserSchema


class AnswerSchema(AuditableBaseSchema):
    """there should be a comment here"""
    title = fields.Str()
    parent = fields.Int(dump_only=True)
    children = fields.Nested('self', many=True)
    answerer = fields.Nested(UserSchema, only=["id", "username", "email"])
