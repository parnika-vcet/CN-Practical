
import socket

try:
    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)
    print("Server is waiting for client...")

    # Accept client connection
    conn, addr = server.accept()
    print("Client connected!")

    # Receive message from client
    message = conn.recv(1024).decode()
    print("Client:", message)

    # Send response to client
    conn.sendall(b"Hello from Server!")

    # Close connections
    conn.close()
    server.close()

except Exception as e:
    print(e)
