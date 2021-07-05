# 19.1 - Etch-A-Sketch App

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def front():
    turtle.forward(10)


def back():
    turtle.backward(10)


def left():
    turtle.left(10)


def right():
    turtle.right(10)


def clear():
    turtle.reset()


game_controls = {
    "w": front,
    "s": back,
    "a": left,
    "d": right,
    "c": clear

}

screen.listen()
for control in game_controls:
    screen.onkey(key=control, fun=game_controls[control])

screen.exitonclick()
