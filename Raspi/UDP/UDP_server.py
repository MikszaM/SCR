import socket
import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append(home+'/SCR/Raspi')
import GUI_support
sys.path.append(home+'/SCR/Raspi/RF')
import RF_client
def run():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('192.168.43.200', 5905)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(4096)
        GUI_support.DataRec.set(data)
        RF_client.execute(data,'3')
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >>sys.stderr, data
        
