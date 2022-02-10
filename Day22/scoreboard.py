# Imports
from turtle import Turtle

# Constants
STARTING_Y = 230
FONT = "courier"
SIZE = 48
TYPE = "bold"
ALIGN = "center"

# Class declaration
class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("yellow")
        self.goto(x, STARTING_Y)
        self.score = 0
        self.pendown()
        self.write(self.score, align=ALIGN, font=(FONT, SIZE, TYPE))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align=ALIGN, font=(FONT, SIZE, TYPE))

    def game_over(self, winner):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"PLAYER {winner} WINS", align=ALIGN, font=(FONT, SIZE, TYPE))


