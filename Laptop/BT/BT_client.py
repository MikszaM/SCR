"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import bluetooth

def send(data):
    serverMACAddress = 'B8:27:EB:3A:15:72'
    port = 1
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    #while 1:
       #text = raw_input() # Note change to the old (Python 2) raw_inpu
    s.send(data)
    sock.close()
