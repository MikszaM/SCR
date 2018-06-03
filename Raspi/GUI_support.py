#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 31, 2018 08:54:00 AM
#    May 31, 2018 09:04:34 AM
#    May 31, 2018 09:14:51 AM
#    Jun 01, 2018 12:58:22 AM


import sys
import thread
from os.path import expanduser
home = expanduser("~")

HOST = 'Raspi'  #or Raspi
sys.path.append(home+'/SCR/'+HOST+'/TCP')
import TCP_client
import TCP_server
sys.path.append(home+'/SCR/'+HOST+'/UDP')
import UDP_client
import UDP_server
sys.path.append(home+'/SCR/'+HOST+'/BT')
#import BT_client
import BT_server
sys.path.append(home+'/SCR/'+HOST+'/HTTP')
import HTTP_client
import HTTP_server

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    

def set_Tk_var():
    global DataSend
    DataSend = StringVar()
    global DataRec
    DataRec = StringVar()
    global Info
    Info = StringVar()
    global Radio
    Radio = StringVar()



def Run_Servers():
    print('GUI_support.Run_Servers')
    thread.start_new_thread ( TCP_server.run, () )
    thread.start_new_thread(UDP_server.run,())
    thread.start_new_thread( HTTP_server.run,())
    thread.start_new_thread( BT_server.run,())
    sys.stdout.flush()

def Send():
    print('GUI_support.Send')
    a=str(DataSend.get())
    print(a)
    b=str(Radio.get())
    print(b)
    if b=='2':
        print('tcp')
        thread.start_new_thread ( TCP_client.send, (a,) )
    elif b=='3':
        print('udp')
        thread.start_new_thread ( UDP_client.send, (a,) )
    elif b=='4':
        print('http')
        thread.start_new_thread ( HTTP_client.send, (a,) )
    #DataRec.set(a)
    sys.stdout.flush()
    
def SendUp(data,b):
    print('GUI_support.SendUP')
    print(data)
    print(b)
    if b=='2':
        print('tcp')
        thread.start_new_thread ( TCP_client.send, (data,) )
    elif b=='3':
        print('udp')
        thread.start_new_thread ( UDP_client.send, (data,) )
    elif b=='4':
        print('http')
	thread.start_new_thread ( HTTP_client.send, (a,) )
    #DataRec.set(a)
    sys.stdout.flush()

def sel():
    print('GUI_support.sel')
 
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import GUI
    GUI.vp_start_gui()





























