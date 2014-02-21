# Calc sum of the squares of the first one hundred natural numbers
sum1 = 0
sumn = 0
for i in range(1, 101):
    sum1 += i * i
    sumn += i

# Calc square of the sum
sum2 = sumn ** 2

# Output
print(sum2 - sum1)
