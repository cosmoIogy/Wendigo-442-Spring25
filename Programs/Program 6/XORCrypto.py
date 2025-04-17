import sys

def decrypt(input):

    # Find the "key" file and converts it into a byte array
    file = open("key", 'rb')
    fileData = bytearray(file.read())

    # Prints out the data from key in binary
    print("key data:\t\t", end="")
    for byte in fileData:
        print(byte & 1, end="")

    # Prints out the data from userInput into binary
    print("\nUser Input Data:\t", end="")
    for byte in input:
        print(byte & 1, end="")

    # XOR's the 2 byte arrays and prints out using stdout as plain text
    print("\nResulting array:\t", end="")
    resultingByteArray = bytearray()
    for i in range(len(fileData)):
        resultingByteArray.append(fileData[i] ^ input[i])
    sys.stdout.buffer.write(resultingByteArray)


userInput = bytearray(sys.stdin.buffer.read())
decrypt(userInput)
