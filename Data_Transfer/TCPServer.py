"""TCPServer.py: Simple Echo Server code using socketserver framework"""

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
        self.data = str(self.request.recv(1024).strip(), "utf-8")
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        if "SECRET" in self.data:
            digits = re.findall(r'\d+', self.data)
            digits = ''.join(digits)
            count = sum(c.isdigit() for c in self.data)
            result = "Digits: " + str(digits) + " Count: " + str(count)
            
        # send back digits + count
        self.request.sendall(bytes(result + "\n", "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.handle_request()
        server.server_close()
