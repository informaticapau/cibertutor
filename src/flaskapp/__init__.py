import os
from flask import Flask
from .utils.db import db


def create_app(test_config: dict = None) -> Flask:
    # create and configure the app
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskapp.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Flask-SQLAlchemy configuration
    db_path: str = os.path.join(app.instance_path, 'flaskapp.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Blueprints
    from .blueprints import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='home.index')

    # CLI
    from .utils import db_cli
    app.cli.add_command(db_cli)

    with app.app_context():
        if os.getenv('FLASK_DB_INIT') == 'True':
            db.create_all()
        return app
