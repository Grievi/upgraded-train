from config import DevConfig
from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# bootstrap = bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #initializing application
    app = Flask(__name__ ,instance_relative_config=True)
    
    #Setting up configurations
    app.config.from_object(DevConfig)
    app.config.from_pyfile(config.py)

    #initializing flask extensions
    # bootstrap.init_app(app)
    db.init_app(app)


# from app import views