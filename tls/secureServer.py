# Server socket that accepts secure connections from the client

import socket
import ssl

client_cert = 'client.crt'
server_key = 'server.key'
server_cert = 'server.crt'
port = 8080

# Default context to support client authentication
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# Ensure that the server checks client certificates
context.verify_mode = ssl.CERT_REQUIRED
# Provide the client and server certificate locations
context.load_verify_locations(cafile=client_cert)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.options |= ssl.OP_SINGLE_ECDH_USE
# Ban all previous versions of TLS
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('', port))
    sock.listen(1)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(addr)
        message = conn.recv(1024).decode()
        capitalizedMessage = message.upper()
        conn.send(capitalizedMessage.encode())