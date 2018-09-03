from .config.database import db
from .config.auditable_model import AuditableBaseModel


class Question(AuditableBaseModel):
    """Class Question model"""
    __tablename__ = 'questions'

    title = db.Column(db.String(), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answers = db.relationship(
        'Answer',
        backref='answer',
        cascade='all, delete-orphan'
    )
