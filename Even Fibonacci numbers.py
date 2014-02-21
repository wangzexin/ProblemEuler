# Initialization
a = 1
b = 2
k = 3
x = 3
sum = 2

# Loop until the terms exceed four million
while x <= 4000000:
    if x % 2 == 0:
        sum += x
    a = b
    b = x
    x = a + b

# Output
print(sum)
