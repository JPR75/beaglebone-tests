#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
import sys
import re

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import cmd_html
from sql_setup import dataBaseSQL
import global_data

def application (environ, start_response) :
  dataBase = dataBaseSQL (global_data.db_path)
  value = ""
  delta = ""
  if environ['REQUEST_METHOD'] == "GET" :
    user_input = parse_qs(environ['QUERY_STRING'])
    delta = user_input.get('delta', [''])[0]
    delta = escape(delta)
    if not re.match(r'^[0-9]\d*(\.\d+)?$', delta) :
      delta = "Error"
    else :
      if (float(delta) < 0.0) or (float(delta) > 360.0) :
        delta = "Phase should be > 0.000 and < 360.000"
      else :
        value = delta
        try :
          dataBase.set_cmd_sql ((float(delta), 32.00))
        except :
          delta = "Data base access error"
  response_body = cmd_html.format(delta, value)

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]

