#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import datetime
import subprocess as sub

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')

from templates import admin_html

def application (environ, start_response) :
#  os.system("echo 1 > /sys/class/leds/beaglebone::usr3/brightness")
  value = open("/sys/class/leds/beaglebone::usr3/brightness",'w')
  value.write(str(1))
  value.close()

  p = sub.Popen('whoami',stdout=sub.PIPE,stderr=sub.PIPE)
  output, errors = p.communicate()
  response_body = admin_html.format(platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version(), output)

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
