# 18.1 - Drawing the square

from turtle import Turtle, Screen


def draw_square():
    my_turtle = Turtle()
    for _ in range(4):
        my_turtle.right(90)
        my_turtle.forward(100)


draw_square()

screen = Screen()
screen.exitonclick()
