# Import Flask class from flask module - will be main object
from flask import Flask
# Import SQL Alchemy and Migrate from their modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import the Config class from the config module - will have all the of the app's applications
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import all of the routes from the routes file in the current folder
from . import routes