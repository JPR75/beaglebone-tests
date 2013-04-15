#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')

from templates import info_html

def application (environ, start_response) :
  response_body = info_html

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
