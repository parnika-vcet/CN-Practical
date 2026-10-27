
import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ("127.0.0.1", 8080)

# Message to send
message = "Hello from UDP Client!"

# Send message to server
client_socket.sendto(message.encode(), server_address)
print("Message sent to server:", message)

# Receive response from server
buffer, address = client_socket.recvfrom(1024)
print("Response from server:", buffer.decode())

# Close socket
client_socket.close()
