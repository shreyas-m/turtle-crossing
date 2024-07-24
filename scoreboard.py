from turtle import Turtle

FONT = ("Comic Sans MS", 24, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "left", FONT)

    def score_point(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER: {self.score}", False, "center", FONT)
