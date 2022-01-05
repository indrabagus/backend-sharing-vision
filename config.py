import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY") or "this-is-my-top-secret-key"
  # SQL ALCHEMY Stuff
  SQLALCHEMY_DATABASE_URI = os.environ.get("SECRET_KEY") or 'mysql://sharingvision:SharingVision@localhost/CDatabase'
  SQLALCHEMY_TRACK_MODIFICATIONS = False




