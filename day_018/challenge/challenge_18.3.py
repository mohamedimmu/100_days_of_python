# 18.3 - Drawing different shape

import random
from turtle import Turtle, Screen

tim = Turtle()
tim.width(10)
screen = Screen()
screen.colormode(255)


def random_rgbColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, blue, green


def draw_shapes(num_of_side):
    angle = 360 / num_of_side
    tim.color(random_rgbColor())
    for _ in range(num_of_side):
        tim.left(angle)
        tim.forward(100)
    for _ in range(num_of_side):
        tim.right(angle)
        tim.forward(100)


for shape_side_no in range(3, 11):
    draw_shapes(shape_side_no)

screen.exitonclick()
