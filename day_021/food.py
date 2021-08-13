import random
from turtle import Turtle
from day_021.colors import get_food_color


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.new_food_color = get_food_color
        self.refresh(self.new_food_color)

    def refresh(self, food_color):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(food_color)
