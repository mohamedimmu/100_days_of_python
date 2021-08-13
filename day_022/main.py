# Project 22 - Pong Game

# Controls
# Right Paddle = Up and Dowm Key
# Left Paddle = W and S Key

# Features
# 1. Create the screen
# 2. Create and move the paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect the collision with ball and bounce
# 6. Detect the collision with paddle
# 7. Detct when paddle misses
# 8. Keep Score

import time
from turtle import Screen
from day_022.paddle import Paddle
from day_022.ball import Ball
from day_022.scoreboard import ScoreBoard
from day_022.nets import Nets

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
left_player_score = ScoreBoard((-100, 200))
right_player_score = ScoreBoard((100, 200))
nets = Nets()


screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key="Up")
screen.onkeypress(fun=l_paddle.move_down, key="Down")
screen.onkeypress(fun=r_paddle.move_up, key="w")
screen.onkeypress(fun=r_paddle.move_down, key="s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detct the collision with paddle
    if ball.xcor() > 330 and ball.distance(l_paddle) < 50 or ball.xcor() < -330 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        left_player_score.updatescore()

    # Detect when leftt paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        right_player_score.updatescore()

screen.exitonclick()
