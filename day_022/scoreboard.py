from turtle import Turtle

SCORE_FONT = ("Courier", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.player_score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(self.player_score, move=False, align="center", font=SCORE_FONT)

    def updatescore(self):
        self.player_score += 1
        self.display_score()


