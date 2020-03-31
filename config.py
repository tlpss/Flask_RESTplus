import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''
    values should be specified in a .env file
    '''
    DEBUG = os.environ.get('DEBUG') == 'TRUE' or os.environ.get('DEBUG') == 'True'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "sqlite:///" + os.path.join(basedir,'app.db')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mlkqjsd5mfoiqjsdmlfkè4jqsdaqzàemlkifr)1nlodfmouut'