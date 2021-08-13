from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 48, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.score_text()

    def score_text(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, font=FONT, align="left")

    def update_score(self):
        self.score += 1
        self.score_text()

    def game_over_text(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, font=GAME_OVER_FONT, align="center")
