import sys

Debug = True
keyfile = "key"

def decrypt(input):

    # Find the "key" file and converts it into a byte array
    file = open(keyfile, 'rb')
    key = bytearray(file.read())
    
    if Debug:
        # Print binary info to stderr instead of stdout
        sys.stderr.write("key data:\t\t")
        for byte in key:
            sys.stderr.write(str(byte & 1))
        sys.stderr.write("\nUser Input Data:\t")
        for byte in input:
            sys.stderr.write(str(byte & 1))
        sys.stderr.write("\n")
    
    #fix key size
    if len(key) < len(input):
        key = (key * (len(input) // len(key) + 1))[:len(input)]
    elif len(key) > len(input):
        key = key[:len(input)]

    #xor (x, y) for each byte in zip
    resultingByteArray = bytearray(x ^ y for x, y in zip(input, key))
    sys.stdout.buffer.write(resultingByteArray)

userInput = bytearray(sys.stdin.buffer.read())
decrypt(userInput)
