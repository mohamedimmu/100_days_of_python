# 4.3 Treasure Map

# Example Input
# column 2, row 3 would be entered as:
# 23

# Example Output
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', 'X', '⬜️']

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
tresure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_digit = int(position[0]) - 1
second_digit = int(position[1]) - 1

tresure_map[second_digit][first_digit] = "X"

print(f"{row1}\n{row2}\n{row3}")