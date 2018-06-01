import socket
import sys

def send(data):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('192.168.0.200', 5905)
    
    try:

        # Send data
        print >>sys.stderr, 'sending "%s"' % data
        sent = sock.sendto(data, server_address)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
