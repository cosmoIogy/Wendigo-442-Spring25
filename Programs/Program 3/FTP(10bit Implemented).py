from ftplib import FTP

#server login info--------------------------------------------
username = "anonymous"
password = ""
port     = 21
host     = "138.47.99.228" #this is the host/VM IP you want to connect to
filePath = "/10"           #this is the desired file path location
#--------------------------------------------------------------
#if code timeout then change
USE_PASSIVE = False

#method variable for switching 7 and 10 bits
#just set to True for 7 and False for 10 
METHOD = False
#--------------------------------------------------------------
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

#login to server
server = FTP(host)
server.connect(host,port)
server.login(username,password)
server.set_pasv(USE_PASSIVE)

#Go to specified Path
server.cwd(filePath)

#grab file permissions and quit
files = []
server.dir(files.append)
server.quit()

#map each permission character to its binary counterpart
replacements = str.maketrans({"-": "0", "r": "1", "x": "1", "w": "1", "d":"1"})
#string to hold covert message
plaintext = ""
binstring = ""

#loop through each file and convert permissions to binary to ascii
for i in files:
    #if 7-bit method
    if(METHOD):

        #first 3 bit check to skip trash files
        filecheck = i[:3]
        bincheck = filecheck.translate(replacements)
        decimalcheck = int(bincheck,2)

        if (decimalcheck > 0):
            plaintext += ""

        else:
            #grab the last 7 bits and decode
            permissions = i[3:10]
            #translate the characters using the mapping
            binary = permissions.translate(replacements)
            #convert and add to plaintext
            decimal = int(binary,2)
            letter = chr(decimal)
            plaintext += letter
    
    #(TO DO)!!! implement 10 bit here-------------------------------------------
    else:
        #grab the first 10 bits
        permissions = i[:10]
        #instead translate and concatonate all binary then translate to ascii to include 
        
        #translate the characters using the mapping
        binary = permissions.translate(replacements)
        binstring += binary

if(METHOD==False):
    plaintext = decode(binstring, 7)


#print results------------------------------------------------------------------
print(plaintext)
#readable print of collected files
for i in files:
    print (i)
