import socket
import sys

def run():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('192.168.0.201', 5904)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    # Listen for incoming connections
    while True:
        # Listen for incoming connections
        sock.listen(1)

    
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
    
        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            
            data = connection.recv(16)
	    if(str(data)!=''):
                print >>sys.stderr, 'received "%s"' % data
		
           
        finally:
            # Clean up the connection
            connection.close()
