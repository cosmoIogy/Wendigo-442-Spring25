from ftplib import FTP

#server login info--------------------------------------------
username = "anonymous"
password = ""
port     = 21
host     = "192.168.1.11" #this is the host/VM IP you want to connect to
filePath = "/7"           #this is the desired file path location
#--------------------------------------------------------------
#if code timeout then change
USE_PASSIVE = True

#method variable for switching 7 and 10 bits
    #just set to True rn until fully implemented
METHOD = True

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
replacements = str.maketrans({"-": "0", "r": "1", "x": "1", "w": "1"})
#string to hold covert message
plaintext = ""

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
    
    #(TO DO) implement 10 bit here
    #else:
    
print(plaintext)

#readable print of collected files
for i in files:
    print (i)

