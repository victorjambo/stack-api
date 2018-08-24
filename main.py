from os import getenv
from flask_restplus import Api
from flask import Flask, jsonify
from flask_cors import CORS
from api import api_blueprint
from config import config
from api.models.config.database import db
from flask_migrate import Migrate


config_name = getenv('FLASK_ENV', default='development')
api = Api(api_blueprint)


def initialize_app(application):
    ''' Initialize error handlers '''
    application.register_blueprint(api_blueprint)


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    # initialize error handlers
    initialize_app(app)

    # bind app to db
    db.init_app(app)

    # import all models
    from api.models import User, Question, Answer

    # import views
    import api.views

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app
