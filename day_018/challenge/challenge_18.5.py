# 18.5 - Spirograph

import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(0)
turtle.width()
screen = Screen()
screen.colormode(255)


def random_rgbColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, blue, green


def draw_spirograph(size_of_gap):
    for degree in range(round(360/size_of_gap)):
        turtle.color(random_rgbColor())
        # turtle.forward(100)
        # turtle.backward(100)
        turtle.circle(100)
        turtle.left(size_of_gap)


draw_spirograph(5.625)
screen.exitonclick()
