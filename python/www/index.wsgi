#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import os
import sys
import platform
import datetime

sys.path.insert(0, '/home/ubuntu/dev/www/template.py')
sys.path.insert(1, '/home/ubuntu/dev/www/')
from templates import info_html, home_html

class Application (object) :
  def __init__ (self, environ, start_response) :
    self.environ = environ
    self.start = start_response
    print("->1")

  def www_homeWindow (self) :
    print("->4")
    response_body = home_html
    return response_body

  def www_not_found(self):
    print("->5")
    return 'Not found'

def application (environ, start_response) :
  print("->0")
  app = Application (environ, start_response)
  response_body = app.www_homeWindow ()
  print(response_body)
  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
