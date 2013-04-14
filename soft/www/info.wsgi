#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import info_html
import global_data

def application (environ, start_response) :
  response_body = info_html.format(global_data.firmware_version, global_data.software_version)

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
