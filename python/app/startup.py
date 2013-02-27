#! /usr/bin/env python

import os

#------------------------------------------------------------------------------
# Stratup sequence
#------------------------------------------------------------------------------
class startup (object) :
  """Initialize the startup envirement"""
  def __init__(self) :
    pass

  def create_data_file (self) :
    """Create the file containing the data"""
    try :
      dataFile = open("data_log.txt", "w")
    except IOError as e :
      print("*** Error while creating data log file : {}\n".format(e))
      raise
    else :
      dataFile.write("000.0000\n0000.0000\n21.0")
      dataFile.close()

  def create_cmd_file (self) :
    """Create the file containing the commands"""
    try :
      cmdFile = open("cmd_log.txt", "w")
    except IOError as e :
      print("*** Error while creating cmd log file : {}\n".format(e))
      raise
    else :
      cmdFile.write("000.0000\n000.0000")
      cmdFile.close()

