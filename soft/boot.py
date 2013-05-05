#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
# Help window class
#------------------------------------------------------------------------------
class helpWindow (Canvas) :
  """Help window"""
  def __init__(self, mainCanevas) :
    self.dataBase = dataBase
    # System info
    self.helpPage = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.helpPage.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = N)
    self.set_warning_help ()
    self.show_help ()

  def set_warning_help (self) :
    """Show warning info & set data base statue to warning"""
    # Push to data base
    try :
      self.dataBase.set_status_sql (("System up, but stopped. Select 'Run' button on front panel to start.", "No error", 2))
    except :
      print("*** Error while connecting database to write data in 'boot.py'\n")
    Label(self.helpPage, text = "Warning system stopped! Select 'Run' button to start", font = ("DejaVu\ Sans \Mono", 12), relief = GROOVE, fg = "red", bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_help (self) :
    """Show help"""
    Label(self.helpPage, text = "{}".format(global_data.help_txt), font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

#------------------------------------------------------------------------------
# Info window class
#------------------------------------------------------------------------------
class infoWindow (Canvas) :
  """Info window"""
  def __init__(self, mainCanevas) :
    self.dataBase = dataBase
    # System info
    self.sysinfo = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.sysinfo.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = N)
    self.set_warning_info ()
    self.show_sys_info ()
    self.show_sys_RAM ()
    self.show_sys_IP ()
    self.show_sys_data ()
    # Dev info
    self.devinfo = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.devinfo.grid(row = 1, column = 1, padx = 5, pady = 0, sticky = N)
    self.show_dev_info ()

  def set_warning_info (self) :
    """Show warning info & set data base statue to warning"""
    # Push to data base
    try :
      self.dataBase.set_status_sql (("System up, but stopped. Select 'Run' button on front panel to start.", "No error", 2))
    except :
      print("*** Error while connecting database to write data in 'boot.py'\n")
    Label(self.sysinfo, text = "Warning system stopped! Select 'Run' button to start", font = ("DejaVu\ Sans \Mono", 12), relief = GROOVE, fg = "red", bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_info (self) :
    """Show system info"""
    platform_info = "Processor :  {} ; {}\nOS            : {}\nVesrion    : {}\nPython     : {}".format(platform.machine(), platform.processor(), platform.platform(), platform.version(), platform.python_version())
    Label(self.sysinfo, text = platform_info, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_RAM (self):
    """Show RAM info"""
    RAMtotal = os.popen("free -m").readlines()[1].split()
    RAMmemory = os.popen("free -m").readlines()[2].split()
    memory = "Memory => total : {}  MB ; used : {} MB ; free : {} MB".format(RAMtotal[1], RAMmemory[2], RAMmemory[3])
    Label(self.sysinfo, text = memory, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_IP (self):
    """Show IP info"""
    IP = os.popen("/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'").readlines()[0][:-1]
    Label(self.sysinfo, text = "IP : {}".format(IP), font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_data (self):
    """Show date and time info"""
    now = datetime.datetime.now()
    uptime = (time.time() - global_data.stratup_time) / 3600.0
    free_RAM = os.popen("free -m").readlines()[2].split()
    memory_leak =  int(free_RAM[3]) - global_data.stratup_RAM
    current_data = "Sys date : {}-{}-{} ; {}h {}mm {}s\nUptime : {:.2f} h\nMemory leak : {} MB".format(now.year, now.month, now.day, now.hour, now.minute, now.second, uptime, memory_leak)
    Label(self.sysinfo, text = current_data, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_dev_info (self) :
    """Show developpement info"""
    dev_info = "{}\n{}\n\n{}".format(global_data.firmware_version, global_data.software_version, global_data.contact_info)
    Label(self.devinfo, text = dev_info, font = ("DejaVu\ Sans\ Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 10, anchor = W)

#------------------------------------------------------------------------------
# Home window class
#------------------------------------------------------------------------------
class homeWindow (Canvas) :
  """Home page window"""
  def __init__(self, mainCanevas, dataBase) :
    self.dataBase = dataBase
    self.homePage = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.homePage.grid(row = 1, column = 0, padx = 5, pady = 0)
    self.showData = Label(self.homePage, text = "\u0394\u03A6 : 00.00\nAmp : 00.00\nT\u00b0C : 0.00", font = ("DejaVu\ Sans \Mono", 40), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT)
    self.showData.pack(padx = 20, pady = 5, anchor = W)
    self.showCmd = Label(self.homePage, text = "Setting\n   \u0394\u03A6 : 000.0000\n   T\u00b0C : 00.00", font = ("DejaVu\ Sans \Mono", 16), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT)
    self.showCmd.pack(padx = 20, pady = 5, anchor = W)
    self.remove_warning ()
    self.update_home_page ()

  def remove_warning (self) :
    """Set data base statue to ok"""
    # Push to data base
    try :
      self.dataBase.set_status_sql (("System up and running", "No error", 1))
    except :
      print("*** Error while connecting database to write data in 'boot.py'\n")

  def update_home_page (self) :
    """Home page update"""
    now = datetime.datetime.now()
    data = "\u0394\u03A6 : {}\nAmp : {}\nT\u00b0C : {}".format(now.hour, now.minute, now.second)
    self.showData.configure(text = data)
    # Get data
    try :
      cmd = self.dataBase.get_cmd_sql ()
    except :
      cmd = [("---.----", "--.--")]
      print("*** Error while connecting database to read cmd in 'boot.py'\n")
    self.showCmd.configure(text = "Setting\n   \u0394\u03A6 : {}\n   T\u00b0C : {}".format(cmd[0][0], cmd[0][1]))
    # Push to data base
    try :
      self.dataBase.set_data_sql ((float(now.hour), float(now.minute), float(now.second)))
    except :
      print("*** Error while connecting database to write data in 'boot.py'\n")
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
    Button(self.menu, text = '   Run   ', font = ("DejaVu\ Sans\ Mono", 10, "bold"), bg = "green", command = self.home_app).grid(row = 0, column = 0, padx = 5, pady = 5)
    Button(self.menu, text = '  Info   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.info_app).grid(row = 0, column = 1, padx = 5, pady = 5)
    Button(self.menu, text = '  Help   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.help_app).grid(row = 0, column = 2, padx = 5, pady = 5)
    Button(self.menu, text = '  Exit   ', font = ("DejaVu\ Sans\ Mono", 10), bg = "gold", command = self.exit_app).grid(row = 0, column = 3, padx = 5, pady = 5)
    Button(self.menu, text = ' Reboot  ', font = ("DejaVu\ Sans \Mono", 10), bg = "red", command = self.reboot).grid(row = 0, column = 4, padx = 5, pady = 5)
    Button(self.menu, text = 'Shut down', font = ("DejaVu\ Sans\ Mono", 10), bg = "red", command = self.shut_down).grid(row = 0, column = 5, padx = 5, pady = 5)
    # Create the canva for displaying information
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    self.home_app ()

  def home_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    homeWindow (self.mainCanevas, self.dataBase)

  def help_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    helpWindow (self.mainCanevas)

  def info_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    infoWindow (self.mainCanevas)

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

