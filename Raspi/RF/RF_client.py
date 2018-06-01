#!/usr/bin/python

import sys
import os


if len(sys.argv)<3 :
    print 'Too little arguments'
else:
    light = int(sys.argv[1])
    onoff = sys.argv[2]
    if light==1:
        if onoff=="on":
            os.system('python wlacz1.py')
            print 'One on'
        elif onoff=="off":
            os.system('python wylacz1.py')
            print 'One off'
        else:
            print "Specify on or off"
    elif light==2:
        if onoff=="on":
            os.system('python wlacz2.py')
            print 'Two on'
        elif onoff=="off":
            os.system('python wylacz2.py')
            print 'Two off'
        else:
            print "Specify on or off"
    elif light==0:
        if onoff=="on":
            os.system('python wlaczall.py')
            print 'All on'
        elif onoff=="off":
            os.system('python wylaczall.py')
            print 'All off'
        else:
            print "Specify on or off"
    else:
        print "Specify number of light - 0 for all"
        
    



print 'Argument List:', sys.argv[2]
