from turtle import Turtle
from day_021.colors import get_new_color


def draw_border():
    square = Turtle()
    square.penup()
    square.forward(280)
    square.left(90)
    square.forward(280)
    square.pendown()
    square.width(5)
    square.hideturtle()
    for i in range(4):
        square.left(90)
        for _ in range(8):
            square.color(get_new_color())
            square.forward(70)
