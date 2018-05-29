import bluetooth

bd_addr = "2C:33:7A:F0:44:36"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()

