import os
import time
import serial

#MAC_ADDRES KLIENTA
MAC_ADDR='2C:33:7A:F0:44:36 1'
command = 'sudo rfcomm bind /dev/rfcomm1 '+MAC_ADDR
os.system(command)

ser = serial.Serial('/dev/rfcomm1',19200,timeout=5)



if ser.isOpen():

    try:
               #and discard all that is in buffer

        #write data

        

        while True:
            try:
                response = ser.readline()
                if(response!=''):
                    print("read data: " + response)
            except KeyboardInterrupt:
                print '^C received, shutting down the web server'
                ser.close()
                os.system('sudo rfcomm release rfcomm1') 
                

    except Exception, e1:
        print "error communicating...: " + str(e1)
        os.system('sudo rfcomm release rfcomm1')

else:
    print "cannot open serial port "
    os.system('sudo rfcomm release rfcomm1') 

