#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#------------------------------------------------------------------------------
# SQL3 database operations
#------------------------------------------------------------------------------
class setupSQL () :
  """Setup a sqlite3 base"""
  def __init__(self) :
    pass

  def create_sql_bases (self, dbName) :
    try :
      conn = sqlite3.connect(dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while creating database in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("CREATE TABLE cmd (phase REAL, temperature REAL)")
      cur.execute("INSERT INTO cmd VALUES(0.0000, 21.00)")
      cur.execute("CREATE TABLE data (phase REAL, amplitute REAL, temperature REAL)")
      cur.execute("INSERT INTO data VALUES(0.0000, 0.0000, 0.00)")
      cur.execute("CREATE TABLE status (info TEXT, error TEXT)")
      cur.execute("INSERT INTO status VALUES('Up', 'No errors')")
      conn.commit()
      cur.close()
      conn.close()

  def get_cmd_sql (self, dbName) :
    try :
      conn = sqlite3.connect(dbName, timeout = 2)
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

  def set_data_sql (self, dbName, data) :
    try :
      conn = sqlite3.connect(dbName, timeout = 2)
    except sqlite3.OperationalError as e :
      print("*** Error while connecting database to write data in 'sql_setup.py' : {}\n".format(e))
      raise
    else :
      cur = conn.cursor()
      cur.execute("UPDATE data SET phase = ?, amplitute = ?, temperature = ?", data)
      conn.commit()
      cur.close()
      conn.close()

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ =="__main__" :
  setup_db = setupSQL ()
#  setup_db.create_sql_bases ("www/data_sql3.db")
  setup_db.set_data_sql ("www/data_sql3.db", (1.1111, 2.2222, 35.35))
  res = setup_db.get_cmd_sql ("www/data_sql3.db")
  print("res = {}".format(res))