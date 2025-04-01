import sys

def encode(plainText, key):
    plainTextLowered = plainText.lower()
    keyLowered = key.lower()
    keyLowered = keyLowered.replace(" ", "")

    encrypted = ""
    count = 0

    for i in range(len(plainTextLowered)):
        P = ord(plainTextLowered[i]) - 97

        if (P >= 0 and P <= 25):
            K = ord(keyLowered[count]) - 97
            if plainText[i].isupper():
                encrypted += chr( ((P + K) % 26) + 97).upper()
            else:
                encrypted += chr( ((P + K) % 26) + 97)
            count += 1
            if count >= len(keyLowered):
                count = 0
        else:
            encrypted += plainTextLowered[i]
    return encrypted

def decode(encodedText, key):
    encodedTextLowered = encodedText.lower()
    keyLowered = key.lower()
    keyLowered = keyLowered.replace(" ", "")

    decrypted = ""
    count = 0
    for i in range(len(encodedTextLowered)):
        P = ord(encodedTextLowered[i]) - 97

        if (P >= 0 and P <= 25):
            K = ord(keyLowered[count]) - 97
            if encodedText[i].isupper():
                decrypted += chr( ((26 + P - K) % 26) + 97).upper()
            else:
                decrypted += chr( ((26 + P - K) % 26) + 97)
            count += 1
            if count >= len(keyLowered):
                count = 0
        else:
            decrypted += encodedTextLowered[i]
    return decrypted

if __name__ == "__main__":
    if (sys.argv[1] == "-e"): 
        while(True):
            key = sys.argv[2] # Gets key from standard input
            input = sys.stdin.readline().strip() # Reads the input from the line
            input = input.replace("\n", "").replace("\r", "").strip() # Sanitizes it
            if (input == ""): # If empty input, leave
                print("goodbye")
                break
            output = encode(input,key) # Get the encoded result and print
            print(output)
    elif (sys.argv[1] == "-d"):
        while(True):
            key = sys.argv[2] 
            input = sys.stdin.readline().strip()
            input = input.replace("\n", "").replace("\r", "").strip() # Same as above, gets key and input and sanitizes them
            if (input == ""): 
                print("goodbye")
                break
            output = decode(input,key) # Gets the decoded text and prints
            print(output)
