from flask import Flask,Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


api_url_prefix = "/"
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)


# article_bp = Blueprint(
#   'article',
#   __name__,
#   static_folder = 'statics',
#   template_folder = 'template',
#   url_prefix=api_url_prefix
# )

# app.register_blueprint(article_bp)




from mainapp import models
from mainapp import article