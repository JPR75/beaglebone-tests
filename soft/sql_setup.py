#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3

#------------------------------------------------------------------------------
# SQL3 database operations
#------------------------------------------------------------------------------
class dataBaseSQL () :
  """Setup a sqlite3 base"""
  def __init__(self, dbName) :
    self.dbName = dbName

  def create_sql_bases (self) :
    """
      Create a sqlite3 base
      state : 0 = error
               1 = ok
               2 = warning
    """
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while creating database in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("CREATE TABLE cmd (phase REAL, temperature REAL)")
      cur.execute("INSERT INTO cmd VALUES(0.0000, 21.00)")

      cur.execute("CREATE TABLE data (phase REAL, amplitute REAL, temperature REAL)")
      cur.execute("INSERT INTO data VALUES(0.0000, 0.0000, 0.00)")

      cur.execute("CREATE TABLE status (info TEXT, error TEXT, state INTEGER)")
      cur.execute("INSERT INTO status VALUES('System up and running', 'No error', 1)")

      conn.commit()
      cur.close()
      conn.close()

      try :
        os.system("chmod a+rw {}".format(self.dbName))
      except sqlite3.OperationalError as e :
        print("*** Error chmod in 'sql_setup.py' : {}\n".format(e))
        raise

  def get_cmd_sql (self) :
    """Get cmd from data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to read cmd in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("SELECT * FROM cmd")
      result = cur.fetchall()
      cur.close()
      conn.close()
      return result

  def get_data_sql (self) :
    """Get data from data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to read data in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("SELECT * FROM data")
      result = cur.fetchall()
      cur.close()
      conn.close()
      return result

  def get_status_sql (self) :
    """Get status from data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to read data in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("SELECT * FROM status")
      result = cur.fetchall()
      cur.close()
      conn.close()
      return result

  def set_cmd_sql (self, data) :
    """Change cmd in data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to write cmd in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("UPDATE cmd SET phase = ?, temperature = ?", data)
      conn.commit()
      cur.close()
      conn.close()

  def set_data_sql (self, data) :
    """Change data in data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to write data in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("UPDATE data SET phase = ?, amplitute = ?, temperature = ?", data)
      conn.commit()
      cur.close()
      conn.close()

  def set_status_sql (self, data) :
    """Change status in data base"""
    try :
      conn = sqlite3.connect(self.dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to write data in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("UPDATE status SET info = ?, error = ?, state = ?", data)
      conn.commit()
      cur.close()
      conn.close()

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ =="__main__" :
  setup_db = setupSQL ()
  setup_db.create_sql_bases ("www/data_sql3.db")
