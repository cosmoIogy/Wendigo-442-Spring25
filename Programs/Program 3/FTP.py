from ftplib import FTP

#server login info--------------------------------------------
username = "anonymous"
password = ""
host     = "192.168.1.176" #this is the host/VM IP you want to connect to
filePath = "/7" #desired file path location
#--------------------------------------------------------------

#method variable for switching 7 and 10 bits
    #just set to True rn until fully implemented
METHOD = True


#login to server
server = FTP(host)
server.login(username,password)

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
        #grab the last 7 bits
        permissions = i[3:10]
        #translate the characters using the mapping
        binary = permissions.translate(replacements)
        #convert and add to plaintext
        decimal = int(binary,2)
        letter = chr(decimal)
        plaintext += letter
    
    #implement 10 bit here
    #else:
    
print(plaintext)

#readable print of collected files
for i in files:
    print (i)

