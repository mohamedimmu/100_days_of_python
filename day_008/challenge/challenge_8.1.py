# 8.1 Area calc
# Formula - number of cans = (wall height ✖ wall width) ÷ coverage per can.


import math

wall_height = int(input("Height of wall : "))
wall_width = int(input("Width of wall : "))
coverage = 5


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint")


paint_calc(height=wall_height, width=wall_width, cover=coverage)


# 8.2 Prime Numbers


