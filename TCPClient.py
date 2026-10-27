
import socket

try:
    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))
    print("Connected to server!")

    # Send message to server
    client.sendall(b"Hello Server!\n")

    # Receive response from server
    response = client.recv(1024).decode()
    print("Server:", response)

    # Close connection
    client.close()

except Exception as e:
    print(e)




# commands:
# ipconfig
# ipconfig/all
# ping
# tracert
# nslookup
# hostname
# arp -a
# route print
# netstat



# ifconfig
# ip r
# ping google.com
# traceroute
# nslookup google.com
# hostname
# arp 
# route
# netstat