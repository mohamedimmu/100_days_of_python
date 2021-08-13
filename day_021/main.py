# Project 21 - Snake Game

# Features
# 1. Detect collision with food
# 2. Create a scoreboard
# 3. Detect collision with wall
# 4. Detect the collision with tail or body

import time
from turtle import Screen, Turtle
from day_021.snake import Snake
from day_021.food import Food
from day_021.score_board import ScoreBoard
from day_021.colors import WHITE, get_new_color, current_food_color, BLACK
from day_021.border import draw_border

screen = Screen()
screen.colormode(255)
screen.bgcolor(BLACK)
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)


game_is_on = True
draw_border()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect the collision with food.
    if snake.head.distance(food) < 15:
        new_food_color = get_new_color()
        food.refresh(new_food_color)

        snake.extend(current_food_color)
        current_food_color = new_food_color

        scoreboard.increase_score()

    # Detct the collision with wall.
    if round(snake.head.xcor()) > 280 or round(snake.head.xcor()) < -280 or round(snake.head.ycor()) > 280 or \
            round(snake.head.ycor()) < -280:

        scoreboard.game_over()
        game_is_on = False

    # Detect the collison with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
