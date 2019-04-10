# -*- coding: utf-8 -*-
"""
    File that contains the initial setup of the application
"""

# Import from flask
from flask import Flask

# SQL Alchemy
from flask_sqlalchemy import SQLAlchemy

# Flask Migrate
from flask_migrate import Migrate

# Config of the Application
from config import Config


def config_app():
    # import blueprints
    from application.endpoints import api as api_blueprint

    # register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api/v1' )



# Instance of the APP
app = Flask(__name__)

# Config APP
app.config.from_object(Config)

config_app()

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import models
