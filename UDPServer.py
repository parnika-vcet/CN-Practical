
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set server address
server_address = ("127.0.0.1", 8080)

# Bind socket
server_socket.bind(server_address)

print("UDP Server started on port 8080...")
print("Waiting for client message...")

# Receive message from client
buffer, client_address = server_socket.recvfrom(1024)
print("Message from client:", buffer.decode())

# Send response
response = "Hello from UDP Server!"
server_socket.sendto(response.encode(), client_address)
print("Response sent to client.")

# Close socket
server_socket.close()
