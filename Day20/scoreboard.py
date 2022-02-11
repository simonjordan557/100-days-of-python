from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(-275, 275)

    def update_score(self, score, hi):
        self.pendown()
        self.clear()
        self.write(f"SCORE: {score}\t\t  HI-SCORE: {hi}", align="left", font=("",18, ""))
        self.penup()

    def game_over(self, score, hi):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER! YOU SCORED: {score}.", align="center", font=("", 24, ""))
