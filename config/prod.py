"""
    Python file that contain a class with the configuration
    of the project
"""

class Config:
    """
        Config Class
    """
    # Flask Configs
    DEBUG = False
    ENV = 'production'

    # Secret Key For App
    SECRET_KEY = 'dz8fHrDhZjOCSKkFzESuoSIizZYIRMih4pqUMeT3RS>UjVEk(4'

    # SQLAlchemy Configs
    SQLALCHEMY_DATABASE_URI = 'mysql://softpymes:SoftPymes.2019@192.168.99.100/migration'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
