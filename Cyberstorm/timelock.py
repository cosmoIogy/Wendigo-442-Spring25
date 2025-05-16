import datetime
import hashlib
import sys

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
        # if it's before the first sunday, in DST
        if (date.day < temp):
            return True
        # if it is, it isn't
        elif (date.day > temp):
            return False
        else:
            # if it's 2AM or later, it's not DST, otherwise it is
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
    # if epoch is in DST and current isn't, add 3600 seconds
    elif (not currentDST and epochDST):
        return seconds+3600
    # i think this works
    else:
        return seconds-3600

debug = False
# if we're debugging, then manually sets the current time to something
if debug:
    cur2 = "2017 04 23 18 02 06"
    cur = cur2.split(" ")
    current = datetime.datetime(int(cur[0]),int(cur[1]),int(cur[2]),int(cur[3]),int(cur[4]),int(cur[5]))
else:
    current = datetime.datetime.now()
    # cuts off the milliseconds just in case
    current = datetime.datetime(current.year,current.month,current.day,current.hour,current.minute,current.second)


# sets so it picks up on whether it's echoing or < 
if (len(sys.argv) > 1):
    string = sys.argv[1]
else:
    string = sys.stdin.readline() 


# doing some split stuff
arr = string.split(" ")
epoch = datetime.datetime(int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3]),int(arr[4]),int(arr[5]))
# thank god python is for little toddlers and lets you do fun things like this
diff = current - epoch
finalSeconds = int(diff.total_seconds())
# if it's in DST act accordingly 
finalSeconds = offset(epoch,current,finalSeconds)
# this does something about the 60 second intervals, i don't remember
rem = finalSeconds % 60
finalSeconds-=rem
# do the md5 sum a couple times. python really is for toddlers man this shouldn't be allowed
md = hashlib.md5(str(finalSeconds).encode())
md = md.hexdigest()
md = hashlib.md5(md.encode()).hexdigest()



code = ""

mdreverse = md[::-1]
# go through and find 2 letters and 2 numbers
for i in md:
    if (i.isalpha() and len(code) < 2):
        code+=i
for i in mdreverse:
    if (i.isdigit() and len(code) < 4):
        code+=i
print(code+md[15:17])
