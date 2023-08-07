import os

from flask import Flask, jsonify

from . import auth, db
from .utils.exceptions import InvalidTypeException, MissingKeyException


def create_app(test_config=None):

    # creating a instance of Flask app
    # instance_relative_config true means that the config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # config app
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "billing.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config passed in
        app.config.from_mapping(test_config)

    try:
        # ensure the instance folder exists
        # os.makedirs() creates a folder
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # call db.init_app() from within the function
    db.init_app(app)

    @app.errorhandler(InvalidTypeException)
    def handle_invalid_type_exception(e):
        return jsonify(error="Invalid Type", description=e.args), 400

    @app.errorhandler(MissingKeyException)
    def handle_missing_key(e):
        return jsonify(error="Missing key", description=e.args), 400

    @app.errorhandler(Exception)
    def handle_exception(e):
        print(e)
        return "Error", 500

    # register the auth blueprint
    app.register_blueprint(auth.bp)

    return app
