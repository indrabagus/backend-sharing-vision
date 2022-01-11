from flask import Flask,Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .api import create_module as create_api


api_url_prefix = "/"
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
create_api(app)

from mainapp import models
