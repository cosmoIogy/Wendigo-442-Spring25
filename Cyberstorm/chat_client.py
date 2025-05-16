import socket
from sys import stdout
from time import time

# Turn to true to see the delta time between each char.
DEBUG = False

# Connect to the server 
ip = "localhost"
port = 1337

# Creat and connect socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Variables to help track and process the data
data = ""               # Character received from server
binstring = ""          # Binary string built from the timing data
threshold = 0.01        # Time threshold to determine 0 or 1
first_char = True       # Flag to skip delta on the first character
t0 = time()             # Initial timer

# For controlling when to stop reading
eof_seen = False        # Marks when the EOF appears in the overt message.
extra_chars = 5         # Collect extra characters after EOF for full covert timing
printing_allowed = True # Marks what we should be printing.

overt_buffer = ""        # Store overt message for printing at the end
print("...")

# Read from the server character by character
while True:
    data = s.recv(1).decode()
    if not data:
        break

    t1 = time()

    # Buffer the overt message
    overt_buffer += data

    # Print overt message until newline '\n' is seen
    if printing_allowed:
        stdout.write(data)
        stdout.flush()

        if data == '\n':
            printing_allowed = False
            print("...")  # after newline, just show loading dots


    # After printing ends watch for EOF at the end of the overt message
    if not printing_allowed and "EOF" in overt_buffer:
        extra_chars -= 1
        if extra_chars == 0:
            break

    if first_char:
        t0 = t1
        first_char = False
        continue

    delta = round(t1 - t0, 3)
    t0 = t1

    # Convert timing delta to binary bit
    if delta > threshold:
        binstring += "1"
    else:
        binstring += "0"

    if DEBUG:
        stdout.write(f" [{delta:.3f}]\n")
        stdout.flush()

# Close the socket
s.close()

# Decode binary string into characters
covert_message = ""
for i in range(0, len(binstring), 8):
    byte = binstring[i:i+8]
    if len(byte) < 8:
        break
    char = chr(int(byte, 2))
    covert_message += char
    if covert_message.endswith("EOF"):
        break

print("Covert message:", covert_message[:-3])
