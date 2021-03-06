from marshmallow import fields
from .config.auditable_schema import AuditableBaseSchema
from .users import UserSchema
from .answers import AnswerSchema


class QuestionSchema(AuditableBaseSchema):
    """Question model schema class"""
    title = fields.Str()
    questioner = fields.Nested(UserSchema, only=["id", "username", "email"])
    answerer = fields.Nested(AnswerSchema, only=["id", "title"])
