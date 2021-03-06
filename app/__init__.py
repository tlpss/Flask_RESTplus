from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# FLASK RESTPLUS ISSUE
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import os
# globally accessible
db = SQLAlchemy()


def create_app():  # FACTORY!
    app = Flask(__name__)

    # dynamic configuration based on the FLASK_ENV system env variable

    # this function would load the env file in production as well,
    # when running flask run, it is done automatically
    # we don't need it as this is handled by docker compose
    #dotenv.load_dotenv()

    app.config.from_object('config.Config')


    # initialize plugins
    db.init_app(app)

    from app.routes import api # do it here to avoid circular dependency with db
    api.init_app(app) # api is the flask-restplus instance

    migrate = Migrate(app,db)

    with app.app_context():
        # include the routes, models
        # importing routes not required as this is done in the RESTFUL API object,
        # for standard flask applications this should be done here

        # from app.routes import hello_world
        from app.models import Competition, Team, Player

    return app



