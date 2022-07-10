
from operator import truediv


result = True
for X in True, False:
    for Y in True, False:
        for Z in True, False:
            if (not(X or Y or Z)) == (not X and not Y and not Z):
                result = True
            else:
                result = False
                break
print(result)


