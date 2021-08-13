# Project 18 - Hirst Spot Painting
# Tk Color Link - https://cs111.wellesley.edu/labs/lab01/colors
# Tk Color Link 2 - https://trinket.io/docs/colors

import random
from turtle import Turtle, Screen

# color list from colr_picker module
color_list = [(41, 104, 174), (234, 205, 114), (228, 151, 85), (189, 46, 74), (231, 118, 144), (115, 90, 46),
              (110, 107, 189), (216, 60, 77), (114, 186, 136), (122, 176, 212), (52, 178, 110), (204, 16, 40),
              (115, 171, 36), (223, 57, 47), (31, 58, 117), (154, 223, 195), (182, 168, 223), (23, 142, 107),
              (29, 164, 172), (85, 35, 37), (39, 45, 84), (229, 169, 182), (232, 174, 161), (81, 39, 38),
              (151, 206, 223), (92, 43, 42)]

turtle = Turtle()
turtle.speed(10)
screen = Screen()
screen.colormode(255)

turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(350)
turtle.setheading(0)
turtle.forward(10)

for vertical in range(10):
    for horizontal in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.backward(50 * 10)


screen.exitonclick()
