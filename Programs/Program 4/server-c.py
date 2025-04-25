import socket
from time import sleep

# Port to listen on
port = 1337

# Create and bind a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# Listen for incoming connections
s.listen(0)
print("Server is listening...")

# Accept the first incoming client connection
c, addr = s.accept()
print(f"Connection from {addr}")

# Convert covert message to binary, 8 bits per char
overt_msg = "Some sort of overt message is being transmitted here. But there is a hidden message being covertly transmitted! Can you guess it?\n"
covert_msg = "Spectacular achievement is always preceded by unspectacular preparation. -- Robert H. SchullerEOF"
covert_bin = "".join(format(ord(c), "08b") for c in covert_msg)

# Ensure overt message is long enough to carry all covert bits
if len(overt_msg) < len(covert_bin):
    overt_msg += " " * (len(covert_bin) - len(overt_msg))

# Send overt message one character at a time
# Inject timing delays to encode covert bits
for i, char in enumerate(overt_msg):
    c.send(char.encode())

    if i < len(covert_bin):
        bit = covert_bin[i]
        # Delay for binary 1
        if bit == '1':
            sleep(0.2)  
        # Delay for binary 0
        else:
            sleep(0.05)
    # Default delay if no more covert bits
    else:
        sleep(0.05)

# Signal end of covert message
c.send("EOF".encode())
print("Message sent...")

# Close the connection
c.close()
