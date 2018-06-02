#!/usr/bin/python

import sys
import os
from os.path import expanduser
home = expanduser("~")
sys.path.append(home+'/SCR/Raspi')
import GUI_support

def execute(data,b):
    list=data.split()
    print(list)
    if len(list)<2 :
        print 'Too little arguments'
    else:
        light = int(list[0])
        onoff = list[1]
        if light==1:
            if onoff=="on":
                os.system('python /home/pi/SCR/Raspi/RF/wlacz1.py')
                print 'One on'
                GUI_support.SendUp("One is on",b)
            elif onoff=="off":
                os.system('python /home/pi/SCR/Raspi/RF/wylacz1.py')
                print 'One off'
                GUI_support.SendUp("One is off",b)
            else:
                print "Specify on or off"
        elif light==2:
            if onoff=="on":
                os.system('python /home/pi/SCR/Raspi/RF/wlacz2.py')
                print 'Two on'
                GUI_support.SendUp("Two is on",b)
            elif onoff=="off":
                os.system('python /home/pi/SCR/Raspi/RF/wylacz2.py')
                print 'Two off'
                GUI_support.SendUp("Two is off",b)
            else:
                print "Specify on or off"
        elif light==0:
            if onoff=="on":
                os.system('python /home/pi/SCR/Raspi/RF/wlaczall.py')
                print 'All on'
                GUI_support.SendUp("All are on",b)
            elif onoff=="off":
                os.system('python /home/pi/SCR/Raspi/RF/wylaczall.py')
                print 'All off'
                GUI_support.SendUp("All are off",b)
            else:
                print "Specify on or off"
        else:
            print "Specify number of light - 0 for all"
            
        


