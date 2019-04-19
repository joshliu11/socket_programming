"""TCPServer.py: Simple File Transfer Slient code using socketserver framework"""

__author__      = "Joshua Liu"

import socketserver
import re

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    Must override the handle() method for request handler
    class to implement communication to the client.
    """

    def handle(self):

        with open('received_file', 'wb') as f:
            print('file opened')
            print('receiving data...')
            self.data = str(self.request.recv(1024).strip(), "utf-8")
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)

            # write data to a file
            f.write(self.data.encode("utf-8"))

        f.close()
        print('Successfully get the file')

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.handle_request()
        server.server_close()
