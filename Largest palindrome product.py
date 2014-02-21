# Initialization
a = 999
f = False
nums = []

# Loop from the largest 3-digit numbers

while a > 99:
    b = a
    while b > 99:
        st = str(a*b)
        if st[0] == st[-1] and st[1] == st[-2] and st[2] == st[-3]:
            nums.append(a*b)
        b -= 1
    a -= 1

# Find the max
m = -1
for num in nums:
    if num > m:
        m = num

# Output
print(m)
