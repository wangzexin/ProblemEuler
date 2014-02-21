# Initialization
primes = [2, 3]
k = 4

# Calc the first 10001 prime numbers
while len(primes) < 10001:
    f = True
    for prime in primes:
        if k % prime == 0:
            f = False
            break
    if f:
        primes.append(k)
    k += 1

# Output
print(primes[-1])
