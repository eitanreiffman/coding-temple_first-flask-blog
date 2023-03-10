from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login.login_view = 'log_in'
login.login_message = 'You must be logged in to perform this action'
login.login_message_category = 'danger'

from app.blueprints.api import api
app.register_blueprint(api)

# import all of the routes from the routes file in the current folder
from . import routes, models