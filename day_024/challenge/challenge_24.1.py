# Write the files

file = open("my_file.txt", mode="w")
file.write("Hello, this is the test file")
file.close()

# Append the files

with open("my_file.txt", mode='a') as file:
    file.write("\nThis is the append line")

# Read the files
# if we use WITH to open the file then close() is not required

with open("my_file.txt") as file:
    content = file.read()
    print(content)

# Abosulte file path - C:\Users\LENOVO\PycharmProjects\100_days_of_python\day_024\challenge\challenge_24.1.py
# Relative file path - day_024/challenge/challenge_24.1.py
