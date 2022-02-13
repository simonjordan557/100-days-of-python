# Imports
from turtle import Turtle

# Constants
XPOS = 250
YPOS = 200
PENCOLOUR = "black"
ALIGN = "center"
FONT = ("courier", 16, "bold")

# Class declaration
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.pencolor(PENCOLOUR)
        self.goto(XPOS, YPOS)
        self.score = 0

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.pendown()
        self.write(f"SCORE:{self.score}/50", align=ALIGN, font=FONT)
        self.penup()


    def reset_scoreboard(self):
        self.clear()
        self.goto(XPOS, YPOS)
