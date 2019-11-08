from flask import Flask
from flasgger import Swagger


def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    flask_app = Flask(__name__)
    swagger = Swagger(flask_app)
    flask_app.config.from_object(config_object)

    return flask_app