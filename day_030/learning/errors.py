# FileNotFoundError
# with open("data.txt") as data:
#     data.read()

try:
    data = open("data.txt")
    dictionary = {"Key": "Value"}
    print(dictionary["No_key"])
except FileNotFoundError:
    # if try block has filenotfounderror it will excute except block.
    # if try block has any other error than filenotfounderror it will stop the execution
    data = open("data.txt", "w")
    data.write("Something")
except KeyError as error_message:
    # if try block has KeyError it will excute this except block.
    print(f"That key {error_message} does not exist")
else:
    # if try work correctly it will execute else part
    content = data.read()
    print(content)
finally:
    # Finally block will execute no matter what happens
    data.close()
    print("data is closed")


# KeyError
# dictionary = {"Key": "Value"}
# print(dictionary["No_key"])

# IndexError
# fruits = ['apple', 'banana', 'orange']
# print(fruits[3])

# TypeError
# print("Hello" + 5)

# Four keywords to avoid error
# try
# except
# else
# finally

# Raising Exceptions
# Using raise keyword we can raise your won exceptions

height = float(input("Enter your height in meter: "))
weight = float(input("Enter youur weight in kgs: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight/ height ** 2
print(bmi)