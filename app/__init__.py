from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# globally accessible
db = SQLAlchemy()


def create_app():  # FACTORY!
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # initialize plugins
    db.init_app(app)

    from app.routes import api # do it here to avoid circular dependency with db
    api.init_app(app)

    migrate = Migrate(app,db)

    with app.app_context():
        # include the routes, models
        # importing routes not required as this is done in the REST API object,
        # for standard flask applications this should be done here

        # from app.routes import hello_world
        from app.models import competition,player,team

    return app



