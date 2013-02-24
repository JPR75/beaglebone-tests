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

  def www_infoWindow (self):
    platform_info = ("Processor :  {} ; {}<br />OS            : {}<br />Vesrion    : {}<br />Python     : {}").format(platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version())
    response_body = info_html.format(platform_info)
    return response_body

def application (environ, start_response) :
  app = Application (environ, start_response)
  response_body = app.www_infoWindow ()
  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
