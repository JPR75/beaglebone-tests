#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import sys
import platform
import subprocess as sub
from cgi import parse_qs, escape

sys.path.insert(0, '/home/ubuntu/ramdisk/soft/www/template.py')
sys.path.insert(1, '/home/ubuntu/ramdisk/soft/www/')
sys.path.append('/home/ubuntu/ramdisk/soft/')

from templates import admin_html
import global_data

def application (environ, start_response) :
#  os.system("echo 1 > /sys/class/leds/beaglebone::usr3/brightness")
  value = open("/sys/class/leds/beaglebone::usr3/brightness",'w')
  value.write(str(1))
  value.close()

  if environ['REQUEST_METHOD'] == "GET" :
    user_input = parse_qs(environ['QUERY_STRING'])
    admin_pwd = user_input.get('pwd', [''])[0]
    admin_pwd = (escape(admin_pwd)).encode('utf-8')
    admin_pwd = hashlib.md5(admin_pwd).hexdigest()
    admin_action = user_input.get('admin_action', [''])
    admin_action = [escape(action) for action in admin_action]
    if admin_pwd == global_data.admin_pwd :
      admin_pwd = "OK"
      if admin_action[0] == "reboot" :
        os.system("reboot")
      elif admin_action[0] == "shut_down" :
        os.system("shutdown -P now")
    else :
      admin_pwd = "NOK"

  free_RAM = os.popen("free -m").readlines()[2].split()
  p = sub.Popen('whoami',stdout=sub.PIPE,stderr=sub.PIPE)
  output, errors = p.communicate()
#  response_body = admin_html.format(global_data.firmware_version, global_data.software_version, free_RAM[3], platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version(), output)
  response_body = admin_html.format(global_data.firmware_version, global_data.software_version, free_RAM[3], platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version(), output, admin_pwd, admin_action[0])

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
