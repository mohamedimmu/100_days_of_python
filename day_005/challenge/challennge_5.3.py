# 5.3 Adding Evens

sum_of_even = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_of_even += number

print(sum_of_even)