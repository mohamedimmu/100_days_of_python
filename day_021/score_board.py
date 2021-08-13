from turtle import Turtle
from day_021.colors import WHITE

ALIGN = "center"
SCORE_FONT = ("Courier", 14, "normal")
GAMEOVER_FONT = ("Courier", 40, "normal")




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = data.read()
        self.penup()
        self.color(WHITE)
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=GAMEOVER_FONT)
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")

    def update_score(self):
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGN, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

