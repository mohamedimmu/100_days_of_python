# 18.4 - Random Walk
# ‘fastest’ :  0
# ‘fast’    :  10
# ‘normal’  :  6
# ‘slow’    :  3
# ‘slowest’ :  1
# 0(east), 90(north), 180(west), 270(south) - Standard mode

import random
from turtle import Turtle, Screen

tim = Turtle()
tim.width(15)
tim.speed(0)
screen = Screen()
screen.colormode(255)
direction_list = [0, 90, 180, 270]


def random_rgbColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, blue, green


for _ in range(250):
    direction = random.choice(direction_list)
    tim.color(random_rgbColor())
    tim.forward(30)
    tim.setheading(direction)


screen.exitonclick()
