# Imports
from turtle import Turtle

# Constants
ALIGN = "center"
FONT = ("courier", 8, "bold")
PENCOLOUR = "black"

# Class declaration
class TextWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(PENCOLOUR)
        self.speed(0)

    def write_text(self, x, y, text):
        self.goto(x, y)
        self.pendown()
        self.write(text, align=ALIGN, font=FONT)
        self.penup()

    def reset_screen(self):
        self.clear()