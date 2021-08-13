# Print the same number from file1, file2, as list using list comprehension

with open("file1.txt") as file1:
    file1_list = [int(num) for num in file1.readlines()]
    print(file1_list)

with open("file2.txt") as file2:
    file2_list = [int(num) for num in file2.readlines()]
    print(file2_list)

result = [num for num in file1_list if num in file2_list]
# Write your code above 👆
# Output - [3, 6, 5, 33, 12, 7, 42, 13]

print(result)

dict = {
    "key": 15,
    "car": 4,
    "bike": 2,
    "lorry": 6
}

for key in dict.values():
    print(key)