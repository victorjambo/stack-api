from .config.database import db
from .config.auditable_model import AuditableBaseModel
from api.utilities.enums import Action


class History(AuditableBaseModel):
    """Class History model track activities"""
    __tablename__ = 'history'

    action = db.Column(db.Enum(Action))
    activity = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
