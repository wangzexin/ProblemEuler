# Initialization
import math
f = False

# Calc all the possible triplets
for a in range(1, 330):
    for b in range(a+1, 500):
        c = math.sqrt(a**2 + b**2)
        if int(c) == c:
            if a+b+c == 1000:
                print(int(a * b * c))
                f = True
                break
    if f:
        break
