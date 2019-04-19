"""TCPServer.py: Simple File Transfer Client code using socketserver framework"""

__author__      = "Joshua Liu"

import socket
import sys

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        client.sendall(l)
        print('Sent ',repr(l))
        l = f.read(1024)
    f.close()

    print('Done sending')
    client.sendall(bytes('Thank you for connecting\n', "utf-8"))
    client.close()
