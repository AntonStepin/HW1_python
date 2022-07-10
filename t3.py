def Quarter (x, y):
    quarterNumber = None
    if x == 0 & y == 0:
        print('The quarter is not defined due x=0 and y = 0')
    elif x > 0 and y > 0:
        quarterNumber = 1
    elif x < 0 and y > 0:
        quarterNumber = 2
    elif x < 0 and y < 0:
        quarterNumber = 3
    else:
        quarterNumber = 4
    print(f'Quarter is {quarterNumber}')

try:
    x = -34
    y = -30
    Quarter(x, y)
except:
    print('You enter not a digit')
