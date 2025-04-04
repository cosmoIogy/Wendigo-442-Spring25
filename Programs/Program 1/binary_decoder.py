import sys

#function to decode binary string 
def decode(input,bit):
    string = ''
    
    for i in range (0, len(input), bit):#start at 0, go to end of string, intervals of bit length
        string_slice = input[i:i+bit]   #get next slice
        num = int(string_slice, 2)      #convert to decimal

        #if backspace ID:8 then remove end of string
        if (num==8):
            string = string[:-1]
        else:
            char = chr(num)          #convert to char
            string += char
    return string

#main function------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Read input and clean
    input = sys.stdin.read().strip()
    input = input.replace("\n", "").replace("\r", "").strip()

    #mod % stripped input to check for 7 or 8 bit 
    if (len(input)%8==0):
        message = decode(input, 8)
    else:
        message = decode(input, 7)

    print ("Decoded Text: " + message)
