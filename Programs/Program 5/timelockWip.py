import datetime
import hashlib


def dst_checker(date):
    # if it's not within the months, exit
    if (date.month < 3 and date.month >11):
        return False
    # if explicitly in the months, it's DST
    if (date.month > 3 and date.month < 11):
        return True
    # yeah this sucks i know
    if (date.month == 3):
        # calculate the second sunday of the month 
        temp = datetime.datetime(date.year,date.month,1,date.hour,date.minute,date.second)
        # isn't that slick?
        temp = temp.day-temp.weekday()+13
        # if it's before the second sunday, not in DST
        if (date.day < temp):
            return False
        # if it is, it is
        elif (date.day > temp):
            return True
        else:
            # if it's 2AM or later, it's DST, otherwise it is not
            if (date.hour >= 2):
                return True
            else: 
                return False
    if (date.month == 11):
        # calculate the FIRST sunday of the month 
        temp = datetime.datetime(date.year,date.month,1,date.hour,date.minute,date.second)
        # isn't that slick?
        temp = temp.day-temp.weekday()+6
        print(temp)
        # if it's before the first sunday, not in DST
        if (date.day < temp):
            return True
        # if it is, it is
        elif (date.day > temp):
            return False
        else:
            # if it's 2AM or later, it's DST, otherwise it is not
            if (date.hour >= 2):
                return False
            else: 
                return True
            
def offset(epoch, current,seconds):
    epochDST = dst_checker(epoch)
    currentDST = dst_checker(current)
    # if they're both in DST, or both out, then no offset
    if (currentDST and epochDST):
        return seconds
    elif (not currentDST and not epochDST):
        return seconds
    # if epoch is in DST and current isn't, subtract 3600 seconds
    elif (not currentDST and epochDST):
        return seconds+3600
    else:
        return seconds-3600
#cur2 = "2013 05 06 07 43 25"
#cur2 = "2017 03 23 18 02 06"
#cur2 = "2017 04 23 18 02 30"
cur2 = "2010 06 13 12 55 34"
cur = cur2.split(" ")
current = datetime.datetime(int(cur[0]),int(cur[1]),int(cur[2]),int(cur[3]),int(cur[4]),int(cur[5]))
#print(current.weekday())

#print(current.weekday())

print(dst_checker(current))
#string = "1999 12 31 23 59 59"
#string = "2017 01 01 00 00 00"
#string = "1999 12 31 23 59 59"
#string = "2014 12 31 00 00 00"
string = "2001 02 03 04 05 06"
arr = string.split(" ")
epoch = datetime.datetime(int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3]),int(arr[4]),int(arr[5]))
diff = current - epoch
finalSeconds = int(diff.total_seconds())
finalSeconds = offset(epoch,current,finalSeconds)
rem = finalSeconds % 60
#print(rem)
#print(finalSeconds)
finalSeconds-=rem
md = hashlib.md5(str(finalSeconds).encode())
md = md.hexdigest()
md = hashlib.md5(md.encode()).hexdigest()

#print(md)
code = ""

mdreverse = md[::-1]
#print(mdreverse)
for i in md:
    if (i.isalpha() and len(code) < 2):
        code+=i
for i in mdreverse:
    if (i.isdigit() and len(code) < 4):
        code+=i
print(code)
