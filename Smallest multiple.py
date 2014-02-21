# Initialization
n = 20
factors = []
coe = []

# Loop from 2 to 20
for i in range(2, n+1):

    # Find all the factors of i
    cur_factors = []
    cur_coe = []
    x = i
    k = 2
    while x > 1:
        if x % k == 0:
            cur_factors.append(k)
            p = 0
            while x % k == 0:
                x = x // k
                p += 1
            cur_coe.append(p)
        k += 1

    for i in range(0, len(cur_factors)):
        if cur_factors[i] in factors:
            index = factors.index(cur_factors[i])
            if cur_coe[i] > coe[index]:
                coe[index] = cur_coe[i]
        else:
            factors.append(cur_factors[i])
            coe.append(cur_coe[i])

# Calc result
total = 1
for i in range(0, len(factors)):
    total = total * (factors[i] ** coe[i])

# Output
print(total)
