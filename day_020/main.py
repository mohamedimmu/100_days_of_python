# Project 20 - Snake Game

# Features in day 20
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake

import time
from turtle import Screen
from day_020.snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.25)

    snake.move()

screen.exitonclick()
