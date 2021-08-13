from turtle import Turtle
from day_021.colors import get_new_color

STARTING_POSITIONS = [(-0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.new_snake_color = get_new_color()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segment(position, self.new_snake_color)
            self.new_snake_color = get_new_color()

    def create_segment(self, position, snake_color):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color(snake_color)
        self.segments.append(new_segment)

    def extend(self, eaten_food_color):
        position = self.segments[-1].position()
        self.create_segment(position, eaten_food_color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
