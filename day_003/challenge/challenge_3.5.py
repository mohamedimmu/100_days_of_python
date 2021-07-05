# 3.5 Love Calculator

# Instructons
"""
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

print("Welcome to love calculator")
your_name = input("What is your name? \n").lower()
partner_name = input("What is their name? \n").lower()

t = your_name.count("t") + partner_name.count("t")
r = your_name.count("r") + partner_name.count("r")
u = your_name.count("u") + partner_name.count("u")
e = your_name.count("e") + partner_name.count("e")

l = your_name.count("l") + partner_name.count("l")
o = your_name.count("o") + partner_name.count("o")
v = your_name.count("v") + partner_name.count("v")
e = your_name.count("e") + partner_name.count("e")

true = t + r + u + e
love = l + o + v + e
score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
