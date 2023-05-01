import socket

# Set up the client socket
HOST = 'localhost'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Send a message to the server
    message = b"Hello, server!"
    s.sendall(message)
    
    # Receive the server's response
    data = s.recv(1024)
    print("Received:", data.decode())
