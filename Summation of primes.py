# Initialization
primes = []
k = 2
nums = [x for x in range(0, 2000001)]
s = 0

# List all the possible prime numbers below two million
while k <= 2000000:
    if nums[k] != 0:
        for j in range(2, 2000000 // k + 1):
            nums[j * k] = 0
        s += k
    k += 1

# Output
print(s)
