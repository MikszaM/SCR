import serial
import os
import time


MAC_ADDR='00:12:6F:36:F3:72 1'
command = 'sudo rfcomm bind /dev/rfcomm1 '+MAC_ADDR
os.system(command)

ser = serial.Serial('/dev/rfcomm1',19200,timeout=5)



if ser.isOpen():

    try:
               #and discard all that is in buffer

        #write data
        ser.write("i")
        print("i")

        time.sleep(0.5)  #give the serial port sometime to receive the data

        numOfLines = 0

        while True:
            response = ser.readline()
            if(response!=''):
                print("read data: " + response)
        ser.close()
        os.system('sudo rfcomm release rfcomm1') 
    except Exception, e1:
        print "error communicating...: " + str(e1)
        os.system('sudo rfcomm release rfcomm1')

else:
    print "cannot open serial port "
    os.system('sudo rfcomm release rfcomm1') 
