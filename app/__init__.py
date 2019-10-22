from flask import Flask
from flask_bootstrap import Bootstrap
from config  import config_options
from flask_sqlalchemy import SQLAlchemy



bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)


    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extentions
    bootstrap.init_app(app)
    db.init_app(app)

    return app