# Project 19 - Turtle Race

import random
from turtle import Turtle, Screen

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose the color: "
                                                          "\n(red,orange,yellow,green,blue,purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_axis = -75
all_turtles = []

for index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_axis)
    y_axis += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win !!! The winning turtle is {winning_turtle}")
            else:
                print(f"You lose !!! The winning turtle is {winning_turtle}")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
