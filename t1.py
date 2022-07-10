

def DayIssue(numberDay):
    if numberDay<1 or numberDay>7:
        print ("There isn't such day")
    elif numberDay<6:
        print ("Is's Weekday")
    else:
        print ("It's weekend")

try:
    DayNumber = int(input('Enter the day number: '))
    DayIssue(DayNumber)
except:
    print('You enter not integer')
