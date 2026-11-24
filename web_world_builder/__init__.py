from web_world_builder.sqlite_db_manager import init_db, db_session
from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    app.config.from_pyfile('config.py', silent=True)

    os.makedirs(app.instance_path, exist_ok=True)

    from .routes import generator
    app.register_blueprint(generator.bp)
    app.add_url_rule('/', endpoint='index')

    init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
