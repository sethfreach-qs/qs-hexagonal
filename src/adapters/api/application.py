from flask import Flask
from flask_cors import CORS

from src.main.containers import Container
from .blueprints.api import blueprint


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)
    CORS(app)
    app.container = container
    app.register_blueprint(blueprint)
    return app
