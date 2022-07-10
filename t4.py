
def RangeOfQuarter (numberOfQuarter):
    quarters = {
        1: "x > 0 and y > 0",
        2: "x < 0 and y > 0",
        3: "x < 0 and y < 0",
        4: "x > 0 and y < 0"
    }
    if numberOfQuarter in quarters:
        print(f"Range of quarte {numberOfQuarter} = {quarters[numberOfQuarter]}")
    else:
        print("There isn't such quarter")

try:
    quarterNumber = 4
    RangeOfQuarter(quarterNumber)
except:
    print("You enter not a integer")