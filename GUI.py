#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 01, 2018 01:04:57 AM

import sys

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

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    GUI_support.set_Tk_var()
    top = SCR (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_SCR(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    GUI_support.set_Tk_var()
    top = SCR (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SCR():
    global w
    w.destroy()
    w = None


class SCR:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("460x300+443+85")
        top.title("SCR")
        top.configure(highlightcolor="black")



        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.65, rely=0.13, relheight=0.07
                , relwidth=0.19)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(command=GUI_support.sel)
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(takefocus="0")
        self.Radiobutton1.configure(text='''Bluetooth''')
        self.Radiobutton1.configure(value="1")
        self.Radiobutton1.configure(variable=GUI_support.Radio)

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.65, rely=0.3, relheight=0.07
                , relwidth=0.11)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(command=GUI_support.sel)
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(overrelief="ridge")
        self.Radiobutton2.configure(takefocus="0")
        self.Radiobutton2.configure(text='''TCP''')
        self.Radiobutton2.configure(value="2")
        self.Radiobutton2.configure(variable=GUI_support.Radio)

        self.Radiobutton3 = Radiobutton(top)
        self.Radiobutton3.place(relx=0.65, rely=0.47, relheight=0.07
                , relwidth=0.12)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(command=GUI_support.sel)
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(takefocus="0")
        self.Radiobutton3.configure(text='''UDP''')
        self.Radiobutton3.configure(value="3")
        self.Radiobutton3.configure(variable=GUI_support.Radio)

        self.Radiobutton4 = Radiobutton(top)
        self.Radiobutton4.place(relx=0.65, rely=0.63, relheight=0.07
                , relwidth=0.13)
        self.Radiobutton4.configure(activebackground="#d9d9d9")
        self.Radiobutton4.configure(command=GUI_support.sel)
        self.Radiobutton4.configure(justify=LEFT)
        self.Radiobutton4.configure(takefocus="0")
        self.Radiobutton4.configure(text='''HTTP''')
        self.Radiobutton4.configure(value="4")
        self.Radiobutton4.configure(variable=GUI_support.Radio)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.8, rely=0.23, height=37, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=GUI_support.Send)
        self.Button1.configure(takefocus="0")
        self.Button1.configure(text='''Send''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.26, rely=0.13,height=21, relwidth=0.32)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(takefocus="0")
        self.Entry1.configure(textvariable=GUI_support.DataSend)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.24, rely=0.27, height=19, width=156)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''[Light number] [ON/OFF]''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.24, rely=0.4, height=19, width=90)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Temp [In/Out]''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.04, rely=0.27, height=19, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Commands:''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.07, rely=0.73, height=19, width=27)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Info''')
        self.Label4.configure(textvariable=GUI_support.Info)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.04, rely=0.57, height=19, width=87)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Data received''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.04, rely=0.13, height=19, width=81)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''Data to send''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.26, rely=0.57, height=29, width=106)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(relief=RIDGE)
        self.Label7.configure(textvariable=GUI_support.DataRec)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.8, rely=0.43, height=37, width=77)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=GUI_support.Run_Servers)
        self.Button2.configure(text='''Run servers''')
        self.Button2.configure(width=77)






if __name__ == '__main__':
    vp_start_gui()



