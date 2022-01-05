from werkzeug.http import HTTP_STATUS_CODES
from flask import jsonify

def error_response(status_code,message=None):
  retresp = {'error': HTTP_STATUS_CODES.get(status_code,'Unknown Error') }
  if message :
    retresp['message'] = message
  response = jsonify(retresp)
  response.status_code = status_code
  return response

def bad_request(message):
  return error_response(400,message)