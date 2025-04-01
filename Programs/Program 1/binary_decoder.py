#function to convert binary to decimal to characters
def convert(num):
    decimal = int(num,2) #convert binary to decimal
    letter = chr(decimal) #convert decimal to character
    return letter

#grab input
binary = input()

#initialize string for plaintext
plaintext = ""

#check whether input is 7-bit or 8-bit
if(len(binary) % 7 == 0):
    Li = 0 ; Ri = 7 #create index markers to mark the first 7 bits

    #loop while the right index marker is not greater than the length  of the input
    while(Ri <= len(binary)):
        plaintext += convert(binary[Li:Ri]) #convert the 7 bits into characters and append plaintext to plaintext string
        Li += 7; Ri += 7 #adjust markers to move onto the next 7 bits
    print(plaintext)
else: #8-bit process
    Li = 0; Ri = 8 #create index markers to mark the first 8 bits
    
    #loop while the right index marker is not greater than the length  of the input
    while(Ri <= len(binary)):
        plaintext += convert(binary[Li:Ri]) #convert the 8 bits into characters and append plaintext to plaintext string
        Li += 8; Ri += 8 #adjust markers to move onto the next 8 bits
    print(plaintext)
        
    
