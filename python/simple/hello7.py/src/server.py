import socket

# Set up the server socket
HOST = 'localhost'  # Use any available interface
PORT = 12345  # Use a non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)  # Listen for incoming connections
    print(f"Server listening on port {PORT}...")
    
    # Wait for a client to connect
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            
            # Send "Hello, World!" back to the client
            response = b"Hello, World!"
            conn.sendall(response)
