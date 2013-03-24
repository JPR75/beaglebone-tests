#!/usr/bin/env python

#from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import sys
import re

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import info_html, home_html
from sql_setup import dataBaseSQL
import global_data

class Application (object) :
  def __init__ (self, environ, start_response) :
    self.environ = environ
    self.start = start_response
    self.dataBase = dataBaseSQL (global_data.db_path)

  def www_homeWindow (self) :
    try :
      result = self.dataBase.get_data_sql ()
    except :
      result = [("---.----", "---.----", "--.--")]
      print("*** Error while connecting database to write cmd in 'index.wsgi'\n")
      raise
    if self.environ['REQUEST_METHOD'] == "GET" :
      user_input = parse_qs(self.environ['QUERY_STRING'])
      delta = user_input.get('delta', [''])[0]
      delta = escape(delta)
      if not re.match(r'^[0-9]\d*(\.\d+)?$', delta) :
        delta = "Error"
      else :
        self.dataBase.set_cmd_sql ((float(delta), 32.00))
    response_body = home_html.format(result[0][0], result[0][1], result[0][2], delta or "Empty")
    return response_body

  def write_cmd_file (self) :
    """Write the file containing the commands"""
    try :
      cmdFile = open("cmd_log.txt", "w")
    except IOError as e :
      print("*** Error while creating cmd log file : {}\n".format(e))
      raise
    else :
      cmdFile.write("000.0000\n000.0000")
      cmdFile.close()

def application (environ, start_response) :
  app = Application (environ, start_response)
  response_body = app.www_homeWindow ()
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

