# Project 2 - Tip Calculator

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print('Welcome to the tip calculator')
bill = int(input('What was the total bill ? '))
tip_percentage = int(input('What percentage tip would like to give ? 10, 12, or 15 ? '))
num_of_people = int(input('How many people to split the bill ? '))

# Method 1

final_bill = (bill / num_of_people) * ((tip_percentage / 100) + 1)
print("Each person should pay: {:.2f}".format(final_bill))

# Method 2

# tip_amount = (tip_percentage / 100) * bill
# final_bill = bill + tip_amount
# bill_per_person = final_bill / num_of_people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(final_amount)
# print(f'Each person should pay : {final_amount}')
