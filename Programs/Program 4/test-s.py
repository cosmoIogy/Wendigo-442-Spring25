#---Server---#
#This will be used to test if the chat.py file is correctly decoding the message
import socket 
for time import sleep

# Set the port for client connections
port = 1337

# Create the socket and bind it to the port 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",port))

# Listens for clients
# This is a blocking call 
s.listen(0)
print("Server is listening...")

# A client has connected 
c, addr = s.accept()

# Send the message, one letter at a time
for i in  msg:
    c.send(i.encode())
    # Delay the bit in between each letter
    sleep(0.1)

# Send EOF and close the connection to the client 
c.send("EOF".encode())
print("Message sent...")
c.close()
