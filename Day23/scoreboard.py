# Imports
from turtle import Turtle

# Constants
STARTING_POS = 260
FONT = "courier"
SIZE = 28
TYPE = "bold"
ALIGN = "left"

# Class declaration
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed(0)
        self.goto(-STARTING_POS, STARTING_POS)
        self.level = 1
        self.pendown()
        self.display_score()

    def increase_score(self):
        self.level += 1

    def display_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align=ALIGN, font=(FONT, SIZE, TYPE))

    def display_game_over(self):
        self.penup()
        self.goto(0, -20)
        self.pendown()
        self.write("GAME OVER", align="center", font=(FONT, SIZE, TYPE))
