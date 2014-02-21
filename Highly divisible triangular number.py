# Initialization
x = 8

# Calc the number of factor for all the triangle numbers
while True:
    n = (x + 1) * x // 2
    nn = n
    k = 2
    m = 1
    while n > 1:
        if n % k == 0:
            p = 0
            while n % k == 0:
                n = n // k
                p += 1
            m = m * (p+1)
        k += 1
    if m > 500:
        print(nn)
        break
    x += 1
