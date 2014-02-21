# Initialization
n = 600851475143
k = 2
prime_factors = []

# Loop all the factors of n
while n > 1:
    if n % k == 0:
        prime_factors.append(k)
        while n % k == 0:
            n = n // k
    k += 1

# Output
print(prime_factors[-1])
