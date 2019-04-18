"""
    Python file that contain a class with the configuration
    of the project
"""
import os

class Config:
    """
        Config Class
    """
    # Flask Configs
    DEBUG = True
    ENV = 'development'
    
    # Secret Key For App
    SECRET_KEY = 'dz8fHrDhZjOCSKkFzESuoSIizZYIRMih4pqUMeT3RS>UjVEk(4'

    # SQLAlchemy Configs
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
        os.environ['MYSQL_USER'],
        os.environ['MYSQL_PASSWORD'],
        os.environ['MYSQL_HOST'],
        os.environ['MYSQL_PORT'],
        os.environ['MYSQL_DATABASE']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

