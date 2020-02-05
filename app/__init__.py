from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_environments import Environments
import os
# globally accessible
db = SQLAlchemy()


def create_app():  # FACTORY!
    app = Flask(__name__)

    # dynamic configuration based on the FLASK_ENV system env variable
    env = Environments(app)
    env.from_object('config') # replaces the traditional flask config.from_object() and dynamically selects a subclass
    print( f"env = {os.environ.get('FLASK_ENV')}")

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
        from app.models import competition,player,team

    return app



