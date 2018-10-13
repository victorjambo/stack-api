from .config.database import db
from .config.auditable_model import AuditableBaseModel

class User(AuditableBaseModel):
    """Class User model"""
    __tablename__ = 'users'

    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    history = db.relationship('History', backref='history')

    questions = db.relationship(
        'Question',
        backref='questioner',
        cascade='all, delete-orphan'
    )
    answers = db.relationship(
        'Answer',
        backref='answerer',
        cascade='all, delete-orphan'
    )
