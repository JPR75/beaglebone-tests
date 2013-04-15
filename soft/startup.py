#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

import global_data
from sql_setup import dataBaseSQL

#------------------------------------------------------------------------------
# Stratup sequence
#------------------------------------------------------------------------------
class startup () :
  """Initialize the startup envirement"""
  def __init__(self, dataBase) :
    self.db = dataBase
    self.set_startup_data ()
    self.check_db ()

  def set_startup_data (self) :
    """Set the start time for uptime calculation
       Set the initial free RAM"""
    global_data.stratup_time = time.time()
    free_RAM = os.popen("free -m").readlines()[2].split()
    global_data.stratup_RAM  = int(free_RAM[3])

  def check_db (self) :
    """Create data base if does not exist"""
    if not os.path.isfile(self.db) :
      try :
        setup_db = dataBaseSQL (self.db)
        setup_db.create_sql_bases ()
      except :
        raise
