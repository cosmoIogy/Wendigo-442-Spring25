import datetime
import hashlib
#cur2 = "2013 05 06 07 43 25"
#cur2 = "2017 03 23 18 02 06"
#cur2 = "2017 04 23 18 02 30"
cur2 = "2015 01 01 00 00 00"
cur = cur2.split(" ")
current = datetime.datetime(int(cur[0]),int(cur[1]),int(cur[2]),int(cur[3]),int(cur[4]),int(cur[5]))


#string = "1999 12 31 23 59 59"
#string = "2017 01 01 00 00 00"
#string = "1999 12 31 23 59 59"
string = "2014 12 31 00 00 00"
arr = string.split(" ")
epoch = datetime.datetime(int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3]),int(arr[4]),int(arr[5]))
diff = current - epoch
finalSeconds = int(diff.total_seconds())-3600
rem = finalSeconds % 60
print(rem)
print(finalSeconds)
finalSeconds-=rem
md = hashlib.md5(str(finalSeconds).encode())
md = md.hexdigest()
md = hashlib.md5(md.encode()).hexdigest()

print(md)
code = ""

mdreverse = md[::-1]
print(mdreverse)
for i in md:
    if (i.isalpha() and len(code) < 2):
        code+=i
for i in mdreverse:
    if (i.isdigit() and len(code) < 4):
        code+=i
print(code)