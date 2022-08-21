# Client socket to establish a secure connection to the server

import socket
import ssl

client_key = 'client.key'
# openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt
client_cert = 'client.crt'
# openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt
server_cert = 'server.crt'
port = 8080

hostname = '127.0.0.1'
# New SSL context to manage the certificates and other socket settings
context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile=server_cert)
# Load client's private key and certificate, to verify the client's identity
context.load_cert_chain(certfile=client_cert, keyfile=client_key)
context.load_verify_locations(cafile=server_cert)
context.verify_mode = ssl.CERT_REQUIRED

# Set appropriate bit in the context's options to select a key-exchange algorithm
# Elliptic-curve Diffie-Hellman
# OR options with the ssl constant
# Forward secrecy: Can calculate a new shared secret for every connection
context.options |= ssl.OP_SINGLE_ECDH_USE
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

# Create socket
with socket.create_connection((hostname, port)) as sock:
    # SSL wrapper context, ensures all information is encrypted before it is sent
    with context.wrap_socket(sock, server_side=False, server_hostname=hostname) as ssock:
        print(ssock.version())
        message = input("Please enter your message: ")
        ssock.send(message.encode())
        receives = ssock.recv(1024)
        print(receives)

