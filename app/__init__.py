from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api

# globally accessible
db = SQLAlchemy()
api = Api()

def create_app(): # FACTORY!
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # initialize plugins
    db.init_app(app)
   # api.init_app(app)

    migrate = Migrate(app,db)

    with app.app_context():
        #include the routes, models
        from app.routes import hello_world
        #from app.models import


    return app



