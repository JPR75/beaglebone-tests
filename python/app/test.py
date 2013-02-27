#! /usr/bin/env python
# -*- coding:Utf8 -*-

from Tkinter import *
import os
import platform
import datetime

from startup import startup
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
    Label(self.sysinfo, text = platform_info, font = ("DejaVu_Sans_Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)
#    Label(self.sysinfo, text = platform_info, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_RAM (self):
    """Show RAM info"""
#    RAMmemory = os.popen("free -m").readlines()[1].split()
    RAMmemory = ["xxx","xxx","xxx","xxx"]
    memory = ("Memory => total : {}  kB ; used : {} kB ; free : {} kB").format(RAMmemory[1], RAMmemory[2], RAMmemory[3])
    Label(self.sysinfo, text = memory, font = ("DejaVu_Sans_Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)
#    Label(self.sysinfo, text = memory, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_sys_date (self):
    """Show date and time"""
    now = datetime.datetime.now()
    current_date_time = ("{}-{}-{} ; {}h {}mm {}s").format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    Label(self.sysinfo, text = current_date_time, font = ("DejaVu_Sans_Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)
#    Label(self.sysinfo, text = current_date_time, font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

  def show_dev_info (self) :
    """Show developpement info"""
    dev_info = ("Firmware : v1.0.0\nSoftware  : v1.0.0\n\nContact    :\n\nJean-Paul Ricaud\n\nSynchrotron SOLEIL\nL'Orme des Merisiers\nSaint-Aubin - BP 48\nFrance\n\njean-paul.ricaud@synchrotron-soleil.fr")
    Label(self.devinfo, text = dev_info, font = ("DejaVu_Sans_Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 10, anchor = W)
#    Label(self.devinfo, text = dev_info, font = ("DejaVu\ Sans\ Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 10, anchor = W)

#------------------------------------------------------------------------------
# Home window class
#------------------------------------------------------------------------------
class homeWindow (Canvas) :
  """Home page window"""
  def __init__(self, mainCanevas) :
    # System info
    self.homePage = Canvas(mainCanevas, bg = "ivory", bd = 0, width = 395, height = 150)
    self.homePage.grid(row = 1, column = 0, padx = 5, pady = 0)
    self.show_home_page ()

  def show_home_page (self) :
    """Home page info"""

    Label(self.homePage, text = "Home Page", font = ("DejaVu_Sans_Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)
#    Label(self.homePage, text = "Home Page", font = ("DejaVu\ Sans \Mono", 10), relief = GROOVE, bg = '#F0F0E0', bd = 2, justify = LEFT).pack(padx = 20, pady = 5, anchor = W)

#------------------------------------------------------------------------------
# Menu bar class
#------------------------------------------------------------------------------
class mainMenuBar (object) :
  """Main Frame menu bar"""
  def __init__(self, mainFrame, menuFrame) :
    self.mainFrame = mainFrame
    self.menu = menuFrame
    # Menu buttons
    Button(self.menu, text = '  Home   ', font = ("DejaVu_Sans_Mono", 10), command = self.home_app).grid(row = 0, column = 0, padx = 5, pady = 5)
#    Button(self.menu, text = '  Home   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.home_app).grid(row = 0, column = 0, padx = 5, pady = 5)
    Button(self.menu, text = '  Info   ', font = ("DejaVu_Sans_Mono", 10), command = self.info_app).grid(row = 0, column = 1, padx = 5, pady = 5)
#    Button(self.menu, text = '  Info   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.info_app).grid(row = 0, column = 1, padx = 5, pady = 5)
    Button(self.menu, text = '  Exit   ', font = ("DejaVu_Sans_Mono", 10), command = self.exit_app).grid(row = 0, column = 2, padx = 5, pady = 5)
#    Button(self.menu, text = '  Exit   ', font = ("DejaVu\ Sans\ Mono", 10), command = self.exit_app).grid(row = 0, column = 2, padx = 5, pady = 5)
    Button(self.menu, text = ' Reboot  ', font = ("DejaVu_Sans_Mono", 10), command = self.reboot).grid(row = 0, column = 3, padx = 5, pady = 5)
#    Button(self.menu, text = ' Reboot  ', font = ("DejaVu\ Sans \Mono", 10), command = self.reboot).grid(row = 0, column = 3, padx = 5, pady = 5)
    Button(self.menu, text = 'Shut down', font = ("DejaVu_Sans_Mono", 10), command = self.shut_down).grid(row = 0, column = 4, padx = 5, pady = 5)
#    Button(self.menu, text = 'Shut down', font = ("DejaVu\ Sans\ Mono", 10), command = self.shut_down).grid(row = 0, column = 4, padx = 5, pady = 5)
    # Create the canva for displaying information
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    self.home_app ()

  def home_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    homePage = homeWindow (self.mainCanevas)

  def info_app (self) :
    self.mainCanevas.destroy()
    canvasWindows = mainCanvasWindows (self.mainFrame)
    self.mainCanevas = canvasWindows.get_mainCanvas_ID ()
    sysInfo = infoWindow (self.mainCanevas)

  def exit_app (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()

  def shut_down (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()
    os.system("shutdown -P now")

  def reboot (self) :
    self.mainFrame.quit()
    self.mainFrame.destroy()
    os.system("reboot")

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
# Main frame class
#------------------------------------------------------------------------------
class mainFrameWindows (Frame) :
  """Main Frame window"""
  def __init__(self) :
    Frame.__init__(self)
    self.master.geometry("800x480+0+0")
    self.master.config(bg = "cadet blue")
    self.master.overrideredirect(1)

    self.master.menu = Canvas(self.master, bg = "midnight blue", bd = 0, width = 780, height = 25)
    self.master.menu.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 30, sticky = W+E)

    # Set the menu bar
    mainMenuBar (self.master, self.master.menu)

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ =="__main__" :
  init = startup ()
  try :
    init.create_data_file()
    init.create_cmd_file()
  except IOError :
    print("*** Error in startup sequence ; aborting\n")
  else :
    mainFrameWindows().mainloop()
