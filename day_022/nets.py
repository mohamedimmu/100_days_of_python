from turtle import Turtle


class Nets(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_middle_line()

    def draw_middle_line(self):
        self.color("white")
        self.penup()
        self.goto((0, 295))
        self.setheading(270)
        self.hideturtle()
        self.width(3)
        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)