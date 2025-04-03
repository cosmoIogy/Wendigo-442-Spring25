#---Client---#
#This will be used to test if the chat.py file is correctly decoding the message
import socket
from sys import stdout
for time import time

# Enables debugging output 
DEBUG = False

# Set the server's IP address and port
ip = "localhost"
port = 1337

# Create the socket
s = socket.socket(socket.AF_INET, SOCK_STREAM)

# Connet to the server
s.connect((ip,port))

# Receive data until EOF
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    # Output the data
    stout.write(data)
    stdout.flush()

    # Start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    # Calculate the time delta (and output if debugging)
    delta = round(t1- t0, 3)
    if(DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# Close the connection to the server
s.close()