from .config.database import db
from .config.auditable_model import AuditableBaseModel


class Answer(AuditableBaseModel):
    """Class Answer model"""
    __tablename__ = 'answers'

    title = db.Column(db.String(), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
    children = db.relationship(
        'Answer',
        lazy=True,
        backref=db.backref('parent', remote_side='Answer.id', lazy='joined')
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('questions.id'),
        nullable=False
    )
