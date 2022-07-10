import math

def distancePoint (Ax, Ay, Bx, By):
    try:
        result = math.sqrt((Bx-Ax)**2 + (By-Ay)**2)
        return round(result,2)
    except:
        return 'You enter not a digit'

Ax = 7
Ay = -5
Bx = 1
By = -1
result = distancePoint(Ax, Ay, Bx, By)
print(result)