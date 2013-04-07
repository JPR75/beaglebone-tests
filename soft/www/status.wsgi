#!/usr/bin/env python
import sys

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import status_html

def application (environ, start_response) :
  dataBase = dataBaseSQL (global_data.db_path)
  try :
    status_icon = '<img class="centred" src="img/ok-icon.png" alt="OK" height="64" width="64" />'
    result = dataBase.get_status_sql ()
  except :
    status_icon = '<img class="centred" src="img/Erreur-icon.png" alt="Error" height="64" width="64" />'
    result = [("System down", "Data base error")]
    print("*** Error while connecting database to read data in 'data.wsgi'\n")
    raise
  response_body = setup_html.format(status_icon, result[0][0], result[0][1])

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
