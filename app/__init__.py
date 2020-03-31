from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import dotenv
import os
# globally accessible
db = SQLAlchemy()


def create_app():  # FACTORY!
    #dotenv.load_dotenv()
    #print(os.environ.get('DEBUG') == 'True')
    app = Flask(__name__)

    # dynamic configuration based on the FLASK_ENV system env variable

    # this function would load the env file in production as well,
    # when running flask run, it is done automatically
    # we don't need it as this is handled by docker compose
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
        from app.models import competition,player,team

    return app



