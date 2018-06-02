"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import bluetooth

def send(data):
    serverMACAddress = '2C:33:7A:F0:44:36'
    port = 1
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    time.sleep(0.5)
    #while 1:
       #text = raw_input() # Note change to the old (Python 2) raw_inpu
    s.send(data)
    s.close()
