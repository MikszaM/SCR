import os
import time
import serial


#MAC_ADDRES SERWERA
MAC_ADDR='B8:27:EB:3A:15:27 1'
command = 'sudo rfcomm bind /dev/rfcomm1 '+MAC_ADDR
os.system(command)


ser = serial.Serial('/dev/rfcomm1',19200,timeout=5)



if ser.isOpen():

    try:
               #and discard all that is in buffer

        #write data
        ser.write("My data")
        print("My data")

        
    except Exception, e1:
        print "error communicating...: " + str(e1)
        os.system('sudo rfcomm release rfcomm1')

else:
    print "cannot open serial port "
    os.system('sudo rfcomm release rfcomm1') 


