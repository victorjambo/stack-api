from .config.database import db
from .config.auditable_model import AuditableBaseModel


class Answer(AuditableBaseModel):
    __tablename__ = 'answers'

    title = db.Column(db.String(), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('questions.id'),
        nullable=False
    )
