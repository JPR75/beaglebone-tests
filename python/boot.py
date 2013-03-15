#! /usr/bin/env python
# -*- coding:Utf8 -*-

from tkinter import *
import os
import platform
#import threading
import datetime
import time

import global_data
from startup import startup
from sql_setup import dataBaseSQL

#------------------------------------------------------------------------------
# Info window class
#------------------------------------------------------------------------------
class infoWindow (Canvas) :
  """Info window"""
  def __init__(self, mainCanevas) :
    # System info
    self.sysinfo = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.sysinfo.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = N)
    self.show_sys_info ()
    self.show_sys_RAM ()
    self.show_sys_date ()
    # Dev info
    self.devinfo = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.devinfo.grid(row = 1, column = 1, padx = 5, pady = 0, sticky = N)
    self.show_dev_info ()

  def show_sys_info (self) :
    """Show system info"""
    platform_info = ("Processor :  {} ; {}\nOS            : {}\nVesrion    : {}\nPython     : {}").format(platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version())
    Label(self.sysinfo, text = platform_info, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_RAM (self):
    """Show RAM info"""
    RAMmemory = os.popen("free -m").readlines()[1].split()
#    RAMmemory = ["xxx","xxx","xxx","xxx"]
    memory = ("Memory => total : {}  MB ; used : {} MB ; free : {} MB").format(RAMmemory[1], RAMmemory[2], RAMmemory[3])
    Label(self.sysinfo, text = memory, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_date (self):
    """Show date and time"""
    now = datetime.datetime.now()
    current_date_time = ("Sys date : {}-{}-{} ; {}h {}mm {}s").format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    Label(self.sysinfo, text = current_date_time, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_dev_info (self) :
    """Show developpement info"""
    dev_info = ("Firmware : v1.0.0\nSoftware  : v1.0.0\n\nContact    :\n\nJean-Paul Ricaud\n\nSynchrotron SOLEIL\nL'Orme des Merisiers\nSaint-Aubin - BP 48\nFrance\n\njean-paul.ricaud@synchrotron-soleil.fr")
    Label(self.devinfo, text = dev_info, font = ("DejaVu\ Sans\ Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 10, anchor = W)

#------------------------------------------------------------------------------
# Home window class
#------------------------------------------------------------------------------
class homeWindow (Canvas) :
  """Home page window"""
  def __init__(self, mainCanevas, dataBase) :
    self.data = "hour : 00.00 \nminute : 00.00 \nsecond : 0.00"
    self.dataBase = dataBase
    self.homePage = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.homePage.grid(row = 1, column = 0, padx = 5, pady = 0)
    self.showMessage = Label(self.homePage, text = self.data, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT)
    self.showMessage.pack(padx = 20, pady = 5, anchor = W)
    self.update_home_page ()

  def update_home_page (self) :
    """Home page update"""
    now = datetime.datetime.now()
    self.data =  "hour : {}\nminute : {}\nsecond : {}".format(now.hour, now.minute, now.second)
    self.showMessage.configure(text = self.data)
    # Get data
    # ---
    # Push to data base
    try :
      self.dataBase.set_data_sql ((float(now.hour), float(now.minute), float(now.second)))
    except :
      print("*** Error while connecting database to write cmd in 'boot.py'\n")
    self.homePage.after(500, self.update_home_page)

#------------------------------------------------------------------------------
# Main canvas class
#------------------------------------------------------------------------------
class mainCanvasWindows (Frame) :
  """Main Canvas window"""
  def __init__(self, mainFrame) :
    self.mainCanevas = Canvas(mainFrame, bg = "cadet blue", bd = -2, width = 790, height = 400)
    self.mainCanevas.grid(row = 1, column = 0, columnspan = 4, padx = 2, pady = 2, sticky = W+E)

  def get_mainCanvas_ID (self) :
    """Return the canvas ID"""
    return self.mainCanevas

  def destroy_mainCanvas (self) :
    """Clear the canvas"""
    self.mainCanevas.delete(ALL)

#------------------------------------------------------------------------------
# Menu bar class
#------------------------------------------------------------------------------
class mainMenuBar (object) :
  """Main Frame menu bar"""
  def __init__(self, mainFrame, menuFrame, dataBase) :
    self.mainFrame = mainFrame
    self.menu = menuFrame
    self.dataBase = dataBase
    # Menu buttons
    Button(self.menu, text = '  Home   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.home_app).grid(row = 0, column = 0, padx = 5, pady = 5)
    Button(self.menu, text = '  Info   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.info_app).grid(row = 0, column = 1, padx = 5, pady = 5)
    Button(self.menu, text = '  Exit   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.exit_app).grid(row = 0, column = 2, padx = 5, pady = 5)
    Button(self.menu, text = ' Reboot  ', font = ("DejaVu\ Sans \Mono", 10), command = self.reboot).grid(row = 0, column = 3, padx = 5, pady = 5)
    Button(self.menu, text = 'Shut down', font = ("DejaVu\ Sans\ Mono", 10), command = self.shut_down).grid(row = 0, column = 4, padx = 5, pady = 5)
    # Create the canva for displaying information
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    self.home_app ()

  def home_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    homePage = homeWindow (self.mainCanevas, self.dataBase)

  def info_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    sysInfo = infoWindow (self.mainCanevas)

  def exit_app (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()
#    self.mainFrame.quit()

  def shut_down (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()
    os.system("shutdown -P now")

  def reboot (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()
    os.system("reboot")

#------------------------------------------------------------------------------
# Main frame class
#------------------------------------------------------------------------------
class mainFrameWindows (Frame) :
#class mainFrameWindows (Frame, threading.Thread) :
  """Main Frame window"""
  def __init__(self, dataBase) :
#    threading.Thread.__init__(self)
    Frame.__init__(self)
#    self.start()

#  def run(self):
    self.master.geometry("800x480+0+0")
    self.master.config(bg = "cadet blue")
    self.master.overrideredirect(1)

    self.master.menu = Canvas(self.master, bg = "midnight blue", bd = 0, width = 780, height = 25)
    self.master.menu.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 30, sticky = W+E)

    # Set the menu bar
    mainMenuBar (self.master, self.master.menu, dataBase)
#    self.master.mainloop()

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ =="__main__" :
  try :
    startup (global_data.db_path)
  except :
    print("*** Error in startup sequence ; aborting\n")
  else :
    dataBase = dataBaseSQL (global_data.db_path)
#    mainFrameWindows()
    mainFrameWindows(dataBase).mainloop()

