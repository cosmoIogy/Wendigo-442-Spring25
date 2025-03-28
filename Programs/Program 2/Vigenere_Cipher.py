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
            if testString[i].isupper():
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
    decodedText = encodedText # temp
    return decodedText

testKey = "This is my key"
testString = "Get ready for Cyber Storm! We're going to turn your world upside down on May 16!"

encrypted = encode(testString, testKey)

print(encrypted)
