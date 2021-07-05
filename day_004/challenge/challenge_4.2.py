# 4.2 Who's paying

# Instructions
# Example Input - ElonMusk, JeffBezos, MarkZuckerberg, SteveJobs, BillGates
# Note: notice that there is a space between the comma and the next name.
# Example Output - BillGates is going to buy the meal today!

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_choice = random.randint(0, len(names) - 1)
print(f"{names[random_choice]} is going to buy the meal today!")