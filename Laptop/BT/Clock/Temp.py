import os
import time
import serial

#MAC_ADDRES KLIENTA
def read(inout):
    MAC_ADDR='00:12:6F:36:F3:72 1'
    command = 'sudo rfcomm bind /dev/rfcomm1 '+MAC_ADDR
    os.system(command)

    ser = serial.Serial('/dev/rfcomm1',19200,timeout=5)

    if ser.isOpen():

        try:
                   #and discard all that is in buffer

            #write data
            ser.write(inout)
            

            time.sleep(0.5)  #give the serial port sometime to receive the data

            while True:
            #    try:
            
                response = ser.readline()
                if(response!=''):
                    print("read data: " + response)
                    break
            
            os.system('sudo rfcomm release rfcomm1')         

        except Exception, e1:
            print "error communicating...: " + str(e1)
            os.system('sudo rfcomm release rfcomm1')

    else:
        print "cannot open serial port "
        os.system('sudo rfcomm release rfcomm1') 

