#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import status_html

def application (environ, start_response) :
  dataBase = dataBaseSQL (global_data.db_path)
  status_icon = 'error.png'
  try :
    result = dataBase.get_status_sql ()
    if result[0][2] == 1 :
      status_icon = 'ok.png'
    elif result[0][2] == 2 :
      status_icon = 'warning.png'
  except :
    result = [("System down", "Data base error", 0)]
  response_body = setup_html.format(status_icon, result[0][0], result[0][1])

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
