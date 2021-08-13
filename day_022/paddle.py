from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def move_up(self):
        new_ycor = self.ycor() + 40
        if self.ycor() < 240:
            self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 40
        if self.ycor() > -240:
            self.goto(self.xcor(), new_ycor)
