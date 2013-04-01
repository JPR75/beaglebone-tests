#!/usr/bin/env python

#from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import sys
import re

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import cmd_html
from sql_setup import dataBaseSQL
import global_data

class Application (object) :
  def __init__ (self, environ, start_response) :
    self.environ = environ
    self.start = start_response
    self.dataBase = dataBaseSQL (global_data.db_path)

  def www_cmdWindow (self) :
    if self.environ['REQUEST_METHOD'] == "GET" :
      user_input = parse_qs(self.environ['QUERY_STRING'])
      delta = user_input.get('delta', [''])[0]
      delta = escape(delta)
      if not re.match(r'^[0-9]\d*(\.\d+)?$', delta) :
        delta = "Error"
      else :
        try :
          self.dataBase.set_cmd_sql ((float(delta), 32.00))
        except :
          delta = "Error"
          print("*** Error while connecting database to write data in 'cmd.wsgi'\n")
    response_body = cmd_html.format(delta or "Empty")
    return response_body

def application (environ, start_response) :
  app = Application (environ, start_response)
  response_body = app.www_cmdWindow ()
  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]


#if __name__ == '__main__' :
#  from wsgiref.simple_server import make_server
#  srv = make_server('localhost', 8080, application)
#  try :
#    srv.serve_forever()
#  except KeyboardInterrupt :
#    pass

