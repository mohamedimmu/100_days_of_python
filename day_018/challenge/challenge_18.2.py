# 18.2 Drawing dashed line

from turtle import Turtle, Screen

tim = Turtle()


def dashed_line():
    for _ in range(20):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


dashed_line()
screen = Screen()
screen.exitonclick()
