# Project 23 - Turtle Crossing Game

import time
from turtle import Screen
from day_023.player import Player
from day_023.car_manager import CarManager
from day_023.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_forward, key="Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            print("Gameover")
            game_is_on = False
            score_board.game_over_text()

    # Detect successful crossing
    if player.finish_line_is_reached():
        player.starting_position()
        car_manager.level_up()
        score_board.update_score()

screen.exitonclick()