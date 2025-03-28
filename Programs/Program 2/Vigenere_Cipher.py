testKey = "mykey"

testString = "hello"


keyLowered = testKey.lower()

for character in keyLowered:
    print(character + ": " + (str(ord(character)-97)))


encrypted = ""
count = 0

for i in range(len(testString)):
    if count >= len(testKey):
        count = 0
    encrypted += chr( ( ( ((ord(keyLowered[count]))-97) + ((ord(testString[i]))-97) ) % 26) + 97)
    count += 1

print(encrypted)

 
