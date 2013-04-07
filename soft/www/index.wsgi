#!/usr/bin/env python
import sys

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import home_html
from sql_setup import dataBaseSQL
import global_data

def application (environ, start_response) :
  dataBase = dataBaseSQL (global_data.db_path)
  try :
    result = dataBase.get_data_sql ()
  except :
    result = [("---.----", "---.----", "--.--")]
    print("*** Error while connecting database to read data in 'index.wsgi'\n")
    raise
  response_body = home_html.format(result[0][0], result[0][1], result[0][2])

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
