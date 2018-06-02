"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth
import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append(home+'/SCR')
import GUI_support
sys.path.append(home+'/SCR/Raspi/RF')
import RF_client
def run():
    while 1:
        hostMACAddress = '' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
        port = 1
        backlog = 1
        size = 1024
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.bind((hostMACAddress, port))
        s.listen(backlog)
        try:
            client, clientInfo = s.accept()
            while 1:
                data = client.recv(size)
                if data:
                    print(data)
		    GUI_support.DataRec.set(data)
		    RF_client.execute(data,'2')
                    #client.send(data) # Echo back to client
        except:	
            print("Closing socket")
            client.close()
            s.close()

