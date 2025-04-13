# use Python 3
import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "localhost" #IP:   138.47.99.228 this is the IP and port of the test server
port = 1337      #Port: 31337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF--------------------------------
data = ""       #declare data
binstring = ""  #delay pattern
t0 = time()     #start time
num = 0.1       #assumed dealy difference

while (data.rstrip("\n") != "EOF"):

    data = s.recv(1).decode() 

    #break infinate loop
    if not data:
        break

    t1 = time()

    # output the data
    stdout.write(data)
    stdout.flush()

    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    #reset timer
    t0=t1

    #find delay pattern
    if (delta > num):
        binstring += "1"
    else:
        binstring += "0"

    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

#show binary results then convert this to char format
print ("\n binary: "+ binstring)

# close the connection to the server
s.close()
