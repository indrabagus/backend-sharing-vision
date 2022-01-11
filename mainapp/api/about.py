from flask import Blueprint, json,jsonify,request,url_for
from mainapp import app,db,api_url_prefix
from mainapp.errors import bad_request

about_bp = Blueprint(
  'about',
  __name__,
  static_folder = 'statics',
  template_folder = 'template',
  url_prefix=api_url_prefix+'about'
)

@about_bp.route('/',methods=['GET'])
def index():
    return jsonify({'about':"This is about message"})