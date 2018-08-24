from os import getenv
from flask import jsonify
from main import create_app
from config import config


config_name = getenv('FLASK_ENV', default='development')
app = create_app(config[config_name])


@app.route('/')
def index():
    return jsonify(dict(message='Welcome to the Stack Overflow API'))


if __name__ == '__main__':
    app.run()
