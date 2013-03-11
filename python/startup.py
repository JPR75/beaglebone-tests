#! /usr/bin/env python
# -*- coding:Utf8 -*-

import os

from sql_setup import setupSQL

#------------------------------------------------------------------------------
# Stratup sequence
#------------------------------------------------------------------------------
class startup () :
  """Initialize the startup envirement"""
  def __init__(self, dataBase) :
    self.db = dataBase
    self.check_db ()

  def check_db (self) :
    """Create data base if does not exist"""
    if not os.path.isfile(self.db) :
      try :
        setup_db = setupSQL ()
        setup_db.create_sql_bases (self.db)
      except :
        raise
