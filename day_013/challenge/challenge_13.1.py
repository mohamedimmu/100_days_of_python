# Debugging Challenge
# Online debugger - http://www.pythontutor.com/visualize.html#mode=edit

# Problem 1
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Solution:
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Problem 2
# year = input("Which year do you want to check?")
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# Solution:

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Problem 3
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Solution:
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Tips to debug
# 1.  Describe the problem
# 2.  Reproduce the bug
# 3.  Play as computer
# 4.  Fix the errors
# 5.  Print to debug
# 6.  Use a debugger
# 7.  Ask other developer
# 8.  Take break
# 9.  Run often
# 10. Ask stackoverflow


