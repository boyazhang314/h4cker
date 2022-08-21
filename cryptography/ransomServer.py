import socketserver
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class ClientHandler(socketserver.BaseRequestHandler):
    # Decrypt the symmetric key and send it back to the client
    def handle(self):
        encrypted_key = self.request.recv(1024).strip()
        print("Implement decryption of data " + encrypted_key)
        # Load private key
        with open("./private_key.key", "rb") as private_key:
            # Decryption
            key = private_key.decrypt(
                encrypted_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        self.request.sendall(key)

if __name__ == "__main__":
    HOST, PORT = "", 8000

    # Instance of the TCP server
    tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)

    try:
        # Start the server
        tcpServer.serve_forever()
    except:
        print("There was an error")